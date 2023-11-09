import pandas as pd

ptz_smart = [
    {
        "comment": "Bagus sekali, Murah sedang ada promo. Barang OK, sudah dipakai lancar jaya, pengiriman cepat, semoga awet. Terima kasih seler terima kasih kurir.",
        "sentiment": "positif",
    },
    {
        "comment": "Produk oke sesuai deskripsi dan normal berfungsi, pengiriman rapih dan buble wrap, dicoba langsung oke, respond sangat cepat, maaf baru beri nilai, belum sempat coba.. Recommend.. Dan langganan ahhh, sukses seller n shoope.",
        "sentiment": "positif",
    },
    {
        "comment": "Respon bagus, pengiriman gak ada 24 jam dari pemesanan, barang juga original, gak mengecewakan sama sekali.. kalau butuh lagi pasti order di sini 👍🏻",
        "sentiment": "positif",
    },
    {
        "comment": "Bisa mendeteksi gerakan dan suara, ada fitur komunikasi 2 arah, video lancar. Cocok dengan harga 300 ribuan.",
        "sentiment": "positif",
    },
    {
        "comment": "Kameranya bening. Sepadan dengan Harga: iya. Pengiriman sesama Surabaya & instan langsung datang kurleb 1 jam an. Barusan dipasang, kualitas gambar jelas, bening, bagus.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: terbaik. Sepadan dengan Harga: Terbaik. Admin fast respon. Perlu diperhatikan kembali sebelum membeli produk di toko ini, produk ready stock atau system PO.",
        "sentiment": "positif",
    },
    {
        "comment": "Produk berfungsi dengan baik, kualitas gambar jelas, dan dilengkapi speaker yang oke. Sepadan dengan Harga: sepadan. Produk sampai tanpa ada reject.",
        "sentiment": "positif",
    },
    {
        "comment": "Gambar bagus HD. Sepadan dengan Harga: sepadan banget. Mantap gan sudah ditest CCTV-nya gambar bagus sudah lengkap fitur nya motion sensor tracking dan sound detect, rekomended untuk mencari CCTV 400rb an.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur lengkap. Sepadan dengan Harga: sepadan. Ini pembelian yang ke 11 CCTV indoor..setelah saya pakai banyak tetangga dan masjid yang minta tolong dipesankan..pemasangan mudah..pemasangan ke aplikasi hp juga sangat mudah..terima kasih seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: cukup sepadan. Fitur Terbaik: Motion detection. Produk dikemas dengan baik dan aman. Sudah digunakan dan berfungsi sebagaimana mestinya. Terima kasih seller, sukses selalu 🙏🏻.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Trims Sophee Mantapp. Sukses terus Sophee. Ini sudah dicoba berhasil penjual Sophee👍. Sepadan dengan Harga: Murah.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengemasan lama karena PO, tapi waktu pengirimannya super cepat. Barang original, mudah pengoperasiannya. Bardi selalu favorit💕.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Fitur lengkap. Sepadan dengan Harga: Harga bersaing. Pengiriman cepat. Pengemasan aman, dikasih fragile. Barang tidak ada yang cacat. Pembelian yang ke-2x.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Canggih CCTV-nya. Sepadan dengan Harga: Worth it to buy. Kualitas gambarnya bagus, terang, mau ditempat gelap masih keliatan jelas muka orang. Fiturnya canggih, ngga nyesel beli BARDI 😍🫰🏻.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Motion tracking. Sepadan dengan Harga: 100% worth it. Keren banget barangnya, harus terus terhubung sm wifi ya biar bisa pantau terus, harga bersahabat, thanks seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Bisa digunakan dengan baik. Sepadan dengan Harga: Kamera jelas. Produk bagus, toko asli Bardi, fungsi sesuai dengan keterangan.",
        "sentiment": "positif",
    },
    ## Negatif
    {
        "comment": "Barang sangat buruk, tidak sesuai deskripsi, tidak berfungsi normal. Pengiriman sangat lambat dan pengemasan tidak aman. Sangat kecewa dengan produk ini, tidak sesuai harapan. Tidak akan membeli lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk cacat dan tidak berfungsi. Pengiriman sangat lambat dan pengemasan buruk. Kecewa dengan pengalaman berbelanja ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga mahal untuk produk yang tidak berfungsi. Pengiriman terlambat dari jadwal estimasi. Kecewa dengan kualitas produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak dan tidak sesuai dengan deskripsi. Pengemasan tidak aman dan pengiriman lambat. Pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas gambar buruk, tidak sesuai dengan deskripsi. Pengiriman terlambat dari jadwal estimasi. Kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan pengemasan buruk. Harga tidak sebanding dengan kualitas produk. Tidak akan merekomendasikan pembelian di sini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk cacat dan tidak berfungsi dengan baik. Pengiriman terlambat dari jadwal estimasi. Kecewa dengan pengalaman berbelanja ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas gambar buruk dan harga mahal. Pengiriman terlambat dari jadwal estimasi. Tidak puas dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai dengan deskripsi dan tidak berfungsi normal. Pengiriman sangat lambat dan pengemasan buruk. Sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas gambar buruk dan harga tidak sepadan. Pengiriman terlambat dari jadwal estimasi. Tidak akan merekomendasikan pembelian di sini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak dan tidak berfungsi dengan baik. Pengiriman sangat lambat dan pengemasan tidak aman. Pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas gambar buruk dan harga mahal. Pengiriman terlambat dari jadwal estimasi. Tidak puas dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai dengan deskripsi dan tidak berfungsi dengan baik. Pengiriman sangat lambat dan pengemasan buruk. Sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas gambar buruk dan harga tidak sepadan. Pengiriman terlambat dari jadwal estimasi. Pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk sangat buruk, tidak sesuai deskripsi, tidak berfungsi normal. Pengiriman sangat lambat dan pengemasan tidak aman. Sangat kecewa dengan produk ini, tidak sesuai harapan. Tidak akan membeli lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas gambar buruk dan harga mahal. Pengiriman terlambat dari jadwal estimasi. Tidak puas dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Motion tracking. Sepadan dengan Harga: Tidak sepadan. Barang buruk, sering putus koneksi wifi, tidak sebanding dengan harganya. Kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Bisa digunakan dengan baik. Sepadan dengan Harga: Tidak sepadan. Produk buruk, kualitas kamera jelek, tidak sesuai dengan deskripsi. Kecewa dengan pengalaman berbelanja ini.",
        "sentiment": "negatif",
    },
]

Light_blub = [
    {
        "comment": "Kualitas: Good\nPerforma: Good\nTampilan: Umum\nIntruksi clear, cepat terkoneksi, semua fitur sangat berguna, bulb aman agak panas karna terpanggang matahari mesakne kurir e kepanasen, box mulus",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: mewah\nKualitas: oke\nPerforma: ini kedua kali beli krn yg lama udah gak berfungsi setelah 4,5thn pemakaian\nToooppp selalu suka, worth it harganya krn seawet itu light bulb nya, thank you seller",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: Bagus\nPerforma: Tinggi\nKualitas: Terbaik",
        "sentiment": "positif",
    },
    {
        "comment": "Sampainya cepet banget, perasaan baru pesen kemarin. Langsung dicoba disiang hari dan berfungsi dg baik. Produk ori. Thank you!",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: ok\nPerforma: baik\nKualitas: ok\nSedikit masukan untuk seller harusnya bagian luar di lapisin kardus, setelah itu pakai bubble wrap supaya mengurangi kerusakan bagian box (penyok) syukur lampunya gak pecah, hanya box luar penyok, sempat takut gak bisa nyala. Puji Tuhan bisa nyala yg 12 watt, yg 9 watt agak susah konek ke hp.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: ok\nPerforma: ok\nTampilan: ok\nProduk Baik...\nProduk Sesuai Deskripsi..\nPacking Ok...\nHarga Pas...\nPengiriman Cepat..\nRespon Ada...",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: nyala sudah dicoba dua2nya\nTampilan: bagus\nLebih ditingkatkan lagi pakai bubble wrap atau kerdus lagi untung kerdusnya tidak penyok",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: baik\nHarga: terjangkau\nDaya listrik: hemat\nRekomendasi banget",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk baik produk original harga produk sangat baik kecepatan pengiriman sangat baik respon penjual sangat baik\nKualitas produk baik produk original harga produk sangat baik kecepatan pengiriman sangat baik respon penjual sangat baik",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: Mantab\nHarga: Relatif\nDaya listrik: rendah\npertama kali coba bardi, gampang sih caranya settingnya\nsimpel juga cara make aplikasinya, pengiriman dan packagingnya juga bagus, terima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: Kualitas produk sangat baik, respon penjual sangat ramah, pengiriman cepat, sangat recommended.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus sekali, terang dan bisa gonta ganti warna sesuai mood, barang original dan berkualitas. Rekomendasi banget karna sangat berguna apalagi kalau mau foto estetik bisa banget. Super rekomendasi. Terima kasih seller",
        "sentiment": "positif",
    },
    {
        "comment": "Produk keren abisss. Saya sangat suka dari segi packaging hingga produk itu sendiri",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: Baik\nHarga: standar\nDaya listrik: kecil\nBarangnya dibungkus rapi dan aman pakai bubble wrap tebal banget jadi super aman",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas: Bagus\nHarga: Terjangkau\nDaya listrik: Hemat\nProduk sesuai deskripsi, pengiriman cepat, dan penjual responsif. Sangat puas dengan pembelian ini.",
        "sentiment": "positif",
    },
    {
        "comment": "Produk berkualitas tinggi, tampilan menarik, dan harga yang pantas. Sangat senang dengan pengiriman yang cepat dan packaging yang aman. Terima kasih, seller!",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Produk tidak berfungsi sama sekali, lampunya tidak menyala.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas buruk, cepat rusak setelah beberapa penggunaan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak sesuai dengan deskripsi, kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengirimannya sangat lambat, butuh berbulan-bulan untuk sampai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat tiba dan sulit untuk menghubungi penjual.",
        "sentiment": "negatif",
    },
    {
        "comment": "Banyak fitur yang tidak berfungsi dengan baik, sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk cacat dan penjual tidak responsif terhadap keluhan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak ada panduan penggunaan yang jelas, sulit untuk mengoperasikannya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pembelian saya hilang dalam pengiriman dan penjual tidak membantu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang saya terima sangat kotor dan tidak terawat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat mahal dan tidak sepadan dengan kualitasnya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Lampunya tidak awet, cepat rusak setelah penggunaan singkat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk jelek, buruk, dan mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak jujur ​​mengenai kondisi produk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai dengan gambar yang ditampilkan, terlihat lebih baik online.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengalaman buruk dengan penjual ini, tidak akan pernah membeli lagi.",
        "sentiment": "negatif",
    },
]

Universal_remote = [
    {
        "comment": "Fitur Terbaik: belum di coba\nSepadan dengan Harga: iya\nPaket di terima dengan aman karena bubblewrap tebal, admin juga fast respon, ada petunjuk pemakaian juga, belum di coba semoga awet🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Ukuran mungil\nSepadan dengan Harga: Sesuai\nKaget ternyata ukurannya jadi 4 kali lebih kecil dari IR remote sebelumnya. Semoga kecil2 begini tetap awet dan berfungsi dengan baik yaa. Tks seller",
        "sentiment": "positif",
    },
    {
        "comment": "Mantep n gercep. Tak perlu menunggu waktu lama pesanan mendarat dengan aman sentosa. Packaging cukup baik. Produk sesuai deskripsi dan sesuai pesanan. Sudah langsung diaplikasikan dan tidak ada kendala, berfungsi dengan baik. Terimakasih bardiofficial dan shopee.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang bagus n Ori. Puas banget belanja disini. Next time akan beli item lainnya disini. Thank you, seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bisa meremot apa saja\nSepadan dengan Harga: lumayan\nBagus tidak ada Miss. Recommended banget buat remot yang menggunakan Ir dari jauh",
        "sentiment": "positif",
    },
    {
        "comment": "Paket orderan BARDI Smart IR sudah sampai dan sudah saya terima dengan baik.. packing aman dg bubble wrap.. dan pengiriman cepat.. terima kasih bardismarthome dan shopee.. sukses selalu.. semoga barang yang saya beli ini bermanfaat dan awet..",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Bisa kontrol elektronik yang memiliki IR dimana saja\nSepadan dengan Harga: sangat worth it sih harganya\nAlat berfungsi dengan baik, semoga tahan lama. Terimakasih Bardi. Sekarang saya bisa menghidupkan AC dari mana saja. Contohnya saya mau pulang dari pasar, saya bisa hidupkan AC ketika dipasar, sehingga tiba dirumah kamar sudah dingin.",
        "sentiment": "positif",
    },
    {
        "comment": "Dapet harga promo , ga tau cara pakainya jadi liat di youtube malah dapat beda model sama yg di youtube padahal merk yg sama...tapi bisa digunakan di aplikasi bardi buat nyalain tv...terima kasih seller dan kurir...sukses terus buat semuanya",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: sangat baik\nSepadan dengan Harga: sangat sesuai\nBegitu bermanfaat dan sangat menarik",
        "sentiment": "positif",
    },
    {
        "comment": "Barang diterima sesuai dengan pesanan... sangat bagus kualitasnya... recomended seller... terimakasih sudah packing rapi & terimakasih atas pelayanannya.. sangat memuaskan.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah, barang sudah sampai dengan selamat.\nMudah-mudahan saja barangnya aman dan awet\nMasih coba dicharger dulu sih. Cuma kita gak tahu saat ngecash sudah masuk atau belum, soalnya tidak ada lampu atau tandanya.\nSelebihnya bagus semua",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk sangat baik. Produk original. Harga produk sangat baik. Kecepatan pengiriman sangat baik. Respon penjual sangat baik. Kualitas produk sangat baik. Produk original. Harga produk sangat baik. Kecepatan pengiriman sangat baik. Respon penjual sangat baik. Kualitas produk sangat baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Dengan Universal IR Remote, bisa bikin otomasi di kamar. Hidupin AC dan Diffuser dengan menggunakan delay, sehingga tidak membuat shock electric. Produk Bardi selalu inovatif dan pintar. #teamKokoGlowing",
        "sentiment": "positif",
    },
    {
        "comment": "Sangat baik kualitasnya. Sangat bermanfaat alatnya. Sangat puas menggunakan Bardi Smart Universal IR Remote wireless ini. Yang jelas recommended banget alatnya...",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai deskripsi dan sudah diterima, packing juga sangat aman sehingga barang tidak penyok, barang juga original mantap buat seller dan recommended 👌",
        "sentiment": "positif",
    },
    {
        "comment": "Langsung enyaaaakkk , langsung berfungsi dong Bardi nya, Bukan begitu, Pak Bardi? Suiiipp wes... Cepet bingits lhooo nyampek nya",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Barang ini rusak saat tiba dan saya tidak bisa menggunakannya. Sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya memesan produk ini dan saya mendapatkan versi yang salah. Sangat membingungkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan tidak sesuai dengan yang dijanjikan. Kurir juga kurang responsif.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk buruk. Tidak tahan lama dan sering mengalami masalah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya mendapatkan produk yang rusak dan penjual tidak responsif. Sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak sesuai dengan deskripsi. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat kecewa dengan produk ini. Tidak sepadan dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Saya tidak akan merekomendasikannya kepada orang lain.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat sulit untuk menghubungi penjual. Pelayanan pelanggan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya tidak menerima produk yang saya pesan. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Paket tiba dalam kondisi rusak dan produknya pecah. Sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan tidak ada pemberitahuan. Kurir tidak profesional.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat tertipu dengan produk ini. Tidak berkualitas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak berfungsi seperti yang diharapkan. Saya sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya mendapatkan produk palsu. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman tidak pernah tiba. Saya sudah menunggu terlalu lama.",
        "sentiment": "negatif",
    },
]


Smart_plug = [
    {
        "comment": "Tidak usah khawatir sama produk Bardi sangat useful dan yang pasti customer servis serta garansinya top. Saya sudah lama percayakan produk home automation di rumah dengan produk dari Bardi dan sampai sekarang Sangat PUAS!",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman Cepat Packing rapi dan aman Produk original bergaransi Bardi Produk berkualitas Recommended",
        "sentiment": "positif",
    },
    {
        "comment": "Barang oke. Harus download aplikasi dulu unt penggunaan smart’nya, jika tidak, unt penggunaan biasa, sudah ada tombol on-off",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Bagus Sepadan dengan Harga: terjangkau Pengiriman Cepat Packing rapi dan aman Produk original bergaransi Bardi Produk berkualitas Recommended",
        "sentiment": "positif",
    },
    {
        "comment": "Proses order lumayan cepat. Pesan tgl 10/10/2021, dikirim tgl 11 dan diterima tgl 13. Brg sesuai deskripsi dan pesanan, udh dicoba dan berfungsi dg baik, dpt free makanan kucing whiskas jg. Trims.",
        "sentiment": "positif",
    },
    {
        "comment": "Brg ad kendala ketika d terima dus rusak packing agak kurang aman... tp msh berfungsi semoga awet thx 🙄",
        "sentiment": "positif",
    },
    {
        "comment": "Colokan ini ngebantu banget utk timer charge HP malem² biar ga terus2an sampe pagi charge nya.. tinggal download apps bardi buat ngatur²nya.. oke banget lahh 👍🏻",
        "sentiment": "positif",
    },
    {
        "comment": "Blm sempet coba sih. Tp mudahan aman aja. Sudah lebih 5 kali beli dsni juga. Cuma lama di pengiriman, but its okay",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: barang bagus Sepadan dengan Harga: sesuai harga Pengiriman cepat, barang dampai dengan selamat",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk sangat baik, produk original, harga terjangkau, kecepatan pengiriman sangat baik",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk sangat baik. Produk original. Harga produk sangat baik. Kecepatan pengiriman barang sangat baik. Respon penjual sangat baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: konektivitas ke aplikasi Bardi Smart Home Sepadan dengan Harga: sangat Buat kalian yg lagi building smart ecosystem di rumah kalian, Bardi adalah merk yang patut kalian beli sih. Karena pengaturannya mudah banget. Saranku, untuk semakin memudahkan akses, pakai satu brand aja utk satu rumah, supaya ga terlalu banyak install aplikasi di smartphone kamu. Aku pakai Bardi mulai dari CCTV sampai electric plug nya. Kereen!!",
        "sentiment": "positif",
    },
    {
        "comment": "desainnya bagus, dan yang pasti berguna banget buat kaum milenial yang semuanya pengen bisa di kontrol lewat hp. good job bardi 🥳🥳",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus banget. egampang pakai nya Sepadan dengan Harga: agak mahal dikit tp emang kualitas bardi tidak di ragukan lagi Udh beli bnyk brg di bardi. Top semua rusak selama masih garansi di ganti baru. Top juara pelayanannya.",
        "sentiment": "positif",
    },
    {
        "comment": 'Terima kasih pesanan sudah sy terima dg baik.. sudah sy setting dan berfungsi dg baik dan sangat puas.. Sayangnya statistik penggunaan daya listrik kedua port masih gabung jd 1, andaikan bisa pisah sendiri" lebih mantul lagi ☺😁.',
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Bisa menyalakan dari jauh Sepadan dengan Harga: Ya Barangnya bagus, bisa di hidupkan tanpa harus pencet tombol Cuma ada 1 kendala, kalo mau di hidupkan bakal nyala dua²nya, gak bisa dihidupkan cuma 1 Switch Ntah saya yg salah dimana atau memang begitu sistemnya Selain itu oke sih, gaka ada masalah",
        "sentiment": "positif",
    },
    # Negatif
    {
        "comment": "Produk ini sangat buruk, tidak berfungsi dengan baik dan respon penjual lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan packing tidak rapi, barang rusak saat diterima.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang saya terima tidak sesuai dengan deskripsi, sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur yang dijanjikan tidak berfungsi, saya kecewa dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk, barang rusak dan tidak bergaransi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga terlalu mahal untuk kualitas produk yang buruk, saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan respon penjual tidak membantu sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak berguna dan saya merasa membuang uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur yang dijanjikan tidak berfungsi dengan baik, saya sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat diterima dan respon penjual buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan produk ini, tidak sesuai dengan ekspektasi saya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lama dan packing kurang aman, barang rusak saat tiba.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk terlalu tinggi untuk kualitas yang buruk, tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak awet dan rusak setelah beberapa kali penggunaan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan pelayanan pelanggan, tidak responsif dan tidak membantu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai dengan gambar dan deskripsi, saya merasa tertipu.",
        "sentiment": "negatif",
    },
]

Outdoor = [
    {
        "comment": "Sukak jernih sekali kamera nya.. juga semua nya lengkap dan packing nya juga baik dan rapi serta aman.",
        "sentiment": "positif",
    },
    {
        "comment": "Kamera bagus, bahan kuat ga ringkih, kabel cukup panjang, disertai bracket.",
        "sentiment": "positif",
    },
    {
        "comment": "CCTV super duper lucu bentuknya 😍😍😍\nBerasa punya robot pengintai 😁\nPacking super aman 👍\nPengiriman jos hari kerja langsung proses 👍\nThanks ya 🥰❤️",
        "sentiment": "positif",
    },
    {
        "comment": "Produk bagus, packing rapi, admin ramah, pengamanan pengiriman super aman, banyak pengamannya juga, sesuai expectation berdasarkan bintang, pengiriman super cepat.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman Cepat, Perlindungan bagus, Kondisi Fisik bagus, kelengkapan lengkap, hasil Video lumayan, namun Produk awal trnyta Ada bercak, lalu bisa di retur ( dikirimkan produk baru ) hasil test bagus, Yg jelas Adminya Ramah dan informatif, semoga kedepanya makin Joss gandos, dan bermanfaat",
        "sentiment": "positif",
    },
    {
        "comment": "Bublewrap bagian dlm produk hrs ada seharusnya biar lbh aman.produk oke,kualitas gmbr jls,suara jelas dan jernih.model cctv oke.mudah digunakn di hpnya.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang nya bagus, sesuai,tapi blm di coba, semoga aja ga ada kendala,\nSaran; karena ini barang elektronik harusnya packing di tambah kan kotak untuk pengamanan,..terima kasih 🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: two way communication !\nSepadan dengan Harga: worth it !\nBagus banget lah membantu sekali Cctv ini. User friendly juga mudah untuk set up nya. Thank you !",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: video dan audio connected dengan baik.\nSepadan dengan Harga: worth the price!\nall good! paket diterima dengan baik, cctv berfungsi dengan baik. gambar dan suara jelas. packaging baik, kecepatan pengiriman baik. terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: CCTV\nSepadan dengan Harga: sangat sepadan\nProduk original bergaransi, harga terbaik, respon seller cepat, semua fitur berfungsi dengan baik. Terimakasih",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih banyaaak barang asli , belum di coba semogaa aaaàaaaaaja awet nanti di pakenya , bagusss\nBeli pas 11 11 kemarin",
        "sentiment": "positif",
    },
    {
        "comment": "Mantap gambarnya jernih bgt, micro sdnya berfungsi, night modeny mantap, bisa menjangkau tiap sudut karna bisa muter, suaranya oke, gampang juga nyetingnya, next mau beli yg outdoor",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: Kualitas bagus\nFitur Terbaik: Cocok buat di rumah\nPemasangannya mudah, cocok buat di dalem rumah. Dan bisa saling ngobrol 2 arah..",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Baik\nSepadan dengan Harga: baik\nProduk sesuai orderan, belum di cek semoga sesuai",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: kualitas gambar dan suara ok\nSepadan dengan Harga: sesuai\nproduk sesuai dengan ulasan,packing aman,dan diterima dalam keadaan baik.respon seller juga cepat.Terima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Barang telah sampai dengan baik, masih proses penyambungan, barang ori terima kasih",
        "sentiment": "positif",
    },
    # Negatif
    {
        "comment": "Produk ini sangat buruk! Tidak sesuai dengan deskripsi sama sekali. Kecewa sekali!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan produk ini. Kualitasnya sangat jelek dan tidak sepadan dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Begitu saya mencoba produk ini, langsung bermasalah. Tidak direkomendasikan sama sekali!",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat mengecewakan! Produk ini rusak saat sampai dan pengirimannya sangat lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Apa ini? Barangnya cacat dan pengirimannya sangat buruk. Tidak akan pernah beli lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah, dan respon penjual sangat buruk. Saya kecewa!",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak bisa percaya betapa buruknya produk ini. Tidak sesuai dengan harapan sama sekali.",
        "sentiment": "negatif",
    },
    {
        "comment": "Jangan pernah membeli produk ini. Sangat buruk, pengiriman lambat, dan admin tidak responsif.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kamera ini sangat buruk! Tidak ada yang bagus darinya. Total pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa tertipu dengan produk ini. Sangat jelek dan tidak berguna.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah, dan respon penjual sangat buruk. Saya sangat marah!",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah pemborosan uang! Produknya tidak berfungsi dan pengirimannya lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat jelek! Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa tertipu dengan produk ini. Tidak sesuai dengan deskripsi dan sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat buruk! Produk ini tidak bekerja dengan baik, dan respon penjual sangat lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah pengalaman yang sangat buruk. Produk tidak berfungsi sama sekali.",
        "sentiment": "negatif",
    },
]


product_ptz_smart_pd = pd.DataFrame(ptz_smart)
product_Light_blub_pd = pd.DataFrame(Light_blub)
product_Universal_remote_pd = pd.DataFrame(Universal_remote)
product_Smart_plug_pd = pd.DataFrame(Smart_plug)
product_Outdoor_pd = pd.DataFrame(Outdoor)


product_ptz_smart_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Light_blub_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Universal_remote_pd.drop_duplicates(
    subset=["comment"], keep="first", inplace=True
)
product_Smart_plug_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Outdoor_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)


print("Value counts Ke-1: ", product_ptz_smart_pd["sentiment"].value_counts())
print("Value counts Ke-2: ", product_Light_blub_pd["sentiment"].value_counts())
print("Value counts Ke-3: ", product_Universal_remote_pd["sentiment"].value_counts())
print("Value counts Ke-4: ", product_Smart_plug_pd["sentiment"].value_counts())
print("Value counts Ke-5: ", product_Outdoor_pd["sentiment"].value_counts())


#### merge

merge_df = pd.concat(
    [
        product_ptz_smart_pd,
        product_Light_blub_pd,
        product_Universal_remote_pd,
        product_Smart_plug_pd,
        product_Outdoor_pd,
    ]
)


positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan positif:", positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_bardi.csv", index=False)

print("Data telah disimpan")
