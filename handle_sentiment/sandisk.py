import pandas as pd


SanDisk_CZ50_8GB = [
    {
        "comment": "Bagus baiklah saatnya kembali nugas menggunakan ini 😊",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih barang sudah sampai di rumah. Barang original. Seller baik. Toko official bukan kaleng-kaleng. Kalo mau beli disini saja, dijamin ORIGINAL!!!!",
        "sentiment": "positif",
    },
    {"comment": "Bagus g cacat, barangnya juga bner yg 64gb", "sentiment": "positif"},
    {
        "comment": "Jangan ragu beli flasdisk dengan ruang penyimpanan yg paling banyak, biar puas 😄 Haha.",
        "sentiment": "positif",
    },
    {
        "comment": "Makasiiih kak... Barang udah dtg n diterima dengan aman tanpa kerusakan, udah dicoba juga berfungsi dengan baik, toko amanah... Barang original 1000% recommended pokoknya 🙏🙏🙏 sukses selalu kak",
        "sentiment": "positif",
    },
    {"comment": "S3lalu percaya sih sama kualitas Sandisk", "sentiment": "positif"},
    {
        "comment": "Barang sudah diterima trima kasih seller\nTrima kasih shopee\nToko ini layak dipercaya.. mantab.. jos\nPertahankan.. insya Allah segera order lagi",
        "sentiment": "positif",
    },
    {
        "comment": "Pengirimannya ga terlalu lama, harga juga cocoklah, belum dicoba sih semoga bisa deh, makasih ya",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah, barang sudah diterima. Pengiriman cepat, barang sesuai, seller ramah.. Semoga awet barang ny, dan semakin sukses terus untuk seller nya.",
        "sentiment": "positif",
    },
    {
        "comment": "Respon toko cepat dan amanah. Barang sudah saya terima, dan sesuai dipkripsi gambar dan pesanan, belum di coba semoga awet dan tahan lama",
        "sentiment": "positif",
    },
    {
        "comment": "Harga sangat compertible\nAlhamdulilah semoga awet dan tahan lama",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah paket nya sudah sampe, pengiriman nya cepat, barang nya sesuai dengan pesanan, semoga aja awet dan ori. Terimakasih",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah paket sdh nyampe... sesuai pesanan.... packing aman... respon seller gercep dan pengiriman jg cpt... blm dcoba...smg awet...mksh kk....",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: berfungsi dengan baik, sudah di test dikomputer\nSepadan dengan Harga: harganya bersaing (live)\nBarang insyaallah original\nAdmin ramah\nGercep\nBerfungsi dg baik \nSudah dicoba di komputer \n\n\nTerima Kasih  banyak min",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah diterima dengan baik.. Semuanya sesuai dengan pesanan.. Packing cukup aman walopun pake bubble warp tapi tebal.. Terima kasih..",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ORI\nSepadan dengan Harga: Yes\nSudah kesekian kalinya beli disini\nTidak pernah mengecewakan\nPengemasan aman, bubble wrap tebal\nBarangx sesuai n yg paling penting ORI\nMantabs",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman sangat lambat, harga terlalu tinggi, belum dicoba. Kecewa banget.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang diterima rusak dan tidak sesuai dengan pesanan. Seller tidak responsif dan tidak bisa dipercaya. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur terbaik yang dijanjikan tidak berfungsi dengan baik. Harganya terlalu mahal untuk kualitas yang didapat. Kecewa dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Paketnya rusak dan barangnya cacat. Seller tidak merespons keluhan saya. Ini adalah pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak pernah mendapatkan produk yang sesuai dengan pesanan. Pengemasan buruk dan barangnya palsu. Saya sangat kecewa dengan toko ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak berfungsi sama sekali, dan seller tidak memberikan solusi. Barang palsu dan uang saya terbuang sia-sia. Kecewa sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat sekali dan barang tidak pernah tiba. Seller tidak merespons dan sangat tidak profesional. Pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang diterima rusak parah dan tidak dapat digunakan. Seller tidak memberikan pengembalian uang dan tidak ada dukungan pelanggan. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur-fitur produk ini tidak berfungsi sama sekali. Harga terlalu tinggi untuk kualitas yang sangat rendah. Produk palsu yang disamar-samarkan sebagai barang asli.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan sangat buruk, sehingga barang rusak saat tiba. Tidak ada tanggapan dari seller untuk mengatasi masalah ini. Kecewa dengan pelayanan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak seperti yang dijanjikan dan sangat tidak berguna. Seller tidak bertanggung jawab dan tidak dapat diandalkan. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sudah menunggu berhari-hari, tetapi paket tidak kunjung tiba. Seller tidak memberikan informasi yang jelas dan tidak membantu. Pengalaman berbelanja yang sangat frustasi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk terlalu mahal untuk kualitas yang buruk. Tidak ada panduan penggunaan yang disertakan dan seller tidak memberikan dukungan. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang diterima tidak seperti yang diiklankan. Saya merasa ditipu oleh seller ini. Pengalaman berbelanja yang sangat negatif.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat tidak andal, paket tiba terlambat dan rusak. Seller tidak peduli dengan masalah ini dan tidak membantu. Saya kecewa dengan pelayanan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur-fitur produk tidak berfungsi sama sekali dan kualitasnya sangat rendah. Harga produk tidak sebanding dengan kualitas yang diberikan. Kecewa sekali.",
        "sentiment": "negatif",
    },
]


Max_Sandisk = [
    {
        "comment": "Produk original, harga produk sangat baik, respon penjual sangat baik, kualitas produk sangat baik, kecepatan pengiriman sangat baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya original pengiriman nya juga okee respon penjualannya okee banget",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: tahan utk cctv\nSepadan dengan Harga: ada mutu ada harga\nUntuk dipake di cctv. Mudah2an awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Good. Barang tiba dengan baik dan aman. Semoga baik micro sd dan ip camera efektif banget untuk security d rumah. Thanks ya Sandisk. Banyak2in update voucher atau promo bunding sperti ini atau malah + diskon. Siapatau taken lagi nih",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus dan cocok buat cctv\nSepadan dengan Harga: lumayan lah",
        "sentiment": "positif",
    },
    {
        "comment": "Unit : ⭐⭐⭐⭐⭐ Superb\n+ minimum 20FpS (FHD auto) \n+  R/W identik dengan datasheet\n+Garansi 10TAHUN <-- BACA BAIK2\n\nPACKING: ⭐⭐⭐⭐ Good\n\nBagai mana bisa jd mitra/staf MERK ini jika tidak tau product knowledge?? Superb brand but...\n\nI DONT CARE YOUR BONUS, I NEED TRUE INFORMATION &  SUPERB AFTER SALE.",
        "sentiment": "positif",
    },
    {
        "comment": "Memory micro SD card bagus, read/write kurang lebih sesuai deskripsi, kalau untuk dashcam recommend pakai yg ini, kalau yg tipe High Endurance sering bermasalah/error, sejauh ini pakai yg Max Endurance tidak ada masalah sampai review ini ditulis. Recommended seller :)",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: sesuai deskripsi\nBelum sempat dipasang di BlackVue..semoga kompatible",
        "sentiment": "positif",
    },
    {"comment": "Bagus pengiriman cepat barang sesuai", "sentiment": "positif"},
    {
        "comment": "Cocok buat dashcam mobil, sebelumnya pake sandisk ultra gak cocok cepet panas. pake endurance langsung jos",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya sudah di terima dengan baik, kualitas barang bagus cocok untuk CCTV di rumah dengan rekaman video yang jernih, recommended seller",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantap\nSepadan dengan Harga: sepadan\nBelum dicoba, semoga cocok dan awet 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Cocok untuk merekam CCTV\nSepadan dengan Harga: kapasitas 128 GB",
        "sentiment": "positif",
    },
    {
        "comment": "Pesanan sdh diterima, blm dicoba mudahan berfungsi, pengiriman kali ini agak lama",
        "sentiment": "positif",
    },
    {
        "comment": "Semoga awet. Makasih buat seller. Bagus lumayan lah dipake",
        "sentiment": "positif",
    },
    {"comment": "Barang sesuai & Pengirimannya cepat👍", "sentiment": "positif"},
    {
        "comment": "Produk tidak asli, harga produk sangat mahal, respon penjual sangat buruk, kualitas produk sangat rendah, kecepatan pengiriman sangat lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang palsu pengiriman nya juga buruk, respon penjualannya sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak sesuai deskripsi\nSepadan dengan Harga: terlalu mahal\nTidak cocok untuk digunakan, tidak awet.",
        "sentiment": "negatif",
    },
    {
        "comment": "Buruk. Barang tiba rusak dan tidak aman. Tidak efektif untuk keamanan di rumah. Sandisk sangat mengecewakan. Kurangnya promosi dan diskon membuat pengalaman berbelanja sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: buruk dan tidak cocok\nSepadan dengan Harga: terlalu mahal\nMembantu?",
        "sentiment": "negatif",
    },
    {
        "comment": "Unit : ⭐ Super buruk\n+ kurang dari 20FpS (FHD auto) \n+  R/W jauh dari datasheet\n+ Garansi palsu <-- JANGAN TERPEDAYA\n\nPACKING: ⭐ Bad\n\nTidak bisa menjadi mitra/staf MERK ini jika tidak memiliki pengetahuan produk. Merek yang sangat buruk...",
        "sentiment": "negatif",
    },
    {
        "comment": "Memory micro SD card buruk, read/write tidak sesuai deskripsi, kalau untuk dashcam tidak direkomendasikan, kalau yang tipe High Endurance sering bermasalah/error, sejauh ini menggunakan yang Max Endurance banyak masalahnya. Tidak direkomendasikan seller :(",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak sesuai deskripsi\nBelum sempat dipasang di BlackVue..tidak kompatible",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tiba rusak dan tidak sesuai dengan pesanan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak cocok buat dashcam mobil, sebelumnya pake sandisk ultra lebih baik tidak cepat panas. pake endurance sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barangnya rusak, kualitas barang sangat buruk, tidak cocok untuk CCTV di rumah dengan rekaman video yang buram, seller sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: buruk dan tidak cocok\nSepadan dengan Harga: terlalu mahal\nBelum dicoba, tidak akan cocok dan tidak awet 👎",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak sesuai untuk merekam CCTV\nSepadan dengan Harga: kapasitas 128 GB terlalu mahal",
        "sentiment": "negatif",
    },
    {
        "comment": "Pesanan tiba terlambat, tidak berfungsi, pengiriman sangat lambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak awet. Tidak bagus buat seller. Buruk dan tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai & Pengirimannya sangat lambat👎",
        "sentiment": "negatif",
    },
]


SanDisk_240gb = [
    {
        "comment": "Fitur Terbaik: fitur sesuai dengan pesanan\nSepadan dengan harga, bagus, berkualitas",
        "sentiment": "positif",
    },
    {
        "comment": "Rekomended seller sudah sesuai dengan ekspetasi respon cepat penjual bagus, packing ada bubble",
        "sentiment": "positif",
    },
    {
        "comment": "Wooow, pengiriman lumayan cepat, respon penjual ramah dan fast respon, maaf sedikit salah paham sewaktu unboxing, semoga awet dan bermanfaat",
        "sentiment": "positif",
    },
    {
        "comment": "Barang bagus, pengiriman cepat, Respon penjual baik. Terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantap\nSepadan dengan Harga: keren\nsemoga awet sering pakai sandisk awet terus",
        "sentiment": "positif",
    },
    {
        "comment": "Sudah diterima dengan baik tanggal 2 Januari 2023, aman, dan sesuai dengan pesanan. Sudah ditest dan berfungsi dengan baik, semoga bisa awet dipakai kedepannya. Senang bisa berbelanja di toko ini. Terimakasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ssd\nSepadan dengan Harga: iya\nKamu nanyae ini Bagus apa engga? Kamu nanyae? Bagus pake banget, maksih semoga awet ya amiin",
        "sentiment": "positif",
    },
    {
        "comment": "Semoga bisa dipakai, laptop ga lelet lagi, kerjaan makin lancar. Aamiin. Min, cara klaim garansinya bgmn kah? Soalnya di box pengiriman tdk ada tanda terima, kartu garansi, maupun kwitansi.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus yaa barangnya oke banget kirimnua juga oke bgt cepetnyaaa. Pokonya best deh sukaaa 👍🏻👍🏻👍🏻",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: OS Default\nSepadan dengan Harga: Ada Harga Ada Kualitas\nAlhamdulillah, paket sesuai pesanan dan kondisi sangat baik, pengiriman cepat, lambat di pihak ekspedisi aja, packing aman, semoga bisa up ke nvme 😏 . Thanks Seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Premium\nSepadan dengan Harga: kualitas terbaik\nBarang original, bagus, terima kasih shopee dan seller barang datang tepat waktu, kurir bagus dan on time... Terima kasih banyak,barang berfungsi dengan baik,mantap dan original...",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: lebih murah sedikit\nFitur Terbaik: akan jauh lebih cepat daripada hardisk\nTiba dengan selamat. Belum dicoba, semoga bagus",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah pengiriman sangat cepat, Dan respect sama kurirnya karna di antarkan walaupun hujan",
        "sentiment": "positif",
    },
    {"comment": "Sepadan dengan Harga: pas\nOrigianl asli", "sentiment": "positif"},
    {
        "comment": "Udah sampe nih cepet banget, pengemasan pengirimannya cepet jadi dua hari setelah bayar udh sampe. Dan udh dicoba buat install os juga. Semoga awet deh, ga kayak hdd kemarin yg bermasalah dan ga ke detect tiba tiba.",
        "sentiment": "positif",
    },
    {
        "comment": "Packing okeeee\nSemoga berfungsi dengan baik \nTenkyuioookok",
        "sentiment": "positif",
    },
    ### Negatif
    {
        "comment": "Produk ini sangat buruk. Fiturnya tidak sesuai dengan yang diharapkan dan tidak sepadan dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Respon penjual sangat buruk dan tidak membantu. Pengemasan juga sangat buruk dan barang rusak saat sampai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan barang tidak sesuai dengan pesanan. Saya merasa sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Barang ini sering mengalami masalah teknis dan tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga yang saya bayar terlalu tinggi untuk produk ini. Saya merasa seperti saya telah tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pelayanan penjual sangat buruk. Mereka tidak merespons keluhan saya dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat rapuh dan mudah rusak. Saya merasa seperti saya telah membuang uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan pengiriman yang lama dan produk yang tidak berkualitas. Saya tidak merekomendasikan pembelian dari penjual ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini terlalu mahal untuk kualitas yang sangat rendah. Saya merasa seperti saya telah ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan penjual tidak responsif. Barang ini tidak sesuai dengan ekspektasi saya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat tidak berguna. Saya menyesal telah membelinya. Fiturnya tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Barang ini sering mengalami masalah teknis dan sangat sulit digunakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat buruk. Saya merasa seperti saya telah membuang uang dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan sangat buruk dan barang rusak saat sampai. Seller tidak responsif dan tidak membantu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat tertipu dengan pembelian ini. Pengiriman sangat lambat dan barang tidak sesuai dengan pesanan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan barang ini. Kualitas produk sangat rendah dan harga yang saya bayar tidak sepadan.",
        "sentiment": "negatif",
    },
]


Sandisk_128GB = [
    {
        "comment": "Fitur Terbaik: terbaik\nSepadan dengan Harga: murah bingit\nPaket sampai dengan aman,\nTop banget, thxz",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah Paket Telah Sampai dengan kondisi selamat,  barangnya Bagus, Sangat Recomended & Sesuai dengan pemesanan yang di inginkan, Hargapun Terjangkau,  Chat toko dan tukang paketnya Baik+Ramah, Pengemasan SANGAT SUPER AMAN Semoga makin banyak voucher dan Diskonnya hihi,Terima Kasih Banyak😊🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: berkualitas terbaik\nSepadan dengan Harga: pas di kantong\nMaaf sebelumnya pakingan nya udah di buka, itu yang baru saya beli di toko ini langsung saya coba untuk memasukkan data ke dalam flashdisk sandis merek yang berkualitas terbaik untuk harganya pun sangat terjangkau dan soal kualitas tidak perlu di ragukan lagi ini sudah sangat bagus mantap dan wow banget pokoknya seneng banget bisa dapat barang sebagus ini",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus\nSepadan dengan Harga: sesuai\nflasdisk nya sudah sampai lagi di coba dan hasil nya sangat cepat koneksi nya mantap terima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baik\nSepadan dengan Harga: harga terjangkau\nproduk baik, sdah bbrpa kali pemesanan, packing baik, produk tidak ada yang rusak/cacat, pengiriman cepat, barang diterima dengan baik",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: belum di coba\nSepadan dengan Harga: terjangkau\nbarangnya bagus,\npengiriman cepat,\nbarang original,\nharga standar bisa  terjangkau,\nrespon penjual cepat,\nsemoga selalu amanah,\ntidak mengecewakan",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok\nSepadan dengan Harga: ok\nSesuai pesanan\nSemoga awet\nBener2 original karena ada hologram datascrip\nBantu subscribe channel YouTube sya di\nSurya Putra son\n\nSalam sukses n lancar slalu buat lapaknya\nTrimakasih byk",
        "sentiment": "positif",
    },
    {
        "comment": "Product cepat sampai, pesan kamis malam sabtu siang sudah sampai.. Respons penjual bagus, product original Dan dari toko officialnya juga , jadi tidsk usah khawatir jika product bermasalah asal buat vidio bisa return. Ini blum saya coba karna masih ditempat kerja nanti saya info lagi kalo sudah dcb",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baik, original\nSepadan dengan Harga: harga murah terjangkau\nproduk baik, original, hrga murah terjangkau, packing baik, kemasan produk tidak rusak/cacat",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: apa\nSepadan dengan Harga: iya\nbagus sesuai pesanan, pengiriman cepat, benar 128 gb saat dicek, semoga sukses slalu",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah barang nya sudah sampai dengan selamat dan dibungkus rapi dan mudah2an awet ya, terima kasih seller ga bosan bosan saya beli di official SanDisk, sudah beli yg ke 10x dan terbukti barang bagus dan original, bukan kaleng kaleng... Sukses selalu buat SanDisk, utk shopee & kurirnya thanks",
        "sentiment": "positif",
    },
    {
        "comment": "Barang original, sesuai deskripsi, dan harga kompetitif. Kapasitas penyimpanan bersih 114 GB, normal untuk flashdisk dengan kapasitas besar. Semoga awet produknya. Memuaskan ☺️👍",
        "sentiment": "positif",
    },
    {
        "comment": "Product original\nPengiriman cepat\nPengepakan standar\nThanks seller and Shopee\nSukses terus ya\nGbu",
        "sentiment": "positif",
    },
    {
        "comment": "Ini pertama kalinya saya belanja disini, kualitas produk sangat baik, produk original, harga produk sangat baik, kecepatan pengiriman juga sangat baik, bahan sangat good quality. Bakal repeat order. Nggak nyesel belanja disini. Sesuai ekspektasi pokoknya amanah banget belanja disini😍😍",
        "sentiment": "positif",
    },
    {
        "comment": "Ini kali kedua saya belanja disini, kualitas produk sangat baik, produk original, harga produk sangat baik, kecepatan pengiriman juga sangat baik, bahan sangat good quality. Bakal repeat order. Nggak nyesel belanja disini. Sesuai ekspektasi pokoknya amanah banget belanja disini😍😍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus\nSepadan dengan Harga: cocok di jamin ori\nMantap, beli di oficial pasti tidak kecewa\nSdh 2x saya beli di oficial selalu terbaik dan di jamin ori",
        "sentiment": "positif",
    },
    {
        "comment": "Barang rusak saat tiba, pengemasan buruk, sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lama dan tidak sesuai dengan estimasi, buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai dengan deskripsi, sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang palsu, penipuan! Tidak akan belanja di sini lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak ada respon dari penjual, pelayanan sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga terlalu mahal untuk kualitas produk yang buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat dan tidak ada informasi yang jelas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk rusak setelah beberapa penggunaan, tidak awet sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak jujur tentang kondisi produk, sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kemasan rusak dan produk dalam keadaan basah saat tiba.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pelayanan pelanggan sangat buruk, sulit dihubungi dan tidak responsif.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai dengan gambar, sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman salah alamat dan sulit mengajukan klaim.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak ada bukti keaslian produk, sangat meragukan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk, tidak sesuai dengan harga.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak menghormati janji garansi, sangat kecewa.",
        "sentiment": "negatif",
    },
]


Uxc_Sandisk = [
    {
        "comment": "Sepadan dengan Harga: Harga cukup baik\nFitur Terbaik: diskon harga cukup lumayan\nMemori terbaca dengan baik, pengiriman cepat, baru dicoba semoga awet karena beli dari distributor resmi, harga cukup  bersaing karena ada diskon yg cukup lumayan.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Menambah kekayaan\nSepadan dengan Harga: Semoga\nDari awal SanDisk tetap pilihan utama buat hal hal memory, \nDari jaman 1gb ampe sekarang belum juga rusak😅\n\nTerima kasih sudah melayani saya dengan cepat dan baik",
        "sentiment": "positif",
    },
    {
        "comment": "Kartu memorinya Bagus, \nKemasan masih segel, \nPengemasan normal rapi, \nPengiriman cepat, \nKartu Ori dan berfungsi normal. \nSemoga Awet dan tahan lama. \nTerima kasih juragan...",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Penyimpanan jd lebih banyak\nSepadan dengan Harga: Ya\nProduknya bisa dipakai. Pengiriman dan pengemasan produknya cepet. Semoga awet deh. Produk alhamdulillah ori, klo beli yg 128GB memang yg kita dapet 119GB penyimpanan. Penjelasannya ada di google.\nThanks",
        "sentiment": "positif",
    },
    {
        "comment": "Pesannya kmrn hr ini sdh dtg..cepet bgt.. Packaging jg rapi dan save.. Produk ori krn memang dr official store nya dan kapasitas jg real 128GB..kepotong 3MB buat sistemnya.. Puas belanja disini..miminnya pun super ramah..recommended store deh..layak dpt predikat star+..sukses trs ya..bakalan dtg lg",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat, respon penjual baik, packing rapih dengan bubble wrap, original, sd card terbaca, dapat freebies spidol biru..\nThanks seller..",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: 128 Gb\nSepadan dengan Harga: sepadan\nPaket diterima dalam keadaan baik, packing cukup, pengiriman cukup cepat, sudah dicoba dan sesuai. Semoga awet, terima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Cocok untuk hp android kecepatan 100mbps\nSepadan dengan Harga: Harga terjangkau..\nPengiriman cepat..",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Barang ori, barang cepat sampai\nSepadan dengan Harga: worth it kok\npengiriman cepat, paket lengkap, biayanya murce kemaren ekspedisi sameday. Barang ori, yang 1nya udh dimasukin ke cctv. Mantapp. Makasih yaa",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: bagus\nFitur Terbaik: bagus\nPenjual ramah dan pengemasannya sangat cepat terimakasih admin",
        "sentiment": "positif",
    },
    {
        "comment": "SandDisk micro SDXC 128 Gb ..\ndijamin original, garansi dari Astrindo.\nproduk ini, setelah dicoba dan ditest, berfungsi dengan sempurna.\nkecepatannya, sangat kencang.\nmakasi ..",
        "sentiment": "positif",
    },
    {
        "comment": "kualitas produk baik, produk original, harga produk sangat baik, kecepatan pengiriman sangat baik, respon penjual sangat baik, trimakasih👍🏼😉",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: ok\nFitur Terbaik: ok\nBarang sesuai deskripsi, original dan bisa berfungsi dengan sangat baik. Begitu dipasang di hp langsung terbaca, dan kecepatan transfer datanya jg sangat baik.",
        "sentiment": "positif",
    },
    {
        "comment": "official udah pasti barangnya asli dan bagus, tidak perlu di ragukan lagi keasliannya 👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: kapasitas real 119GB. itu normal boss, gw ga protes. kecepatan transfer data yaa sesuai dengan tipe\nSepadan dengan Harga: lumayan terjangkau dibandingkan beli secara offline\nDah bertahun-tahun pakai Mmc Sandisk, dan file di dalam nya selalu aman terjaga.. ga corrupt kayak merk anu",
        "sentiment": "positif",
    },
    {
        "comment": "Yes, Alhamdulillah barang datang dengan selamat, pengemasan baik, respon penjual baik, semoga awet, barang sangat bagus. Makasih, Seller.",
        "sentiment": "positif",
    },
    ## Negatif
    {
        "comment": "Produk ini sangat buruk. Fiturnya tidak sesuai dengan yang diharapkan dan tidak sepadan dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Respon penjual sangat buruk dan tidak membantu. Pengemasan juga sangat buruk dan barang rusak saat sampai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan barang tidak sesuai dengan pesanan. Saya merasa sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Produk ini sering mengalami masalah teknis dan tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga yang saya bayar terlalu tinggi untuk produk ini. Saya merasa seperti saya telah tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pelayanan penjual sangat buruk. Mereka tidak merespons keluhan saya dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat rapuh dan mudah rusak. Saya merasa seperti saya telah membuang uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan pengiriman yang lama dan produk yang tidak berkualitas. Saya tidak merekomendasikan pembelian dari penjual ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini terlalu mahal untuk kualitas yang sangat rendah. Saya merasa seperti saya telah ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan penjual tidak responsif. Produk ini tidak sesuai dengan ekspektasi saya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat tidak berguna. Saya menyesal telah membelinya. Fiturnya tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Produk ini sering mengalami masalah teknis dan sangat sulit digunakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat buruk. Saya merasa seperti saya telah membuang uang dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan sangat buruk dan barang rusak saat sampai. Seller tidak responsif dan tidak membantu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat tertipu dengan pembelian ini. Pengiriman sangat lambat dan barang tidak sesuai dengan pesanan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan barang ini. Kualitas produk sangat rendah dan harga yang saya bayar tidak sepadan.",
        "sentiment": "negatif",
    },
]


product_sandisk_8gb_pd = pd.DataFrame(SanDisk_CZ50_8GB)
product_sandisk_max_pd = pd.DataFrame(Max_Sandisk)
product_sandisk_240gb_pd = pd.DataFrame(SanDisk_240gb)
product_sandisk_128gb_pd = pd.DataFrame(Sandisk_128GB)
product_sandisk_Uxc_pd = pd.DataFrame(Uxc_Sandisk)


product_sandisk_8gb_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_sandisk_max_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_sandisk_240gb_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_sandisk_128gb_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_sandisk_Uxc_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)


print("Value counts Ke-1: ", product_sandisk_8gb_pd["sentiment"].value_counts())
print("Value counts Ke-2: ", product_sandisk_max_pd["sentiment"].value_counts())
print("Value counts Ke-3: ", product_sandisk_240gb_pd["sentiment"].value_counts())
print("Value counts Ke-4: ", product_sandisk_128gb_pd["sentiment"].value_counts())
print("Value counts Ke-5: ", product_sandisk_Uxc_pd["sentiment"].value_counts())


merge_df = pd.concat(
    [
        product_sandisk_8gb_pd,
        product_sandisk_max_pd,
        product_sandisk_240gb_pd,
        product_sandisk_128gb_pd,
        product_sandisk_Uxc_pd,
    ]
)


Positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan Positif:", Positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_sandisk.csv", index=False)

print("Data telah disimpan")
