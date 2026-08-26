# Prompt Baku untuk Gemini

Salin blok di bawah apa adanya setiap kali menyerahkan tata letak ke Gemini. Ganti hanya
bagian di dalam kurung siku.

**Prinsip di baliknya:** desain AI jadi norak karena prompt-nya memberi kebebasan memilih.
Obatnya bukan menulis "buat yang elegan" — itu justru menyerahkan keputusan. Obatnya adalah
mencabut keputusannya: beri nilai heksadesimal yang pasti, ukuran huruf yang pasti, dan daftar
larangan yang eksplisit. Gemini diposisikan sebagai **penata huruf yang menjalankan sistem**,
bukan sebagai perancang yang mencari gaya.

**Satu keputusan teknis:** minta keluaran **HTML + CSS**, bukan gambar. Model gambar menggeser
angka, mengarang label, dan membuat panjang batang tidak sesuai nilainya. HTML bisa kamu buka
di peramban, periksa, lalu tangkap layar pada ukuran persis 1080 × 1350.

---

```
PERAN
Kamu penata huruf, bukan perancang. Sistem visualnya sudah final dan tidak dalam
pembahasan. Tugasmu menempatkan isi ke dalam sistem itu dengan rapi. Kamu tidak
sedang diminta mencari gaya, menyegarkan tampilan, atau membuatnya lebih menarik.

KELUARAN
Satu berkas HTML mandiri berisi [6] elemen <section>, masing-masing tepat
1080 × 1350 piksel. CSS ditulis inline di dalam <style>. Tanpa pustaka luar,
tanpa kerangka kerja, tanpa JavaScript. Aku akan menangkap layar tiap section.

SISTEM — SALIN PERSIS, JANGAN DIUBAH SATU NILAI PUN

  Kanvas    1080 × 1350 px
  Margin    padding 120 px atas-bawah, 90 px kiri-kanan
            kaki slide adalah anak flex terakhir dengan margin-top: auto —
            jangan pakai position: absolute untuk menempatkannya

  Warna     latar    #F4F1EA
            tinta    #16161A
            abu      #8A8A85   (hanya untuk catatan kaki dan label sekunder)
            aksen    [#7A3E9D]  (hanya SATU aksen; tidak ada warna kedua)
            garis    #DED9CE

  Huruf     satu keluarga saja: Plus Jakarta Sans
            angka besar 160 px / bobot 800 / tinggi baris 1 / warna aksen
            judul     44 px / bobot 800 / tinggi baris 1.2
            subjudul  24 px / bobot 400
            isi       20 px / bobot 400 / tinggi baris 1.6
            label     16 px / bobot 400 / warna abu
            catatan   13 px / bobot 400 / warna abu
            tidak ada ukuran lain. tidak ada bobot di bawah 400.

  Perataan  semua teks rata kiri. tidak ada yang rata tengah.

ASET TERLAMPIR
  grafik-*.png — grafik polos berlatar transparan, tanpa judul dan tanpa
    catatan kaki bawaan. Judul dan catatan kaki ditulis di HTML, bukan di
    dalam gambar. Tempatkan gambarnya apa adanya.
  teks-slide.txt — teks persis tiap slide.

ATURAN ISI
1. Salin teks dari teks-slide.txt kata per kata. Jangan memparafrase, jangan
   memperbaiki, jangan memperpendek, jangan menerjemahkan, jangan mengubah satu
   angka pun — termasuk tanda desimal dan tanda kurang-dari.
2. Jangan membuat, menggambar ulang, mewarnai ulang, atau memperbaiki grafik apa
   pun. Gambar yang kulampirkan adalah data; mengubahnya berarti memalsukan data.
3. Jangan menambah kalimat, judul, kesimpulan, ajakan, atau keterangan yang tidak
   ada di teks-slide.txt.

LARANGAN — semuanya keras, tanpa pengecualian
  gradien apa pun · bayangan, glow, bevel, emboss, garis luar pada teks ·
  warna di luar daftar di atas · lebih dari satu warna aksen · ikon atau bentuk
  3D · ilustrasi orang bergaya korporat (tubuh panjang, warna pastel) · foto stok ·
  emoji · teks di atas foto · sudut membulat lebih dari 4 px · bentuk abstrak
  melayang, blob, swoosh, gelombang, percikan · pola atau tekstur latar ·
  kartu yang sekaligus punya garis tepi, bayangan, dan latar berwarna ·
  huruf tipis · huruf miring untuk penekanan (pakai bobot 800) · KALIMAT PENUH
  HURUF KAPITAL · label atau lencana yang tidak menyampaikan informasi ·
  garis dekoratif yang tidak memisahkan apa pun

YANG BOLEH KAMU PUTUSKAN
  jarak antarblok di dalam aturan margin · di mana baris teks dipotong ·
  urutan vertikal blok dalam satu slide · nomor slide kecil di sudut

KAIDAH RAGU
  Kalau ragu antara menambah elemen atau menghilangkannya, hilangkan.
  Kalau ragu antara dua ukuran huruf, pilih yang lebih besar.
  Kalau sebuah elemen tidak menyampaikan informasi, ia tidak boleh ada.

PEMERIKSAAN SEBELUM MENJAWAB
  Sebelum mengirim HTML-nya, jalankan daftar ini dan tulis hasilnya sebagai
  komentar di baris pertama berkas:
  [ ] setiap nilai warna dalam berkas ada di daftar sistem — tidak ada yang lain
  [ ] hanya satu keluarga huruf dipakai
  [ ] tidak ada ukuran huruf di luar lima yang ditentukan
  [ ] tidak ada gradien, bayangan, atau warna kedua
  [ ] semua teks rata kiri
  [ ] setiap angka cocok persis dengan teks-slide.txt
  [ ] tidak ada kalimat yang tidak kutulis
  [ ] tiap section tepat 1080 × 1350 px
  [ ] tidak ada judul atau catatan kaki yang muncul dua kali — sekali di HTML
      dan sekali lagi di dalam gambar
  Kalau ada yang tidak tercentang, perbaiki dulu, jangan dikirim.
```

---

## Kalau hasilnya masih norak

Jangan menulis prompt panjang baru. Kirim satu kalimat ini:

```
Kamu melanggar larangan: [sebut yang mana]. Perbaiki hanya itu, jangan
menyentuh yang lain, dan jalankan ulang daftar pemeriksaan sebelum menjawab.
```

Menyalahkan satu pelanggaran yang spesifik hampir selalu lebih efektif daripada
meminta "buat lebih minimalis" — permintaan seperti itu mengembalikan kebebasan memilih
yang justru jadi sumber masalahnya.
