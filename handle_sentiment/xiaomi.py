import pandas as pd

Xiaomi_Tv_43 = [
    {
        "comment": 'Alhamdulillah mimin nya fast respon bgt gercep tanya" langsung di jawab suka bgt. Sesuai bagus fiturnya banyak, seperti handphone suka tokoh nya amanah, packingnya rapi tanpa ada lecet sedikit pun. Semoga awet amin berkah selalu.',
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman sangat cepat, packing super duper aman walaupun pengiriman pake instan, bubble wrap nya banyak. Seller baik, ramah, fast respon. Best seller lah pokonya.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang bagus dan pengiriman cepat. Sesuai dengan deskripsi. Terima kasih seller, seller nya juga sangat ramah.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur terbaik menurutku bagus sih. Harga juga sepadan dengan kualitasnya. Lumayan bagus untuk TV android dengan harga segitu. Terimakasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah produk bagus, sesuai dengan deskripsi. Terima kasih seller, seller nya juga sangat ramah, kirim pake instant di kasih tau nggak perlu pake kayu lagi.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah barang oke, feking juga oke. Harga sesuai. Barang oke, feking juga oke, pengiriman cepat.",
        "sentiment": "positif",
    },
    {
        "comment": "Mantap gambar dan suara OK BANGET, makasih juga Buat Penjualnya Udah memberi pelayanan terbaiknya... 🙏🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah paket udah kmi terima dg selamat dan secepat kilat ...seller sangat gercep dan ramah. Tidak order buble wrap tp dibungkus dg bubble wrap. Terima kasih ya kak moga makin laris manis penuh keberkahan Aamiin",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai. Pengiriman cepat. Packing super duper aman. Direkomendasikan lah ni toko. Sukses gan.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan harga murah. Fitur terbaik bagus. Gercep packing rapi aman. Terima kasih seller, semoga sukses toko ini amanah sekali puas belanja di sini Shopee mantap.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah barang mendarat dengan selamat & semoga awet yah...",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur terbaik bagus. Sepadan dengan harga bagus banget dan harga terjangkau. Packingnya rapi dan aman banget asliiii padahal pake instan, makasih 🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Barang di terima dengan baik.. Saran memang bagus packing kayu.. biar lebih aman untuk semua. Sepadan dengan harga terjangkau.",
        "sentiment": "positif",
    },
    {
        "comment": "Mantul tvnya. Sepadan dengan harga kualitas terbaik. Pokoknya mantap betul dan luar biasa.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur terbaik bagus. Sepadan dengan harga. Datangnya cepat, semoga awet ya 🙏🏻🙏🏻",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur terbaik: bisa menggunakan wifi. Sepadan dengan harga sangat bagus. Kurirnya juga cepat, barang aman sampai tujuan. Produk original dan berfungsi dengan baik. Adminnya juga fast respon. Top pokoknya.",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Barang datang dalam keadaan rusak. Packing buruk, banyak lecet dan pecah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur terbaik tidak berfungsi dengan baik. Harga mahal untuk kualitas yang buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat dan kurang aman. Barang tiba dalam keadaan rusak.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga tidak sepadan dengan kualitas produk. Kecewa dengan barang yang diterima.",
        "sentiment": "negatif",
    },
    {
        "comment": "Seller tidak responsif dan kurang ramah. Pengiriman sangat lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang tidak sesuai dengan deskripsi. Harga mahal untuk kualitas yang buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Barang tiba dalam keadaan rusak dan tidak berfungsi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk. Barang tiba dalam keadaan rusak dan lecet.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat. Tidak ada informasi yang jelas mengenai status pengiriman.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga mahal dan tidak sepadan dengan kualitas produk. Kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Seller tidak profesional. Tidak menjawab pertanyaan dengan baik dan sopan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang datang dalam keadaan rusak. Kualitas produk sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk. Barang tiba dalam keadaan rusak dan pecah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat dan tidak sesuai dengan yang dijanjikan. Kecewa dengan pelayanan ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga sangat mahal dan tidak sepadan dengan kualitas produk. Pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Seller tidak responsif dan tidak memberikan informasi yang jelas. Pengiriman terlambat.",
        "sentiment": "negatif",
    },
]


Buds_4 = [
    {
        "comment": "FAST pair. Langsung work. Packaging aman, dengan kardus dan bubble wrap. Kurir handle with care. Semua fitur-fitur berfungsi dengan sangat baik. Terbaik. Terimakasih seller dan kurir.",
        "sentiment": "positif",
    },
    {
        "comment": "Harga murah dengan kualitas terbaik, cocok disandingkan dengan semua perangkat Xiaomi saya mulai dari HP, Pad, bahkan Laptop. Pengiriman cepat, paking aman dan rapih. Semoga awet dan selalu menjadi andalan.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah brhbsdh sampai dg selamat dan aman. Peking ny mantap. Aman dan tidak ada yang rusak. Terima kasih ya semuanya.",
        "sentiment": "positif",
    },
    {
        "comment": "Recomend bgt untuk brg ini, cuma sedikit disayangkan pengiriman ketempat saya agak lama.",
        "sentiment": "positif",
    },
    {
        "comment": "Original OFFICIAL XIAOMI. Bas mantap, suara jos. Mantap untuk semuanya. Overall jos mantap lah. Terima kasih XIAOMI. Terima kasih SHOPEE.",
        "sentiment": "positif",
    },
    {
        "comment": "Kedap suara, sehingga tidak keras terdengar suara bising disebelah. Kerasa agak besar case nya. Suara sesuai dengan harga.",
        "sentiment": "positif",
    },
    {
        "comment": "Mantap brg sampai sangat cepat. Lumayanlah untuk TWS harga segini. Tidak sakit di telinga, sangat nyaman dipakai, bassnya pas bgt. Mantap Xiaomi. Makasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih barangnya sudah sampai. Barang dalam kondisi baik & normal, suara nya bagus untuk harganya. Minusnya packing sangat simple banget, tapi overall saya suka modelnya.",
        "sentiment": "positif",
    },
    {
        "comment": 'Lumayan tapi saya agak "kecewa ringan😅" dengan ekspektasi saya. Saya kira barangnya sama dengan fitur seperti earphone wah gitu karena saya berpikir di HP dengan earphone nya sama mereknya bakal lebih bagus, ternyata tidak begitu karena "di anime tidak begitu😒", tapi sudahlah, "mau bagaimana lagi😁", sudah😍😘" 😋😜. Intinya, jaga barangmu, mungkin tidak terlalu bagus, tetapi percayalah kalian pasti akan membutuhkannya suatu saat nanti😁.',
        "sentiment": "positif",
    },
    {
        "comment": "Review jujur build quality earbuds oke bahannya solid dan rigid. Tetapi ternyata bentuknya besar, kuping saya kecil jadi aneh dilihat :( Next, kualitas suara, untuk suara klo telepon, zoom dll itu ada echonya suara jadi nyaring solusi volume di 10 - 15% biar jadi santai klo ngobrol. Untuk musik bass jelek, edm gk cocok, tapi suara vokalis jadi jelas, dengerin Taylor Swift cocok, tetep kasih bintang lima karena murah bgt harganya, lumayan buat koleksi, yg nyesel cuman looknya aja jelek, besar bgt earbudsnya :(",
        "sentiment": "positif",
    },
    {
        "comment": "Worth the price. Berfungsi dengan baik di device Mi 10T Pro. Kualitas suara yang dihasilkan juga bagus. Pengemasan dan pengiriman cepat. Quick connect and quick charge. Terima kasih Xiaomi.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus sekali mantap. Sepadan dengan harga, terjangkau rekomended. Pengiriman cepat, produk original, harga lumayan terjangkau. Mantap.",
        "sentiment": "positif",
    },
    {
        "comment": "Bass enak, lembut, trebel tidak bikin terlalu strong, midle nya emang menonjol, tinggal di kontrol di equalizer di app nya aja, overall enak, nyaman di kuping. Proses toko nya sedikit lambat, 3 hari baru di serahkan ke jasa kirim, mungkin restock dulu kali, jasa kirim sedang bagus, 2 hari sampai. Terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Suara. Cocok. Pengemasan baik, kualitas barang baik, semuanya baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Tentu saja. Iyalah tuh. Makasih MI Official Store, earbuds nya bagus suaranya oke, batre awet, mudah-mudahan awet selamanya. Makasih untuk kurir Shopee Express.",
        "sentiment": "positif",
    },
    {
        "comment": "Oke lah. Kebanyakan fitur, tapi yang paling bagus fitur fast pair nya sih. Worth it sih, suara yang dihasilkan sudah cukup untuk daily, bassnya bersih, treblenya dapet. Cuma yang bikin kurang, yaitu untuk penggunaan lama tidak nyaman di telinga, bikin cepat capek atau sakit. Itu saja sih tapi worth it lah 9.2/10.",
        "sentiment": "positif",
    },
    # Negatif
    {
        "comment": "Kualitas produk ini sangat rendah, suaranya buruk dan earbuds terlalu besar. Tidak puas dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini tidak awet, baterai cepat habis. Saya sangat kecewa dengan kualitasnya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing produk sangat buruk, barang datang dalam keadaan rusak. Pengiriman sangat lambat juga.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya mengharapkan banyak dari fitur-fitur yang dijanjikan, namun sebagian besar tidak berfungsi dengan baik. Kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Earbuds ini sangat tidak nyaman dipakai, saya merasa sakit dan cepat capek saat menggunakannya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak sesuai dengan ekspektasi saya. Suaranya tidak bagus dan saya merasa sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas suara produk ini sangat rendah. Saya tidak merekomendasikan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak cocok untuk penggunaan sehari-hari. Saya merasa uang saya terbuang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Earbuds ini tidak nyaman di telinga. Saya merasa sakit saat menggunakannya untuk waktu yang lama.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini tidak sesuai dengan deskripsi yang diberikan. Fitur-fitur yang dijanjikan tidak ada.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini tidak sebanding dengan kualitasnya. Saya merasa saya membayar terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya tidak merekomendasikan produk ini. Kualitasnya rendah dan baterai cepat habis.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman produk sangat lambat. Saya harus menunggu lama sebelum menerima barang ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Earbuds ini terlalu besar dan tidak nyaman di telinga. Saya tidak suka dengan desainnya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas suara produk ini sangat rendah. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
]


Poco_x5 = [
    {
        "comment": "Bagus bangettt.. barang sesuai yang di order.. keren hpnya.. semoga awet dan nggak gampang panas, sudah dapat casing.. mantap ini.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk baik, produk original. Packing baik, pengiriman cepat, sampai tujuan aman. Pemakaian kurang lebih 1 bulan fine-fine saja. Overall oke, sesuai ekspektasi. Seller ramah dan responsif. Recommended seller and product.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah paket sudah sampai, packing rapi dan aman, barang sesuai dengan pesanan, HP berfungsi dengan baik, semoga awet, seller responsif dan amanah, pengiriman cepat, terima kasih seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus banget ini hp dengan harga segini, cocok untuk anak cowok. Pengemasan rapi dan aman pengiriman cepat. Thank you so much seller GBU.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat banget. Padahal mau minta di-pending. Tapi ternyata sudah dikirim. Good banget. Fast response. Terima kasih Shopee.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sampai dengan aman dan berfungsi dengan baik sesuai pesanan. Terima kasih seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah udah sampai, spek bengis harga manis setelah nonton gadgetin sama nyari hp yang lain ttp balik lagi ke poco emang gada obat, review gadgetin ga pernah ngecewain camera'y bener² bagus banget, tapi sayang aku ambil ram 6 semoga cukup hehe, cantik banget warnanya, spek nya cukup gagah buat aku ga suka nge-game paling utama si incer cameranya 😁, semoga awet berkah selalu shopee, pengirimannya juga cepat banget mantap pokonya 👍❤️",
        "sentiment": "positif",
    },
    {
        "comment": "Good pesanan dikirim dengan cepat dikirim. Hp nya bagus sesuai yang diinginkan kelengkapan aman semuanya ada, mantap lah.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman seminggu, soalnya dari Semarang. Packing aman, kardus luar+dibungkus bubble wrap dalam. Terima kasih seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Gila, kameranya jernih banget.. emang bagus banget ini.. nggak nyesel. Beli poco x5 pro ditoko ini.. keren pokoknya.. baterai cepat casnya juga tidak lama.. buat main game enak juga.. barengan ama casing datanya padahal sudah dapat di boknya tapi pengen casing evos😂😂😂",
        "sentiment": "positif",
    },
    {
        "comment": "MasyaAllah Tabbarakkalah.. bagus HP nya semoga awet.. pengiriman sangat cepat.. next order.",
        "sentiment": "positif",
    },
    {
        "comment": "Kamera oke banget, hp tidak over panas. Worth it banget dengan harga segini udah dapat hp spek seperti Poco X5 Pro 5G.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah setelah menunggu beberapa hari datang juga, pengalaman pertama beli hp online, untuk hp masih segel, packing aman, ada bubble wrap nya, hp sudah dicoba juga alhamdulillah normal berfungsi dengan baik semoga awet. Pengiriman cepat, overall 👍👍👍 sukses terus Poco & Xiaomi Indonesia.",
        "sentiment": "positif",
    },
    {
        "comment": "Pertama kali beli hp online mantap pengirimannya cepat biar ngeri² gimana gitu lihat kerususnya. Semoga awet ganti pake MIUI, awalnya pake produk sebelah yang sama-sama PO, makasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas dari semua fitur sesuai harga dan sangat bagus, buat foto-foto bagus banget, dan untuk bermain game aman, nyaman, lancar tanpa lag. Mantap banget dapet harga murah ditambah lagi voucher potongan harga.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus banget, baterai awet, chipset kencang, dan yang paling disuka, kameranya benar-benar bagus, hasil fotonya suka banget, cocok untuk merekam video stabil, cocok untuk konten, semoga awet dan tahan lama karena baru pertama beli hp Poco… aamiin.",
        "sentiment": "positif",
    },
    ### Negatif
    {
        "comment": "Barang rusak saat diterima, layar retak, sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya memesan varian tertentu, tetapi yang diterima adalah varian yang berbeda. Ini sangat mengganggu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan tidak sesuai dengan estimasi yang diberikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "HP ini mengalami masalah teknis yang mengganggu, seperti sering restart sendiri.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sudah mencoba menghubungi penjual untuk mengatasi masalah dengan produk ini, tetapi mereka tidak merespons.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk, hanya dalam kardus tanpa perlindungan tambahan, sehingga barang tiba dalam kondisi rusak.",
        "sentiment": "negatif",
    },
    {
        "comment": "Baterai HP sangat cepat habis dan perlu sering diisi ulang, tidak sesuai dengan ekspektasi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya memesan HP ini dengan harapan kualitas kamera akan bagus, tetapi hasil foto tidak sesuai dengan yang diharapkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat dan saya telah menunggu terlalu lama untuk menerima produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Setelah beberapa minggu pemakaian, HP ini mulai mengalami masalah seperti layar tidak responsif.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pembelian ini adalah kekecewaan besar. HP ini tidak sebanding dengan harganya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak jujur ​​mengenai kondisi produk yang dijual. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya telah mencoba menghubungi layanan pelanggan, tetapi tidak ada respons yang memuaskan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas konstruksi HP ini sangat rendah, mudah rusak, dan tidak tahan lama.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak bagus sama sekali, baterainya cepat habis, chipsetnya lelet, dan yang paling dibenci, kameranya sangat buruk, hasil fotonya sangat jelek, tidak cocok untuk merekam video stabil, tidak cocok untuk konten, semoga tidak tahan lama karena ini adalah kesalahan besar membeli hp Poco… aamiin.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan performa HP ini. Sering terjadi lag dan hang.",
        "sentiment": "negatif",
    },
]


Tv_stick = [
    {
        "comment": "Fitur Terbaik: android tv\nSepadan dengan Harga: harga worth to buy dari pada beli tv baru\nPengiriman lumayan cepat, connectnya jg gampang trimakasih seller sukses selalu. Ini membantu bgt sih buat tv smart yg belum android jd gk perlu upgrade tv lagi hehe",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: 👌🏼\nSepadan dengan Harga: sesuai harga\nNicee, barang sesuai pesanan\nPacking juga aman, ada buble wrap nya juga\nTerimaksih seller, sukses selalu 😁",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagusss bisa untuk nonton YouTube or Netflix\nCocok untuk tv Samsung, bagusss 🥰🥰🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok\nSepadan dengan Harga: ok\nMakasih min alhamdulillah paketnya uda smpai. Pecking bubble tebal dan aman sampai sulbar. Sesuai pesanan 👍🏻\nAwalX layar tv kedip2. Lama2 uda ngk. Smoga awet yah... Makasih 🙏🏻. Tp Expedisinya lama yah 1 mingguan.",
        "sentiment": "positif",
    },
    {
        "comment": "Mengubah TV biasa menjadi pintarrrr :)\nPacking rapi dan aman",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baik sekali\nSepadan dengan Harga: agak mahal dikit\nDa harga da kualitas, bagus bngt berfungsi dengan baik, reseller jg baik di kasih hadiah mainan",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: produk original, pengemasan bagus, pengiriman cepat\nSepadan dengan Harga: sepadan, sesuai dengan deskripsi\nSeller responsif, setelah datang langsung saya coba, Alhamdulillah berjalan dengan baik. TV saya sudah jadi smart TV",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: terbaik\nSepadan dengan Harga: sepadan\nRekomend....toko amanah, respon penjual cepat dan ramah sekali, pengiriman cepat sekali, kurirnya cakep, ok tengkyu.....🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: seperti deskripsi\nSepadan dengan Harga: standar\nBelum dicoba karena utk di rumah adik sepupu, awet, tahan lama, dan mantul mantul",
        "sentiment": "positif",
    },
    {
        "comment": "Mantap! Kecepatan pengiriman sesuai standar. Pengemasan produk okelah. Gampang cara penggunaannya, langsung lancar. Makasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok\nSepadan dengan Harga: ok\nAlhamdulillah sampai dengan aman, pengiriman dan pengemasan sangat baik, produk ok, semoga awet dan banyak manfaatnya",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok\nSepadan dengan Harga: harga standar\nTerimakasih paket sampai dengan cepat",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Xiaomi Smart TV\nSepadan dengan Harga: harga sesuai\nXiaomi Smart TV ini bisa membantu kita menonton Netflix, YouTube, dll... Tapi sayang kekurangannya di remotenya yang kadang-kadang suka error dan tidak terdeteksi kursornya... Jadi harus reset remotenya terus kalau mau pakai... Next, tolong ditingkatkan lagi untuk remotenya... Kalau untuk yang lain semua sudah ok, pengiriman, penjual fast respon....",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Mudah digunakan\nPengiriman dan pengemasan lumayan cepat, produk mudah digunakan",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: layar bening\nSepadan dengan Harga: standar\nSudah sampai\nBagus\nPengiriman cepat, terima kasih....",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat, harga sangat bersahabat. Berfungsi dengan sempurna. Terima Kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus\nSepadan dengan Harga: terjangkau\nKualitas oke banget, pengirimannya juga cepat, dan mudah digunakan, mantap!",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Pengiriman sangat lambat. Barangnya tidak sesuai dengan deskripsi. Sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak sesuai dengan deskripsi\nSepadan dengan Harga: terlalu mahal\nBarangnya sudah rusak saat sampai. Tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat buruk. Barang cacat dan tidak dapat digunakan. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak berfungsi dengan baik\nSepadan dengan Harga: tidak sepadan\nSaya merasa uang saya terbuang percuma. Tidak puas dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat sampai. Tidak ada respons dari penjual. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lama. Produk tidak sesuai dengan harapan. Saya sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak berfungsi\nSepadan dengan Harga: tidak sepadan\nProduk cacat dan tidak dapat digunakan. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan buruk. Produk rusak saat sampai. Saya merasa ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat mengecewakan. Produk tidak berkualitas. Saya tidak merekomendasikan ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Buruk\nSepadan dengan Harga: tidak sepadan\nSaya merasa terjebak dengan produk ini. Tidak sesuai dengan harapan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lama. Produk tidak berkualitas. Saya sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak berfungsi\nSepadan dengan Harga: harga terlalu tinggi\nSangat mengecewakan. Tidak sesuai dengan deskripsi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat sampai. Tidak ada garansi. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlalu lambat. Produk tidak sesuai dengan deskripsi. Saya merasa ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk tidak berkualitas. Tidak berfungsi dengan baik. Tidak direkomendasikan.",
        "sentiment": "negatif",
    },
]


M5_xiaomi = [
    {
        "comment": "Fitur Terbaik: terbaik\nSepadan dengan Harga: iya\nAlhamdulillah benar benar puas dan bagus berbelanja di toko ini. Hp sampai dengan sangat aman, masih segel, sesuai pesanan. Makasih ya ka, sukses selalu untuk kita 🥳🤗",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: terupdate\nSepadan dengan Harga: terjangkau\nAlhamdulillah barang sudah mendarat dengan selamat, pengiriman nya oke di bungkus dengan rapih mantap. Kurir nya juga ramah mantap terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: sepadan banget\nFitur Terbaik: baik\nBarang datang tanpa cacat bonus case hp, pengiriman cepat pengemasan rapi tidak rusak tidak penyok bagus banget anakku suka makasih banyak, bisa langganan.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: memiliki sesuatu yang spesial\nSepadan dengan Harga: harga sangat murah dibanding di toko offline\nPuas banget belanja di sini. Barang aman, packing rapi. Semoga awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Pokoknya baik karena masih baru\nSepadan dengan Harga: Iya\nPengemasan & pengiriman ok. Packing ok, barang ok. Langganan beli disini selalu cocok. Alhamdulillah dapat harga promo kemerdekaan free cover HP. Makasih yaaa...",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: iyaa\nFitur Terbaik: baik\nHp nya bagus, meski awalnya sempat panik hp nya lama nyala pas baru sampai, setelah nyala hp nya bagus, sesuai deskripsi dan semoga awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Semua Baik\nSepadan dengan Harga: Tentu\nSuka banget, pengiriman cepat, karena datang tepat waktu, mau buat surprise ke anak. Pengemasan Oke, barang bagus, original... Gak kecewa pokoknya belanja disini",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: chipset nya sangat powerful di kelasnya\nSepadan dengan Harga: harganya terjangkau\nProduk sesuai pesanan, dan adikku senang banget dan ini sudah yang kedua kalinya aku beli HP di sini, dan sangat puas dengan produknya, mantap dan recommended deh pokoknya 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: NFC dan Kapasitas Internal 128GB\nSepadan dengan Harga: Sangat Sepadan\nAlhamdulillah barang sampai dengan aman dan kualitas bagus. Perlu diingat bagi yang mau beli bahwa HP ini tidak ada ULTRAWIDE pada kameranya ya. Dan please jangan pilih paket pengiriman sameday karena rugi waktu, lama sampainya. Sama aja kayak pake jasa reguler. Thanks tetap bintang 5 kok.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: Terjangkau\nFitur Terbaik: Sesuai Pesanan\nPengiriman cepat, packing rapi, barang sampai tujuan dengan aman, kurir ramah, kualitas barang bagus dengan harga terjangkau, dan yang pasti original. Terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya sudah diterima kk, barang sesuai pesanan.. Pengiriman cepat, packing rapi.. Semoga bisa beli lagi gak kan nyesel beli di sini.. Makasih kaka",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: berharap yang terbaik 👍💯\nSepadan dengan Harga: mudah-mudahan sepadan\nPacking aman, rapi, pengiriman cepat, mendarat dengan aman.. Semoga barangnya baik-baik saja dan awet 😁👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok\nSepadan dengan Harga: ok\nAlhamdulillah.... pesanan sudah sampai tujuan\nPacking aman, rapi, dan kuat\nHpnya langsung bisa dipakai dengan baik\n\nTerima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Sangat cepat untuk bermain game\nSepadan dengan Harga: Worth it pisann\nKenceng banget performa hpnya, batrenya tahan lama, ga terlalu panas lagi kalo di pake maen game, worth it parahhhhh👌",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mantap full fitur\nSepadan dengan Harga: harga official store\nHP bagus. Browsing lancar. Ga lemot lagi. Aksesoris lengkap. Mantap pokoknya.",
        "sentiment": "positif",
    },
    {
        "comment": "Packing nya rapi, penjual juga ramah. Cuma lambat pengiriman aja karna lagi super sale. Selebihnya bagus banget fitur nya canggih juga. Semoga awet deh pokoknyaa",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Fitur Terbaik: buruk\nSepadan dengan Harga: tidak sepadan\nSangat kecewa dengan produk ini. Pengiriman sangat lambat dan barangnya rusak saat sampai. Saya tidak akan pernah membeli di sini lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: sangat buruk\nSepadan dengan Harga: terlalu mahal\nProduk ini adalah sampah. Tidak sesuai dengan deskripsi dan harganya terlalu mahal. Saya merasa ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak ada\nSepadan dengan Harga: harga tidak sepadan\nBarang tidak pernah sampai, dan penjual tidak merespons. Uang saya hilang begitu saja. Ini adalah pengalaman buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: rusak\nSepadan dengan Harga: terlalu mahal\nSaya mendapatkan produk yang rusak dan penjual tidak memberikan pengembalian uang. Ini adalah penipuan!",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak sesuai dengan deskripsi\nSepadan dengan Harga: mahal\nSaya merasa tertipu dengan produk ini. Deskripsi tidak akurat dan harganya terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: sangat mengecewakan\nSepadan dengan Harga: tidak sepadan\nSaya sangat kecewa dengan pengalaman belanja di sini. Produknya buruk dan pengirimannya lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: buruk sekali\nSepadan dengan Harga: harga terlalu mahal\nProduk ini tidak berfungsi dengan baik dan harganya terlalu mahal. Saya menyesal membelinya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak ada\nSepadan dengan Harga: mahal\nSaya merasa uang saya terbuang percuma. Produknya tidak memiliki fitur yang dijanjikan dan harganya mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: rusak parah\nSepadan dengan Harga: sangat mahal\nBarang yang saya terima rusak parah dan penjual tidak merespons. Saya sangat marah dengan pengalaman ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak ada\nSepadan dengan Harga: harga terlalu tinggi\nSaya merasa ditipu. Produk ini tidak memiliki fitur apa pun yang berarti dan harganya terlalu tinggi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: sangat mengecewakan\nSepadan dengan Harga: tidak sepadan\nPengiriman lambat dan produknya sangat buruk. Saya tidak akan merekomendasikan ini kepada siapa pun.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: sangat buruk\nSepadan dengan Harga: terlalu mahal\nIni adalah pemborosan uang. Produknya sangat buruk dan harganya terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: tidak ada\nSepadan dengan Harga: mahal\nSaya sangat kecewa dengan produk ini. Tidak ada fitur yang berguna dan harganya terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: rusak\nSepadan dengan Harga: terlalu mahal\nSaya mendapatkan produk yang rusak dan penjual tidak mau mengganti. Ini adalah pengalaman yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing nya rapi, penjual juga ramah. Sayangnya pengiriman sangat lambat, terutama karena lagi super sale. Selebihnya fiturnya memang canggih, tapi pengiriman yang lambat membuat pengalaman berbelanja ini tidak menyenangkan. Semoga produknya tetap awet.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: sangat mengecewakan\nSepadan dengan Harga: tidak sepadan\nSaya merasa sangat kecewa dengan pembelian ini. Produknya buruk dan harganya tidak sepadan.",
        "sentiment": "negatif",
    },
]


product_Xiaomi_Tv_43_pd = pd.DataFrame(Xiaomi_Tv_43)
product_Buds_4_pd = pd.DataFrame(Buds_4)
product_Poco_x5_pd = pd.DataFrame(Poco_x5)
product_Tv_stick_pd = pd.DataFrame(Tv_stick)
product_M5_xiaomi_pd = pd.DataFrame(M5_xiaomi)


product_Xiaomi_Tv_43_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Buds_4_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Poco_x5_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Tv_stick_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_M5_xiaomi_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)


print("Value counts Ke-1: ", product_Xiaomi_Tv_43_pd["sentiment"].value_counts())
print("Value counts Ke-2: ", product_Buds_4_pd["sentiment"].value_counts())
print("Value counts Ke-3: ", product_Poco_x5_pd["sentiment"].value_counts())
print("Value counts Ke-4: ", product_Tv_stick_pd["sentiment"].value_counts())
print("Value counts Ke-5: ", product_M5_xiaomi_pd["sentiment"].value_counts())


merge_df = pd.concat(
    [
        product_Xiaomi_Tv_43_pd,
        product_Buds_4_pd,
        product_Poco_x5_pd,
        product_Tv_stick_pd,
        product_M5_xiaomi_pd,
    ]
)


positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan positif:", positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_xiaomi.csv", index=False)

print("Data telah disimpan")
