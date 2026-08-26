#!/usr/bin/env python3
"""Susun laporan PDF konten #1 dari data dan grafik yang sudah ada."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether,
                                PageBreak, PageTemplate, Paragraph, Spacer, Table,
                                TableStyle)

AKAR = Path(__file__).parent
TINTA = colors.HexColor("#16161A")
ABU = colors.HexColor("#6E6E68")
AKSEN = colors.HexColor("#7A3E9D")
GARIS = colors.HexColor("#DDD8CE")
LEMBUT = colors.HexColor("#F4F1EA")

REG, SEMI, TEBAL = "PJS", "PJS-Semi", "PJS-Bold"
for nama, berat in ((REG, 400), (SEMI, 600), (TEBAL, 800)):
    berkas = AKAR / "fonts" / f"PJS-{berat}.ttf"
    pdfmetrics.registerFont(TTFont(nama, str(berkas)))

L, T = 22 * mm, 20 * mm
LEBAR = A4[0] - 2 * L


def gaya(nama, **kw):
    dasar = dict(fontName=REG, fontSize=9.6, leading=15.2, textColor=TINTA, spaceAfter=7)
    dasar.update(kw)
    return ParagraphStyle(nama, **dasar)


J1 = gaya("j1", fontName=TEBAL, fontSize=23, leading=27, spaceAfter=4)
SUB = gaya("sub", fontSize=11.4, leading=17, textColor=ABU, spaceAfter=16)
J2 = gaya("j2", fontName=TEBAL, fontSize=13, leading=17, spaceBefore=17, spaceAfter=7)
J3 = gaya("j3", fontName=SEMI, fontSize=10.2, leading=14, spaceBefore=9, spaceAfter=3)
P = gaya("p", alignment=TA_JUSTIFY)
KECIL = gaya("kecil", fontSize=8.4, leading=12.6, textColor=ABU, spaceAfter=5)
MATA = gaya("mata", fontName=SEMI, fontSize=7.6, leading=11, textColor=ABU, spaceAfter=3)
TARIK = gaya("tarik", fontName=SEMI, fontSize=11, leading=17, textColor=AKSEN, spaceAfter=9)


def kaki_halaman(kanvas, dok):
    kanvas.saveState()
    kanvas.setFont(REG, 7.6)
    kanvas.setFillColor(ABU)
    kanvas.drawString(L, 12 * mm, "ceritadataa · Laporan konten #1 · 26 Agustus 2026")
    kanvas.drawRightString(A4[0] - L, 12 * mm, str(dok.page))
    kanvas.setStrokeColor(GARIS)
    kanvas.setLineWidth(0.5)
    kanvas.line(L, 16 * mm, A4[0] - L, 16 * mm)
    kanvas.restoreState()


def tabel(baris, lebar):
    t = Table(baris, colWidths=lebar, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), SEMI),
        ("FONTNAME", (0, 1), (-1, -1), REG),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("LEADING", (0, 0), (-1, -1), 13.5),
        ("TEXTCOLOR", (0, 0), (-1, -1), TINTA),
        ("BACKGROUND", (0, 0), (-1, 0), LEMBUT),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, GARIS),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (0, -1), 8),
    ]))
    return t


def gambar(nama, lebar_mm, keterangan):
    im = Image(str(AKAR / "grafik" / nama), width=lebar_mm * mm, height=lebar_mm * 1.25 * mm)
    im.hAlign = "LEFT"
    return KeepTogether([im, Spacer(1, 3), Paragraph(keterangan, KECIL)])


isi = []
A = isi.append

# ------------------------------------------------------------------ pembuka
A(Paragraph("LAPORAN PRODUKSI KONTEN", MATA))
A(Paragraph("Peta pencarian jelang aksi 27 Agustus", J1))
A(Paragraph("@ceritadataa · konten #1 · tayang Rabu 26 Agustus 2026, 19.30 WIB<br/>"
            "Batas data: 26 Agustus 2026, 17.00 WIB", SUB))

A(Paragraph("Ringkasan", J2))
A(Paragraph(
    "Konten pertama akun ini memetakan perhatian publik terhadap rencana aksi 27 Agustus 2026 "
    "lewat data pencarian Google se-Indonesia, 26 Juli–26 Agustus 2026. Sudutnya sengaja bukan "
    "“berapa persen setuju atau menolak” — itu tidak bisa diukur dari data pencarian, dan mengejarnya "
    "akan membuat akun ini terbaca sebagai akun opini sejak unggahan pertama. Yang diukur adalah "
    "anatomi perhatian: kapan ia muncul, seberapa cepat naik, tertuju ke apa, dan di mana ia terpusat.", P))
A(Paragraph("Temuan utamanya satu kalimat: yang dicari orang adalah peristiwanya, bukan tuntutannya.", TARIK))

A(Paragraph("Tiga temuan", J2))
A(tabel([
    ["#", "Temuan", "Angka"],
    ["1", "Pencarian “demo 27 agustus” praktis nol sampai 15 Agustus.\n"
          "Lonjakan terbesar terjadi 24 Agustus.", "0 → 24\n(naik 4,8× dalam sehari)"],
    ["2", "Perhatian tertuju ke peristiwanya, bukan ke tuntutannya.\n"
          "“Hukuman mati koruptor” tidak pernah beranjak dari <1 selama 32 hari.", "100 : 5\n(20× lipat)"],
    ["3", "Terpusat di Jakarta, tapi Yogyakarta melampaui provinsi\n"
          "berpenduduk jauh lebih besar.", "DIY 18\nJateng & Jatim 14"],
], [10 * mm, LEBAR - 48 * mm, 38 * mm]))

# ------------------------------------------------------------------ metode
A(Paragraph("Data dan metode", J2))
A(Paragraph("Sumber", J3))
A(Paragraph(
    "Google Trends Indonesia, diakses 26 Agustus 2026 pukul 17.00 WIB. Empat kata kunci diunduh "
    "dalam <b>satu perbandingan</b>: “demo 27 agustus”, “RUU perampasan aset”, “hukuman mati koruptor”, "
    "dan “MBG”. Sebaran per provinsi diunduh <b>terpisah</b> dengan satu kata kunci saja.", P))
A(Paragraph("Kenapa dua unduhan terpisah", J3))
A(Paragraph(
    "Indeks Trends dinormalisasi terhadap puncak <i>di dalam satu set perbandingan</i>. Kalau peta "
    "provinsi diunduh sambil membandingkan empat kata kunci, warna tiap provinsi menjadi campuran "
    "keempatnya dan tidak berarti apa-apa. Konsekuensi lanjutannya: angka dari dua unduhan berbeda "
    "tidak boleh dibandingkan satu sama lain — 100 di berkas A bukan 100 yang sama di berkas B.", P))
A(Paragraph("Penanganan nilai khusus", J3))
A(Paragraph(
    "Trends menuliskan nilai sangat kecil sebagai “&lt;1”. Dalam perhitungan, nilai itu diperlakukan "
    "sebagai 0,5 dan tetap ditampilkan apa adanya sebagai “&lt;1” di slide — tidak dibulatkan menjadi 1 "
    "maupun 0. Dua provinsi tanpa nilai (Gorontalo dan Sulawesi Barat) diwarnai abu sebagai "
    "“data tidak tersedia”, bukan nol.", P))
A(Paragraph("Konteks aksi", J3))
A(Paragraph(
    "Dihimpun dari pemberitaan Kompas, Kontan, dan Bisnis, 21–25 Agustus 2026. Kelompok yang turun "
    "tidak dinamai di slide karena belum seluruhnya terkonfirmasi dari dua sumber independen; yang "
    "ditampilkan hanya jenis tuntutannya, dan alasan penghilangan nama ditulis terbuka di catatan kaki slide.", P))

A(PageBreak())

# ------------------------------------------------------------------ temuan
A(Paragraph("Temuan rinci", J2))

A(Paragraph("1. Perhatian ini berumur sepuluh hari", J3))
A(Paragraph(
    "Selama tiga minggu pertama rentang pengamatan, indeks pencarian “demo 27 agustus” bernilai nol. "
    "Nilai pertama yang bukan nol muncul 16 Agustus (&lt;1), lalu 21 Agustus (1), 23 Agustus (5), dan "
    "melonjak ke 24 pada 24 Agustus — kenaikan 4,8 kali lipat dalam satu hari, lompatan terbesar "
    "sepanjang rentang. Pemicu lompatan itu belum diverifikasi, dan karena itu grafik hanya menandai "
    "lonjakannya tanpa menyebut sebabnya.", P))
A(gambar("slide-3.png", 74, "Slide 3. Titik 26 Agustus digambar sebagai lingkaran kosong dengan garis "
                            "putus-putus karena harinya masih berjalan saat data diambil."))

A(Paragraph("2. Yang dicari peristiwanya, bukan tuntutannya", J3))
A(Paragraph(
    "Pada hari data diambil, indeks “demo 27 agustus” mencapai 100 sementara “RUU perampasan aset” "
    "— tuntutan utama aksi itu — hanya 5. Selisihnya dua puluh kali lipat. “Hukuman mati koruptor”, "
    "tuntutan kedua, tidak pernah melewati &lt;1 selama 32 hari penuh. Sebagai pembanding, “MBG” "
    "bergerak stabil di kisaran 28 sepanjang bulan dan sama sekali tidak terpengaruh rencana aksi.", P))
A(gambar("slide-4.png", 74, "Slide 4. Keempat kata kunci berasal dari satu unduhan perbandingan, "
                            "sehingga angkanya setara satu sama lain."))

A(PageBreak())

A(Paragraph("3. Jakarta pusatnya, Yogyakarta anomalinya", J3))
A(Paragraph(
    "Sebaran per provinsi menempatkan DKI Jakarta di 100, Banten 37, dan Jawa Barat 22 — pola yang "
    "wajar untuk aksi yang digelar di Jakarta. Yang tidak wajar: Daerah Istimewa Yogyakarta di 18, "
    "melampaui Jawa Tengah dan Jawa Timur yang sama-sama 14. Karena indeks provinsi mengukur "
    "<i>porsi</i> pencarian di wilayah itu, jumlah penduduk sudah ikut diperhitungkan; artinya warga "
    "Yogyakarta memang mencari topik ini lebih intens per orang dibanding dua provinsi tetangganya "
    "yang berpenduduk jauh lebih besar.", P))
A(gambar("slide-5.png", 74, "Slide 5. Lima kelas nilai, satu rona, terang ke gelap. Dua provinsi tanpa "
                            "data diwarnai abu netral."))

# ------------------------------------------------------------------ batas
A(Paragraph("Yang tidak bisa disimpulkan", J2))
A(Paragraph(
    "Bagian ini tayang sebagai slide tersendiri, bukan sebagai catatan kaki. Mengakui batas data "
    "adalah bagian dari produknya.", KECIL))
A(tabel([
    ["Klaim yang tidak boleh dibuat", "Alasan"],
    ["Berapa banyak orang mendukung\natau menolak aksi",
     "Data pencarian tidak merekam sikap. Ini peta perhatian,\nbukan jajak pendapat."],
    ["Berapa orang yang mencari",
     "Indeks Trends adalah nilai relatif 0–100 terhadap puncaknya\nsendiri, bukan hitungan orang."],
    ["Publik tidak peduli pada\nRUU Perampasan Aset",
     "Orang yang sudah paham isinya tidak perlu mencarinya.\nRendahnya pencarian bukan bukti rendahnya kepedulian."],
    ["Perbandingan lintas unduhan",
     "Normalisasi Trends berlaku per set perbandingan, jadi angka\nantar-unduhan tidak setara."],
], [52 * mm, LEBAR - 52 * mm]))

A(Paragraph("Ruang lingkup yang dipotong", J2))
A(Paragraph(
    "Rencana awal delapan slide, terbit enam. Dua slide yang gugur — perbandingan volume antarkanal "
    "dan komposisi nada percakapan — bergantung pada korpus komentar dari YouTube, Reddit, dan GDELT "
    "yang belum sempat ditarik sebelum batas waktu. Keputusannya memotong, bukan menunda tayang: "
    "keenam slide yang terbit berdiri penuh di atas data yang sudah diverifikasi, dan memaksakan dua "
    "slide sisanya dalam dua jam adalah cara tercepat menayangkan angka yang salah pada unggahan pertama.", P))

A(Paragraph("Keterlacakan", J2))
A(Paragraph(
    "Tidak ada satu angka pun yang diketik tangan ke dalam berkas gambar. Seluruh slide dirender "
    "<font face='PJS-Semi'>render_slide.py</font> langsung dari CSV mentah, dan bisa dibangun ulang "
    "kapan saja dengan satu perintah.", P))
A(tabel([
    ["Berkas", "Isi"],
    ["data-mentah/trends_harian.csv", "4 kata kunci × 32 hari, unduhan Google Trends"],
    ["data-mentah/trends_provinsi.csv", "1 kata kunci × 34 provinsi"],
    ["data-mentah/indonesia-prov.geojson", "Geometri 34 provinsi"],
    ["render_slide.py", "Merender keenam slide dari ketiga berkas di atas"],
    ["grafik/slide-1.png … slide-6.png", "Keluaran siap unggah, 1080 × 1350"],
    ["caption.md", "Caption final dan catatan produksi"],
], [62 * mm, LEBAR - 62 * mm]))

A(Paragraph("Langkah berikutnya", J2))
A(Paragraph(
    "Jumat 28 Agustus: versi H+1 yang membandingkan bentuk kurva sebelum dan sesudah aksi berlangsung, "
    "menggunakan rentang dan kata kunci yang persis sama agar kedua unduhan bisa dibandingkan. "
    "Minggu 30 Agustus: pembahasan metode di #MingguDapur, termasuk kenapa hari berjalan tidak "
    "digambar sebagai titik penuh dan kenapa peta provinsi harus diunduh dengan satu kata kunci.", P))

dok = BaseDocTemplate(str(AKAR / "laporan-konten-1.pdf"), pagesize=A4,
                      leftMargin=L, rightMargin=L, topMargin=T, bottomMargin=24 * mm,
                      title="Laporan konten #1 — ceritadataa",
                      author="ceritadataa", subject="Peta pencarian jelang aksi 27 Agustus 2026")
bingkai = Frame(L, 24 * mm, LEBAR, A4[1] - T - 24 * mm, id="isi",
                leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
dok.addPageTemplates([PageTemplate(id="utama", frames=[bingkai], onPage=kaki_halaman)])
dok.build(isi)
print("laporan-konten-1.pdf jadi")
