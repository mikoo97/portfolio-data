# Strategi Akun @ceritadataa

## 1. Posisi

> **Satu pertanyaan sehari, dijawab dengan data yang bisa kamu cek sendiri.**

Yang membedakan akun ini dari akun infografis lain bukan grafiknya — grafik bagus sudah banyak. Pembedanya tiga:

1. **Sumber selalu terbuka.** Setiap unggahan menyebut sumber, tanggal akses, dan cara menghitungnya. Slide sumber bukan basa-basi, tapi bagian dari produk.
2. **Keterbatasan ikut ditulis.** Akun ini mengaku apa yang tidak bisa disimpulkan dari datanya. Ini yang membuat orang percaya jangka panjang.
3. **Spasial jadi senjata.** Kamu punya kemampuan yang jarang dimiliki akun sejenis: peta tematik yang benar secara kartografi. Pakai itu sebagai tanda tangan visual.

**Bukan** akun opini politik. Bukan akun "fakta unik". Bukan akun berita. Kalau sebuah topik tidak bisa dijawab dengan data yang bisa diverifikasi, topik itu dilewat.

## 2. Sasaran pembaca

- Inti: mahasiswa dan pekerja muda 18–34, melek isu, suka menyimpan konten untuk dibagikan ulang.
- Lapis kedua: jurnalis, peneliti, ASN muda, pegiat data — kelompok kecil tapi menentukan kredibilitas dan sering membagikan ke jaringan yang lebih besar.

Tulis untuk pembaca yang pintar tapi tidak punya waktu. Jangan menggurui, jangan menyederhanakan sampai salah.

## 3. Bio dan profil

```
ceritadataa
Cerita Data
Satu pertanyaan sehari, dijawab dengan data terbuka.
Politik · Kependudukan · Ekonomi · Peta · Iklim
Sumber selalu dicantumkan · Indonesia
↳ [tautan ke masmik.netlify.app]
```

- Foto profil: satu bentuk geometris sederhana yang terbaca di ukuran 40 piksel (bukan grafik rumit, bukan wajah).
- Sorotan Story: `Mulai di sini` · `Sumber Data` · `Cara Baca Grafik` · `Koreksi` · `Peta`.
- Sorotan `Koreksi` itu penting. Akun data yang punya rak koreksi terbuka jauh lebih dipercaya daripada akun yang seolah tak pernah salah.

## 4. Sistem visual

Sistem ini yang kamu serahkan ke Gemini sebagai aturan tetap. Jangan biarkan berubah tiap unggahan — konsistensi adalah setengah dari branding.

**Kanvas**
- Carousel feed: 1080 × 1350 (4:5). Selalu 4:5, jangan 1:1 — 4:5 memakan layar paling banyak.
- Story dan Reels: 1080 × 1920.
- Margin aman: 90 px kiri-kanan, 120 px atas-bawah. Elemen penting jangan masuk 250 px paling bawah (tertutup UI dan caption).

**Warna**
- Latar: `#F4F1EA` (krem kertas). Tinta: `#16161A`. Abu netral: `#8A8A85`.
- Aksen per pilar — satu warna per hari, jadi orang mengenali pilar sebelum membaca judul:
  - Senin Kuasa `#B3261E` · Selasa Kita `#1F6F5C` · Rabu Rupiah `#C77D22`
  - Kamis Peta `#2B4C7E` · Jumat Layar `#7A3E9D` · Sabtu Bumi `#3E7A46` · Minggu Dapur `#5A5A55`
- Aturan tinta data: maksimal dua warna berarti dalam satu grafik, sisanya abu. Kalau butuh lebih dari lima warna, grafiknya salah pilih.

**Huruf**
- Satu keluarga huruf saja: Plus Jakarta Sans (buatan Indonesia, gratis, lengkap). Judul Bold/ExtraBold, isi Regular, angka Medium.
- Skala tetap: Judul 72 px · Sub 40 px · Isi 32 px · Label grafik 26 px · Catatan kaki 22 px.
- Jangan pernah kurang dari 22 px. Kalau tidak muat, isinya yang dipotong, bukan hurufnya.

**Anatomi carousel 8 slide**

| Slide | Isi |
|---|---|
| 1 | Kail: satu angka besar + satu pertanyaan. Tanpa grafik. |
| 2 | Konteks: kenapa ini penting sekarang, 3–4 baris. |
| 3–5 | Grafik utama. Satu grafik, satu gagasan, satu kalimat judul yang menyatakan temuan (bukan "Grafik 1"). |
| 6 | Jadi apa artinya. Tiga poin, kalimat pendek. |
| 7 | Cara baca dan keterbatasan. Apa yang **tidak** bisa disimpulkan dari data ini. |
| 8 | Sumber, tanggal akses, metode singkat, ajakan (simpan / bagikan / usul topik). |

Slide 7 adalah slide yang paling jarang dibuat akun lain dan paling sering membuat orang menyimpan unggahan.

## 5. Rumus caption

```
[1 baris kail — ulangi temuan utama, jangan ulangi judul slide 1]

Tiga hal yang aku temukan:
1. …
2. …
3. …

Cara membacanya: […satu kalimat…]
Yang tidak bisa disimpulkan dari data ini: […satu kalimat…]

Sumber: […nama lembaga, nama dataset, diakses [tanggal]…]
Pertanyaan buat kamu: […satu pertanyaan yang mudah dijawab di kolom komentar…]

#ceritadataa #[tagar pilar] + 8–12 tagar lain
```

**Tagar tiga lapis** (total 10–15, jangan lebih):
- Milik sendiri: `#ceritadataa` + tagar pilar (`#SeninKuasa` dan seterusnya).
- Topik: `#datavisualization` `#visualisasidata` `#datajurnalisme` `#infografis` `#dataindonesia`
- Isi: menyesuaikan topik (`#RUUPerampasanAset`, `#kependudukan`, `#BPS`, `#peta`).

## 6. Metrik yang dipantau

Jangan kejar suka. Untuk akun data, urutan pentingnya:

1. **Simpan (saves)** — tanda kontennya berguna. Target: ≥ 3% dari jangkauan.
2. **Bagikan (shares)** — tanda kontennya layak diteruskan. Target: ≥ 2%.
3. **Pengikut baru per unggahan** — tanda pilarnya menarik orang.
4. Waktu tonton carousel / persentase yang sampai slide terakhir.
5. Suka dan komentar — paling akhir.

Catat di satu lembar sederhana tiap Minggu: tanggal, pilar, judul, jangkauan, simpan, bagikan, pengikut baru. Setelah empat minggu, kamu punya bukti pilar mana yang hidup dan mana yang perlu diganti. Jangan ubah pilar sebelum empat minggu — datanya belum cukup.

## 7. Aturan etika dan hukum

Ini bukan hiasan. Akun data yang salah satu kali bisa kehilangan kepercayaan selamanya.

1. **Tidak ada data pribadi.** Tidak menayangkan nama akun, foto, atau tangkapan layar unggahan orang biasa. Kutipan dari medsos diparafrase dan dianonimkan. Mengacu UU PDP 27/2022, agregat saja.
2. **Ambang agregasi.** Jangan tayangkan sel data yang mewakili kurang dari 10 orang atau satu wilayah yang bisa mengidentifikasi individu.
3. **Estimasi diberi label.** Angka proyeksi, hasil model, atau hitungan sendiri diberi tanda `estimasi` — jangan disamakan dengan angka resmi.
4. **Tidak memihak.** Untuk topik politik: tampilkan semua pihak yang relevan, gunakan kata netral (`aksi`, `unjuk rasa`, bukan istilah bermuatan), jangan menyimpulkan niat siapa pun dari data agregat.
5. **Kebijakan koreksi.** Kalau ada angka salah: perbaiki di Story dalam 24 jam, tambahkan slide koreksi pada unggahan berikutnya, simpan di sorotan `Koreksi`. Jangan menghapus unggahan diam-diam.
6. **Hormati lisensi.** Data BPS, BMKG, dan Satu Data boleh dipakai dengan atribusi. Data berlisensi tertutup jangan ditayangkan mentah.

## 8. Catatan jujur soal jangkauan

Dua hal yang perlu kamu tahu sejak awal supaya tidak kecewa di minggu pertama:

- Instagram membatasi rekomendasi **konten politik** ke akun yang belum mengikutimu (pengaturan bawaan di sisi pengguna). Unggahan Senin Kuasa dan konten seperti sentimen 27 Agustus kemungkinan besar akan lebih sepi di Jelajahi dibanding pilar lain. Bukan berarti buruk — konten itu yang membangun kredibilitas dan paling banyak dibagikan lewat pesan langsung. Jangkauan luas datang dari Kamis Peta dan Jumat Layar.
- Akun baru dengan nol pengikut hampir tidak punya jangkauan organik. Untuk 48 jam pertama, sebar manual: bagikan ke Story pribadi, Threads, X, LinkedIn, dan grup yang relevan. Sepuluh orang yang benar-benar menyimpan lebih berharga daripada seribu tayangan pasif.
