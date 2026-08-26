#!/usr/bin/env python3
"""Render enam slide konten #1 @ceritadataa langsung dari data mentah.

Semua angka dibaca dari CSV, tidak ada yang diketik tangan. Jalankan ulang
setiap kali data berubah; jangan pernah menyunting angkanya di berkas gambar.

    python3 render_slide.py
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon as MplPolygon, Rectangle
from matplotlib.collections import PatchCollection

AKAR = Path(__file__).parent
MENTAH, GRAFIK = AKAR / "data-mentah", AKAR / "grafik"
GRAFIK.mkdir(exist_ok=True)

# ---------------------------------------------------------------- gaya tetap
LATAR, TINTA, ABU = "#F4F1EA", "#16161A", "#8A8A85"
AKSEN, REDAM, GARIS = "#14615A", "#C9C5BC", "#DED9CE"
RAMPA = ["#E2EDEA", "#B9D6D0", "#86B8AF", "#4C8E85", "#1E5E56"]
AMBANG = [5, 10, 20, 40]
LABEL_BIN = ["di bawah 5", "5–9", "10–19", "20–39", "40 ke atas"]
KOSONG = "#DDD8CE"

W, H, DPI = 10.80, 13.50, 100          # 1080 x 1350 piksel
KIRI, KANAN, ATAS, BAWAH = 0.083, 0.917, 0.911, 0.089   # margin aman

TANGGAL_DATA = "26 Agustus 2026, 17.00 WIB"


def daftarkan_font() -> str:
    """Pasang Plus Jakarta Sans kalau ada; kalau tidak, pakai bawaan sistem."""
    var = AKAR / "fonts" / "PJS.ttf"
    if not var.exists():
        return "DejaVu Sans"
    try:
        from fontTools import ttLib
        from fontTools.varLib import instancer
        for berat in (400, 600, 800):
            keluar = AKAR / "fonts" / f"PJS-{berat}.ttf"
            if not keluar.exists():
                f = ttLib.TTFont(str(var))
                instancer.instantiateVariableFont(f, {"wght": berat}, inplace=True)
                f.save(str(keluar))
            font_manager.fontManager.addfont(str(keluar))
        return font_manager.FontProperties(fname=str(AKAR / "fonts" / "PJS-400.ttf")).get_name()
    except Exception:
        return "DejaVu Sans"


KELUARGA = daftarkan_font()
plt.rcParams.update({"font.family": KELUARGA, "figure.dpi": DPI})


def angka(v: str) -> float | None:
    v = (v or "").strip()
    if not v:
        return None
    return 0.5 if v.startswith("<") else float(v)


def kanvas():
    fig = plt.figure(figsize=(W, H), facecolor=LATAR)
    return fig


def kop(fig, judul: str, kicker: str | None = None, y: float = ATAS):
    """Judul temuan di kepala slide. Judul menyatakan temuan, bukan 'Grafik 1'."""
    fig.text(KIRI, y, judul, color=TINTA, fontsize=27, weight=800,
             va="top", ha="left", linespacing=1.28)


def kaki(fig, sumber: str, catatan: str | None = None):
    y = BAWAH - 0.012
    if catatan:
        fig.text(KIRI, y + 0.026, catatan, color=ABU, fontsize=11.5,
                 va="top", linespacing=1.45)
        y -= 0.018
    fig.text(KIRI, y, sumber, color=ABU, fontsize=11, va="top", linespacing=1.45)
    fig.text(KANAN, BAWAH - 0.012, "@ceritadataa", color=ABU, fontsize=11,
             va="top", ha="right", weight=600)


# ------------------------------------------------------------------ baca data
def baca_harian():
    r = list(csv.reader((MENTAH / "trends_harian.csv").open(encoding="utf-8")))
    kol = [h.split(":")[0].strip() for h in r[2][1:]]
    tgl, seri = [], {k: [] for k in kol}
    for baris in r[3:]:
        if not baris or not baris[0]:
            continue
        tgl.append(baris[0])
        for k, v in zip(kol, baris[1:]):
            seri[k].append(angka(v))
    return tgl, seri


def baca_provinsi():
    r = list(csv.reader((MENTAH / "trends_provinsi.csv").open(encoding="utf-8")))
    return {baris[0]: angka(baris[1]) for baris in r[3:] if baris and baris[0]}


def samakan(nama: str) -> str:
    s = nama.upper().replace(".", "")
    for a, b in [("DAERAH KHUSUS IBUKOTA", "DKI"), ("DAERAH ISTIMEWA YOGYAKARTA", "DI YOGYAKARTA"),
                 ("DI ACEH", "ACEH"), ("KEPULAUAN BANGKA BELITUNG", "BANGKA BELITUNG"),
                 ("KEPULAUAN RIAU", "KEPRI"), ("NUSATENGGARA", "NUSA TENGGARA"),
                 ("PROBANTEN", "BANTEN"), ("IRIAN JAYA BARAT", "PAPUA BARAT"),
                 ("IRIAN JAYA TIMUR", "PAPUA")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def warna_bin(v):
    if v is None:
        return RAMPA[0]
    for i, batas in enumerate(AMBANG):
        if v < batas:
            return RAMPA[i]
    return RAMPA[-1]


# -------------------------------------------------------------------- slide 1
def slide1(seri):
    fig = kanvas()
    fig.text(KIRI, 0.845, "Aksinya baru besok.\nPercakapannya sudah\nlebih dulu berjalan.",
             color=TINTA, fontsize=40, weight=800, va="top", linespacing=1.2)
    rasio = seri["demo 27 agustus"][-1] / seri["RUU perampasan aset"][-1]
    fig.text(KIRI, 0.545, f"{rasio:.0f}×", color=AKSEN, fontsize=155, weight=800, va="top")
    fig.text(KIRI, 0.335,
             "Sebanyak itu pencarian “demo 27 Agustus”\n"
             "dibanding “RUU Perampasan Aset” hari ini —\n"
             "padahal itu tuntutan utama aksinya sendiri.",
             color=TINTA, fontsize=20, va="top", linespacing=1.6)
    fig.text(KIRI, 0.185, "Jadi sebenarnya, yang ramai itu apa?",
             color=AKSEN, fontsize=21, weight=600, va="top")
    kaki(fig, f"Sumber: Google Trends Indonesia, 26 Juli–26 Agustus 2026. Diakses {TANGGAL_DATA}.")
    fig.savefig(GRAFIK / "slide-1.png", dpi=DPI, facecolor=LATAR)
    plt.close(fig)


# -------------------------------------------------------------------- slide 2
def slide2():
    fig = kanvas()
    kop(fig, "Yang turun besok tidak\nmembawa satu tuntutan", "Konteks")
    tuntutan = [
        ("Antikorupsi", "Mendesak pengesahan RUU Perampasan Aset\ndan hukuman mati bagi pelaku korupsi."),
        ("Pekerja dapur MBG", "Menuntut kepastian kontrak kerja dan\nperlindungan bagi pekerja dapur program MBG."),
        ("Pendukung program", "Mendukung keberlanjutan program pemerintah,\ndengan catatan perbaikan tata kelola."),
    ]
    y = 0.725
    for tajuk, isi in tuntutan:
        fig.add_artist(Rectangle((KIRI, y - 0.105), 0.006, 0.115, transform=fig.transFigure,
                                     facecolor=AKSEN, edgecolor="none"))
        fig.text(KIRI + 0.032, y, tajuk, color=AKSEN, fontsize=17, weight=800, va="top")
        fig.text(KIRI + 0.032, y - 0.032, isi, color=TINTA, fontsize=17, va="top", linespacing=1.55)
        y -= 0.165
    fig.text(KIRI, 0.215,
             "Aksi direncanakan di depan Gedung DPR/MPR RI,\n"
             "Jalan Gatot Subroto, Senayan, Jakarta.",
             color=TINTA, fontsize=17, va="top", linespacing=1.6)
    kaki(fig, "Dihimpun dari pemberitaan Kompas, Kontan, dan Bisnis, 21–25 Agustus 2026.",
         "Kelompok yang turun tidak dinamai di sini karena belum semuanya\nterkonfirmasi dari dua sumber independen.")
    fig.savefig(GRAFIK / "slide-2.png", dpi=DPI, facecolor=LATAR)
    plt.close(fig)


# -------------------------------------------------------------------- slide 3
def slide3(tgl, seri):
    y = seri["demo 27 agustus"]
    fig = kanvas()
    kop(fig, "Sepuluh hari lalu, hampir\ntidak ada yang mencarinya", "Kapan mulai ramai")
    ax = fig.add_axes([KIRI, 0.235, KANAN - KIRI, 0.52])
    ax.set_facecolor(LATAR)
    x = list(range(len(tgl)))
    ax.plot(x[:-1], y[:-1], color=AKSEN, lw=2.6, solid_capstyle="round", zorder=3)
    ax.plot(x[-2:], y[-2:], color=AKSEN, lw=2.6, ls=(0, (2, 2)), zorder=3)
    ax.scatter([x[-1]], [y[-1]], s=90, facecolor=LATAR, edgecolor=AKSEN, lw=2.6, zorder=4)

    for i, lbl, dy, ha in [(x[tgl.index("2026-08-21")], "21 Agu\nindeks 1", 9, "center"),
                           (x[tgl.index("2026-08-24")], "24 Agu — naik 4,8×\ndalam satu hari", 14, "right")]:
        ax.annotate(lbl, (i, y[i]), textcoords="offset points", xytext=(0 if ha == "center" else -12, dy),
                    ha=ha, va="bottom", fontsize=13, color=TINTA, linespacing=1.4)
    ax.annotate("26 Agu — hari berjalan,\ndata belum lengkap", (x[-1], y[-1]),
                textcoords="offset points", xytext=(-14, -6), ha="right", va="top",
                fontsize=13, color=ABU, linespacing=1.4)

    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100])
    tik = [i for i, t in enumerate(tgl) if t.endswith(("-01", "-08", "-15", "-22", "-26")) or i == 0]
    ax.set_xticks(tik)
    ax.set_xticklabels(["26 Jul" if tgl[i] == "2026-07-26" else
                        f"{int(tgl[i][8:])} {'Agu' if tgl[i][5:7]=='08' else 'Jul'}" for i in tik])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GARIS)
    ax.tick_params(colors=ABU, labelsize=13, length=0, pad=9)
    ax.grid(axis="y", color=GARIS, lw=1)
    ax.set_axisbelow(True)
    fig.text(KIRI, 0.79, "Indeks pencarian “demo 27 agustus” di Indonesia — 100 = titik tertinggi",
             color=ABU, fontsize=13.5)
    fig.text(KIRI, 0.192,
             "Sampai 15 Agustus indeksnya nol. Rencana aksi ini praktis\n"
             "tidak dicari siapa pun sampai sepuluh hari terakhir.",
             color=TINTA, fontsize=17, va="top", linespacing=1.6)
    kaki(fig, f"Sumber: Google Trends Indonesia, 26 Juli–26 Agustus 2026. Diakses {TANGGAL_DATA}.",
         "Indeks Trends adalah nilai relatif 0–100 terhadap puncaknya sendiri, bukan jumlah orang.")
    fig.savefig(GRAFIK / "slide-3.png", dpi=DPI, facecolor=LATAR)
    plt.close(fig)


# -------------------------------------------------------------------- slide 4
def slide4(seri):
    puncak = {k: max(v for v in s if v is not None) for k, s in seri.items()}
    urut = sorted(puncak.items(), key=lambda kv: kv[1])
    nama = {"demo 27 agustus": "“demo 27 agustus”", "MBG": "“MBG”",
            "RUU perampasan aset": "“RUU perampasan aset”",
            "hukuman mati koruptor": "“hukuman mati koruptor”"}
    fig = kanvas()
    kop(fig, "Yang dicari peristiwanya,\nbukan tuntutannya", "Empat kata kunci, satu bulan")
    ax = fig.add_axes([0.36, 0.30, 0.555, 0.44])
    ax.set_facecolor(LATAR)
    for i, (k, v) in enumerate(urut):
        w = AKSEN if k == "demo 27 agustus" else REDAM
        ax.barh(i, v, height=0.52, color=w, zorder=3)
        tampil = "<1" if v == 0.5 else f"{v:.0f}"
        ax.text(v + 1.8, i, tampil, va="center", fontsize=17,
                color=TINTA if k == "demo 27 agustus" else ABU, weight=800 if k == "demo 27 agustus" else 400)
    ax.set_yticks(range(len(urut)))
    ax.set_yticklabels([nama[k] for k, _ in urut], fontsize=16.5, color=TINTA)
    ax.set_xlim(0, 118)
    ax.set_xticks([])
    for s in ("top", "right", "bottom", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0, pad=12)
    fig.text(KIRI, 0.775, "Indeks tertinggi tiap kata kunci sepanjang 26 Juli–26 Agustus 2026",
             color=ABU, fontsize=13.5)
    fig.text(KIRI, 0.235,
             "“Hukuman mati koruptor” tidak pernah beranjak dari <1\n"
             "selama 32 hari. “MBG” justru stabil di sekitar 28 sepanjang\n"
             "bulan, tidak terpengaruh rencana aksi.",
             color=TINTA, fontsize=17, va="top", linespacing=1.6)
    kaki(fig, f"Sumber: Google Trends Indonesia. Diakses {TANGGAL_DATA}.",
         "Keempatnya diunduh dalam satu perbandingan, jadi angkanya setara satu sama lain.")
    fig.savefig(GRAFIK / "slide-4.png", dpi=DPI, facecolor=LATAR)
    plt.close(fig)


# -------------------------------------------------------------------- slide 5
def slide5(prov):
    geo = json.loads((MENTAH / "indonesia-prov.geojson").read_text(encoding="utf-8"))
    nilai = {samakan(k): v for k, v in prov.items()}
    fig = kanvas()
    kop(fig, "Jakarta pusatnya — tapi\nYogyakarta ikut menyala", "Di mana orang mencarinya")
    ax = fig.add_axes([0.030, 0.415, 0.950, 0.385])
    ax.set_facecolor(LATAR)
    tambal, warna = [], []
    for f in geo["features"]:
        v = nilai.get(samakan(f["properties"]["Propinsi"]))
        g = f["geometry"]
        polis = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poli in polis:
            tambal.append(MplPolygon(poli[0], closed=True))
            warna.append(warna_bin(v))
    ax.add_collection(PatchCollection(tambal, facecolor=warna, edgecolor=LATAR, lw=0.5, zorder=2))
    ax.set_xlim(94.5, 141.5)
    ax.set_ylim(-11.5, 7.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # legenda
    lx, ly = KIRI, 0.372
    for i, (c, l) in enumerate(zip(RAMPA, LABEL_BIN)):
        fig.add_artist(Rectangle((lx + i * 0.152, ly), 0.036, 0.017,
                                     transform=fig.transFigure, facecolor=c, edgecolor="none"))
        fig.text(lx + i * 0.152, ly - 0.016, l, color=ABU, fontsize=12.5, va="top")
    fig.text(KIRI, 0.268,
             "Indeks provinsi mengukur porsi pencarian di wilayah itu, jadi\n"
             "jumlah penduduk sudah ikut diperhitungkan. Yogyakarta (18)\n"
             "berada di atas Jawa Tengah dan Jawa Timur yang sama-sama 14 —\n"
             "padahal penduduknya jauh lebih sedikit.",
             color=TINTA, fontsize=16.5, va="top", linespacing=1.6)
    kaki(fig, f"Sumber: Google Trends Indonesia, sebaran per provinsi. Diakses {TANGGAL_DATA}.",
         "Geometri: batas provinsi Indonesia, disederhanakan untuk tampilan.")
    fig.savefig(GRAFIK / "slide-5.png", dpi=DPI, facecolor=LATAR)
    plt.close(fig)


# -------------------------------------------------------------------- slide 6
def slide6():
    fig = kanvas()
    kop(fig, "Cara membacanya —\ndan batasnya", "Metode")
    butir = [
        ("Ini peta pencarian, bukan jajak pendapat.",
         "Data ini tidak bisa menjawab berapa banyak orang mendukung\natau menolak aksi. Ia hanya menunjukkan apa yang dicari."),
        ("Indeks Trends bukan jumlah orang.",
         "Angka 0–100 adalah nilai relatif terhadap titik tertinggi\ndalam rentang yang sama. Jangan dibandingkan lintas unduhan."),
        ("Rendahnya pencarian bukan bukti rendahnya kepedulian.",
         "Orang yang sudah paham RUU Perampasan Aset tidak perlu\nmencarinya. Yang bisa disimpulkan: perhatian baru tertuju\nke peristiwanya."),
        ("Hari terakhir belum tuntas.",
         "26 Agustus masih berjalan saat data diambil, jadi\nangkanya ditandai terpisah dan bukan titik penuh."),
    ]
    y = 0.775
    for tajuk, isi in butir:
        fig.text(KIRI, y, tajuk, color=TINTA, fontsize=17.5, weight=800, va="top")
        fig.text(KIRI, y - 0.031, isi, color=ABU, fontsize=15.5, va="top", linespacing=1.55)
        y -= 0.148
    fig.text(KIRI, 0.185, "Simpan kalau berguna. Besok kita lihat\nangkanya setelah aksinya berlangsung.",
             color=AKSEN, fontsize=19, weight=600, va="top", linespacing=1.5)
    kaki(fig, f"Sumber: Google Trends Indonesia, 26 Juli–26 Agustus 2026. Diakses {TANGGAL_DATA}.")
    fig.savefig(GRAFIK / "slide-6.png", dpi=DPI, facecolor=LATAR)
    plt.close(fig)


# ---------------------------------------------------------- grafik polos
# Versi tanpa judul, tanpa catatan kaki, latar transparan — untuk ditempel
# ke tata letak HTML. Angka dan sumbunya identik dengan versi slide.
def polos_kanvas(w=9.0, h=6.4):
    fig = plt.figure(figsize=(w, h), facecolor="none")
    return fig


def grafik3_polos(tgl, seri):
    y = seri["demo 27 agustus"]
    fig = polos_kanvas(9.0, 6.0)
    ax = fig.add_axes([0.085, 0.13, 0.895, 0.84])
    ax.patch.set_alpha(0)
    x = list(range(len(tgl)))
    ax.plot(x[:-1], y[:-1], color=AKSEN, lw=3.0, solid_capstyle="round", zorder=3)
    ax.plot(x[-2:], y[-2:], color=AKSEN, lw=3.0, ls=(0, (2, 2)), zorder=3)
    ax.scatter([x[-1]], [y[-1]], s=110, facecolor=LATAR, edgecolor=AKSEN, lw=3.0, zorder=4)
    ax.annotate("24 Agu — naik 4,8×\ndalam satu hari", (x[tgl.index("2026-08-24")], y[tgl.index("2026-08-24")]),
                textcoords="offset points", xytext=(-14, 16), ha="right", va="bottom",
                fontsize=15, color=TINTA, linespacing=1.4)
    ax.annotate("26 Agu — hari berjalan,\ndata belum lengkap", (x[-1], y[-1]),
                textcoords="offset points", xytext=(-16, -8), ha="right", va="top",
                fontsize=15, color=ABU, linespacing=1.4)
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100])
    tik = [i for i, s in enumerate(tgl) if s.endswith(("-01", "-08", "-15", "-22", "-26")) or i == 0]
    ax.set_xticks(tik)
    ax.set_xticklabels(["26 Jul" if tgl[i] == "2026-07-26" else
                        f"{int(tgl[i][8:])} {'Agu' if tgl[i][5:7]=='08' else 'Jul'}" for i in tik])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GARIS)
    ax.tick_params(colors=ABU, labelsize=15, length=0, pad=9)
    ax.grid(axis="y", color=GARIS, lw=1)
    ax.set_axisbelow(True)
    fig.savefig(GRAFIK / "grafik-3.png", dpi=120, transparent=True)
    plt.close(fig)


def grafik4_polos(seri):
    puncak = {k: max(v for v in s if v is not None) for k, s in seri.items()}
    urut = sorted(puncak.items(), key=lambda kv: kv[1])
    nama = {"demo 27 agustus": "“demo 27 agustus”", "MBG": "“MBG”",
            "RUU perampasan aset": "“RUU perampasan aset”",
            "hukuman mati koruptor": "“hukuman mati koruptor”"}
    fig = polos_kanvas(9.0, 5.2)
    ax = fig.add_axes([0.315, 0.04, 0.60, 0.92])
    ax.patch.set_alpha(0)
    for i, (k, v) in enumerate(urut):
        ax.barh(i, v, height=0.52, color=AKSEN if k == "demo 27 agustus" else REDAM, zorder=3)
        ax.text(v + 1.8, i, "<1" if v == 0.5 else f"{v:.0f}", va="center", fontsize=19,
                color=TINTA if k == "demo 27 agustus" else ABU,
                weight=800 if k == "demo 27 agustus" else 400)
    ax.set_yticks(range(len(urut)))
    ax.set_yticklabels([nama[k] for k, _ in urut], fontsize=18, color=TINTA)
    ax.set_xlim(0, 118)
    ax.set_xticks([])
    for s in ("top", "right", "bottom", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0, pad=12)
    fig.savefig(GRAFIK / "grafik-4.png", dpi=120, transparent=True)
    plt.close(fig)


def grafik5_polos(prov):
    geo = json.loads((MENTAH / "indonesia-prov.geojson").read_text(encoding="utf-8"))
    nilai = {samakan(k): v for k, v in prov.items()}
    fig = polos_kanvas(9.0, 5.0)
    ax = fig.add_axes([0.0, 0.20, 1.0, 0.80])
    ax.patch.set_alpha(0)
    tambal, warna = [], []
    for f in geo["features"]:
        v = nilai.get(samakan(f["properties"]["Propinsi"]))
        g = f["geometry"]
        for poli in (g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]):
            tambal.append(MplPolygon(poli[0], closed=True))
            warna.append(warna_bin(v))
    ax.add_collection(PatchCollection(tambal, facecolor=warna, edgecolor=LATAR, lw=0.5, zorder=2))
    ax.set_xlim(94.5, 141.5); ax.set_ylim(-11.5, 7.0)
    ax.set_aspect("equal"); ax.axis("off")
    lg = fig.add_axes([0.0, 0.0, 1.0, 0.18]); lg.axis("off"); lg.patch.set_alpha(0)
    for i, (c, l) in enumerate(zip(RAMPA, LABEL_BIN)):
        lg.add_patch(Rectangle((0.02 + i * 0.165, 0.58), 0.042, 0.26, facecolor=c, edgecolor="none"))
        lg.text(0.02 + i * 0.165, 0.42, l, color=ABU, fontsize=14, va="top")
    lg.add_patch(Rectangle((0.02, 0.06), 0.042, 0.26, facecolor=KOSONG, edgecolor="none"))
    lg.text(0.072, 0.30, "data tidak tersedia (Gorontalo, Sulawesi Barat)", color=ABU, fontsize=14, va="top")
    lg.set_xlim(0, 1); lg.set_ylim(0, 1)
    fig.savefig(GRAFIK / "grafik-5.png", dpi=120, transparent=True)
    plt.close(fig)


def main():
    tgl, seri = baca_harian()
    prov = baca_provinsi()
    slide1(seri); slide2(); slide3(tgl, seri); slide4(seri); slide5(prov); slide6()
    grafik3_polos(tgl, seri); grafik4_polos(seri); grafik5_polos(prov)
    print(f"font: {KELUARGA}")
    for p in sorted(GRAFIK.glob("*.png")):
        print(f"  {p.name}  {p.stat().st_size//1024} KB")


if __name__ == "__main__":
    main()
