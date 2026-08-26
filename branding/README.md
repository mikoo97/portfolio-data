# ceritadataa — identitas merek

Paket identitas untuk akun media sosial **ceritadataa**: data Indonesia, dibaca dari dekat.

Dokumen lengkapnya ada di **[`brandbook.html`](./brandbook.html)** — buka di peramban.
Berkas ini hanya ringkasan dan daftar aset.

## Lima keputusan inti

1. **Wilayah** — Indonesia dari unit terkecil (kabupaten, kecamatan, desa, RT), bukan angka nasional.
2. **Peran** — analis yang bercerita dengan suara orang pertama, bukan redaksi anonim.
3. **Bukti** — setiap unggahan membawa nama data, tahun, tanggal akses, dan cara mengolah.
4. **Bentuk** — satu grafik, satu kesimpulan; satu seri disorot, sisanya diredam abu.
5. **Ukuran** — sukses diukur dari simpanan + kiriman per 1.000 tayangan, bukan suka.

## Isi folder

| Berkas | Isi |
|---|---|
| `brandbook.html` | Buku merek lengkap: strategi, verbal, visual, standar grafik, rencana konten, peluncuran 90 hari, etika data |
| `tokens.css` | Warna & huruf sebagai variabel CSS |
| `tokens.json` | Nilai yang sama untuk skrip Python/JS |
| `logo/mark.svg` | Lambang, latar terang |
| `logo/mark-inverse.svg` | Lambang, latar gelap |
| `logo/mark-mono.svg` | Lambang satu warna (`currentColor`) |
| `logo/lockup-horizontal.svg` | Lambang + nama + tagline, mendatar |
| `logo/lockup-stacked.svg` | Lambang + nama + tagline, bertumpuk |
| `logo/avatar.svg` | Foto profil 1000×1000 |
| `logo/favicon.svg` | Tiga batang tanpa balon, untuk ukuran di bawah 24 px |

## Cara pakai

**Di situs / templat HTML** — impor `tokens.css`, lalu rujuk perannya:

```css
@import "branding/tokens.css";
.judul { font-family: var(--cd-font-tampil); color: var(--cd-tinta); }
.batang-disorot { background: var(--cd-seri-1-l); }
.batang-lain { background: var(--cd-redam-l); }
```

**Di skrip grafik (Python/JS)** — baca `tokens.json`:

```python
import json
t = json.load(open("branding/tokens.json"))
palet = t["color"]["categoricalLight"]   # 6 slot, dipakai berurutan
redam = t["color"]["mutedSeries"]["light"]
```

## Catatan produksi

- **Kuning `#FFC93C` tidak pernah jadi warna teks.** Hanya blok latar di belakang teks tinta.
- **Palet data sudah diuji**, terang dan gelap, terhadap rentang terang, kroma, keterbacaan bagi mata dengan buta warna, dan kontras permukaan. Kalau satu warna diganti, uji ulang seluruh set.
- **`lockup-*.svg` masih memakai teks hidup.** Ubah jadi *outline* sebelum dikirim ke percetakan atau pihak ketiga.
- Huruf: Plus Jakarta Sans, Newsreader, IBM Plex Mono — semuanya tersedia di Google Fonts.

## Asumsi

Strategi disusun dengan asumsi pemilik akun adalah analis data & geospasial di balik
proyek-proyek pada `data.json` (Dusun Krajan, Spatial Base System Indonesia,
Indonesia Mobility Flow Explorer, Sistem Peringatan Dini Tempursari).
Kalau asumsi itu keliru, yang perlu ditinjau ulang adalah bab 01 dan 05 buku merek;
bab 02–04 tetap berlaku.
