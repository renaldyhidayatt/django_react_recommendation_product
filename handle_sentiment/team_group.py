import pandas as pd


Ssd_m2_256 = [
    {
        "comment": "Alhamdulillah, barang sesuai, original, packing baik, respon cepat, dapat harga flash sale saat live jd dpt diskon n voucher jg, mantul, ditambah lagi masya Allah dpt bonus fd Team 16gb USB 3.2. Makasih byk ya, semoga lancar n berkah usahanya, aamiin allahuma aamiin 🙏🤲",
        "sentiment": "positif",
    },
    {
        "comment": "Produk original 😍😍😍 tapi belum nyoba masang sih 😅 Pengemasan super aman + super kilattt, hari ini pesen lgsg dikirim hari itu jg👍👍👍 Dapat masker gratis pula👍👍👍 Mantap seller, semoga selalu amanah👍👍👍 Terimakasih 👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantap. Sepadan dengan Harga: terbaik. Mantap tinggal test max kecepatan data transfer. Terima Kasih banyak untuk TeamGroup.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Baik. Sepadan dengan Harga: Baik. Barang mendarat dengan aman dan baik dan semoga awet dan cocok Aamiin",
        "sentiment": "positif",
    },
    {
        "comment": "Barang mantap, sesuai deskripsi. Alhamdulillah, berfungsi dengan baik. Kedua kalinya belanja di TeamGroup. Selalu memuaskan.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Baik. Sepadan dengan Harga: Sangat sepadan. Alhamdulilah pesanan telah sampai dengan selamat. Dari RAM+m.2 NVMe lebih percaya sama merk ini. Top markotop, RAM dari tahun 2018 sampai sekarang masih awet, dari awal punya laptop biasa sampai punya yang gaming. Mudah2an kualitasnya serupa dengan RAMnya. 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Barang original. Kualitas mantap. SSD NVMe Teamgroup memang luar biasa, read and write-nya joss. Semoga awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: belum dicoba dan install di komputer, semoga awet dan sepertinya underrated. Sepadan dengan Harga: cukup miring dengan review di internet yang tidak jelek. Mari kita coba.",
        "sentiment": "positif",
    },
    {
        "comment": "Paket mendarat dengan aman, pengiriman cepat, baru pesan kemarin hari ini sudah sampai. Terimakasih min.",
        "sentiment": "positif",
    },
    {
        "comment": "SSD-nya aman dan sudah dipasang, migrasi lancar. JNT lelet.",
        "sentiment": "positif",
    },
    {
        "comment": "Seller responsif, pengiriman cepat, packing rapi. Belum dicoba, masih nunggu beberapa part lain. Semoga awet. Terimakasih bonus maskernya.",
        "sentiment": "positif",
    },
    {
        "comment": "Packing rapi, tebal. Ga banyak basa basi. Langsung dikirim di hari pertama pesan. Terbilang cepat pengiriman. Dan... SSD works af. Niceee....",
        "sentiment": "positif",
    },
    {
        "comment": "Selalu bagus. Mantab banget. Tidak pernah mengecewakan. Packing cepat.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah diterima dalam kondisi yang baik dan tidak ada kendalanya. Terimakasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: meningkatkan performance laptop. Sepadan dengan Harga: sangat worth it. Pengiriman cepat, instalasi mudah, barang sesuai dengan deskripsi.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: iyaa. Fitur Terbaik: Fast. kece. 2 hari nyampe. Gileee banget. Teamgroup memang oke, gausah diragukan lagi. Oiya dapet bonus flash drive 16 GB, lumayan banget. Thanks TG.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang rusak saat tiba, pengemasan buruk. Kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: jelek. Sepadan dengan Harga: mahal. Tidak puas dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak responsif, pengiriman sangat lambat. Buruk sekali pengalaman berbelanja.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai deskripsi, sangat mengecewakan. Saya tidak merekomendasikan ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak berfungsi. Sepadan dengan Harga: terlalu mahal. Saya menyesal membeli ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang hilang dalam pengiriman, penjual tidak memberikan solusi. Pengalaman yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk, produk tiba dalam keadaan rusak. Sangat tidak puas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak ada. Sepadan dengan Harga: sangat mahal. Saya merasa ditipu dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Seller tidak jujur, produk palsu. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat terlambat, barang baru tiba setelah berbulan-bulan. Sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak berfungsi sama sekali. Sepadan dengan Harga: mahal. Pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat tiba, penjual tidak merespons keluhan. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak berkualitas, fitur-fitur rusak. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak sesuai deskripsi. Sepadan dengan Harga: mahal. Penjual tidak terpercaya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk, produk tiba dalam keadaan rusak parah. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Seller tidak mengirim produk, uang saya hilang. Pengalaman yang sangat buruk.",
        "sentiment": "negatif",
    },
]


Ssd_256 = [
    {
        "comment": "Penjual ramah dan responsif, meskipun banyak nanya tetap dijawab. Pengiriman sangat cepat, kemarin sore dikirim, tadi pagi jam 10.30 sampai. Packing baik. Dapet bonus mask. Belum dicoba, karena hdd laptop saya masih proses backup ke cloud. Mudah-mudahan cocok dan awet ssd nya.",
        "sentiment": "positif",
    },
    {
        "comment": 'Dari dulu selalu percaya sih sama kualitas teamgroup gak abal", selain seller responsif dan komunikatif, packing kardus good. Top markotop !',
        "sentiment": "positif",
    },
    {
        "comment": "Sip sesuai barangnya, packing jiga baguss sip sip rekomendasi.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantaap, Sepadan dengan Harga: terjangkau, Barang sudah sampai dg selamat..belum dicoba tapi semoga berfungsi dg baik dan awet..",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: original , authentic, Sepadan dengan Harga: sangat worth it sekali, Seller nya best, responsif waktu di chat dan di tanya, langsung di proses, 2 jam sampai, harga buat ssd ini worth it, barang pasti authent, keren. Thanks seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baik dan bagus, Sepadan dengan Harga: ssd, Entah kenapa yang terbaca di laptop gak sampai 256, tapi gak masalah yang penting lancar jos.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Bagus\nSepadan dengan Harga: Pas\nMantul... Install win10 cepat",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Terbaik\nSepadan dengan Harga: sepadan\nMantab berfungsi dengan baik semoga awet dan tidak ada apa apa, cocok untuk yang mau up grade laptop kentang dengan harga terjangkau dan berkualitas baik",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus\nBarang bagus, sesuai dengan pesanan. Packing aman dan rapi, Semoga cocok di laptop saya. Free kalender 2023 juga nih, thanks seller",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: sepadan bgt\nFitur Terbaik: kualitas top\nProduk baik pengiriman standar harga rasional quality oke punya mudahan tahan lama",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ssd\nSepadan dengan Harga: ssd\nTerima kasih seller pengiriman ssd nya cepat banget loh",
        "sentiment": "positif",
    },
    {
        "comment": "Packing nya ala kadarnya, tapi ya lumayan dari pada gk di kardusin.\nDi dalam ada bubble wrap nya juga.\nKualitas nya belum tau, belum dicoba. Semoga baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Pesanan sudah diterima. Fast respon. Mantap. Tapi belum dicoba.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: performa laptop ku jadi cepat\nSepadan dengan Harga: ya",
        "sentiment": "positif",
    },
    {
        "comment": "Admin seller ramah bintang 5, barang sampai dengan aman dan tanpa minus, sudah di coba aman dan sat set jika di bandingkan dengan HDD, bonus masker, barang sampai namun sudah terbuka, kemungkinan di pasang segel dulu.\nSemoga Awet sampe puluhan tahun (hehe)\nDi beli Rp.465.000 per tanggal 31 Mei 2022",
        "sentiment": "positif",
    },
    {
        "comment": "Laptop jadi enteng buka semuanya. Pake app design jg enak. Untuk kualitas ketahanan brp lama kita coba dlulu. Thx",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman sangat lambat dan produk rusak. Sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak responsif dan sulit dihubungi. Produk juga tidak sesuai deskripsi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sudah menunggu lama untuk pengiriman, tetapi produknya tidak sampai dan penjual tidak memberikan informasi yang jelas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat buruk. Produk tidak berfungsi sama sekali dan penjual tidak mau bertanggung jawab.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing buruk, produk rusak saat sampai. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lambat. Saya membutuhkan produk ini dengan segera, tetapi harus menunggu berhari-hari.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak berkualitas. Saya sudah mencobanya dan langsung rusak.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak jujur. Produknya palsu dan penjual tidak memberikan informasi yang benar.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman tertunda tanpa alasan yang jelas. Sangat tidak puas dengan pelayanan ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai dengan yang diiklankan. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak kompeten. Produk rusak saat sampai dan penjual tidak bisa memberikan solusi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya membeli produk ini dengan harga yang tinggi, tetapi kualitasnya sangat rendah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak dan penjual tidak responsif. Saya sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lambat dan produk tidak berkualitas. Saya tidak merekomendasikan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa tertipu. Produk palsu dan penjual tidak bertanggung jawab.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat buruk. Produk tidak awet dan penjual tidak memberikan garansi yang baik.",
        "sentiment": "negatif",
    },
]


Ssd_128gb = [
    {
        "comment": "Barang sesuai pesanan dan telah dicoba berfungsi dengan baik. Pelayanan dan pengiriman sangat cepat. Rekomendasi!",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai pesanan, segel warranty juga masih aman, semoga barang awet. Terima kasih ya min.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baik sekali. Sepadan dengan Harga: sangat sepadan. Pengiriman cepat, produk original, dapet bonus masker, rekomendasi buat yang mau upgrade laptop KENTANGnya.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantap. Sepadan dengan Harga: mantap. Packing aman, respon cepat, pengiriman juga cepat. 👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: sipp. Sepadan dengan Harga: mantap. 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: pengiriman cepat. Sepadan dengan Harga: sangat puas. Sudah yang kedua kalinya cuma yang pertama beda tipe saja, thanks, barang berfungsi dengan sangat baik. 👍👌",
        "sentiment": "positif",
    },
    {
        "comment": "Biasanya klau Shopee Mall/Official packing-nya pake dus oren tulisan Shopee, tp ini cuma pake bubble wrap 2 lapis d lpisi sma dus aja, tp it's ok lah karna barang mendarat dgn aman, wlau kemasan SSD nya uda d buka, mungkin utk nmpel stiker garansi nya, positif tingking aja ini ori karna dri officialny.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: cepat. Sepadan dengan Harga: ya. Barang berfungsi baik. Sudah dites, tapi belum coba diinstal windows.",
        "sentiment": "positif",
    },
    {
        "comment": "Packing bagus dan aman dengan bubble wrap. Kualitas harusnya tdk diragukan lagi. Nanti dibuktikan kalau udah dicoba.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sampai. Sesuai deskripsi, kemasan udah kebuka, mungkin bekas pemeriksaan, segel aman. Mudahan ga ada masalah waktu instal ulang. Terima kasih. Update: Udah instal ulang dan aman. SSD bikin laptop jadul gw kenceng abis. Terima kasih Teqmgrup, akhirnya laptop jadul saya bisa hidup lagi 🤣. AO722.",
        "sentiment": "positif",
    },
    {
        "comment": "Produk sudah diterima dengan kondisi normal, segel terpasang dengan baik, dan ditest dalam kondisi baik. Rekomendasi mend mend 🤙🤙🤙",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ngebut seperti ku reply chat si dia. Sepadan dengan Harga: sangat sangat worth it👍. Top markotoppp joss markojosssssssss. Sangat jauh perbedaan make HDD ke SSD. HDD: ngambil sarjana baru nyala. SSD: Kedip doang dah bisa maen 👍👍. Kalo ada masalah bisa di claim garansi entar kata seller nya, TOP dah 👍👍.",
        "sentiment": "positif",
    },
    {
        "comment": "Sesuai pesanan pengiriman cepat official store mantap dapat kalender.",
        "sentiment": "positif",
    },
    {
        "comment": "Cepat sampai, performanya mantep, semoga awet, dapet bonus masker juga.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat, packing rapih barang sesuai, semoga awet² dah, berfungsi dengan normal, recommended seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih pesanan datang dengan selamat. Packing rapih dan respon seller baik. Produk original. Pokoknya sangat puas.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang tidak sesuai pesanan dan telah dicoba berfungsi dengan buruk. Pelayanan dan pengiriman sangat lambat. Tidak direkomendasikan!",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai pesanan, segel warranty juga rusak, semoga barang cepat rusak. Terima kasih ya min.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: buruk sekali. Sepadan dengan Harga: sangat tidak sepadan. Pengiriman lambat, produk palsu, tidak ada bonus masker, tidak direkomendasikan buat yang mau upgrade laptop KENTANGnya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: buruk. Sepadan dengan Harga: buruk. Packing rusak, respon lambat, pengiriman juga lambat. 👎👎👎",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: buruk. Sepadan dengan Harga: buruk. 👎",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: pengiriman lambat. Sepadan dengan Harga: sangat tidak puas. Sudah yang kedua kalinya cuma yang pertama beda tipe saja, tidak puas, barang tidak berfungsi dengan baik. 👎👌",
        "sentiment": "negatif",
    },
    {
        "comment": "Biasanya kalau Shopee Mall/Official packing-nya pake dus oren tulisan Shopee, tp ini cuma pake bubble wrap 2 lapis d lpisi sama dus aja, dan barang rusak, mungkin utk nmpel stiker garansi nya, sangat negatif tingking aja ini palsu karna dari officialny.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: lambat. Sepadan dengan Harga: ya. Barang tidak berfungsi baik. Sudah dites, tapi belum coba diinstal windows, dan tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing buruk dan tidak aman dengan bubble wrap. Kualitas harusnya tdk diragukan lagi. Nanti dibuktikan kalau udah dicoba, tetapi tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang sampai. Tidak sesuai deskripsi, kemasan sudah kebuka, mungkin bekas pemeriksaan, segel rusak. Mudahan ada masalah waktu instal ulang. Tidak puas. Update: Tidak bisa instal ulang dan tidak aman. SSD tidak membuat laptop jadul gw kenceng abis. Tidak terimakasih Teqmgrup, akhirnya laptop jadul saya tidak bisa hidup lagi 🤣. AO722.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk sudah diterima dengan kondisi rusak, segel terpasang dengan buruk, dan ditest dalam kondisi buruk. Tidak direkomendasikan mend mend 🤙🤙🤙",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: lambat seperti ku reply chat si dia. Sepadan dengan Harga: sangat sangat tidak worth it👎. Top markotoppp joss markojosssssssss. Sangat jauh perbedaan make HDD ke SSD. HDD: ngambil sarjana baru nyala. SSD: Kedip doang dah tidak bisa maen 👎👎. Kalo ada masalah bisa di claim garansi entar kata seller nya, sangat buruk 👎👎.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak sesuai pesanan pengiriman sangat lambat official store tidak mantap tidak dapat kalender.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak cepat sampai, performanya tidak mantap, tidak semoga awet, tidak dapat bonus masker juga.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman lambat, packing buruk, barang tidak sesuai, tidak semoga awet² dah, tidak berfungsi dengan normal, tidak direkomendasikan seller.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak lancar. Sepadan dengan Harga: Kualitas tidak sesuai harga. Tidak puas dengan produk ini, kualitas tidak terjamin. 😁",
        "sentiment": "negatif",
    },
]


Ddr4_4Gb = [
    {
        "comment": "Barang belum dicoba, semoga berfungsi dengan normal. Barang sesuai foto dan deskripsi. Pengiriman cepat. Respon penjual cepat. Dibungkus dengan rapih.",
        "sentiment": "positif",
    },
    {
        "comment": "Pesanan sudah sampai, pengiriman cepat, packing aman walaupun cuma 1 keping.",
        "sentiment": "positif",
    },
    {"comment": "Membantu?", "sentiment": "positif"},
    {
        "comment": "Overall bagus, cuma kalo chat kurang responsive 😅.",
        "sentiment": "positif",
    },
    {
        "comment": "Keren, dikemas dengan aman, pengiriman cepat, dan seller ramah👍🏻. Maaf gak ke foto, langsung di terap hehe.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat banget, order hari Sabtu sore, Senin siang udah sampai. Packing aman dan rapi. Mantap banget lah.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah sampai tapi belum diuji, semoga aman saja.",
        "sentiment": "positif",
    },
    {
        "comment": "Sudah sampai dan dicoba, berfungsi dengan baik. Jadi agak menghela nafas dengan enak nih PC ane pakai tambahan RAM yang baru ane beli. OK punya Team Elite, maturnuwun. Sip!",
        "sentiment": "positif",
    },
    {
        "comment": "Mantap banget di toko resmi, dapet masker pula. Barang selamat sampai tujuan, sesuai pesanan 👍🏼.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai deskripsi. Pengiriman cepat. Thanks ya. 😉",
        "sentiment": "positif",
    },
    {"comment": "Barang ok, bekerja dengan baik.", "sentiment": "positif"},
    {"comment": "Mantap... barangnya cepat sampainya.", "sentiment": "positif"},
    {
        "comment": "Mantullll, terimakasih sellerrrr semoga kedepannya lebih baik lagi.",
        "sentiment": "positif",
    },
    {"comment": "Suka sama produk Team Elite.", "sentiment": "positif"},
    {
        "comment": "Barangnyaaaaaaaa bagussssssss sesuai ekspektasiiiiii.",
        "sentiment": "positif",
    },
    {"comment": "Mantab gan.... Ngebutttt.", "sentiment": "positif"},
    ## Negatif
    {
        "comment": "Barang ini sangat buruk. Tidak sesuai dengan deskripsi dan tidak berfungsi dengan baik. Saya merasa sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan barang rusak saat sampai. Respon penjual juga buruk, tidak membantu sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai ekspektasi. Saya merasa seperti saya telah membuang uang untuk produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk, barang rusak saat sampai. Penjual tidak responsif dan tidak bertanggung jawab.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat, dan barang yang diterima dalam kondisi buruk. Saya sangat kecewa dengan pengalaman ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah, tidak berfungsi dengan baik. Saya merasa seperti saya telah tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak ramah dan kurang responsif. Barang yang diterima tidak sesuai dengan pesanan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan pengiriman yang lambat. Produk ini sangat buruk dan tidak sesuai dengan deskripsi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini terlalu mahal untuk kualitas yang sangat rendah. Saya merasa seperti saya telah ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat tidak berguna. Saya menyesal telah membelinya. Fiturnya tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Saya merasa seperti saya telah membuang uang dengan pembelian ini.",
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
        "comment": "Produk ini sangat buruk. Fiturnya tidak sesuai dengan yang diharapkan dan tidak sepadan dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan barang ini. Kualitas produk sangat rendah dan harga yang saya bayar tidak sepadan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan sangat buruk dan barang rusak saat sampai. Seller tidak responsif dan tidak membantu.",
        "sentiment": "negatif",
    },
]


Nvme_256gb = [
    {
        "comment": "Produk original, pengiriman cepat, respon cepat, packing baik. Alhamdulillah, berkah usahanya, semoga sukses selalu.",
        "sentiment": "positif",
    },
    {
        "comment": "Produk original 😍😍😍, pengemasan super aman, pengiriman super cepat. Dapat masker gratis pula. Mantap seller, semoga selalu amanah. Terimakasih 👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantap. Sepadan dengan Harga: terbaik. Mantap tinggal test max kecepatan data transfer. Terima Kasih banyak untuk TeamGroup.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Baik. Sepadan dengan Harga: Baik. Barang mendarat dengan aman dan baik dan semoga awet dan cocok. Aamiin.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang mantap, sesuai deskripsi. Alhamdulillah, berfungsi dengan baik. Kedua kalinya belanja di TeamGroup. Selalu memuaskan.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Baik. Sepadan dengan Harga: Sangat sepadan. Alhamdulilah pesanan telah sampai dengan selamat. Dari RAM+m.2 NVMe lebih percaya sama merk ini. Top markotop, RAM dari tahun 2018 sampai sekarang masih awet, dari awal punya laptop biasa sampai punya yang gaming. Mudah2an kualitasnya serupa dengan RAMnya. 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Barang original. Kualitas mantap. SSD NVMe Teamgroup memang luar biasa, read and write-nya joss. Semoga awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: belum dicoba dan install di komputer, semoga awet dan sepertinya underrated. Sepadan dengan Harga: cukup miring dengan review di internet yang tidak jelek. Mari kita coba.",
        "sentiment": "positif",
    },
    {
        "comment": "Paket mendarat dengan aman, pengiriman cepat, baru pesan kemarin hari ini sudah sampai. Terimakasih min.",
        "sentiment": "positif",
    },
    {
        "comment": "SSD-nya aman dan sudah dipasang, migrasi lancar. JNT lelet...",
        "sentiment": "positif",
    },
    {
        "comment": "Seller responsif, pengiriman cepat, packing rapi. Belum di coba, masih nunggu beberapa part lagi. Semoga awet. Terimakasih bonus maskernya.",
        "sentiment": "positif",
    },
    {
        "comment": "Packing rapi, tebal. Ga banyak basa-basi. Langsung dikirim di hari pertama pesan. Terbilang cepat pengiriman. And... SSD works af. Niceee....",
        "sentiment": "positif",
    },
    {
        "comment": "Selalu bagus. Mantab banget. Tidak pernah mengecewakan. Packing cepat.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah diterima dalam kondisi yang baik dan tidak ada kendalanya. Terimakasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: meningkatkan performance laptop. Sepadan dengan Harga: sangat worth it. Pengiriman cepat, instalasi mudah, barang sesuai dengan deskripsi.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: iyaa. Fitur Terbaik: Fast. kecewa. 2 hari nyampe, Gileee benerrr. Teamgroup memang okeee, gausah diragukan lagi. Oiya dapet bonus flash drive 16 gb, lumayan bgt heuheu. Thanks TG.",
        "sentiment": "positif",
    },
    # Negatif
    {
        "comment": "Pengiriman lama, barang rusak. Tidak puas sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai dengan deskripsi, sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas barang jelek, tidak sepadan dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan buruk, barang sampai dalam kondisi rusak.",
        "sentiment": "negatif",
    },
    {
        "comment": "Respon penjual sangat buruk, tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak dan penjual tidak memberikan solusi yang baik.",
        "sentiment": "negatif",
    },
    {"comment": "Barang tidak asli, penipuan!", "sentiment": "negatif"},
    {
        "comment": "Pengiriman terlambat, tidak sesuai dengan yang dijanjikan.",
        "sentiment": "negatif",
    },
    {"comment": "Penjual tidak responsif, sulit dihubungi.", "sentiment": "negatif"},
    {
        "comment": "Barang tidak terlindungi dengan baik dalam pengiriman, rusak saat tiba.",
        "sentiment": "negatif",
    },
    {"comment": "Packing buruk, barang patah saat sampai.", "sentiment": "negatif"},
    {
        "comment": "Pengiriman sangat lambat, kecewa dengan pelayanan ini.",
        "sentiment": "negatif",
    },
    {"comment": "Barang cacat, kualitas sangat rendah.", "sentiment": "negatif"},
    {"comment": "Penjual tidak jujur, barang palsu!", "sentiment": "negatif"},
    {"comment": "Respon penjual lambat, sulit berkomunikasi.", "sentiment": "negatif"},
    {
        "comment": "Paket hilang dalam pengiriman, penjual tidak membantu.",
        "sentiment": "negatif",
    },
]


product_m2_256_pd = pd.DataFrame(Ssd_m2_256)
product_256_pd = pd.DataFrame(Ssd_256)
product_128_pd = pd.DataFrame(Ssd_128gb)
product_ddr_4gb_pd = pd.DataFrame(Ddr4_4Gb)
product_nvme_256_pd = pd.DataFrame(Nvme_256gb)

product_m2_256_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_256_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_128_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_ddr_4gb_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_nvme_256_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)


print("Value counts Ke-1: ", product_m2_256_pd["sentiment"].value_counts())
print("Value counts Ke-2: ", product_256_pd["sentiment"].value_counts())
print("Value counts Ke-3: ", product_128_pd["sentiment"].value_counts())
print("Value counts Ke-4: ", product_ddr_4gb_pd["sentiment"].value_counts())
print("Value counts Ke-5: ", product_nvme_256_pd["sentiment"].value_counts())


merge_df = pd.concat(
    [
        product_m2_256_pd,
        product_256_pd,
        product_128_pd,
        product_ddr_4gb_pd,
        product_nvme_256_pd,
    ]
)


positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan positif:", positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_teamgroup.csv", index=False)

print("Data telah disimpan")
