# Katalog Sumber Data

Semua gratis dan boleh dipakai ulang dengan atribusi kecuali disebut lain. Simpan halaman ini sebagai penyangga Hari Dapur.

## Serba guna

| Sumber | Alamat | Catatan |
|---|---|---|
| BPS | bps.go.id · webapi.bps.go.id | Tulang punggung. Web API butuh kunci gratis lewat pendaftaran. Perhatikan tahun dasar dan revisi angka. |
| Satu Data Indonesia | data.go.id | Katalog lintas kementerian. Kualitas tidak merata, selalu cek pemilik datanya. |
| Portal data daerah | data.jakarta.go.id, dan portal provinsi lain | Untuk cerita berskala kota. |
| World Bank / Our World in Data | data.worldbank.org · ourworldindata.org | Untuk pembanding antarnegara. |
| Wikipedia pageviews API | wikimedia.org/api/rest_v1 | Proxy perhatian publik, gratis, tanpa kunci. |
| Google Trends | trends.google.com · pytrends | Bukan jumlah orang — indeks relatif 0–100. Selalu sebut itu. |

## Senin Kuasa

- **Kemenkeu** — APBN Kita (bulanan, PDF+data), djpk.kemenkeu.go.id untuk APBD seluruh daerah
- **DPR RI** — dpr.go.id untuk Prolegnas, status RUU, risalah; wikidpr.org untuk data rapat yang lebih rapi
- **KPU** — infopemilu.kpu.go.id: hasil pemilu per TPS, dana kampanye
- **KPK** — elhkpn.kpk.go.id (harta pejabat), acch.kpk.go.id (statistik penindakan)
- **Mahkamah Agung** — putusan.mahkamahagung.go.id: teks putusan, bisa diurai untuk lama vonis
- **ICW** — antikorupsi.org: rekap tahunan tren korupsi, sudah bersih dan siap pakai
- **Lembaga survei** — LSI, SMRC, Indikator, Litbang Kompas: rilis publik, selalu catat margin of error dan ukuran sampel

## Selasa Kita

- **BPS** — SP2020, Susenas, Sakernas, proyeksi penduduk 2020–2050, Long Form SP2020
- **Dukcapil Kemendagri** — data administrasi kependudukan semesteran
- **Kemendikbudristek** — dapo.kemdikbud.go.id: sekolah, guru, murid sampai tingkat desa
- **Kemenkes** — data kesehatan, profil kesehatan tahunan
- **BKKBN** — data keluarga, stunting (SSGI)
- **UN WPP** — population.un.org: pembanding internasional dan proyeksi alternatif

## Rabu Rupiah

- **PIHPS Bank Indonesia** — hargapangan.id: harga pangan harian per provinsi dan per pasar. Sumber terbaik untuk konten cepat.
- **BPS** — IHK/inflasi, upah buruh, PDB, ekspor-impor bulanan
- **Bank Indonesia** — bi.go.id: SEKI, kurs, survei harga properti residensial
- **Kemendag** — harga bahan pokok, neraca perdagangan
- **OJK** — statistik perbankan, fintech lending
- **Kemnaker** — UMP/UMK tiap provinsi dan kabupaten

## Kamis Peta

- **Ina-Geoportal / BIG** — tanahair.indonesia.go.id: batas administrasi resmi, RBI
- **DEMNAS** — tanahair.indonesia.go.id/demnas: model elevasi nasional 8 meter
- **OpenStreetMap** — via Geofabrik atau Overpass API: jalan, fasilitas, POI. Untuk isochrone pakai OSRM/Valhalla lokal atau openrouteservice (kuota gratis).
- **WorldPop** — worldpop.org: penduduk grid 100 m
- **Global Forest Watch** — globalforestwatch.org: tutupan hutan dan kehilangannya
- **NASA FIRMS** — firms.modaps.eosdis.nasa.gov: titik panas hampir real-time
- **Google Earth Engine** — citra dan analisis deret waktu, gratis untuk nonkomersial
- **Meta Data for Good** — movement range maps, populasi berdensitas tinggi
- **BAKTI/Komdigi** — cakupan sinyal dan desa blank spot

## Jumat Layar

- **Google Trends** — pola pencarian per jam, per provinsi
- **YouTube Data API v3** — kuota gratis 10.000 unit/hari: video, statistik, komentar
- **Spotify Charts** — charts.spotify.com: tangga lagu harian Indonesia
- **Wikipedia pageviews** — perhatian pada tokoh, film, peristiwa
- **Reddit API** — r/indonesia, endpoint `.json` gratis tanpa kunci untuk pembacaan ringan
- **Transfermarkt / API-Football** — data pemain dan pertandingan (cek syarat pakai)
- **RSS media** — Google News RSS untuk menghitung volume pemberitaan
- **GDELT** — api.gdeltproject.org: volume dan nada pemberitaan global, termasuk media Indonesia, gratis tanpa kunci

## Sabtu Bumi

- **BMKG** — data.bmkg.go.id: katalog gempa, prakiraan cuaca, data iklim; feed TEWS untuk peringatan dini
- **MAGMA/PVMBG** — magma.esdm.go.id: status gunung api
- **BNPB** — dibi.bnpb.go.id: basis data kejadian bencana sejak 1815
- **KLHK** — sipsn.menlhk.go.id (sampah), data kualitas air dan udara
- **ESDM/PLN** — statistik ketenagalistrikan, SAIDI/SAIFI
- **Copernicus / ERA5** — cds.climate.copernicus.eu: data iklim historis global, butuh pendaftaran gratis
- **IQAir / OpenAQ** — kualitas udara per kota

## Mendengar percakapan medsos

Ini bagian tersulit karena akses ditutup rapat. Yang realistis pada 2026:

| Kanal | Cara | Biaya | Catatan |
|---|---|---|---|
| YouTube | Data API v3 (`search.list`, `commentThreads.list`) | Gratis, kuota 10.000 unit/hari | Paling praktis untuk mengumpulkan ribuan komentar berbahasa Indonesia |
| Berita | GDELT DOC 2.0 API (`timelinevol`, `timelinetone`) | Gratis | Memberi deret waktu volume **dan** nada. Ini media, bukan medsos — beri label jelas. |
| Google | Trends, termasuk sebaran per provinsi | Gratis | Indeks relatif, bukan jumlah |
| Reddit | endpoint `.json` atau API resmi | Gratis untuk skala kecil | r/indonesia: diskusi panjang, kualitas tinggi, tapi bias demografis besar |
| Wikipedia | pageviews API | Gratis | Proxy perhatian yang bersih dan mudah dipertanggungjawabkan |
| TikTok | Research API (khusus akademik) atau pencatatan manual jumlah video/tayangan per tagar | Gratis/terbatas | Kalau manual: catat waktu tepat, simpan tangkapan layar sebagai bukti, sebut sebagai potret satu waktu |
| X/Twitter | API resmi berbayar (mulai ratusan dolar/bulan) | Berbayar | Kalau tidak berlangganan: **jangan mengarang**. Kutip analisis pihak lain (Drone Emprit, peneliti kampus) sebagai data sekunder dengan atribusi penuh. |
| Instagram | Graph API hanya untuk akun bisnis milik sendiri | Terbatas | Tidak bisa dipakai untuk mendengar percakapan publik |

**Aturan pilar Layar:** kalau kamu tidak bisa mengumpulkan datanya sendiri, katakan dari mana angkanya datang. Menyebut "berdasarkan analisis X" itu kredibel. Menyebut "berdasarkan pantauan medsos" tanpa metode itu tidak.
