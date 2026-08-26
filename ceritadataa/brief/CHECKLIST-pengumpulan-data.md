# Daftar Periksa Pengumpulan Data — Konten #1

Selasa 25 Agustus 2026. Batas data: **23.59 WIB**.
Semua hasil masuk ke `ceritadataa/konten/2026-08-26-sentimen-27-agustus/data-mentah/`.

Perkiraan waktu total: **2–2,5 jam.** Tugas 1, 5, dan 6 wajib. Sisanya boleh gugur tanpa membatalkan konten.

---

## Cara mengirim hasilnya ke Claude

Lewat git — jangan tempel CSV besar ke obrolan.

```bash
git checkout claude/ceritadataa-content-plan-zmqdqz
git pull origin claude/ceritadataa-content-plan-zmqdqz
# taruh semua berkas di ceritadataa/konten/2026-08-26-sentimen-27-agustus/data-mentah/
git add -A
git commit -m "Data mentah konten 1"
git push -u origin claude/ceritadataa-content-plan-zmqdqz
```

> **Cek dulu repo ini publik atau privat.** Kalau publik, **jangan** commit korpus komentar mentah — meski tanpa nama akun, mengunggah ribuan komentar orang ke repo terbuka bukan praktik yang mau kita bela di slide metode. Kalau publik: commit hanya berkas Trends, kronologi, kelompok, dan snapshot; korpus komentarnya kirim terpisah atau jadikan repo ini privat dulu.

---

## TUGAS 1 — Google Trends ★ wajib

**Waktu: 20 menit. Tanpa kunci API. Ini yang menghidupi slide 3 dan slide 7 (peta).**

Coba dulu lewat skrip. Kalau `pytrends` kena 429 atau gagal — sering terjadi — kerjakan manual, dan itu tidak apa-apa.

### Manual, langkah demi langkah

**1a. Deret waktu (untuk slide 3)**

1. Buka `trends.google.com/trends/explore?geo=ID`
2. Kata kunci pertama: `demo 27 agustus`
3. Wilayah: **Indonesia**
4. Rentang waktu: Custom → **1 Agu 2026 – 25 Agu 2026**
5. Klik **+ Compare**, tambahkan tiga lagi: `RUU perampasan aset`, `hukuman mati koruptor`, `MBG`
6. Di panel *Interest over time*, klik ikon unduh (panah ke bawah, kanan atas)
7. Simpan sebagai **`trends_harian.csv`**

**1b. Peta provinsi (untuk slide 7)**

Ini unduhan **terpisah**, dan urutannya penting:

1. Hapus semua pembanding — sisakan **satu kata kunci saja**: `demo 27 agustus`
2. Rentang dan wilayah sama seperti di atas
3. Gulir ke panel *Compared breakdown by subregion* → ubah ke **Region**
4. Unduh, simpan sebagai **`trends_provinsi.csv`**

> **Kenapa harus terpisah:** indeks Trends dinormalisasi terhadap puncak **di dalam satu set perbandingan**. Kalau peta diunduh sambil membandingkan empat kata kunci, warna provinsinya jadi campuran keempatnya dan tidak berarti apa-apa. Satu kata kunci, satu peta.
>
> Konsekuensi lain: **jangan pernah membandingkan angka antar dua unduhan berbeda.** Angka 100 di satu berkas bukan angka yang sama dengan 100 di berkas lain.

**Kriteria selesai:** `trends_harian.csv` berisi 25 baris tanggal; `trends_provinsi.csv` berisi daftar provinsi (idealnya 38, tapi provinsi dengan volume rendah bisa kosong — itu normal, jangan diisi nol, biarkan kosong dan tandai abu di peta).

---

## TUGAS 2 — YouTube ☆ opsional tapi bernilai tinggi

**Waktu: 15 menit setup + 20 menit jalan. Ini korpus utama slide 5 dan 6.**

### Ambil kunci API (gratis, tanpa kartu kredit)

1. `console.cloud.google.com` → **New Project**, namai `ceritadataa`
2. **APIs & Services → Library** → cari **YouTube Data API v3** → **Enable**
3. **APIs & Services → Credentials → Create Credentials → API key**
4. Salin kuncinya:
   ```bash
   export YOUTUBE_API_KEY='...'
   ```

### Jalankan

```bash
python3 ceritadataa/scripts/ambil_data_27agustus.py --mulai 2026-08-01 --sampai 2026-08-25
```

**Yang perlu kamu tahu soal kuota:** jatahnya 10.000 unit per hari. `search.list` mahal (100 unit sekali panggil), `commentThreads.list` murah (1 unit). Empat kueri berarti 400 unit untuk pencarian, sisanya lebih dari cukup untuk komentar.

Kalau muncul `403 quotaExceeded`, kuotamu habis dan **baru pulih pukul 14.00–15.00 WIB besok** (tengah malam waktu Pasifik). Kalau itu terjadi malam ini, hentikan — jangan kejar, kita jalan tanpa YouTube.

**Target:** ≥2.000 komentar. Di bawah 500, slide 6 harus dicoret.

---

## TUGAS 3 — GDELT, Reddit, Wikipedia ☆ otomatis

Ikut jalan bersama Tugas 2, tanpa kunci apa pun. Setelah selesai, buka `data-mentah/manifest.json` dan periksa kolom `jumlah_baris`.

Kalau ada yang **0**, catat nama kanalnya dan kabari aku — jangan didiamkan, karena aku perlu tahu slide mana yang kehilangan tumpuan.

---

## TUGAS 4 — Snapshot manual ☆ 20 menit

Ini potret satu waktu, bukan deret waktu. Yang membuatnya sah adalah **jam pencatatan** dan **bukti tangkapan layar**.

Buat `data-mentah/snapshot_manual.csv` dengan kolom persis ini:

```csv
platform,tagar,ukuran,nilai,waktu_wib,berkas_tangkapan_layar,catatan
TikTok,#demo27agustus,jumlah_tayangan,,2026-08-25 21:15,tiktok-1.png,
TikTok,#27agustus,jumlah_tayangan,,2026-08-25 21:17,tiktok-2.png,
TikTok,#ruuperampasanaset,jumlah_tayangan,,2026-08-25 21:19,tiktok-3.png,
Instagram,#ruuperampasanaset,jumlah_kiriman,,2026-08-25 21:22,ig-1.png,
X,27 Agustus,peringkat_trending,,2026-08-25 21:25,x-1.png,"kosongkan kalau tidak masuk trending"
```

**Untuk X: cukup lihat halaman trending yang memang publik, catat peringkatnya, tangkap layar.** Mengamati boleh; menarik datanya tidak. Jangan pasang alat pengikis apa pun.

---

## TUGAS 5 — Kronologi ★ wajib, jangan diremehkan

**Waktu: 30 menit. Ini yang membuat slide 3 punya arti — grafik tanpa anotasi cuma garis naik-turun.**

Buat `data-mentah/kronologi.csv`:

```csv
tanggal,peristiwa,media,url,tanggal_akses,konfirmasi
```

Kolom `konfirmasi` diisi `ganda` kalau kamu menemukannya di **dua media independen**, `tunggal` kalau hanya satu.

**Aturan:** hanya peristiwa berkonfirmasi `ganda` yang boleh jadi anotasi di slide 3. Yang `tunggal` boleh disimpan, tapi tidak tayang.

### Yang harus kamu cari (enam baris minimum)

| # | Cari ini | Petunjuk pencarian |
|---|---|---|
| 1 | Kapan seruan aksi 27 Agustus **pertama** muncul di pemberitaan | Cari dengan rentang tanggal dibatasi ke awal Agustus. Ini yang paling sulit dan paling berharga — ia menentukan titik awal cerita. |
| 2 | Tanggal warga Pati tiba / menduduki depan DPR | Sekitar 21 Agustus menurut Suara.com — **konfirmasi tanggal pastinya** |
| 3 | Pernyataan DPR soal percepatan pembahasan RUU Perampasan Aset | Kompas.id memberitakan ini menjelang aksi |
| 4 | Pernyataan Polda Metro Jaya soal pengamanan dan rekayasa lalu lintas | Bisnis.com, sekitar 24 Agustus |
| 5 | Imbauan Satuan Siber Mabes TNI agar tidak terprovokasi | Kompas TV |
| 6 | Peristiwa apa pun antara 23–25 Agustus yang bisa menjelaskan lonjakan pencarian | Ini yang paling penting sekarang: data Trends menunjukkan lonjakan tajam 23→24 Agustus. Cari pemicunya — pernyataan pejabat, video viral, seruan yang menyebar. |

Nomor 6 yang paling penting sekarang, karena datanya sudah menunjuk ke sana. Kalau pemicunya tidak ketemu, slide 3 tetap jalan — anotasinya cukup menandai lonjakannya tanpa mengarang sebabnya.

---

## TUGAS 6 — Kelompok dan tuntutan ★ wajib

**Waktu: 25 menit. Ini isi slide 2, dan slide inilah yang paling berisiko membuatmu terlihat memihak kalau salah.**

Buat `data-mentah/kelompok_tuntutan.csv`:

```csv
singkatan,kepanjangan,asal_daerah,tuntutan_utama,posisi,sumber_url,media,tanggal_akses
```

Kolom `posisi` diisi salah satu: `menuntut-pemerintah`, `mendukung-pemerintah`, atau `isu-sektoral`.

### Yang sudah kutemukan — semuanya perlu kamu konfirmasi ulang

| Singkatan | Perlu dicari |
|---|---|
| AMPB | Kepanjangannya (dugaan: Aliansi Masyarakat Pati Bersatu) + tuntutan persisnya |
| ARIB | **Kepanjangan belum jelas.** Kalau tidak ketemu, jangan tayangkan. |
| ARPI | Kepanjangan + rincian tuntutan soal pekerja dapur MBG |
| RMP4 | **Kepanjangan belum jelas.** Ini kelompok yang mendukung program pemerintah — justru penting supaya slide 2 tidak berat sebelah. |
| DPP Brigade Merah Putih Indonesia | Konfirmasi ikut atau tidak |
| Aliansi Tiga Pilar Demokrasi Bogor Raya | Konfirmasi ikut atau tidak |
| Kelompok mahasiswa | Nama aliansi/BEM yang spesifik, jangan generik |

**Aturan keras:** kalau sebuah kelompok hanya disebut satu media **dan** kepanjangannya tidak jelas, jangan ditayangkan. **Empat kelompok yang solid jauh lebih baik daripada tujuh yang setengah matang.** Salah menulis nama organisasi di unggahan pertama adalah cara tercepat kehilangan kepercayaan.

**Aturan kedua:** slide 2 harus memuat sedikitnya satu kelompok dari **tiap** posisi. Kalau kamu hanya menemukan kelompok yang menuntut pemerintah, cari lebih keras yang mendukung — ketimpangan di slide 2 akan langsung dibaca sebagai keberpihakan.

---

## TUGAS 7 — Verifikasi ulang, Rabu pagi ★ wajib

**Waktu: 15 menit, sebelum grafik dikunci.**

Tiga pertanyaan:

1. Aksinya masih jadi digelar 27 Agustus?
2. Lokasinya masih di depan DPR, atau bertambah/berpindah?
3. Ada kelompok yang baru bergabung atau mengundurkan diri?

Kalau ada yang berubah, kabari aku — slide 2 direvisi, dan kalau perubahannya besar, sudut kontennya yang disesuaikan, bukan datanya yang dipaksakan.

---

## Kriteria selesai malam ini

Centang sebelum tidur:

- [ ] `trends_harian.csv` — 25 baris tanggal
- [ ] `trends_provinsi.csv` — daftar provinsi, satu kata kunci saja
- [ ] `kronologi.csv` — ≥5 baris, ≥3 di antaranya berkonfirmasi `ganda`
- [ ] `kelompok_tuntutan.csv` — ≥4 baris, mencakup ≥2 posisi berbeda
- [ ] `snapshot_manual.csv` — ≥3 baris + tangkapan layar
- [ ] `manifest.json` — sudah dibaca, kanal yang gagal sudah dicatat
- [ ] Sudah di-`push` ke branch
- [ ] *(kalau sempat)* korpus komentar ≥500 baris

Empat centang pertama sudah cukup untuk enam dari delapan slide. Sisanya bonus.

---

## Yang aku kerjakan malam ini

- `render_grafik.py` — semua grafik slide 3–7, palet dan tipografi sudah terkunci, jalan dengan data contoh dulu
- `label_sentimen.py` — pemilihan sampel acak berbenih, pelabelan batch pakai buku kode, berkas pemeriksaan manual 15%
- Basis peta provinsi untuk slide 7
- Kerangka `teks-slide.txt` dan brief Gemini, dengan tempat kosong untuk angka
