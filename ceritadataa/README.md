# @ceritadataa — Ruang Kerja Konten

Akun Instagram visualisasi data berbahasa Indonesia. Satu hari, satu pilar, satu pertanyaan yang dijawab dengan data publik.

## Isi folder

| Berkas | Isi |
|---|---|
| `01-strategi-akun.md` | Posisi akun, bio, sistem visual, rumus caption, metrik yang dipantau, aturan etika |
| `02-pilar-harian.md` | Tujuh pilar harian, format tiap hari, dan 42 ide judul awal |
| `03-ritme-produksi.md` | Alur kerja mingguan, pembagian tugas dengan Gemini, templat brief desain, daftar periksa QC |
| `04-sumber-data.md` | Katalog sumber data terbuka Indonesia, dikelompokkan per pilar |
| `05-kalender-4-minggu.md` | Jadwal tanggal-per-tanggal, 26 Agustus – 20 September 2026 |
| `brief/2026-08-26-sentimen-27-agustus.md` | Brief lengkap konten pertama: pertanyaan riset, metode, storyboard 8 slide, caption, brief desain |
| `scripts/ambil_data_27agustus.py` | Skrip pengumpul data mentah untuk konten pertama |

## Pembagian peran

- **Kamu** — merumuskan pertanyaan, mencari dan membersihkan data, menghitung, menulis narasi, memutuskan angka mana yang tayang.
- **Claude (aku)** — bantu berburu sumber, menyusun metode, menulis skrip pengambilan data, menyiapkan storyboard dan caption, mengecek angka.
- **Gemini** — tata letak, ilustrasi, ikon, penyempurnaan tipografi. **Bukan** pembuat grafik dan bukan penulis angka.

Aturan keras: setiap angka yang tayang harus bisa ditelusuri ke satu baris di berkas data mentah yang tersimpan. Kalau tidak bisa, angka itu tidak tayang.

## Menjalankan skrip pengumpul data

```bash
pip install -r ceritadataa/scripts/requirements.txt
export YOUTUBE_API_KEY=...           # gratis lewat Google Cloud Console
export CERITADATAA_KONTAK=...        # alamat kontak untuk User-Agent (diminta Wikimedia)
python3 ceritadataa/scripts/ambil_data_27agustus.py --mulai 2026-08-01 --sampai 2026-08-25
```

Skrip menulis CSV mentah plus `manifest.json` berisi sumber, alamat, waktu unduh,
dan jumlah baris tiap berkas. Kanal yang gagal diambil dilewati tanpa menghentikan
yang lain — periksa manifest untuk tahu mana yang benar-benar terisi.
