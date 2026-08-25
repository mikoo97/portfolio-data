#!/usr/bin/env python3
"""Pengumpul data mentah untuk konten #1 @ceritadataa.

Menarik percakapan dan perhatian publik seputar rencana aksi 27 Agustus 2026
dari kanal-kanal yang aksesnya masih terbuka dan gratis:

  - GDELT DOC 2.0     : volume dan nada pemberitaan daring (tanpa kunci)
  - Wikipedia         : kunjungan harian artikel terkait (tanpa kunci)
  - Reddit            : utas dan komentar r/indonesia (tanpa kunci)
  - YouTube Data v3   : video dan komentar (butuh YOUTUBE_API_KEY)
  - Google Trends     : minat harian dan sebaran provinsi (butuh paket pytrends)

X/Twitter sengaja tidak diambil: API-nya berbayar dan pengikisan melanggar
ketentuan layanan. Ketiadaan itu harus disebut sebagai keterbatasan di konten.

Setiap keluaran disertai baris manifest berisi sumber, alamat, waktu unduh, dan
jumlah baris — supaya setiap angka yang tayang bisa ditelusuri balik.

Contoh:
    export YOUTUBE_API_KEY=...
    python3 ambil_data_27agustus.py --mulai 2026-08-01 --sampai 2026-08-25
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests

# Wikimedia mewajibkan alamat kontak di User-Agent. Isi dengan alamat yang kamu
# rela dibagikan ke layanan pihak ketiga, atau atur lewat CERITADATAA_KONTAK.
UA = "ceritadataa-research/1.0 (kontak: {})".format(
    os.environ.get("CERITADATAA_KONTAK", "surel-kontak@contoh.id")
)
KUERI = [
    "demo 27 agustus",
    "aksi 27 agustus",
    "RUU perampasan aset",
    "hukuman mati koruptor",
]
ARTIKEL_WIKI = [
    "Unjuk_rasa_Agustus_2026_di_Indonesia",
    "Dewan_Perwakilan_Rakyat_Republik_Indonesia",
]

manifest: list[dict] = []


def catat(sumber: str, alamat: str, berkas: Path, jumlah: int) -> None:
    manifest.append(
        {
            "sumber": sumber,
            "alamat": alamat,
            "berkas": berkas.name,
            "jumlah_baris": jumlah,
            "waktu_unduh_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    print(f"  [{jumlah:>6}] {berkas.name}")


def tulis_csv(berkas: Path, kolom: list[str], baris: list[dict]) -> None:
    with berkas.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kolom, extrasaction="ignore")
        w.writeheader()
        w.writerows(baris)


def ambil_json(url: str, params: dict | None = None, jeda: float = 1.0) -> dict | None:
    """GET dengan sopan: satu percobaan ulang, jeda antar-permintaan."""
    for percobaan in range(2):
        try:
            r = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=30)
            if r.status_code == 200:
                time.sleep(jeda)
                return r.json()
            print(f"    ! {r.status_code} dari {url}", file=sys.stderr)
        except (requests.RequestException, ValueError) as e:
            print(f"    ! gagal ({e})", file=sys.stderr)
        time.sleep(2 * (percobaan + 1))
    return None


# --------------------------------------------------------------------------- #
# GDELT: volume dan nada pemberitaan
# --------------------------------------------------------------------------- #
def gdelt(keluaran: Path, mulai: str, sampai: str) -> None:
    print("GDELT DOC 2.0 — volume dan nada pemberitaan")
    awal = mulai.replace("-", "") + "000000"
    akhir = sampai.replace("-", "") + "235959"
    baris = []
    for kueri in KUERI:
        for mode in ("timelinevol", "timelinetone"):
            params = {
                "query": f'"{kueri}" sourcecountry:ID',
                "mode": mode,
                "format": "json",
                "startdatetime": awal,
                "enddatetime": akhir,
            }
            data = ambil_json("https://api.gdeltproject.org/api/v2/doc/doc", params)
            if not data:
                continue
            for seri in data.get("timeline", []):
                for titik in seri.get("data", []):
                    baris.append(
                        {
                            "kueri": kueri,
                            "ukuran": "volume" if mode == "timelinevol" else "nada",
                            "tanggal": titik.get("date", "")[:8],
                            "nilai": titik.get("value"),
                        }
                    )
    berkas = keluaran / "gdelt_berita.csv"
    tulis_csv(berkas, ["kueri", "ukuran", "tanggal", "nilai"], baris)
    catat("GDELT DOC 2.0", "https://api.gdeltproject.org/api/v2/doc/doc", berkas, len(baris))


# --------------------------------------------------------------------------- #
# Wikipedia: kunjungan harian
# --------------------------------------------------------------------------- #
def wikipedia(keluaran: Path, mulai: str, sampai: str) -> None:
    print("Wikipedia — kunjungan harian artikel")
    awal, akhir = mulai.replace("-", ""), sampai.replace("-", "")
    baris = []
    for artikel in ARTIKEL_WIKI:
        url = (
            "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
            f"id.wikipedia/all-access/user/{quote(artikel, safe='')}/daily/{awal}/{akhir}"
        )
        data = ambil_json(url)
        if not data:
            continue
        for titik in data.get("items", []):
            baris.append(
                {
                    "artikel": artikel,
                    "tanggal": titik["timestamp"][:8],
                    "kunjungan": titik["views"],
                }
            )
    berkas = keluaran / "wikipedia_kunjungan.csv"
    tulis_csv(berkas, ["artikel", "tanggal", "kunjungan"], baris)
    catat("Wikimedia Pageviews API", "https://wikimedia.org/api/rest_v1", berkas, len(baris))


# --------------------------------------------------------------------------- #
# Reddit: utas dan komentar r/indonesia
# --------------------------------------------------------------------------- #
def reddit(keluaran: Path) -> None:
    print("Reddit — r/indonesia")
    utas, komentar = [], []
    for kueri in KUERI:
        data = ambil_json(
            "https://www.reddit.com/r/indonesia/search.json",
            {"q": kueri, "restrict_sr": 1, "sort": "new", "limit": 100, "t": "month"},
            jeda=2.0,
        )
        if not data:
            continue
        for anak in data.get("data", {}).get("children", []):
            p = anak["data"]
            utas.append(
                {
                    "kueri": kueri,
                    "id": p["id"],
                    "waktu_utc": datetime.fromtimestamp(
                        p["created_utc"], timezone.utc
                    ).isoformat(timespec="seconds"),
                    "judul": p.get("title", ""),
                    "skor": p.get("score"),
                    "jumlah_komentar": p.get("num_comments"),
                    "teks": (p.get("selftext") or "").replace("\n", " ")[:2000],
                }
            )

    for p in {u["id"]: u for u in utas}.values():
        data = ambil_json(
            f"https://www.reddit.com/comments/{p['id']}.json", {"limit": 200}, jeda=2.0
        )
        if not data or len(data) < 2:
            continue
        for anak in data[1].get("data", {}).get("children", []):
            c = anak.get("data", {})
            if c.get("body"):
                komentar.append(
                    {
                        "utas_id": p["id"],
                        "komentar_id": c.get("id"),
                        "waktu_utc": datetime.fromtimestamp(
                            c["created_utc"], timezone.utc
                        ).isoformat(timespec="seconds"),
                        "skor": c.get("score"),
                        "teks": c["body"].replace("\n", " ")[:2000],
                    }
                )

    b1 = keluaran / "reddit_utas.csv"
    tulis_csv(b1, ["kueri", "id", "waktu_utc", "judul", "skor", "jumlah_komentar", "teks"], utas)
    catat("Reddit r/indonesia", "https://www.reddit.com/r/indonesia", b1, len(utas))
    b2 = keluaran / "reddit_komentar.csv"
    tulis_csv(b2, ["utas_id", "komentar_id", "waktu_utc", "skor", "teks"], komentar)
    catat("Reddit r/indonesia", "https://www.reddit.com/comments", b2, len(komentar))


# --------------------------------------------------------------------------- #
# YouTube: video dan komentar
# --------------------------------------------------------------------------- #
def youtube(keluaran: Path, mulai: str, kunci: str, batas_komentar: int) -> None:
    print("YouTube Data API v3 — video dan komentar")
    dasar = "https://www.googleapis.com/youtube/v3"
    video, komentar = [], []

    for kueri in KUERI:
        data = ambil_json(
            f"{dasar}/search",
            {
                "part": "snippet",
                "q": kueri,
                "type": "video",
                "maxResults": 50,
                "order": "relevance",
                "relevanceLanguage": "id",
                "regionCode": "ID",
                "publishedAfter": f"{mulai}T00:00:00Z",
                "key": kunci,
            },
        )
        if not data:
            continue
        for item in data.get("items", []):
            s = item["snippet"]
            video.append(
                {
                    "kueri": kueri,
                    "video_id": item["id"]["videoId"],
                    "waktu_terbit": s["publishedAt"],
                    "kanal": s["channelTitle"],
                    "judul": s["title"],
                }
            )

    for v in {x["video_id"]: x for x in video}.values():
        if len(komentar) >= batas_komentar:
            break
        token = None
        for _ in range(3):  # maksimal 300 komentar per video
            params = {
                "part": "snippet",
                "videoId": v["video_id"],
                "maxResults": 100,
                "order": "relevance",
                "textFormat": "plainText",
                "key": kunci,
            }
            if token:
                params["pageToken"] = token
            data = ambil_json(f"{dasar}/commentThreads", params)
            if not data:
                break
            for item in data.get("items", []):
                c = item["snippet"]["topLevelComment"]["snippet"]
                komentar.append(
                    {
                        "video_id": v["video_id"],
                        "komentar_id": item["id"],
                        "waktu_terbit": c["publishedAt"],
                        "suka": c.get("likeCount"),
                        "teks": c["textDisplay"].replace("\n", " ")[:2000],
                    }
                )
            token = data.get("nextPageToken")
            if not token:
                break

    b1 = keluaran / "youtube_video.csv"
    tulis_csv(b1, ["kueri", "video_id", "waktu_terbit", "kanal", "judul"], video)
    catat("YouTube Data API v3", f"{dasar}/search", b1, len(video))
    b2 = keluaran / "youtube_komentar.csv"
    tulis_csv(b2, ["video_id", "komentar_id", "waktu_terbit", "suka", "teks"], komentar)
    catat("YouTube Data API v3", f"{dasar}/commentThreads", b2, len(komentar))

    print(
        "  catatan: nama penulis komentar sengaja TIDAK diambil (UU PDP 27/2022).",
        file=sys.stderr,
    )


# --------------------------------------------------------------------------- #
# Google Trends
# --------------------------------------------------------------------------- #
def trends(keluaran: Path, mulai: str, sampai: str) -> None:
    print("Google Trends — minat harian dan sebaran provinsi")
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("  ! pytrends belum terpasang — lewati (pip install pytrends)", file=sys.stderr)
        return

    tr = TrendReq(hl="id-ID", tz=-420)
    tr.build_payload(KUERI[:5], timeframe=f"{mulai} {sampai}", geo="ID")

    waktu = tr.interest_over_time()
    if not waktu.empty:
        baris = [
            {"tanggal": idx.strftime("%Y-%m-%d"), "kueri": k, "indeks": int(r[k])}
            for idx, r in waktu.iterrows()
            for k in KUERI[:5]
            if k in waktu.columns
        ]
        berkas = keluaran / "trends_harian.csv"
        tulis_csv(berkas, ["tanggal", "kueri", "indeks"], baris)
        catat("Google Trends", "https://trends.google.com", berkas, len(baris))

    wilayah = tr.interest_by_region(resolution="REGION", inc_low_vol=True)
    if not wilayah.empty:
        baris = [
            {"provinsi": idx, "kueri": k, "indeks": int(r[k])}
            for idx, r in wilayah.iterrows()
            for k in KUERI[:5]
            if k in wilayah.columns
        ]
        berkas = keluaran / "trends_provinsi.csv"
        tulis_csv(berkas, ["provinsi", "kueri", "indeks"], baris)
        catat("Google Trends", "https://trends.google.com", berkas, len(baris))

    print("  catatan: indeks Trends adalah nilai relatif 0-100, BUKAN jumlah orang.", file=sys.stderr)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--mulai", default="2026-08-01", help="tanggal awal, YYYY-MM-DD")
    p.add_argument("--sampai", default="2026-08-25", help="tanggal akhir, YYYY-MM-DD")
    p.add_argument("--keluaran", default="data-mentah", help="map keluaran")
    p.add_argument("--batas-komentar", type=int, default=3000, help="batas komentar YouTube")
    p.add_argument(
        "--lewati",
        default="",
        help="kanal yang dilewati, dipisah koma: gdelt,wikipedia,reddit,youtube,trends",
    )
    a = p.parse_args()

    keluaran = Path(a.keluaran)
    keluaran.mkdir(parents=True, exist_ok=True)
    lewati = {x.strip() for x in a.lewati.split(",") if x.strip()}

    print(f"Rentang: {a.mulai} sampai {a.sampai} — keluaran: {keluaran}/\n")

    if "gdelt" not in lewati:
        gdelt(keluaran, a.mulai, a.sampai)
    if "wikipedia" not in lewati:
        wikipedia(keluaran, a.mulai, a.sampai)
    if "reddit" not in lewati:
        reddit(keluaran)
    if "youtube" not in lewati:
        kunci = os.environ.get("YOUTUBE_API_KEY")
        if kunci:
            youtube(keluaran, a.mulai, kunci, a.batas_komentar)
        else:
            print("YouTube dilewati — YOUTUBE_API_KEY belum diatur", file=sys.stderr)
    if "trends" not in lewati:
        trends(keluaran, a.mulai, a.sampai)

    berkas_manifest = keluaran / "manifest.json"
    berkas_manifest.write_text(
        json.dumps(
            {
                "konten": "sentimen-27-agustus-2026",
                "rentang": {"mulai": a.mulai, "sampai": a.sampai},
                "kueri": KUERI,
                "tidak_diambil": {
                    "x_twitter": "API berbayar; pengikisan melanggar ketentuan layanan",
                    "instagram": "tidak ada akses publik untuk percakapan pihak lain",
                    "tiktok": "dicatat manual — lihat brief",
                },
                "berkas": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"\nManifest ditulis: {berkas_manifest}")
    print("Langkah berikutnya: ambil sampel acak >=500 baris, labeli dengan buku kode di brief.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
