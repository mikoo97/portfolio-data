# Konten #1 — Peta pencarian jelang 27 Agustus

**Tayang:** Rabu 26 Agustus 2026, 19.30 WIB · carousel 6 slide, 1080 × 1350
**Batas data:** 26 Agustus 2026, 17.00 WIB

## Temuan

1. Indeks pencarian "demo 27 agustus" nol sampai 15 Agustus; lonjakan terbesar 24 Agustus (4,8× dalam sehari).
2. Pada 26 Agustus, "demo 27 agustus" 20× "RUU perampasan aset"; "hukuman mati koruptor" tidak pernah > <1 selama 32 hari.
3. Sebaran provinsi: Jakarta 100, Banten 37, Jawa Barat 22, **DI Yogyakarta 18** — di atas Jawa Tengah dan Jawa Timur (14).

## Isi map

```
data-mentah/trends_harian.csv       unduhan Google Trends, 4 kata kunci, 26 Jul–26 Agu
data-mentah/trends_provinsi.csv     unduhan Google Trends, 1 kata kunci, per provinsi
data-mentah/indonesia-prov.geojson  geometri 34 provinsi
render_slide.py                     merender keenam slide dari CSV di atas
grafik/slide-1.png … slide-6.png    keluaran siap unggah
caption.md                          caption final + catatan produksi
```

Jalankan ulang kapan saja: `python3 render_slide.py`. Tidak ada angka yang diketik
tangan di dalam gambar — semuanya dibaca dari CSV.
