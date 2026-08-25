# Brief Konten #1 — Peta Percakapan Jelang 27 Agustus

- **Tayang:** Rabu, 26 Agustus 2026, 19.30 WIB (H-1)
- **Format:** Carousel 8 slide, 1080 × 1350
- **Pilar:** khusus peluncuran (masuk keluarga `#JumatLayar`, tagar `#ceritadataa`)
- **Batas data:** Selasa, 25 Agustus 2026, 23.59 WIB
- **Lanjutan:** Jumat 28 Agustus — versi H+1, banding sebelum vs sesudah

## 1. Sudut cerita

Godaan terbesar konten ini adalah membuatnya jadi "berapa persen setuju demo". Jangan. Itu tidak bisa diukur dari medsos, dan akun ini akan langsung terbaca sebagai akun opini.

Sudut yang dipakai: **anatomi percakapan, bukan jajak pendapat.**

> Dua hari sebelum orang turun ke jalan, percakapannya sudah lebih dulu ramai. Yang kita ukur bukan siapa yang benar — tapi kapan percakapan itu mulai, di mana ia hidup, isu apa yang dibawa, dan seberapa organik penyebarannya.

Ini sudut yang aman, jujur, dan justru lebih menarik. Ia juga langsung memperkenalkan janji akun: metode terbuka, keterbatasan diakui.

## 2. Konteks yang harus akurat

Diverifikasi dari pemberitaan 21–25 Agustus 2026. **Cek ulang sebelum tayang** — situasi bisa berubah dalam hitungan jam.

- Aksi direncanakan **Kamis, 27 Agustus 2026**, di depan Gedung DPR/MPR RI, Jalan Gatot Subroto, Senayan.
- Setidaknya ada **dua kubu dengan tuntutan berbeda**, dan ini inti kerumitan yang jarang ditangkap dengan benar:
  - **AMPB (Aliansi Masyarakat Pati Bersatu) dan ARIB** — pengesahan RUU Perampasan Aset dan hukuman mati bagi koruptor. Warga Pati sudah berada di depan DPR sejak sekitar 21 Agustus.
  - **Kelompok mahasiswa** — menuntut kejelasan nasib RUU Perampasan Aset.
  - **ARPI** — isu pekerja dapur MBG: kepastian kontrak kerja dan perlindungan pekerja.
  - **RMP4** — justru mendukung keberlanjutan program pemerintah termasuk MBG, dengan catatan perbaikan tata kelola.
  - Kelompok lain yang disebut polisi: DPP Brigade Merah Putih Indonesia, Aliansi Tiga Pilar Demokrasi Bogor Raya (isu RUU Perampasan Aset).
- **DPR** kembali menjanjikan percepatan pembahasan RUU Perampasan Aset menjelang aksi.
- **Polda Metro Jaya** menyiapkan pengamanan dan rekayasa lalu lintas situasional.
- **Satuan Siber Mabes TNI** mengimbau masyarakat tidak mudah terprovokasi, terutama di media sosial.
- Peneliti **Monash University Indonesia** menemukan dugaan pola amplifikasi terkoordinasi pada konten terkait demonstrasi, dari analisis percakapan di X, Instagram, TikTok, YouTube, dan Facebook periode **26 Juli – 1 Agustus 2026**.

Temuan Monash itu adalah kail terbaik untuk slide terakhir: ada pertanyaan terbuka tentang seberapa organik keramaian ini, dan kamu bisa menguji indikasinya sendiri dengan data yang bisa kamu ambil.

## 3. Lima pertanyaan riset

1. **Kapan mulai ramai?** Deret waktu harian volume percakapan dan pemberitaan, 1–25 Agustus. Adakah lonjakan mendadak, dan apa pemicunya?
2. **Di mana ia hidup?** Perbandingan volume antarkanal (YouTube, berita daring, Reddit, pencarian Google, TikTok).
3. **Isu apa yang dibawa?** Proporsi penyebutan: RUU Perampasan Aset · hukuman mati koruptor · MBG dan pekerja dapur · ketertiban dan lalu lintas · kecurigaan amplifikasi.
4. **Nada percakapan seperti apa?** Empat kelas: mendukung aksi · menolak atau meragukan aksi · netral-informatif · di luar topik.
5. **Seberapa organik?** Indikasi amplifikasi terkoordinasi: teks nyaris identik, lonjakan dalam jendela waktu sempit, akun baru.

## 4. Sumber dan cara mengambil

Jalankan `../scripts/ambil_data_27agustus.py`. Semua sumber di bawah gratis; hanya YouTube yang butuh kunci API.

| Sumber | Yang diambil | Peran di konten |
|---|---|---|
| **Google Trends** (pytrends) | Minat harian 30 hari untuk `demo 27 agustus`, `RUU perampasan aset`, `hukuman mati koruptor`, `MBG` + sebaran per provinsi | Deret waktu (slide 3) dan peta (slide 7) |
| **GDELT DOC 2.0** | `timelinevol` dan `timelinetone` untuk kueri bahasa Indonesia, `sourcecountry:ID` | Volume dan nada **pemberitaan** — beri label tegas: ini media, bukan medsos |
| **YouTube Data API v3** | `search.list` untuk video terkait, lalu `commentThreads.list` — target 2.000–3.000 komentar | Korpus utama untuk pelabelan nada dan isu |
| **Reddit** (`.json`) | Utas dan komentar di r/indonesia | Korpus pembanding, diskusi lebih panjang |
| **Wikipedia pageviews** | Kunjungan harian artikel terkait | Proxy perhatian publik yang bersih |
| **TikTok** | Pencatatan manual: jumlah video dan tayangan per tagar, dengan waktu tepat + tangkapan layar | Potret satu waktu — **bukan** deret waktu |
| **Monash University Indonesia** | Temuan amplifikasi terkoordinasi 26 Juli – 1 Agustus | Data sekunder, dikutip dengan atribusi penuh |

**X/Twitter tidak diambil.** API-nya berbayar dan pengikisan melanggar ketentuan. Ini justru harus ditulis di slide keterbatasan: X kemungkinan besar adalah kanal paling ramai untuk isu ini, dan ketidakhadirannya adalah lubang terbesar dalam analisis ini. Mengakui itu jauh lebih kuat daripada menyembunyikannya.

## 5. Metode pelabelan

**Unit analisis: satu komentar atau unggahan — bukan satu orang.** Satu orang bisa menulis lima puluh komentar. Ini harus disebut di slide keterbatasan.

**Pengambilan sampel.** Dari korpus penuh, ambil acak berlapis per kanal, minimal 500 komentar (target 800). Catat benih acaknya supaya bisa diulang.

**Pelabelan.** Kirim ke model bahasa dalam batch 25 komentar dengan buku kode di bawah, suhu 0. Lalu **periksa manual 15% secara acak** dan laporkan tingkat kesesuaiannya di slide metode. Kalau kesesuaian di bawah 80%, perbaiki buku kode dan ulangi.

Jangan pakai kamus sentimen mentah. Bahasa Indonesia di kolom komentar penuh sarkasme, singkatan, dan campur kode — kamus akan salah membaca "mantap sekali negara ini" sebagai positif.

### Buku kode

```
NADA (pilih satu)
  DUKUNG   — menyatakan setuju pada aksi/tuntutannya, mengajak ikut,
             memuji peserta aksi
  TOLAK    — menolak aksi, meragukan motifnya, menuduh ditunggangi,
             mengeluhkan dampaknya
  NETRAL   — menyampaikan informasi, bertanya, mengabarkan lokasi/jadwal,
             tanpa penilaian
  LUAR     — tidak berkaitan dengan aksi 27 Agustus, spam, promosi

ISU (boleh lebih dari satu, boleh kosong)
  ASET     — RUU Perampasan Aset, penyitaan aset koruptor
  MATI     — hukuman mati bagi koruptor
  MBG      — program MBG, pekerja dapur, kontrak kerja
  TERTIB   — lalu lintas, keamanan, kekhawatiran kericuhan
  BUZZER   — kecurigaan akun bayaran, amplifikasi, penggiringan opini
  DPR      — kinerja DPR, janji legislasi

Kalau ragu antara dua nada, pilih NETRAL.
Sarkasme dinilai berdasarkan maksud, bukan kata harfiah.
```

### Indikator amplifikasi

Hitung tiga hal, laporkan sebagai **indikasi**, bukan bukti:

1. **Kembar teks** — proporsi komentar dengan kemiripan ≥ 0,9 (SimHash atau kosinus TF-IDF) terhadap komentar lain.
2. **Lonjakan sempit** — persentase unggahan yang jatuh dalam jendela 10 menit yang sama.
3. **Akun muda** — proporsi akun berusia < 90 hari, bila metadatanya tersedia.

Kalimat yang dipakai di slide: *"Pola ini konsisten dengan amplifikasi terkoordinasi, tapi tidak membuktikannya. Percakapan asli juga bisa melonjak serentak."* Jangan pernah menulis kata "buzzer" sebagai kesimpulan — hanya sebagai kategori isu yang **dibicarakan warganet**.

## 6. Storyboard

| Slide | Isi | Visual |
|---|---|---|
| 1 | **Kail.** "Aksinya baru besok. Percakapannya sudah tiga minggu berjalan." + angka besar: jumlah komentar yang dianalisis | Angka besar, tanpa grafik |
| 2 | **Apa yang terjadi 27 Agustus.** Siapa turun, di mana, menuntut apa — semua kubu, netral, tanpa penilaian | Daftar bergaya kartu: 4 kelompok, 4 tuntutan |
| 3 | **Kapan mulai ramai.** Deret waktu harian 1–25 Agustus, diberi anotasi kejadian (warga Pati tiba 21 Agu; janji DPR; imbauan aparat) | Grafik garis, dua seri: minat pencarian + volume berita |
| 4 | **Di mana ia hidup.** Perbandingan antarkanal | Batang horizontal, dengan catatan bahwa cakupan tiap kanal berbeda |
| 5 | **Isu apa yang dibawa.** Enam kategori isu berdasarkan frekuensi | Batang horizontal, dua warna aksen |
| 6 | **Nada percakapan.** Empat kelas, per kanal | Batang bertumpuk 100% |
| 7 | **Di mana orang mencarinya.** Peta provinsi dari sebaran minat Google Trends | Peta koroplet — tanda tangan visualmu |
| 8 | **Cara baca, keterbatasan, sumber.** Termasuk: X tidak tercakup; medsos bukan opini publik; unit analisis komentar bukan orang; temuan Monash sebagai pembanding | Teks, hierarki rapi |

Slide 7 sengaja diletakkan menjelang akhir: peta adalah yang paling mungkin membuat orang berhenti menggeser, dan ia memperkenalkan kekuatan utama akun sejak unggahan pertama.

## 7. Kalimat kunci untuk slide

Isi angkanya setelah data masuk. Jangan biarkan Gemini menulis ulang kalimat-kalimat ini.

- Slide 1: `Aksinya baru besok. Percakapannya sudah tiga minggu berjalan.` / `[N] komentar dan unggahan dianalisis · 1–25 Agustus 2026`
- Slide 3: `Percakapan melonjak [N]× setelah [pemicu] pada [tanggal].`
- Slide 4: `[Kanal] paling ramai — tapi setiap kanal punya cakupan berbeda, jadi ini bukan lomba.`
- Slide 5: `[N] dari 10 komentar menyebut RUU Perampasan Aset. Isu yang paling jarang muncul justru [isu].`
- Slide 6: `[N]% netral. Percakapan yang ramai belum tentu percakapan yang terbelah.`
- Slide 7: `Yang paling banyak mencari bukan Jakarta, tapi [provinsi].`
- Slide 8: `Yang tidak bisa disimpulkan dari data ini: berapa banyak orang Indonesia yang mendukung atau menolak aksi ini. Pengguna media sosial bukan sampel penduduk.`

## 8. Caption

```
Aksinya baru besok. Percakapannya sudah tiga minggu berjalan.

Aku kumpulkan [N] komentar dan unggahan soal rencana aksi 27 Agustus dari
YouTube, Reddit, pemberitaan daring, dan data pencarian Google — 1 sampai
25 Agustus 2026 — lalu melabelinya satu per satu.

Tiga hal yang aku temukan:
1. Percakapan tidak naik perlahan. Ia melonjak [N]× dalam [N] hari setelah [pemicu].
2. Isu yang dibawa tidak tunggal: RUU Perampasan Aset, hukuman mati koruptor,
   nasib pekerja dapur MBG, sampai kecurigaan terhadap keramaiannya sendiri.
3. [N]% komentar sebenarnya netral — mengabarkan lokasi, jadwal, dan rute.
   Yang paling keras terdengar bukan yang paling banyak.

Cara membacanya: ini peta percakapan, bukan jajak pendapat.

Yang tidak bisa disimpulkan dari data ini: berapa banyak orang Indonesia
yang mendukung atau menolak aksi ini. Pengguna media sosial bukan sampel
penduduk, X tidak tercakup karena datanya berbayar, dan satu orang bisa
menulis lima puluh komentar.

Metode lengkap dan keterbatasannya aku bahas Minggu nanti di #MingguDapur.

Sumber: YouTube Data API v3, GDELT DOC 2.0, Reddit, Google Trends,
Wikipedia Pageviews — diakses 25 Agustus 2026. Konteks aksi dari
pemberitaan Kompas, Kontan, Tirto, Bisnis, 21–25 Agustus 2026. Temuan
amplifikasi terkoordinasi: peneliti Monash University Indonesia.

Buat kamu: dari lima isu di slide 5, mana yang paling jarang kamu lihat
dibahas di beranda kamu?

#ceritadataa #JumatLayar #visualisasidata #datajurnalisme #dataindonesia
#analisismedsos #RUUPerampasanAset #27Agustus #infografis #literasidata
```

## 9. Risiko dan pagar pengaman

| Risiko | Pagar |
|---|---|
| Terbaca memihak salah satu kubu | Tampilkan **semua** kelompok dan tuntutannya di slide 2. Pakai kata `aksi` dan `unjuk rasa`, bukan istilah bermuatan. Jangan menilai tuntutan siapa pun. |
| Dituduh menuduh "buzzer" | Kata itu hanya muncul sebagai kategori isu yang dibicarakan warganet. Indikator amplifikasi disebut sebagai indikasi, dengan kalimat penyangkal eksplisit. |
| Data pribadi ikut tayang | Tidak ada nama akun, tidak ada tangkapan layar komentar. Kalau perlu contoh, parafrase sampai tidak bisa dicari balik. |
| Angka berubah setelah tayang | Batas data ditulis jelas di slide 8 dengan tanggal dan jam. Versi H+1 pada 28 Agustus jadi pembaruannya. |
| Situasi memburuk di lapangan | Kalau terjadi kekerasan atau korban, **hentikan seri ini**. Konten analitik tentang percakapan menjadi tidak pantas saat orang terluka. Ganti ke pilar lain, kembali setelah situasi jelas. |
| Jangkauan kecil karena batasan konten politik | Sudah diperhitungkan. Nilai unggahan ini adalah kredibilitas dan jumlah simpan, bukan tayangan. |

## 10. Jadwal pengerjaan

**Selasa 25 Agustus**
- 19.00–20.30 — jalankan skrip pengambilan data, periksa hasilnya
- 20.30–22.00 — pelabelan batch + pemeriksaan manual 15%
- 22.00–23.00 — hitung agregat, hasilkan `data-siap.csv`

**Rabu 26 Agustus**
- 09.00–11.00 — render tujuh grafik dari kode, ekspor PNG transparan
- 11.00–12.00 — tulis `teks-slide.txt` dengan angka final
- 13.00–15.00 — kirim brief ke Gemini, tinjau, revisi satu putaran
- 15.00–16.00 — daftar periksa QC, verifikasi ulang konteks berita hari itu
- 19.30 — tayang, lalu Story, lalu balas komentar sampai 21.00
