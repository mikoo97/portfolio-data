# Ritme Produksi

## 1. Prinsip: batch, bukan harian

Jangan mencari data setiap hari. Kalau tiap hari kamu mulai dari nol, akun ini mati dalam sebulan. Yang harian adalah **tayangnya**, bukan risetnya.

```
MINGGU sore  →  Hari Dapur: riset dan tarik data untuk 7 hari ke depan (3–4 jam)
SENIN–SABTU  →  tiap hari: hitung akhir, storyboard, brief ke Gemini, QC, tayang (1–1,5 jam)
```

Yang keluar dari Hari Dapur adalah tujuh map, masing-masing berisi: satu pertanyaan, satu berkas data mentah, dan satu tautan sumber. Itu saja. Belum perlu grafik.

## 2. Tujuh langkah tiap unggahan

| # | Langkah | Keluaran | Siapa |
|---|---|---|---|
| 1 | **Pertanyaan** — tulis satu kalimat tanya. Kalau tidak bisa dijawab angka, buang. | satu baris di `README` map konten | kamu |
| 2 | **Sumber** — cari dan unduh data mentah. Simpan apa adanya, jangan diedit. | `data-mentah/…` + catatan tanggal akses | kamu (+ aku) |
| 3 | **Hitung** — bersihkan dan agregasi lewat skrip, bukan lewat klik. | `skrip.py` + `data-siap.csv` | kamu (+ aku) |
| 4 | **Storyboard** — tentukan berapa slide, grafik apa, judul temuan tiap slide. | `storyboard.md` | kamu + aku |
| 5 | **Grafik** — render grafik jadi PNG transparan atau SVG dari `data-siap.csv`. | `grafik/*.png` | kamu |
| 6 | **Tata letak** — susun slide, ilustrasi, ikon, penyempurnaan tipografi. | berkas desain | Gemini |
| 7 | **QC + tayang** — cocokkan tiap angka ke data siap, cek sumber, tanggal, disclaimer. | unggahan | kamu |

**Aturan paling penting di seluruh dokumen ini:** langkah 5 tidak boleh dikerjakan model gambar. Angka, sumbu, label, dan proporsi batang dibuat dari kode (matplotlib, plotly, atau D3), lalu diekspor. Model gambar rutin menggeser angka, mengarang label, dan membuat panjang batang tidak sesuai nilainya. Satu batang yang salah panjang menghapus kredibilitas yang dibangun berminggu-minggu.

Gemini mengerjakan yang memang kuat: komposisi, hierarki visual, warna, ilustrasi, ikon, dan variasi tata letak.

## 3. Templat brief untuk Gemini

Kirim persis format ini setiap kali. Sertakan PNG grafik dan daftar teks yang harus muncul — jangan biarkan Gemini menulis ulang teksnya.

```
KONTEKS
Akun Instagram visualisasi data berbahasa Indonesia, @ceritadataa.
Pilar hari ini: [Senin Kuasa / …]. Warna aksen: [#kode].

FORMAT
Carousel [8] slide, 1080 × 1350 piksel, latar #F4F1EA, tinta #16161A,
huruf Plus Jakarta Sans. Margin aman 90 px kiri-kanan, 120 px atas-bawah.
Jangan letakkan apa pun penting di 250 px paling bawah.

ASET TERLAMPIR
- grafik-1.png … grafik-n.png  (transparan, sudah final — JANGAN digambar ulang,
  jangan diubah proporsinya, jangan diberi label tambahan)
- teks-slide.txt  (teks persis tiap slide — salin apa adanya, jangan diparafrase,
  jangan mengubah satu angka pun)

TUGASMU
1. Susun tata letak tiap slide sesuai struktur di teks-slide.txt.
2. Buat hierarki visual: judul temuan paling menonjol, catatan kaki paling kecil
   tapi tetap terbaca (minimal 22 px).
3. Tambahkan elemen grafis sederhana: garis pemisah, nomor slide, penanda pilar
   di sudut, ikon minimal bergaya garis.
4. Slide 1 harus terbaca sebagai gambar mini di feed: satu angka besar, satu pertanyaan.

LARANGAN
- Jangan membuat, mengubah, atau menggambar ulang grafik apa pun.
- Jangan mengubah, membulatkan, atau menerjemahkan angka.
- Jangan menambah klaim, kesimpulan, atau kalimat yang tidak ada di teks-slide.txt.
- Jangan pakai gambar orang, bendera partai, atau logo lembaga.
- Jangan pakai gradien pelangi, bayangan tebal, atau lebih dari dua warna aksen.

KELUARAN
[8] berkas PNG 1080 × 1350, diberi nama slide-01.png … slide-08.png.
```

## 4. Daftar periksa QC sebelum tayang

Jalankan setiap kali. Butuh sepuluh menit dan menyelamatkan reputasi.

- [ ] Setiap angka di slide cocok dengan satu baris di `data-siap.csv`
- [ ] Nama lembaga dan nama dataset ditulis lengkap dan benar
- [ ] Tanggal akses data tercantum
- [ ] Satuan jelas (rupiah nominal atau riil? per kapita atau total? per tahun mana?)
- [ ] Sumbu Y grafik batang mulai dari nol
- [ ] Ada slide keterbatasan yang menyebutkan apa yang **tidak** bisa disimpulkan
- [ ] Angka estimasi/hitungan sendiri diberi label `estimasi`
- [ ] Tidak ada nama orang, nama akun, atau tangkapan layar unggahan pribadi
- [ ] Teks terkecil ≥ 22 px, dicek dengan melihat gambar di layar ponsel
- [ ] Caption memuat sumber lengkap dan satu pertanyaan untuk pembaca
- [ ] Berkas data mentah, skrip, dan CSV siap tersimpan — kalau ada yang membantah, kamu bisa buktikan dalam dua menit

## 5. Enam puluh menit pertama setelah tayang

- Bagikan ke Story dengan stiker "usul topik besok".
- Balas semua komentar dalam satu jam pertama.
- Sebar ke satu kanal luar (Threads / X / LinkedIn) dengan kalimat pembuka yang berbeda dari caption.
- Catat angka jangkauan pada H+1 pukul 20.00, bukan lebih awal.

## 6. Struktur map per konten

```
ceritadataa/konten/2026-08-26-sentimen-27-agustus/
├── README.md          ← pertanyaan, ringkasan temuan, status
├── data-mentah/       ← unduhan apa adanya + manifest.json (sumber, waktu unduh)
├── skrip.py           ← pembersihan dan agregasi
├── data-siap.csv      ← tabel final yang jadi dasar grafik
├── grafik/            ← PNG/SVG hasil render
├── teks-slide.txt     ← teks persis tiap slide untuk Gemini
└── caption.md         ← caption final + tagar
```

Struktur yang sama untuk setiap konten. Setelah sebulan kamu punya arsip yang bisa diaudit — dan bahan portofolio yang jauh lebih meyakinkan daripada tangkapan layar feed.
