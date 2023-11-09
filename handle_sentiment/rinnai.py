import pandas as pd


Kompor_Gas_3 = [
    {
        "comment": "Harga: ok, Kualitas: bagus, Kegunaan: berfungsi, Kompornya keren... Dgn harga segitu udah ada pemanggang nya. Dan admin rinnai nya juga ramah. Thanks rinnai. Sangat puas. Jd semangat masak buat suami",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: sesuai, Kualitas: bagus banget, Ketajaman: bagus sekaki, Barang bagus, pengiriman cepat, packing sangat aman sekali",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: terjangkau, Kualitas: baik, Kegunaan: sangat berguna, Recomended seller, good seller, original produk, fast respond seller👍👍👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: murah, Kualitas: original, cepet bgt. semoga awet. thank youu❣❣❣",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: Bagus banget, Performa: Semoga awet, Kualitas: Sepadan dengan harga, Syukurlah udah sampe barangnya, semoga awet ya amin. Kalo awet nanti beli lagi hhaha",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus, Performa: mantap, Kualitas: bagus sesuai harga, Pengiriman cepat produk original",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: ok, Kualitas: bagus, Ketajaman: ok, Cepet bgt nyampe nya, dan overall ok bgt lho",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: mewah, Performa: baik, Kualitas: baik, Semoga bermanfaat... sukses selalu buat rinnai....",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus bgt kompor nya cakep lagi keker keliatan nya, Gg nyesel deh pokok nya belanja d sini, Semoga awet nanti nya, Terimakasih😊",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya bagus, harganya juga murah, semua nyala dan berfungsi dgn baik, terima kasih shoope",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: sesuai, Kualitas: bagussss, Pengemasan rapih, aman, pengiriman cepat",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus, Sepadan dengan Harga: sepadan, Barang bagus aman maksi",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: yang penting original, Kualitas: bagus, Ketajaman: tajam? Haha, So far oke, semoga awet tiada kendala",
        "sentiment": "positif",
    },
    {
        "comment": "Kompornya bagus, pengiriman juga aman dan cepat. Checkout kemarin, hari ini datang. Kompornya belum dicoba. Mudah-mudahan bagus semua...",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah barangnya sudah sampai, barangnya bagus, tidak ada yang lecet. Terima kasih...",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus, body lumayan kokoh. Api cepat merata. Worth it lah untuk harga segitu",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Kualitas sangat buruk, kompor ini benar-benar mengecewakan. Harganya terlalu tinggi untuk barang seburuk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan pembelian ini. Kompornya tidak berfungsi dengan baik dan kualitasnya jelek. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga mahal, kualitas buruk. Saya merasa seperti pemborosan uang. Tidak ada yang bagus dari kompor ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitasnya sangat rendah, dan pengiriman sangat lambat. Saya sangat frustasi dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Jangan pernah membeli kompor ini. Kualitasnya sangat jelek, dan penjualnya tidak peduli. Saya merasa seperti ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga terlalu tinggi untuk barang yang tidak berfungsi dengan baik. Kualitasnya sangat buruk, dan pengiriman sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah kompor terburuk yang pernah saya beli. Harga yang saya bayar terasa sia-sia. Sangat marah dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa seperti dibohongi. Kualitas rendah, harga tinggi, pengiriman lambat. Pengalaman yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat rendah, dan kompor ini rusak saat tiba. Saya sangat kecewa dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga tidak sesuai dengan kualitasnya. Saya merasa seperti tertipu. Kompor ini adalah pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat jelek. Saya sangat menyesal membeli ini. Pengirimannya juga sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak ada yang baik dari kompor ini. Harga terlalu tinggi untuk kualitas yang sangat rendah. Saya merasa dipermainkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat marah dengan pembelian ini. Kompor rusak dan kualitasnya sangat rendah. Harga terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah barang yang sangat buruk. Kualitas rendah, pengiriman lambat, dan penjual tidak responsif. Jangan membelinya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa seperti pemborosan uang. Kompor ini tidak berfungsi dengan baik dan kualitasnya sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitasnya sangat rendah, dan harga yang saya bayar terasa sia-sia. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
]  # 16 Positif dan 16 Negatif


####

Kompor_Gas_1 = [
    {
        "comment": "Harga: standart, Kualitas: oke dan kuat, Ketajaman: oke banget, Terimakasih, packing safety, fast deliver",
        "sentiment": "positif",
    },
    {"comment": "Tampilan: ok, Performa: ok, Kualitas: ok, Ok", "sentiment": "positif"},
    {
        "comment": "Harga: lumayan, Kualitas: ori, Kegunaan: produk original, pengemasan rapih dan aman, pengiriman cpet bgt Bru smlem d kirim hri ni Uda smpe",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: oke, Kualitas: bagus mdh2an awet, Ketajaman: mantap, Pesen jam 2 sampe jam 4.. mantapp.. thanks",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: harga sesuai, Kualitas: ok sesuai harga, Ketajaman: baik, Barang ok mamah saya suka, packing rapi, pengiriman sangat cepat 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: harga oke, Kualitas: semoga awet, Kegunaan: semoga berfungsi dengan baik, Belum dicoba dipasangkan gas tapi semoga aman dan berfungsi dengan baik terimakasih",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah berfungsi dengan baik dan semoga awet terus, dan bermanfaat, Produk original, Respon penjual sangat ramah, Pengiriman cepat banget dari Jkt ke Madura cuma 4 hari pake JTR cargo",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: oke, Performa: oke, Kualitas: oke, Kualitas produk sangat baik, pengiriman sangat cepat, produk original, respon penjual sangat baik",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: Joss gandos kotos kotos, Performa: baik, Kualitas: baik, Sesuai pesanan, bagus, teman ku suka",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: lumayan, Kualitas: baik, Kegunaan: baik, Produk ori dari official store, semoga awett, kualitas semoga sesuai dengan harga",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: baik, Kualitas: baik, Ketajaman: baik, Oke oke Alhamdulillah ngga ada lecet barang normal juga nyala api besar. Maaf videonya nggabisa di upload tapi barang nya oke jgn ragu beli",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih... barang sudah sampai dengan kondisi sangat baik... produk original... respon penjual sangat baik...",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus, mantab bgt pengirimannya buble nya tebal bgt jadi barang sampai dengan selamat",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih... barang sudah sampai dengan kondisi sangat baik... produk original... respon penjual sangat baik...",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus, mantab bgt pengirimannya buble nya tebal bgt jadi barang sampai dengan selamat",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: Bagus, Performa: menarik, Kualitas: good, Semoga awet barang nya terimakasih:)",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: terjangkau, Kualitas: bagus, Kegunaan: sangat membantu. Senang sekali... sangat membantu... produknya lumayan bagus... penjualnya ramah terima kasih!",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: menawan, Performa: sangat baik, Kualitas: sangat tinggi. Barang ini sangat bagus, dan pengiriman sangat cepat. Saya sangat puas!",
        "sentiment": "positif",
    },
    ## Negatif
    {
        "comment": "Harga: terlalu mahal, Kualitas: sangat buruk, Ketajaman: nol. Produk ini adalah pemborosan uang. Saya sangat kecewa!",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: buruk, Performa: buruk, Kualitas: sangat jelek. Harga tidak sebanding dengan kualitasnya. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: mahal, Kualitas: palsu, Kegunaan: tidak berguna. Pengemasan buruk, pengiriman sangat lambat. Saya sangat frustasi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat buruk, dan harga yang saya bayar terasa seperti pemborosan uang. Saya merasa seperti ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: terlalu tinggi, Kualitas: sangat jelek, Ketajaman: nol. Produk ini adalah bencana! Pengalaman buruk sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat rendah, dan pengiriman sangat buruk. Saya sangat kecewa dengan pembelian ini. Harganya tidak sebanding.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: sangat mengecewakan, Performa: buruk, Kualitas: sangat jelek. Saya sangat marah dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: terlalu tinggi, Kualitas: sangat buruk. Saya merasa seperti dibohongi. Produk ini adalah salah satu yang terburuk yang pernah saya beli.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat jelek, dan harga yang saya bayar terasa sia-sia. Pengiriman juga sangat buruk. Saya merasa dipermainkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: sangat mahal, Kualitas: sangat rendah, Ketajaman: tidak ada. Saya sangat menyesal membeli produk ini. Pengirimannya sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat buruk, dan pengiriman sangat lambat. Harga terlalu tinggi untuk produk yang sangat jelek. Saya sangat marah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: pemborosan uang, Kualitas: sangat jelek, Kegunaan: tidak ada. Produk ini adalah kegagalan total! Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat rendah, dan penjualnya sangat tidak responsif. Pengalaman buruk sekali. Harga yang saya bayar terasa seperti pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: mahal sekali, Kualitas: sangat buruk! Kegunaan: nihil. Saya sangat marah dengan pembelian ini. Produk rusak saat tiba.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas sangat jelek, dan pengiriman sangat buruk. Saya sangat kecewa. Harga yang saya bayar terasa sia-sia. Saya merasa seperti tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: mengecewakan, Performa: sangat buruk, Kualitas: sangat rendah. Harga: pemborosan uang! Saya merasa seperti dipermainkan.",
        "sentiment": "negatif",
    }
    ## Negatif
]  # 16 Positif dan 16 Negatif


###
Burner = [
    {
        "comment": "Tampilan: Sesuai deskripsi, Performa: Bagus, Kuningan Halus, Kualitas: Original, Untuk pemakaian Rinnai grande RI 712 BGX",
        "sentiment": "positif",
    },
    {
        "comment": "Sempat tergoda untuk beli yang murah, karena perbedaan harga lumayan banyak, tapi takut gak pas di kompornya. Akhirnya beli di sini dan harga emang gak bohong ya. Kualitas udah pasti bagus. Dan api nyala merata lagi. Btw ini kompor udah 10 tahun jadi kayak baru lagi.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus, Performa: baik, Kualitas: Original, Bagus produk Ori gak KW. kompor seperti baru, Semoga awet. Trims....",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus, Performa: baik, Kualitas: Original, Bagus produk Ori gak KW. kompor seperti baru, Semoga awet. Trims....",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai pesanan, Aman sampai tujuan, Pengiriman cepat, Makasih ya",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah sudah sampai, original Rinnai ada kode nya, semoga awet ya. Dari kemarin beli nya yang mw aja jadi sering ganti, trimaksasih Shopee",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai etalase / ori, packet aman dan pengiriman cepat 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya bagus tebel berat, semoga awet bertahun-tahun",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih ya head tornadonya bagus, cocok sama kompornya, packing nya juga rapih",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: original, Performa: baik, Kualitas: sangat baik, Beli yang KW cari murah malah gak kpake, udahlah beli di store resmi aja barang ori udah pasti bagus, mahal tapi memang kualitas terjamin. Yang penting komporku nyala",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: sesuai barang, Kualitas: original, Kegunaan: pelengkap, Produk original, bekerja dengan baik, warna api biru, cocok dengan kompor BGX 12, dikemas dengan rapi dan baik. Pengiriman sesuai estimasi. Thank",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: keren, Kualitas: mantap, Performa: good, Pengiriman cepat. Kemasan aman rapih. Harga agak lebih mahal produk original",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: sesuai, Kualitas: sangat baik, Untuk RI-06 BGX. Asli krn dr beratnya saja sudah terasa. Pengiriman juga cepat. Terimakasih",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus, Performa: bagus, Kualitas: bagus, Packaging aman. Barang sampai dengan selamat.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: very good, Performa: very good, Kualitas: very good, Real pri",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus, Performa: bagus, Kualitas: original, Cocok dengan 712 TG",
        "sentiment": "positif",
    },
    {
        "comment": "Produk sesuai dengan deskripsi, kualitas terjamin, pengiriman cepat. Saya sangat puas dengan pembelian ini!",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Tampilan: Buruk, Performa: Buruk, Kualitas: Buruk, Barang cacat dan rusak, Pengiriman sangat lambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Buruk, Performa: Buruk, Kualitas: Buruk, Barang cacat dan rusak, Pengiriman sangat lambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu mahal, Kualitas: Sangat buruk, Tidak sesuai dengan deskripsi, Kecewa dengan produk ini, Tidak akan membeli lagi",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Tidak sesuai deskripsi, Performa: Buruk, Kualitas: Sangat buruk, Produk palsu, Mengalami kerusakan saat pengiriman",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sampai dengan baik, Pengiriman terlambat, Kompor rusak saat tiba, Tidak sesuai dengan yang diharapkan, Kecewa dengan layanan ini",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu mahal, Kualitas: Buruk, Kegunaan: Tidak berfungsi dengan baik, Produk tidak original, Respon penjual buruk",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Buruk, Performa: Sangat buruk, Kualitas: Tidak memuaskan, Pengemasan buruk, Pengiriman sangat terlambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Tidak sesuai, Kualitas: Buruk, Ketajaman: Sangat buruk, Tidak ada petunjuk penggunaan yang jelas, Pengiriman terlambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Tidak asli, Performa: Buruk, Kualitas: Palsu, Produk rusak saat tiba, Kecewa dengan pembelian ini",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Tidak sesuai, Kualitas: Tidak memuaskan, Kegunaan: Tidak berfungsi dengan baik, Tidak cocok dengan kompor, Pengiriman sangat lambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Palsu, Performa: Buruk, Kualitas: Sangat rendah, Produk tidak berkualitas, Kecewa dengan pelayanan",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu tinggi, Kualitas: Sangat buruk, Kegunaan: Tidak sesuai, Produk rusak, Pengiriman sangat lambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Tidak sesuai deskripsi, Performa: Buruk, Kualitas: Buruk, Barang rusak saat tiba, Kecewa dengan pembelian ini",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Tidak terjangkau, Kualitas: Sangat buruk, Ketajaman: Tidak ada, Pengiriman sangat lambat, Tidak akan merekomendasikan produk ini",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Tidak asli, Performa: Sangat buruk, Kualitas: Palsu, Produk tidak berfungsi, Kecewa dengan produk ini",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu mahal, Kualitas: Tidak memuaskan, Kegunaan: Tidak berguna, Pengemasan buruk, Pengiriman sangat terlambat",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan produk ini. Kualitasnya sangat buruk, dan pengiriman sangat lambat. Saya merasa seperti pemborosan uang.",
        "sentiment": "negatif",
    },
]


###


Kompor_Gas_1_tungku = [
    {
        "comment": "Tampilan: Baik\nPerforma: Baik\nKualitas: Baik\nSetelah sekian lama pake, baru review. Alhamdulillah paketnya nyampe dengan aman, tanpa ada kurang dan rusak sama sekali. Kompor dan regulatornya bekerja sesuai yg di harapkan bagus. Apinya juga bagus. Kompornya nyala tentunya Alhamdulillah. Terima kasih seller, semoga komporku ini awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus\nPerforma: ok\nKualitas: tidak diragukan merk rinai\nSudah diterima dengan aman alhamdulillah. Tinggal belum di coba kompornya. Semoga sich aman....\nRecomended toko kelola shopee... tks ya 👌👍",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: Relatif lah, plus minus kalau soal harga\nKualitas: Oke, barang original sepertinya, sesuai ekspektasi\nKetajaman: Owh tajam sekali apinya, panas, api biru.\nGak repot sudah satu bundling kompor dan regulator, cukup nambah beli gas melon saja sekitar Rp 190.000,- (include isi), harga bisa beda² di tempat anda. Saya masih dibawa garis kemiskinan jadi masih pakai gas subsidi, mohon maaf ya pemerintah, pengennya beli blue gas tapi gak da yang kecil.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: kokoh bukan kaleng²\nPerforma: api biru lancar\nTampilan: bagus elegan dengan warna hitam nya",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah barang sampe dengan selamat😊nyampe dengan selamat. barang juga komplit. pengiriman standan. pengemasan lumayan rapi. semoga kompornya awet...aamiin",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: harga lumayan untuk 1 set\nKualitas: baik\nKetajaman: api aman\nAlhamdulillah barang nyampe aman dan ga ada yang rusak bisa di pakai dengan baik terima kasih kak",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: terjangkau\nKualitas: belum tau\nKetajaman: belum tau\npesanan trlah sampai,,barang lengkap gak ada yg kurang,,belum d coba semoga berpungsi dgn baik 🙏🙏🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: Lumayan\nKualitas: Bagus\nKetajaman: ? \nKompor bagus, pengiriman nya juga cepet, tp untuk regulator nya ada penyok sedikit😌",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: lumayan\nKualitas: bagus\nLebih murah di sini,barangnya nyampe tanpa cacat,semuanya bagus,lengkap..pokoknya gak nyesel beli di sini👍🏽👍🏽",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: lumayan\nKualitas: bagus\nKetajaman: ok\nbarang ori,lengkap,blm d rakit,pengiriman sangat cepat,kemasan ok,thankss shopee",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: baik\nKualitas: baik\nKetajaman: baik\nSampai dengan baik tp ada penyok sedikit saja\nKompornya bagus.Terimakasih",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: bersaing\nKualitas: lumayan buat anak kos\nKetajaman: bagus\nLumayan buat d kosan dan produk rinnai skh mmang gak ragu lagi .bagus dan terpercaya",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: Good\nKualitas: Good\nKetajaman: Good\nRespon ramah, teliti, rapih & aman, barang yg dikirim sesuai pesanan, pengemasan & pengiriman cepat, terimakasih banyak",
        "sentiment": "positif",
    },
    {
        "comment": "Harga:  Terjangkau dari pada beli offline \nKualitas: Bagus banget\nKetajaman: Apanih? Wkwk\nBagus banget kompornya, berfungsi dengan baik. Regulator + selang aman terkendali ga susah buat nyambung ke tabung. Bismillah no bocor bocor. Kartu garansi lengkap, gaada cacat. Sip lah recomended",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: terjangkau\nKualitas: baik\nKetajaman: bagus\nNtapssssss, baru pesen kemaren sore. Udh sampe aja😍😍 semoga awet! Thanks seller!",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus\nPerforma: ok\nKualitas: baguss\nPas pemasangan nya agak sulit sih\nGatau sih krna belum pernah sama sekali pasang nya\nKata orang rinnai bagus\nDan semua rata2 recommend ini sih\nSemoga awet dan performa nya bagus",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Harga: Mahal sekali\nKualitas: Buruk sekali\nKetajaman: Sangat jelek\nBarang ini sungguh mengecewakan. Harganya terlalu tinggi, kualitasnya buruk, dan api kompornya bahkan tidak stabil.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Jelek\nPerforma: Sangat buruk\nKualitas: Tidak sebanding dengan harganya\nSayang sekali, kompor ini benar-benar mengecewakan. Tampilannya jelek, performanya sangat buruk, dan kualitasnya tidak sesuai dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Tidak sepadan\nKualitas: Sangat rendah\nKetajaman: Tidak ada\nSaya sangat kecewa dengan pembelian ini. Harganya tidak sepadan dengan kualitas yang sangat rendah. Bahkan ketajamannya nol.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Sangat buruk\nPerforma: Tidak memuaskan\nKualitas: Sangat rendah\nSaya merasa menyesal membeli kompor ini. Tampilannya sangat buruk, performanya tidak memuaskan, dan kualitasnya sangat rendah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Mahal\nKualitas: Sangat buruk\nKetajaman: Nol\nKompor ini adalah pemborosan uang. Harganya mahal, tapi kualitasnya sangat buruk, dan api kompornya bahkan tidak ada ketajaman sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Mengerikan\nPerforma: Sangat buruk\nKualitas: Buruk\nSungguh mengerikan! Kompor ini tampilannya buruk, performanya tidak memuaskan, dan kualitasnya juga rendah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu tinggi\nKualitas: Sangat rendah\nKetajaman: Tidak ada\nSaya merasa ditipu dengan harga yang terlalu tinggi untuk produk dengan kualitas yang sangat rendah. Tidak ada ketajaman dalam kompor ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Sangat jelek\nPerforma: Buruk\nKualitas: Tidak memadai\nSaya sangat kecewa dengan kompor ini. Tampilannya sangat jelek, performanya buruk, dan kualitasnya tidak memadai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Mahal\nKualitas: Sangat rendah\nKetajaman: Tidak ada\nSaya benar-benar menyesal membeli kompor ini. Harganya mahal, tetapi kualitasnya sangat rendah, dan tidak ada ketajaman sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Mengerikan\nPerforma: Tidak memuaskan\nKualitas: Buruk\nIni adalah pembelian terburuk yang pernah saya lakukan. Tampilan kompornya mengerikan, performanya tidak memuaskan, dan kualitasnya buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Tidak sepadan\nKualitas: Sangat rendah\nKetajaman: Nol\nSaya merasa tertipu dengan harga yang tidak sepadan dengan kualitas yang sangat rendah. Bahkan, tidak ada ketajaman pada kompor ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Sangat buruk\nPerforma: Sangat jelek\nKualitas: Tidak memadai\nSungguh mengecewakan. Tampilannya sangat buruk, performanya sangat jelek, dan kualitasnya tidak memadai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu mahal\nKualitas: Sangat rendah\nKetajaman: Tidak ada\nSaya sangat menyesal telah mengeluarkan uang sebanyak ini untuk kompor yang kualitasnya sangat rendah. Bahkan tidak ada ketajaman pada api kompornya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Mengerikan\nPerforma: Buruk sekali\nKualitas: Tidak sebanding dengan harga\nKompor ini benar-benar mengerikan. Tampilannya buruk, performanya sangat buruk, dan kualitasnya tidak sebanding dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu tinggi\nKualitas: Sangat rendah\nKetajaman: Tidak ada\nSaya merasa sangat kecewa dengan pembelian ini. Harganya terlalu tinggi untuk kualitas yang sangat rendah. Tidak ada ketajaman pada kompor ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: Sangat jelek\nPerforma: Sangat buruk\nKualitas: Buruk sekali\nSungguh malapetaka. Kompor ini memiliki tampilan yang sangat jelek, performa yang sangat buruk, dan kualitas yang sangat buruk.",
        "sentiment": "negatif",
    },
]  # 16 Positif dan 16 Negatif


print("Kompor Gas 1: ", len(Kompor_Gas_1))


####

Kompor_Gas_tunggu_2 = [
    {
        "comment": "Kompor gas ini sangat luar biasa! Dua tungku memungkinkan saya memasak lebih efisien, dan desainnya membuat dapur saya terlihat lebih modern. Sangat puas dengan pembelian ini!",
        "sentiment": "positif",
    },
    {
        "comment": "Saya senang dengan kualitas produk ini. Material stainless steel membuatnya terlihat kokoh, dan fitur pemantik mekaniknya sangat praktis. Terima kasih, Rinnai!",
        "sentiment": "positif",
    },
    {
        "comment": "Kompor gas ini adalah investasi yang sangat baik untuk dapur saya. Material terbaik dan desain modern membuatnya menjadi pilihan terbaik. Sangat puas!",
        "sentiment": "positif",
    },
    {
        "comment": "Dapur saya sekarang terlihat lebih rapi dan modern berkat kompor gas ini. Kualitas produknya sangat baik, dan saya senang bisa memasak dengan dua tungku sekaligus. Rekomendasi!",
        "sentiment": "positif",
    },
    {
        "comment": "Kompor gas ini sangat mudah dibersihkan berkat lapisan anti lengketnya. Kualitasnya tidak diragukan lagi, dan harga yang terjangkau membuatnya sempurna!",
        "sentiment": "positif",
    },
    {
        "comment": "Saya sudah lama mencari kompor gas dengan fitur seperti ini. Dua tungku memungkinkan saya menghemat waktu memasak. Terima kasih, Rinnai!",
        "sentiment": "positif",
    },
    {
        "comment": "Dengan kompor gas ini, saya bisa memasak makanan dengan mudah dan efisien. Material stainless steel memberikan tampilan yang sangat bagus. Puas!",
        "sentiment": "positif",
    },
    {
        "comment": "Rinnai benar-benar memahami kebutuhan memasak saya. Kompor gas 2 tungku ini sangat membantu. Dapur saya kini semakin lengkap!",
        "sentiment": "positif",
    },
    {
        "comment": "Kompor gas ini adalah solusi sempurna untuk dapur saya. Material stainless steel membuatnya tahan lama, dan pemantik mekaniknya sangat praktis. Bagus sekali!",
        "sentiment": "positif",
    },
    {
        "comment": "Produk ini sangat berkualitas dan sesuai dengan harga terbaik. Saya senang bisa memasak dengan dua tungku sekaligus. Terimakasih, Rinnai!",
        "sentiment": "positif",
    },
    {
        "comment": "Kompor gas ini adalah solusi sempurna untuk dapur saya. Material stainless steel membuatnya tahan lama, dan pemantik mekaniknya sangat praktis. Bagus sekali!",
        "sentiment": "positif",
    },
    {
        "comment": "Saya senang bisa menemukan produk ini. Kualitasnya sangat baik, dan dua tungku memungkinkan saya memasak lebih banyak makanan dalam satu waktu. Rekomendasi!",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk ini memang terjamin. Desainnya sangat modern, dan anti lengket membuatnya mudah dibersihkan. Rinnai memang pilihan terbaik!",
        "sentiment": "positif",
    },
    {
        "comment": "Kompor gas ini sangat membantu dalam memasak. Material stainless steel memberikan kesan yang kuat, dan pemantik mekaniknya sangat nyaman digunakan. Saya suka!",
        "sentiment": "positif",
    },
    {
        "comment": "Rinnai benar-benar memahami kebutuhan dapur modern. Dengan kompor gas 2 tungku ini, saya bisa memasak dengan lebih efisien. Puas sekali!",
        "sentiment": "positif",
    },
    {
        "comment": "Produk ini memenuhi ekspektasi saya. Kualitasnya sangat baik, desainnya modern, dan harganya terjangkau. Terima kasih, Rinnai, atas produk yang luar biasa!",
        "sentiment": "positif",
    },
    {
        "comment": "Saya sangat puas dengan kompor gas ini. Dua tungku memungkinkan saya memasak dengan lebih efisien, dan desainnya memberikan tampilan modern untuk dapur saya. Ini adalah investasi yang sangat baik!",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Produk ini sangat mengecewakan. Kualitasnya buruk dan tidak tahan lama. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kompor gas ini sangat sulit digunakan. Fitur pemantik mekaniknya sering macet dan sulit dinyalakan. Saya menyesal membeli produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Dapur saya menjadi lebih berantakan setelah menggunakan kompor ini. Lapisan anti lengketnya tidak berfungsi dengan baik. Saya merasa frustasi dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kompor gas ini mudah rusak dan sering bocor gas. Saya merasa tidak aman menggunakan produk ini. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini tidak sebanding dengan kualitasnya. Saya merasa sangat rugi dan menyesal membeli kompor gas ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kompor ini tidak sesuai dengan deskripsi. Materialnya terasa murahan dan cepat rusak. Pengiriman juga lambat. Saya merasa sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat marah dengan produk ini. Tidak ada nilai tambah dalam penggunaan kompor gas ini. Saya tidak merekomendasikan produk ini kepada siapa pun.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas kompor gas ini sangat rendah. Tidak ada daya tahan, dan desainnya juga buruk. Saya sangat menyesal membeli produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat terganggu dengan produk ini. Fitur pemantik mekaniknya sering rusak, dan pemasangannya sulit. Sangat sulit digunakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kompor gas ini tidak memiliki daya tahan. Saya hanya menggunakannya beberapa kali, dan sudah rusak. Saya sangat marah dengan kualitas produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengalaman saya dengan produk ini sangat buruk. Tidak ada yang baik dari kompor gas ini. Saya sangat menyesal membelinya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas kompor ini sangat rendah. Saya merasa sangat kecewa dengan pembelian ini. Saya tidak merekomendasikan produk ini kepada siapa pun.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat menyesal membeli produk ini. Tidak ada yang positif tentang kompor gas ini. Tidak ada daya tahan, dan fitur pemantiknya tidak berfungsi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kompor gas ini tidak awet sama sekali. Saya hanya menggunakannya beberapa bulan, dan sudah rusak. Saya merasa sangat tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk ini sangat jelek. Tidak sesuai dengan deskripsi dan harga yang mahal. Saya sangat menyesal membeli kompor gas ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk ini sangat jelek. Tidak sesuai dengan deskripsi dan harga yang mahal. Saya sangat menyesal membeli kompor gas ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga: Terlalu mahal\nKualitas: Sangat buruk\nKetajaman: Tidak ada\nSaya merasa sangat kecewa dengan pembelian ini. Harganya terlalu mahal untuk kualitas yang sangat buruk. Tidak ada ketajaman pada kompor ini.",
        "sentiment": "negatif",
    },
]  # 16 Positif dan 16 Negatif


product_Gas_3_pd = pd.DataFrame(Kompor_Gas_3)
product_Gas_1_pd = pd.DataFrame(Kompor_Gas_1)
product_Burner_pd = pd.DataFrame(Burner)
Kompor_Gas_tunggu_1_pd = pd.DataFrame(Kompor_Gas_1_tungku)
product_Gas_tunggu_2_pd = pd.DataFrame(Kompor_Gas_tunggu_2)


product_Gas_3_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Gas_1_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Burner_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
Kompor_Gas_tunggu_1_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Gas_tunggu_2_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)


print("Value counts Ke-1: ", product_Gas_3_pd["sentiment"].value_counts())
print("Value Counts Ke-2: ", product_Gas_1_pd["sentiment"].value_counts())
print("Value Counts Ke-3: ", product_Burner_pd["sentiment"].value_counts())
print("Value Counts Ke-4: ", Kompor_Gas_tunggu_1_pd["sentiment"].value_counts())
print("Value Counts ke-5: ", product_Gas_tunggu_2_pd["sentiment"].value_counts())


### merge

merge_df = pd.concat(
    [
        product_Gas_3_pd,
        product_Gas_3_pd,
        product_Burner_pd,
        Kompor_Gas_tunggu_1_pd,
        product_Gas_tunggu_2_pd,
    ]
)


Positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan Positif:", Positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_rinnai.csv", index=False)

print("Data telah disimpan")
