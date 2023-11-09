import pandas as pd


Bear_Panci = [
    {
        "comment": "Fitur Terbaik: bagus bgt. Sepadan dengan Harga: sepadan. Alhamdulillah barang sudah diterima dan sampai dengan aman. Packing aman rapi, pengiriman cepat, barang bagus bgt pliss, asli ga boong recommended pokoknya, harga murah kualitas bagus bgt, gausah bingung yg mau cek out segera, dijamin bagus bgt terimakasih semoga barang nya awet, berkah selalu seller 🙏🙏🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: anti lengket, dan cepat panas. Sepadan dengan Harga: sangat sepadan. Direkomendasikan untuk dibeli untuk anak kost, bahan bagus tidak lengket.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: sesuai sama harga, bagus banget. Fitur Terbaik: harga murah tapi berkualitas. Barangnya bagus banget, harganya juga murah kemaren checkout pas flash sale jadi murah, pengiriman cepat ga nyampe 3 hari, admin fast respon dan ramah banget, colokan panci diujung gagang jadi kalo pas nyuci ga kena air, pokoknya ⭐⭐⭐⭐⭐.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: Sepadan. Fitur Terbaik: Bisa untuk pemanas makanan. Panci listriknya berjalan bagus, semua lancar, pengiriman cepat, hanya sedikit penyok. Alhmdulillah bisa di betulin sendiri Dan Masih bisa di pakai. Kelihatannya kebentur barang lain selama proses pengiriman. Terimakasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: Bahannya Lumayan Ringan dgn warna yang bagus. Sepadan dengan Harga: harganya sesuai. Belum sempat dicoba,, semoga barangnya awet dan tidak cepet rusak,, ini pertama kali mau coba masak pakai panci listrik.. terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: alhamdulillah sepadan dengan uang. Fitur Terbaik: alhamdulillah bekerja dengan baik. Alhamdulillah udh sampai dan berfungsi dengan baik aku udh coba masak air dan mie oke matang dengan sempurna 😍😍.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus. Sepadan dengan Harga: barang. Produk berfungsi dengan baik. Produk bagus. Packing aman & rapi. Thank you GM Bear",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: Kualitas bagus. Fitur Terbaik: Belum coba. Worth it untuk harga segitu, tapi belum coba apakah bakal tahan lama atau tidak. Dilihat dari review yang lain pada tahan lama, jadi semoga ini juga tahan lama sama saya.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus. Sepadan dengan Harga: baik. Bekerja dengan baik, tapi ada penyok di badan bawah panci, tapi itu tidak mempengaruhi kinerja.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baikkk. Sepadan dengan Harga: pas bgt ma harga. Bagus bagus semoga awet sebagai anak kost yg dapur umum ya terbantu klo mager masak diluar love you muach.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus. Sepadan dengan Harga: sepadaan. Multi fungsi, cepat panas, semoga awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: sepadan. Yeyyy udah sampai, cepat banget sumpah, harganya juga worth it, cocok banget buat anak kost, belum dicoba, semoga aja awet, thanks seller.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus, Sepadan dengan Harga: sepadaan, Multi fungsi, cepat panas, semoga awet",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: sepadan, Yeyyy udah sampai, cepat banget sumpah, harganya juga worth it, cocok banget buat anak koss, belum dicoba, semoga aja awet, thanks seller",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: kualitas baik sangat sesuai, Fitur Terbaik: baik, Kualitas baik sesuai dengan yang di foto, packing rapih aman, panci berfungsi baik",
        "sentiment": "positif",
    },
    {
        "comment": "Saya sungguh senang dengan pembelian ini! Barangnya tiba dalam kondisi sempurna, dan pengiriman cukup cepat. Sungguh suatu kebahagiaan bagi saya.",
        "sentiment": "positif",
    },
    ## Negatif
    {
        "comment": "Panci listrik ini sangat buruk. Saya baru saja mencobanya dan itu tidak berfungsi sama sekali. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang diterima rusak. Terdapat penyok yang cukup besar pada bagian bawah panci listrik. Pengemasan juga buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat. Saya harus menunggu terlalu lama untuk menerima barang ini, dan ketika itu tiba, itu rusak.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Panci ini cepat panas, tetapi tidak bertahan lama. Saya merasa seperti saya telah membayar terlalu banyak.",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual tidak ramah dan tidak responsif. Saya mencoba menghubunginya mengenai barang yang rusak, tetapi tidak mendapatkan tanggapan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur panci listrik ini sangat buruk. Ini tidak menghangatkan makanan dengan baik dan seringkali melekat. Saya sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga terlalu mahal untuk kualitas ini. Saya tidak merekomendasikan produk ini. Saya merasa seperti saya telah ditipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan respon penjual buruk. Saya tidak puas dengan pengalaman berbelanja ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat buruk. Saya mencobanya dan barang tidak berfungsi sama sekali. Saya merasa seperti saya telah membuang uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk dan barang rusak saat sampai. Penjual tidak membantu dalam menyelesaikan masalah ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Saya merasa seperti saya telah membuang uang untuk barang ini. Tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Panci ini sangat buruk. Bahan pembuatannya tidak berkualitas dan mudah rusak. Saya sangat kecewa dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan tidak sesuai dengan yang diharapkan. Barang yang diterima dalam kondisi buruk. Saya merasa sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Respon penjual buruk. Saya mencoba menghubunginya mengenai masalah barang yang rusak, tetapi tidak mendapatkan jawaban yang memuaskan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa tertipu dengan harga produk ini. Tidak sepadan dengan kualitas yang sangat rendah. Saya tidak merekomendasikan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat buruk. Saya sangat kecewa dengan pembelian ini. Pengiriman lambat dan barang rusak saat sampai.",
        "sentiment": "negatif",
    },
]

Spatula_Set = [
    {
        "sentiment": "positif",
        "comment": "Barang sudah sampai, isi lengkap sudah sesuai dengan deskripsi, tidak ada kendala. Dan tdk ad salahnya kasih bintang 5 utk seller dan jasa pengirimannya yg sdh handle with care. Kualitas barang tergantung merk sih mnurut gw",
    },
    {
        "sentiment": "positif",
        "comment": "Tampilan: bagus\nPerforma: elegan\nKualitas: baik\nAlhamdulillah pesenankuh sudah sampai .\nSuka banget belanja disini karna udah langganan juga jadi pasti bagus ❤️💐😘🤗👍.\nDapet voucher belanja pun 😀\nMakasih shopee dan GM bear 👍",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: hemat\nBahan/Material: plastik\nKegunaan: memasak\nBahan nya bagus, produk nya sesuai, produk original, barang tidak mengecewakan",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: terjangkau\nBahan/Material: baik\nKegunaan: banyak\nTerima kasih banyak ya pesanannya sudah diterima dengan baik packing nya rapih Alhamdulillah akhirnya baik pengiriman cepat barangnya sesuai dengan gambar tidak ada yang cacat dapatnya banyak banget Lila nih bisa buat lebaran yang sangat membantu ini berapa ini hanya ada yang bermacam-macam .. ok",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: bersahabat\nBahan/Material: plastik\nKegunaan: perlengkapan dapur\nBarang sampe sesuai pesanan hanya saja aku ga baca bahan material nya ternyata plastik .. Tapi its oke gpp sesuai harga next time aku pngn order yg stenlis / bahan lain yg bisa buat di pake masak",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: murah\nBahan/Material: lumayan\nKegunaan: belum dicoba\nSemoga awet, udah beli produk GM bear 3x hasilnya gak mengecewakan\nBaru pesen kemarin, hari ini udah nyampek..",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: murah banget\nBahan/Material: plastik tahan panas\nKegunaan: memasak\nPengemasan agak lama sih\nTapi barang bagus kok\nHarga murah\nBarang original\n1 ser dapat 6",
    },
    {
        "sentiment": "positif",
        "comment": "Tampilan: bagus\nPerforma: belum di coba\nKualitas: semoga sih awet yaa heheh\nKedua kali beli disini. Selisih 1 hari doang si pesen nya😁 admin ramah, baik juga ngabarin pesanan proses kirim. Spatula set 6pcs elegant. Mayan buat hadiah ibu kosan spesial hari ibu.",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: ok\nBahan/Material: lumayan sesuai harganya\nKegunaan: memasak\nAlhamdulillah barang bagus sesuai dg harga,muda2 n g cepet patah d meleleh saay digunkan",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: murah\nBahan/Material: bagus\nKegunaan: aman\nBahan nya bagus bngt kurirnya ramah",
    },
    {
        "sentiment": "positif",
        "comment": "Tampilan: baik\nPerforma: belum smpt d coba\nKualitas: blm coba tp klihatan nya baik\nBth alat2 masak eh tau nya ada dsni produknya lg promo, alat2 nya bahan nya tebal, model nya bgs, klihatan sgt baik n cocok utk alat masak yg teflon, pengiriman,agk lama smp sekitar 6 har, packing bgs pke dus tp ga pke bubble wrap cm plastik,tp aman, seller veey recomended, kurir sgt ramah 🙏🏻🙏🏻☺👍🏻",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: murah\nBahan/Material: bagus\nKegunaan: memasak\nPake GM gear spatula membuat pengalaman memasak jd lebih simple",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: Alhamdulillaah terjangkau\nBahan/Material: oke\nKegunaan: masaaak memasaakkk biar lebih mudah\nAlhamdulillaah barang oke harga terjangkau masak jadi lebih mudah. makasiihh yaaaa",
    },
    {
        "sentiment": "positif",
        "comment": "Tampilan: sesuai\nPerforma: bagus\nKualitas: bagus(semoga awet ya)\nsesungguhnya saya takut kl dipake masak jadi blonyokk ky punya temen saya tapi belinya ga ditoko ini, yaa semga toko ini baguslah yaa bisa rekomendasi buat anak kost juga ky saya",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: terjankau\nBahan/Material: plastik\nKegunaan:  belum dicoba\nSpatula plastik isi 6 baik dan sesuai harga.packing baik dan rapi.respon penjual baik.pengiriman paket pesanan cepat.tetap semangat,jaga kesehatan dan sukses selalu,gan.tetap semangat,jaga kesehatan dan sukses selalu,gan.terima kasih,gan",
    },
    {
        "sentiment": "positif",
        "comment": "Suka bangettt dngn produknya, dngn hrga terjangkau sdh bisa menambah perabotan dapur mama 😁😁 Pengiriman juga cepat, Luuvvvvv dehhh pkkny ❤️❤️",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: mahal\nBahan/Material: buruk\nKegunaan: tidak sesuai\nBarangnya rusak, harga terlalu mahal, tidak sesuai dengan deskripsi.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tampilan: jelek\nPerforma: buruk\nKualitas: sangat buruk\nSaya sangat kecewa dengan produk ini. Tampilannya jelek, kualitas buruk, dan performanya sangat buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: tidak terjangkau\nBahan/Material: plastik murahan\nKegunaan: tidak berguna\nIni adalah pemborosan uang. Harganya tidak terjangkau, bahan plastik murahan, dan tidak ada gunanya.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: terlalu tinggi\nBahan/Material: sangat buruk\nKegunaan: tidak berguna\nSaya merasa seperti ditipu. Harganya terlalu tinggi untuk kualitas yang sangat buruk. Barangnya tidak berguna.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tampilan: tidak sesuai\nPerforma: buruk\nKualitas: sangat buruk\nProduk ini sangat mengecewakan. Tampilannya tidak sesuai dengan deskripsi, performanya buruk, dan kualitasnya sangat buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: tidak wajar\nBahan/Material: plastik murahan\nKegunaan: tidak berguna\nSaya merasa sangat kecewa dengan pembelian ini. Harganya tidak wajar untuk produk dengan bahan plastik murahan yang tidak berguna.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tampilan: jelek\nPerforma: sangat buruk\nKualitas: buruk\nSaya menyesal membeli produk ini. Tampilannya jelek, performanya sangat buruk, dan kualitasnya buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: terlalu mahal\nBahan/Material: buruk\nKegunaan: tidak berguna\nSaya tidak merekomendasikan produk ini. Harganya terlalu mahal untuk bahan yang buruk dan tidak ada gunanya.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: tidak sesuai\nBahan/Material: sangat buruk\nKegunaan: sangat terbatas\nSaya merasa tertipu. Harganya tidak sesuai dengan kualitas yang sangat buruk, dan penggunaannya sangat terbatas.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tampilan: mengecewakan\nPerforma: buruk\nKualitas: sangat buruk\nProduk ini adalah buang-buang uang. Tampilannya mengecewakan, performanya buruk, dan kualitasnya sangat buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: tidak masuk akal\nBahan/Material: murahan\nKegunaan: tidak berguna\nSaya sangat kecewa. Harganya tidak masuk akal untuk produk dengan bahan murahan yang tidak berguna.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tampilan: sangat jelek\nPerforma: sangat buruk\nKualitas: buruk\nProduk ini adalah salah satu yang terburuk yang pernah saya beli. Tampilannya sangat jelek, performanya sangat buruk, dan kualitasnya buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: terlalu tinggi\nBahan/Material: sangat buruk\nKegunaan: tidak sesuai\nSaya merasa seperti dibohongi. Harganya terlalu tinggi untuk kualitas yang sangat buruk. Produk ini tidak sesuai dengan deskripsi.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: tidak masuk akal\nBahan/Material: plastik murahan\nKegunaan: tidak berguna\nSaya sangat menyesal membeli produk ini. Harganya tidak masuk akal untuk bahan plastik murahan yang tidak berguna.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tampilan: sangat mengecewakan\nPerforma: sangat buruk\nKualitas: buruk\nProduk ini adalah bencana. Tampilannya sangat mengecewakan, performanya sangat buruk, dan kualitasnya buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga: terlalu tinggi\nBahan/Material: sangat buruk\nKegunaan: tidak berguna\nSaya tidak merekomendasikan produk ini. Harganya terlalu tinggi untuk bahan yang sangat buruk dan tidak ada gunanya.",
    },
]

Wajan_16cm = [
    {
        "sentiment": "positif",
        "comment": 'Alhamdulillaah pesanan sudah nyampek dg sangat amanah tanpa kurang sedikitpun, tokonya benar" amanah, pokoknya sangat puas belanja disini, terimakasih shopee, toko, agen shopee semoga tambah amanah barokah Aamiin...',
    },
    {
        "sentiment": "positif",
        "comment": "Pesanan telah sampai sesuai pesanan, pengiriman cukup cepat Kualitas original Terimakasih",
    },
    {
        "sentiment": "positif",
        "comment": "Alhamdulillah teplon nya udh nyampe kk.. bagus bnget..mungil. Cocok untuk ceplok telor..goreng sosis / naget...dapet hrga murce..☺️☺️👍👍 Toko nya amanah....responnya cepat..👍👍 Terimakasih seller..🙏🙏",
    },
    {
        "sentiment": "positif",
        "comment": "Semoga awet, udah beli produk GM bear 3x hasilnya gak mengecewakan Baru pesen kemarin, hari ini udah nyampek..",
    },
    {"sentiment": "positif", "comment": "Top dah mantul (mantap betul) ok"},
    {
        "sentiment": "positif",
        "comment": "Lucu kecil banget kaya mainan hahahahahah tp bagus imut gituuu, lumayan buat dadar telor mana lagi harga promo lagiii. Semoga awet yaaaaaa. Terimaksihhhhhhh",
    },
    {
        "sentiment": "positif",
        "comment": "barang bagus, bahan bagus ringan sekali tapi. sesuai harga, lumayan untuk ceplok telor. semoga tidak lengket. thank youu",
    },
    {
        "sentiment": "positif",
        "comment": "Sumpahh.. ini imut banget. Comel😂🤣🤣. Cocoklah untuk bkin fried egg🍳",
    },
    {
        "sentiment": "positif",
        "comment": "Udah kedua kalinya beli produk GM Bear disini bener bener memuaskan , bahannya tebel dan kualitas nya sangat sangat bagus next bakalan order yang kesekian kalinya lagi",
    },
    {
        "sentiment": "positif",
        "comment": "Sesuai ekspektasi. Memang butuhnya yg sekecil ini aja buat bikin roti bakar sama telur cukup lah. Thanks,gan",
    },
    {
        "sentiment": "positif",
        "comment": "Belum di coba barangnya tapi mdh2an bagus ya, pengiriman cepet banget , pesen kemarin , Sekarang dah dateng",
    },
    {"sentiment": "positif", "comment": "Sesuai picture n deskripsi thank you"},
    {
        "sentiment": "positif",
        "comment": "Alhamdulillah barang sudah sampai di rumah, udah aku pake teplonnya",
    },
    {
        "sentiment": "positif",
        "comment": "Teflonnya kecil imut barang nyampai dengan selamat gak ada yang cacat sedikit pun harga sangat terjangkau pengiriman cepat terima kasih",
    },
    {
        "sentiment": "positif",
        "comment": "Pengiriman cepat, barang ngak ada yang rusak, harga juga murah, makasih seller",
    },
    {
        "sentiment": "positif",
        "comment": "Harga: murah\nBahan/Material: lumayan\nPengemasan: bagus, pakai kerdus\nPengiriman cepat, barang ngak ada yang rusak, harga juga murah, makasih seler",
    },
    {"sentiment": "negatif", "comment": "Barang rusak saat tiba, sangat kecewa."},
    {
        "sentiment": "negatif",
        "comment": "Kualitas produk sangat buruk, tidak sesuai dengan deskripsi.",
    },
    {
        "sentiment": "negatif",
        "comment": "Pengiriman sangat lambat, butuh waktu berhari-hari untuk sampai.",
    },
    {
        "sentiment": "negatif",
        "comment": "Harga terlalu mahal untuk kualitas yang buruk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Pengemasan sangat buruk, barang tiba dalam keadaan rusak.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tidak ada respon dari penjual terkait keluhan pelanggan.",
    },
    {
        "sentiment": "negatif",
        "comment": "Produk tidak sesuai dengan gambar yang ditampilkan.",
    },
    {
        "sentiment": "negatif",
        "comment": "Pelayanan pelanggan sangat buruk, sulit untuk menghubungi penjual.",
    },
    {
        "sentiment": "negatif",
        "comment": "Pengiriman terlalu lama, tidak sesuai dengan yang dijanjikan.",
    },
    {"sentiment": "negatif", "comment": "Barang tidak awet dan cepat rusak."},
    {"sentiment": "negatif", "comment": "Penjual tidak jujur tentang kondisi produk."},
    {
        "sentiment": "negatif",
        "comment": "Harga tidak sebanding dengan kualitas produk.",
    },
    {
        "sentiment": "negatif",
        "comment": "Pengiriman tidak aman, barang tiba dalam keadaan rusak.",
    },
    {
        "sentiment": "negatif",
        "comment": "Pelayanan pelanggan sangat buruk, tidak ada tanggapan dari penjual.",
    },
    {
        "sentiment": "negatif",
        "comment": "Produk palsu, bukan produk asli seperti yang diiklankan.",
    },
    {
        "sentiment": "negatif",
        "comment": "Tidak ada tanggapan atau respon dari penjual terhadap keluhan pelanggan.",
    },
]

Panci_listrik_0259 = [
    {
        "comment": "kotak sampai dalam keadaan sangat bagus dan tidak penyok, barang lengkap tidak ada yang lecet dan kurang sama sekali.. panci juga cepat panas ketika dinyalakan, cocok buat anak kost yang buru2 ke kantor atau ke kampus.. bagian dalam tidak lengket ketika dipakai memasak.. thank you seller!!! ☀☀☀🌻🌻",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ada opsi level panasnya\nSepadan dengan Harga: sepadan banget!!\nini di saranin sama temen aku untuk beli karena bentar lagi mau mulai nge kos, pas nyampe iseng dulu manasin air eh ternyata rebusnya gak gitu lama. udah gitu pancinya ringan dan gak gitu gede, cukup buat porsi makan seorang/dua. nanti mau debut masak mie pakai ini, tapi udah gak ragu sih pasti bakal lancar masaknya",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus\nSepadan dengan Harga: iya\nBarang nya bagus realpice pengiriman nya juga cepat respon penjualan nya sangat bagus rekomendasi sih buat anak kosan",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: kualitas dasar panci yang tidak mudah mengelupas\nSepadan dengan Harga: kualitasnya bagus\nTerimakasih seller, alhamdulilah barang sampai dengan aman, pengiriman cepat, kualitas panci bagus dan sesuai harga, susah coba dipakai dan berjalan dengan baik 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat, nggak expect bakal secepet ini. Udah dites sekilas dan bisa nyala. Bagian tengahnya juga udah mulai terasa hangat padahal cuma dinyalain beberapa detik doang. Makasih, Seller.",
        "sentiment": "positif",
    },
    {
        "comment": "_ini si bagus banget dengan harga yg ok, gak terlalu berat, cantik warna nya, panas nya juga cepet,. Packing rapih, cepat sampai, dus gak ada yg penyok, pancinya aman, gak ada yg lecet,. Makasih seller, sukses selalu,.👍🏻👍🏻🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: cepat panas\nSepadan dengan Harga: yes\nCepet sampe, kualitas bagus, mudah dibersihkan, mudah digunakan. Ringan dan minimalis sekali. Kecil tp bukan yg kecil bgt. Cukup buat mie seukuran shin ramyun (cukup gede lho). Trus sejauh ini aku baru coba buat rebus aja sih. Soon bakal coba fungsi menggorengnya juga. Recommended sih. Cepet bgt panasnya.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: panci listrik serbaguna.\nAkhirnya udah datang barangnya. Packing aman pakai bubble wrap dan ada kardus (ga penyok sama sekali). Pas dibuka warnanya lebih ke hijau toska tp yg muda, gemeshhh bgt. Barang berfungsi dengan baik ketika di coba ke listrik dan ada tombol on off ya kok. Pokoknya cocok bgt utk anak kos yg gamau ribet kyk aku. Hahah. Thank you sellerrr♥️♥️♥️",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah bagussss 😍 memuaskan🤩 pengirim nya cpt ku kira bakal lamaa😭😭😭\nPacking aman👍🏻 kardusnya jg tebel👍🏻 pengemasan cpt 👍🏻😭 pengiriman cpt👍🏻 kualitas baguss udh aq coba buat masak air lumayan bgt buat anak kos👍🏻 Thanks seller 🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok lah\nSepadan dengan Harga: utk harga segitu menurut ku wort it si\nRealpick model nya juga bagus walaupun pas mau pesan penuh dgn drama karena takut gagal lagi tapi pke produk yang ini bner² serbaguna bgt\nThankyu:)",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: baik\nSepadan dengan Harga: harga murce\nPancinya sangat bagus, worth it si ini. Cocok buat anak kos kalau pngen masak. Bagus banget pokoknya, terimakasih seller",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: worth it simply\nSepadan dengan Harga: murah meriah\nBarang sudah sampai,pesan kamarin besok udah nyampe,kurir juga ramah, terimakasih seller barang sesuai pesanan,dan dapet harga promo lagi. Pokoknya mantap,belom di coba semoga berfungsi dengan baik",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus\nSepadan dengan Harga: rekomeded dengan harga segitu\nBagus, menarik, lampu nyala, semoga awet lama. Makasih min🥰😇",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: menarik\nSepadan dengan Harga: ya sangat sepadan\nBarangnya jujur bagus banget dengan harga segitu cepet panas juga suka banget sih pengiriman cepat lagi pertama ini beli dan bagus",
        "sentiment": "positif",
    },
    {
        "comment": "Sepadan dengan Harga: Iya harganya samalah dengan kualitas barangnya datang dengan keadaan yang baik\nFitur Terbaik: Alhamdulillah berfungsi dengan baik dan cepat mendidih airnya semoga bisa awet pengirimannya lumayan tingkat keamanan memuaskan",
        "sentiment": "positif",
    },
    {
        "comment": "Ya ampun suka bangett cocok banget untuk saya yg anak kost baru pesan td malam sehari doang udah nyampe bg kurirnya juga gercep bangett nganternyaa dan barangnya juga aman gg ada lecet banyak bablenya aman bgt dan lampunya nyala dan berfungsi senang banget makasih admin dan dapat harga promo senang",
        "sentiment": "positif",
    },
    {
        "comment": "Barang ini sangat buruk dan tidak sepadan dengan harganya. Pengiriman sangat lambat dan pelayanan pelanggan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada fitur berarti\nSepadan dengan Harga: Tidak sepadan sama sekali\nProduk ini sangat mengecewakan. Tidak sepadan dengan harga yang saya bayar.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada fitur istimewa\nSepadan dengan Harga: Overpriced\nSaya sangat kecewa dengan produk ini. Sangat mahal dan tidak ada fitur yang istimewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak berfungsi dengan baik\nSepadan dengan Harga: Mahal\nProduk ini tidak berfungsi dengan baik dan terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat, produk ini sudah rusak saat tiba, dan pelayanan pelanggan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada fitur berguna\nSepadan dengan Harga: Tidak sepadan sama sekali\nSaya sangat menyesal membeli produk ini. Tidak ada fitur berguna dan tidak sepadan dengan harga yang saya bayar.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Sangat buruk\nSepadan dengan Harga: Harga terlalu mahal\nProduk ini sangat buruk. Saya merasa seperti telah membuang uang untuk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada\nSepadan dengan Harga: Mahal\nProduk ini adalah pemborosan uang. Tidak ada fitur yang berguna dan terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat tiba, pengemasan buruk, dan pengiriman sangat lambat. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada fitur yang berarti\nSepadan dengan Harga: Harga terlalu tinggi\nSangat mengecewakan. Produk ini tidak memiliki fitur yang berarti dan harganya terlalu tinggi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada\nSepadan dengan Harga: Terlalu mahal\nSaya merasa sangat menyesal membeli produk ini. Tidak ada fitur dan terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini tidak berfungsi dengan baik, pengiriman sangat lambat, dan pelayanan pelanggan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada fitur istimewa\nSepadan dengan Harga: Harga terlalu tinggi\nSangat mengecewakan. Produk ini tidak memiliki fitur istimewa dan harganya terlalu tinggi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada fitur berguna\nSepadan dengan Harga: Harga terlalu tinggi\nSaya merasa seperti telah membuang uang untuk produk ini. Tidak ada fitur berguna dan harganya terlalu tinggi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat, produk ini rusak saat tiba, dan pelayanan pelanggan buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Fitur Terbaik: Tidak ada\nSepadan dengan Harga: Terlalu mahal\nProduk ini adalah pemborosan uang. Tidak ada fitur dan terlalu mahal.",
        "sentiment": "negatif",
    },
]

Alat_Pemanggang = [
    {
        "comment": "Produk ok barang juga ok, sesuai dengan harga, pengiriman cepat bgttt. Fix langganan ini toko, trimakasihhhh, semoga awettt dengan harga spesial",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: murah meriah, Kualitas: lumayan bagus sesuai harga, Kegunaan: untuk memasak daging dan shabu shabu. Packingan agak nderawasi karena cuma di plastik wrap sama bubble wrap bening aja selapis. Pengiriman cepat dan belum menggunakan karena buat kado. Harga yang lumayan murah si.",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: Standar, Kualitas: Bagus, Kegunaan: Berfungsi dengan baik. Kualitas produk baik, harga lumayan murah, pengiriman cepat, respon penjual baik, thanks ya 😃😃😃",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: harga terjangkau 👍, Kualitas: baik, Kegunaan: buat nyate ayam. Semoga awet barangx bisa di gunakan serbaguna pengiriman cepat👍",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus, Performa: 👍, Kualitas: mudah mudahan awet. Ini bagus loh alhamdulilah lengkap ada penutup, blom dicoba. Mudah mudahan bisa dipake 👍🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: murmer, Kualitas: ok, Kegunaan: untuk gril seafood. Belum di coba, mudah2an bagus dan sesuai serta awettt",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: murah, Kualitas: lumayan, Kegunaan: sangat membantu. Seneng sekali... sangat membantu... wajan nya lumayan gede ya... harga nya murah... penjual nya ramah terimakasih ya kakak lain kali saya order lagi🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏😱🙏🙏🙏🙏🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: sesuai, Kualitas: bagus, Kegunaan: grill & hotpot",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: murah, Kualitas: bagus, Kegunaan: untuk barbeque ala sabuhachi. Pengiriman cepat semoga berfungsi dengan baik. Belum dicoba... Barang aman... packing ok...",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah pas nyampe full set & pas dicoba dicolok ke listrik langsung panas. Cuma masih bingung cara mencucinya aja sih. Semoga seller membantu",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: murah, Kualitas: bagus sekali, Kegunaan: belum dicoba. Semoga semuanya bermanfaat. Makasih seller pengiriman cepat banget. Makasih. Bakal repeat order deh. Packing juga aman banget makasih seller",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: lumayan murah, Kualitas: lumayan bagus, Kegunaan: buat bakar daging. Barang sudah sampai. Pengiriman lumayan cepat. Bisa digunakan untuk malam tahun baru",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: Ok Sesuai Kualitas, Kualitas: Ok, Kegunaan: BBQ. Setelah aku unboxing Barang nya ok banget. Berfungsi dengan baik. Penjual nya ramah. Pengiriman lumayan cepat. Overall ok lah buat rekomendasi 👍👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Walaupun sebetulnya ada yang kurang, yaitu TUTUPNYA ga ikut kekirim sebenernya kecewa banget, tapi alhamdulillah ibuku mau terima aja dan kebetulan ada tutup yg pas.. cuman ga ikut ke foto karena agak ga matching. LAIN KALI DI TELITI LAGI ya kakk. Terima kasih banyak 😄",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: ok, Sepadan dengan Harga: yap. Belum dicoba karena buat kado... packaging semua lengkap. Pengiriman juga cepat. Terima kasih Shopee dan seller...",
        "sentiment": "positif",
    },
    {
        "comment": "Harga: dapet harga flash sale 12:12, Kualitas: lumayan, Kegunaan: belum sempat coba. Lumayan dapet harga flash sale, semoga awet. Terima kasih seller pengiriman cepat.",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Saya benar-benar marah dengan produk ini! Kualitasnya sangat buruk, dan harga yang saya bayar terasa seperti pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengalaman buruk! Produk ini rusak saat tiba, dan pengirimannya sangat lambat. Saya merasa dipermainkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah bencana! Harga yang saya bayar tidak sebanding dengan kualitasnya. Saya merasa seperti pemborosan uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa! Barang ini tidak berfungsi dengan baik dan kualitasnya sangat jelek. Saya tidak akan pernah membeli dari penjual ini lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini adalah sampah! Kualitasnya sangat rendah, dan pengirimannya sangat buruk. Saya benar-benar menyesal membelinya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah pemborosan uang! Produk ini tidak sesuai deskripsi, dan penjualnya sangat tidak responsif. Saya merasa tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya benar-benar frustasi dengan pembelian ini. Produk rusak dan kualitasnya sangat jelek. Pengiriman juga sangat lambat.",
        "sentiment": "negatif",
    },
    {
        "comment": "Jangan pernah membeli produk ini! Harganya terlalu mahal untuk kualitas yang sangat buruk. Saya merasa seperti tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat mengecewakan! Kualitasnya sangat jelek, dan penjualnya tidak responsif. Pengalaman buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya tidak bisa mengerti mengapa orang membeli ini. Kualitasnya sangat rendah, dan harga yang saya bayar terasa sia-sia.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah kegagalan total! Produk rusak saat tiba, dan pengirimannya sangat buruk. Saya benar-benar marah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa seperti ditipu! Harga yang saya bayar tidak sepadan dengan kualitasnya. Produk ini adalah sampah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat marah dengan produk ini. Kualitasnya sangat rendah, dan pengiriman sangat lambat. Saya merasa dipermainkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini adalah salah satu yang terburuk yang pernah saya beli. Kualitasnya sangat jelek, dan harga yang saya bayar terlalu mahal.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat menyesal membeli produk ini. Kualitasnya sangat rendah, dan penjualnya tidak peduli. Pengalaman yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Jangan buang uang Anda pada produk ini. Saya sangat kecewa dengan kualitasnya, dan pengiriman sangat buruk. Saya merasa seperti tertipu.",
        "sentiment": "negatif",
    },
]


product_Bear_Panci_pd = pd.DataFrame(Bear_Panci)
product_Spatula_Set_pd = pd.DataFrame(Spatula_Set)
product_Wajan_16cm_pd = pd.DataFrame(Wajan_16cm)
product_Panci_listrik_0259_pd = pd.DataFrame(Panci_listrik_0259)
product_alat_pemanggang_pd = pd.DataFrame(Alat_Pemanggang)


product_Bear_Panci_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Spatula_Set_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Wajan_16cm_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_Panci_listrik_0259_pd.drop_duplicates(
    subset=["comment"], keep="first", inplace=True
)
product_alat_pemanggang_pd.drop_duplicates(
    subset=["comment"], keep="first", inplace=True
)


print("Value counts Ke-1: ", product_Bear_Panci_pd["sentiment"].value_counts())
print("Value counts Ke-2: ", product_Spatula_Set_pd["sentiment"].value_counts())
print("Value counts Ke-3: ", product_Wajan_16cm_pd["sentiment"].value_counts())
print("Value counts Ke-4: ", product_Panci_listrik_0259_pd["sentiment"].value_counts())
print("Value counts Ke-5: ", product_alat_pemanggang_pd["sentiment"].value_counts())


## Merge

merge_df = pd.concat(
    [
        product_Bear_Panci_pd,
        product_Spatula_Set_pd,
        product_Wajan_16cm_pd,
        product_Panci_listrik_0259_pd,
        product_alat_pemanggang_pd,
    ]
)

positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan positif:", positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_gm.csv", index=False)

print("Data telah disimpan: ", len(merge_df))
