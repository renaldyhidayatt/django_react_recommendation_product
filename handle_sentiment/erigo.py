import pandas as pd

Chino_Pants_erigo = [
    {
        "comment": "Bahan sdkt strecth tebal halus bagus.. jahitan rapi, harga oke.. makasihhh",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: modelnya keren\nWarna: warnanya cerah, bagus\nPacking aman, pengiriman jg cepat, jahitannya rapih , bahannya halus dan nyaman dipakainya, terima kasih semoga tokonya makin ramai👍",
        "sentiment": "positif",
    },
    {
        "comment": "Barang diterima dengan baik dan ga ada yang kurang. Pengiriman termasuk cepat walaupun lagi ada promo payday. Celana nya bagus dan dapet harga murah karena lagi ada discount. Ukuran pas dan warna nya juga ga jauh beda sama difoto. Next mau coba order lagi warna lain dan please sering-sering discount",
        "sentiment": "positif",
    },
    {
        "comment": "Celananya sampai dengan cepat, selamat, dan tampa cacat. Dan kainnyaaa keren nyaman banget dipake, ga ngepresss dan ga kedodoran tp pas di kaki. Dibuat jalan juga ringan dan fleksibel. Mantap dan suka! Thanks seller and shopee!🌟",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus\nWarna: keren\nKualitas produk original dan harganya murah meriah dan kecepatan pengiriman sangat cepat dan respon penjual baik & warnanya keren",
        "sentiment": "positif",
    },
    {
        "comment": "Yesss ... Pesanan ERIGO Chino Pants Ata Olive 38 sudah sampai, best quality, bahan halus istimewa, Original, harga discount Year End Sales, size sesuai, real pic, Recomended Seller, Thank's ERIGO - Thanks SHOPEE... Happy New Year 2021",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya cepet sampai, sesuai dengan yang saya pesan, kualitas nya juga bagus, oke banget, produk kekinian, warna nya juga sesuai dengan yang saya pesan, pakingnya juga rapih banget, tidak ada yang cacat sama sekali, produk bagus harga pas buat kita - kita yg anak kaula muda ini, mantap 👍 pisann....",
        "sentiment": "positif",
    },
    {
        "comment": "Good bagus warn sseseui foto... Enak dipake untuk 85kg tinggi 170 cm cukup pence beli lagi bagus kualitas baik bahan tidak panas, saya suka",
        "sentiment": "positif",
    },
    {
        "comment": "Product Mantap bgt untuk harga yg sangat2 kompetitif Dan ukuran 36 nya pas bgt buat Saya. Bahan juga lumayan utk harga segitu. Bakalan RO nih hehe. Thanks",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah sesuai pesanan, pastinya ori, kualitasnya bagus, ukuran juga pas, nyaman dipakai, pengemasan sangat rapi dan aman, pengiriman standar Buat yg BB ±53 Kg TB ±173 cm pilih ukuran 32, tpi ttp harus diukur dulu, biar celana yg dibeli pas, cara ukur celana banyak di YouTube, tinggal cari aja",
        "sentiment": "positif",
    },
    {
        "comment": "MANTAPPP!! Selalu langganan di erigo, size 38 nya real, panjangnya pas utk tb 180 cm/ bb 80 kg. Bahan tebal, stretch, adem. Packing exclusive label erigo.",
        "sentiment": "positif",
    },
    {
        "comment": "Celananya bagus banget, tebal dan pas ukurannya. Next order. Thanks buat erigo❣️",
        "sentiment": "positif",
    },
    {
        "comment": "Erigo chino pants ata olive uk.28 bahan nya bagus halus tebal, packing nya rapih respon seller baik pengiriman nya juga ok mantap keren J&T.",
        "sentiment": "positif",
    },
    {
        "comment": "Yeaaayy barangnya cepet banget sampe nya , adminya super ramah dan baik bgt , kualitasnya gak mengecewakan , gila produk lokal tp kualitasnya oke bgt , size nya pun pas banget di adek aku , pengirimannya super cepet sehari nyampe , maaciw erigo , bakal repurchase sih 🙏🙏👌👌👌👌❤",
        "sentiment": "positif",
    },
    {
        "comment": "barang sesuai pesanan, dapet harga diskon spesial 3.3, bahan dan cuttingan cakep, semoga suami suka, pengiriman jg cepat. thanks erigo",
        "sentiment": "positif",
    },
    {
        "comment": "Paket sudah diterima. Sesuai pesanan, bagus bgt bahannya🥺 pengemasan dan pengirimannya juga cpt bgt. Gak prnh kecewa sih sama produk erigo👍👍",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Kirain bakal dapat celana yg bagus bgt karena brand Erigo\nBahannya tipis mudah sobek keliatan dibagian pantat udah mulai blubang\nSangat disayangkan harganya lumayan mahal jatohnya klo celananya bahan biasa banget\nMengecewakan",
        "sentiment": "negatif",
    },
    {
        "comment": "PengalaMan pertama beli super duper MENGECEWAKAN‼️ pdhl niat mau koleksi pakai merk ini tp ga jd lah beralih ke merk lain ajaah..\nPengemasan nya jg Luammaaa bangettt..\nYg 1 lg psn emerald malah dikirim hitam 😏\nDeskripsi ukuran penjual dgn real pas dipakai jg ga sesuai kebesaran jauh Rrrrrrrrgh 😓",
        "sentiment": "negatif",
    },
    {
        "comment": "Beli produk dengan ukuran sama tapi ukurannya beda jauh, chat penjual ribet banget suruh ngukur dulu dll, nggak semua orang punya meteran \nbaju ya kaka 😁 intinya nggak sesuai",
        "sentiment": "negatif",
    },
    {
        "comment": "Warna yg di kirim berbeda warnanya seperti warna army..  Tidak seperti di foto",
        "sentiment": "negatif",
    },
    {
        "comment": "Warna ga sesuai gambar, ukuran juga agak sedikit kecil, padahal ini pemesanan ke dua, yg pertama bagus yg kedua sedikit mengecewakan",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman lambat mungkin karena banyak pengirimian dan setelah datang ukuran 28 sangat kecil. Celananya kekecilan dan sangat mubajir karena tidak terpakai.\nSaran saya yg ukuran 28 lebih baik pilih ukuran 30🙏",
        "sentiment": "negatif",
    },
    {
        "comment": "barangnya baguus original,tapi warnanya tidak sesuai pesanan udah itu aja shh\nPengiriman cepatt sampai👌",
        "sentiment": "negatif",
    },
    {
        "comment": "Mall ko yang kaya gini di jual, mencong sebelah ga ngerti .\ntukang jahitnya ngantuk apa gmna ampe salah motong,",
        "sentiment": "negatif",
    },
    {
        "comment": "Pesan warna olive dikirim coklat, order 2x ini ini yg mengecewakan tidak sesuai pesanan, sekelas Shopee mall harus nya jaga kepercayaan pembeli 😊",
        "sentiment": "negatif",
    },
    {
        "comment": "Baru 1x cuci berbarengan chino lain.masa ini Warna dari lutut ke bawah langsung pudar",
        "sentiment": "negatif",
    },
    {
        "comment": "Atau olive? Yg dikirim coklat LOL\nKlo ga ada barangnya ya jngan kirim barang yg lain, contohnya ini dikasih coklat muda gtu warnanya\nMinta pembatalan pesanan krna salah alamat juga sulit d toko ini_-",
        "sentiment": "negatif",
    },
    {
        "comment": "Jujur cuttingnya gk nyaman bngt, apalg bagian selangkangan.. Biasa ane pke size 29, ini mesen size 30 msh ngatung.. Wajarlah murah tp hrga segitu di online msh bnyak yg lebih bgus kok..  Kalo bahan sih bgus..",
        "sentiment": "negatif",
    },
    {
        "comment": "Warna celana kenapa beda dengan gambar warna asli yg diterima sangat berbeda.  Digambar lebih cerah, pas ditrma jadi beda banget.\nDan tidak ada tanda strip dibawah celananya. \nPadahal baru pertama coba brand erigo.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ata olive katanyam di picture erigo kaya yang ijo army datang kaya coklat kayu. Mana ukuran kekecilan lagi haduhhh gajado meeting pake barang ergio",
        "sentiment": "negatif",
    },
    {
        "comment": "Warna produk ga sesuai sama yg dikirim. Difoto terang pas sampe jd warna abu abu hijau",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman LAMA, pas barang diterima malah WARNA SALAH, minta yg mocca dikirim yang hijau",
        "sentiment": "negatif",
    },
]

print("Chino Pants: ", len(Chino_Pants_erigo))

product_chino_pd = pd.DataFrame(Chino_Pants_erigo)

Positif_count_chino = (product_chino_pd["sentiment"] == "positif").sum()
negatif_count_chino = (product_chino_pd["sentiment"] == "negatif").sum()


print("Jumlah ulasan Positif Chino:", Positif_count_chino)
print("Jumlah ulasan negatif Chino:", negatif_count_chino)


Jacket_Fujinkai = [
    {
        "comment": "Pesanan sudah diterima, proses pengemasan serta pengiriman barang tergolong cepat, Barang datang dalam kondisi baik, Untuk orang dgn BB.62 & TB.170, ukuran M udah sangat PAS.. Pokoknya ini rekomended Seller..👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Sumpah bagus bangetttt, gak tebel banget gak tipis banget. Intinya sesuai harga lah, barang cepet sampe, CO hari Jumat dateng hari minggu, sablon nya juga bagus banget, bagus banget intinya gak boong aaaaa><",
        "sentiment": "positif",
    },
    {
        "comment": "Jujur agak kecewa sama pengemasannya karena ternyata hari libur ngga diproses. Tapi itu semua ketutup sama barang yang didapetin! Pengemasannya, produk dan jahitannya super rapih! Real pict, color dll, ngga ada bekas jahitan nyisa atau lainnya. First impressions gue lgsg pesen 4 pcs dari 700rb>645rb",
        "sentiment": "positif",
    },
    {
        "comment": "Bahannya seperti jaket Boomber pada umumnya, Desainnya & Modelnya yg bagus, Size L buat kado 🙏, Recommended Seller",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: Keren + Stylish, Warna: Dark Grey, Bagus banget ini woyy, dapet harga flashsale plus ada voucher belanja jadi miring banget harganya kek ini gak sesuai soalnya barangnya bagus dengan murah banget. Ukurannya pas sih buat badan aku yang 172 cm + 74 Kg",
        "sentiment": "positif",
    },
    {
        "comment": "Ada empat kantong, model seperti kemeja. bahan sablon oke. gak tipis tapi gak tebel. ukuran juga pas😁 gak ada cacat juga, puas banget🤍",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk sangat baik. Produk original. Harga produk sangat baik. Kecepatan pengiriman sangat baik. Respon penjual sangat baik. Packing aman.",
        "sentiment": "positif",
    },
    {
        "comment": "Nggk pernah kecewa beli ERIGO. Selalu puas. Packingnya oke, pengirimannya cepet. Bahannya juga bagus banget, halus juga, nyaman juga pas dipakai. The best lah pokoknya.",
        "sentiment": "positif",
    },
    {
        "comment": "Penanganan cepat, pengiriman juga cepat, jaketnya bagus banget, modis, kekinian, nyaman di pakek, anak saya suka banget....👍👍👍👍👍 Bs buat langganan.....siippp......thanks seller...",
        "sentiment": "positif",
    },
    {
        "comment": "Kenyamanan: bagus Saran Tampilan: bagus Kualitas: bagus bahan nya Makasih ka pesanan nya udh smpe bahan nya bagus walaupun lumayan gede juga dia aku next bakal order yg model lain lagi 🤗🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah barang sampe, pengemasannya oke, bahan jaketnya bagus dalemnya juga bagus, top deh",
        "sentiment": "positif",
    },
    {
        "comment": "Bb 49 tinggi 156 ukuran S sesuai di aku, recomend buat naik motor bahan e enak Trmksih luv bgt sma erigo.",
        "sentiment": "positif",
    },
    {
        "comment": "Cepat untuk pengiriman nya, bagusss bangett model nya, sy suka sekali, mungkin sebulan sekali order kali yaa hehehe, mantap abisssss pokoknya, recomended sekali.",
        "sentiment": "positif",
    },
    {
        "comment": "Kereeeeeennnn.... Pengiriman cepat Kualitas ok Semoga awet terimakasih seller shopee dan si cepat sukses selalu 🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sampai dengan selamat, bahannya bagus, adem, sampenya cepet banget pesen kemarin malem, malem ini udah sampee good job thankyoouu",
        "sentiment": "positif",
    },
    {
        "comment": "Produknya baguss, alhamdulillah barang pembelian ke 2 kalinya ditokoh ini bagus (yg kedua ini temen saya nitip karena rekomen saya hehehe) terima kasih adminnya jg fast respon dan baik 😊🙏. Pengiriman juga fast banget",
        "sentiment": "positif",
    },
    {
        "comment": "Barang nya udh nyampe mantap bangett. Maaf aku kasih 3 bintang, soalnya pengiriman nya lama bngett :( klo barang nya mh bagusss pisan aslina...",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yg datang sesuai pesanan, cuman ada s edikit cacat, untuk perhatian kedepanya. Biar lebih menyeluruh ngeceknya. Kancingya ada yg copot satu. Untk ukuran pas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Untuk yang mau beli Kekurangan nya kantong 4 buah gak aman buat taro hp, andai di perbesar lagi kantong nya, dan diberi kantong tambahan di dalem Untuk bahan dan kwalitas bagus, dipake untuk berkendara walau tipis gak tembus angin",
        "sentiment": "negatif",
    },
    {
        "comment": "bahannya bagus sesuai dg gambar tapi kancing sakunya lepass 1,kecewa sih tapi gpp cuma 1",
        "sentiment": "negatif",
    },
    {
        "comment": "Kancing nya rusak 1, ternyata ukuran M kebesaran untuk wanita tinggi 160 cm",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang bagus original Cuma pengirim kurang teliti mengecek sebelum mengirim Ada bolong di saku bawah Mau refund / tuker ribet Jadi saya jahit aja di permaks",
        "sentiment": "negatif",
    },
    {
        "comment": "Maaf kecewa sih barang kancingnya ilang 1 pas datang, minta ajuin pembatalan pesanan ingin mengganti model jaket padahal belum dikemas tapi ga diterima. Respond penjual juga lama. Semoga kedepannya lebih baik lagi dalam mengirim produk, terimakasih",
        "sentiment": "negatif",
    },
    {
        "comment": "Warna: grey kali ini mengecewakan banget, coach erigo ny kaya bekas gru,kaya barang returan,kancing ny karatan,name tag label ga ada,jahitan nya ga rapi",
        "sentiment": "negatif",
    },
    {
        "comment": "Jangan sampai pembeli seperti saya , saya tidak menerima produk dari erigo sebanyak 3 item , hodiie,sweter,coach jaket , saya sudah kecewa sebagai pelanggan terima kasih......!!!!!!",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lama dan bikin kapok, semoga erigo berbenah dari sisi pengiriman barang nya agar lebih cepat. Penilaian kurang baik karena layanan jasa kirim.",
        "sentiment": "negatif",
    },
    {
        "comment": "Baru dateng tapi kancingnya udah copot, maaf ya kak bintang 2 dulu",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini adalah sampah terbesar yang pernah saya beli! Tidak hanya rusak, tetapi juga bau busuk. Saya sangat kecewa!",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak ada kata yang cukup buruk untuk mendeskripsikan produk ini. Semua rusak dan tidak berguna. Uang saya terbuang sia-sia!",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat-sangat lambat. Saya menunggu berhari-hari tanpa hasil. Saya benar-benar marah!",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah barang palsu! Gambar online sangat menipu. Saya merasa seperti ditipu!",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini adalah sampah! Tidak ada kualitas, dan penjualnya sangat tidak profesional. Saya tidak akan pernah membeli dari mereka lagi!",
        "sentiment": "negatif",
    },
]

print("Jacket Fujinkai: ", len(Jacket_Fujinkai))

product_fujinkai_pd = pd.DataFrame(Jacket_Fujinkai)

Positif_count_fujinkai = (product_fujinkai_pd["sentiment"] == "positif").sum()
negatif_count_fujinkai = (product_fujinkai_pd["sentiment"] == "negatif").sum()


print("Jumlah ulasan Positif Kuina:", Positif_count_fujinkai)
print("Jumlah ulasan negatif Kuina:", negatif_count_fujinkai)

Kuina_Navy_Unisex = [
    {
        "comment": "Packing cepat, rapi dan aman. Pengiriman cepat dan sesuai. Produk original, warna dan ukuran sesuai. Kualitas produk sangat baik. Harga produk sangat baik. Respone penjual sangat baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas baik. Sepadan dengan Harga: sepadan. Kenyamanan: nyaman. Dpt harga 21k kaos erigo lumayan kan 😅 Kain halus dan dingin tapi ukurannya besar ya ternyata gak papalah buay pk su Terimakasih",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus. Warna: navi. Paket saya sudah sampai trimakasih, bagus sablonan juga bagus tapi bahan nya beda sama yang pertama beli, gak papa bagus ko adem bahan nya gak tebal gak tipis",
        "sentiment": "positif",
    },
    {
        "comment": "Soal packing udah pasti bagus 👍 selebihnya bagus banget. Udh sering beli baju buat suami atau ade disini. Krna bahannya emang sebagus itu, harga nya worth it banget ✌️🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Bahan adem, sablonan bagus, jahitannya rapi, sesuai ekspektasi",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah ini ke dua kali pesan, produk ori packing oke, sampenya juga cepat",
        "sentiment": "positif",
    },
    {
        "comment": "Antusias untuk beli produk dalam negri yang sudah mendunia. Mau tahu sih klo harga lagi gak diskon kira-kira bahan nya sama gak kayak gini. Beb... Untuk harga diskon 50 ribu sesuai lah bahan dan sablonan nya.",
        "sentiment": "positif",
    },
    {
        "comment": "Paketnya udah sampe. Pesenin cowokku baju erigo mumpung lagi diskon. Murah banget gillsss... Bajunya juga bagus bahannya adem ada free gift nya juga lohhh.. Pengiriman cepat banget gapake lama.. Thankss erigo official....",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulilah paket nya udah sampai. Makasih ga kecewa dech beli produk erigo bahan nya pun adem.. Makasih juga abang kurir nya yang baik sopan lg nex aq order lg dech",
        "sentiment": "positif",
    },
    {
        "comment": "Warna: navy. Tampilan: bagus. Packing aman, barang dikirim sesuai pesanan, sablonan bagus, pas dapet harga diskon dan gambar yang dipengenin.",
        "sentiment": "positif",
    },
    {
        "comment": "Mantep banget, Kualitas Bagus, adem juga, Auto langganan sih, packing aman, pengiriman cepat banget, Cintailah produk Indonesia",
        "sentiment": "positif",
    },
    {
        "comment": "bahannya tebal, sangat di anjurkan sekali dan sablonnya sangat menarik, terima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Dapet harga murah flash sale 50 ribu/each, pengiriman seminggu karna lebaran, good, gaada yang rusak all good, mantep. Bahan bagus adem.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: sesuai. Warna: navy. Sesuai dengan foto, dapet harga sale suka deh, bahannya adem juga.",
        "sentiment": "positif",
    },
    {
        "comment": "Walaupun cod tetap cepat pengirimannya, kualitas nya bagus, dan harga segini terbilang worth it lahh.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: cakep. Warna: navy. Barang nya bagus sesuai dengan pesanan, pengiriman cepat.",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Tampilan: Udah pernah beli sebelumnya dengan ukuran yang sama (XXL) tapi orderan sekarang kaosnya kaya LD ukuran XL. Di tag bener ukuran XXL tapi kenapa LD nya cuma 56. Klo emang selisih karna jaitan harusnya ngga sampe 2 cm. Rada kecewa si soalnya sebelumnya udah pernah beli disini tapi aman aja ukurannya sesuai deskripsi. Tapi pas order yang ini jujur rada mengecewakan udah gtu ada noda dibagian atasnya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Bahan nya bagus. Lembut. Ademnyaman d pakai nggak gerah👍👍👍👍👍👍👍👍",
        "sentiment": "negatif",
    },
    {
        "comment": "Cukup puas sih cuma kecewa nya pelayanan nya yang kurang. Order pertama di kirim paling akhir. Kenapa gak di barengin aja. Kam alamat tujuan sama. Pertama beli ud kecewa. Kalo kurir udh langganan jadi udh paham..",
        "sentiment": "negatif",
    },
    {
        "comment": "Bahan yang ke-4 lebih tipis, kenapa sekarang kualitas bahannya tipis ya Erigo.",
        "sentiment": "negatif",
    },
    {
        "comment": "Baru kali ini beli disini tidak dapat stiker, padahal beli 4 pc dan sering beli disini.",
        "sentiment": "negatif",
    },
    {"comment": "Kok sekarang makin kesini bahannya tipis.", "sentiment": "negatif"},
    {
        "comment": "Pengiriman sangat lambat dan sangat mengecewakan. Barang yang saya terima cacat dan rusak parah. Sangat kecewa dengan layanan ini!",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk yang saya beli tidak sesuai dengan gambar dan deskripsi. Ini adalah pemborosan uang. Sangat marah!",
        "sentiment": "negatif",
    },
    {
        "comment": "Pelayanan pelanggan buruk sekali. Saya mengirim beberapa pesan dan tidak pernah mendapatkan balasan. Ini adalah pengalaman yang sangat buruk!",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang yang saya terima sangat kualitas rendah. Terlihat seperti barang palsu. Saya merasa tertipu!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya menunggu pengiriman selama berbulan-bulan dan barangnya akhirnya datang rusak. Ini adalah pengalaman yang sangat frustasi!",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk terlalu mahal untuk kualitas yang buruk. Saya merasa seperti saya dibohongi. Tidak akan membeli lagi!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya telah berbelanja di sini beberapa kali dan setiap kali pengiriman sangat lambat. Ini adalah kecewa yang berulang kali!",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk semakin menurun dari waktu ke waktu. Saya sangat kecewa dan tidak akan membeli lagi!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya mencoba untuk menghubungi layanan pelanggan tetapi tidak pernah mendapatkan tanggapan. Ini adalah pelayanan pelanggan yang sangat buruk!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat marah dan kecewa dengan produk ini. Barang yang saya terima sangat jauh dari harapan. Tidak akan merekomendasikan kepada siapa pun!",
        "sentiment": "negatif",
    },
]

print("Kuina: ", len(Kuina_Navy_Unisex))


product_kuina_pd = pd.DataFrame(Kuina_Navy_Unisex)

Positif_count_kuina = (product_kuina_pd["sentiment"] == "positif").sum()
negatif_count_kuina = (product_kuina_pd["sentiment"] == "negatif").sum()


print("Jumlah ulasan Positif Kuina:", Positif_count_kuina)
print("Jumlah ulasan negatif Kuina:", negatif_count_kuina)


Emerald_Chino = [
    {
        "comment": "Istimewa, Order Erigo Chino Pants Beryl Emerald Variasi 40 sudah sampai, best quality, bahan terbaik & lembut, Original, harga discount, size international, Recomended Seller - Thanks ERIGO. Thanks SHOPEE.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang nya bagus banget saya suka, jadi pengen pesen lagi jadi nya barang nya tidak mengecewakan, super bagus.. kurir nya juga ramah, sukses terus buat toko nya..",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih kak celananya sudah mendarat dengan selamat.. Pengiriman cepat, Kualitas barang sangat bagus. Terima kasih sukses selalu👍🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Allhamdulillah barang udh sampe terimakasih erigo cepat pengirimannya dan sumpah celananya bagus bgt pas bgt disaya saya suka bgt top bgt dah..untuk kedepannya saya akan pesan terus dgn warna yg berbeda terima kasih erigo store👍👍🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Produk sesuai dengan gambar warna dan ukuran nya pas, terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Kecepatan pengiriman nya cepat, bahanya juga Oke lembut, slim fit nya jg nggak nggepress. Mantaplah pokoknya 🔥🔥🔥",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas celana bagus dan rapih jahitan nya, Harga terjangkau untuk kualitas yang baik, Pengiriman cepat, Erigo memang terbaik, saya selalu suka product lokal dengan kualitas dan model yang di design oleh erigo, Terima Kasih ERIGO APPAREL",
        "sentiment": "positif",
    },
    {
        "comment": "Celana nya bagus banget, sumpah ini bahan lembut dan agak ngaret loh jadi ga press bgt. Warnanya sesuai pict. Ini suami aku pake yang size 36 BB dia 90kg tinggi 175cm dan masih termasuk muat ya mskipun agak press, cuma karena bahannya Alus dan melar jadi enak aja tuh. Next beli yang 38, thanks seller 🥰🤍🙏",
        "sentiment": "positif",
    },
    {
        "comment": "Pengemasan dari toko cepat, packing rapi & aman.. Pengiriman dari expedisi cepat. Kualitas barang oke punya. Nyaman bahannya. Terimakasih seller",
        "sentiment": "positif",
    },
    {
        "comment": "Erigo selalu terbaik, sudah order yang kesekian kali, Suka bgt sama model nya, Harga terjangkau, Bahan nya tebal, lembut dan tidak panas, Nyaman dipakainya, Terima Kasih ERIGO",
        "sentiment": "positif",
    },
    {
        "comment": "Barang telah dikirim dan telah diterima dengan keadaan baik dan rapi. Tidak ada terjadi kerusakan sebelum pemakaian dan sesudah pemakaian. Pengiriman juga cepat. Semoga awet",
        "sentiment": "positif",
    },
    {
        "comment": "Mantap banget bahannya ga kecewa warna cocok yang sesuai diingink",
        "sentiment": "positif",
    },
    {
        "comment": "Overall bagus sih, cuma belum tau ini nanti bakalan berbulu setelah beberapa kali pemakaian atau engga, kalau engga bakalan beli lagi. Terus bahannya gak kaku dan kasar jadi nyaman di kulit.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus banget celananya, bahan oke, pengiriman okee, packing okee 😍 Semoga menjadi langganan di toko ini 🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Mantappp bosss.. Bahannya halus, tebel, melar. Pengiriman lumayan cpet pdhal udh bentar lagi mau lebaran yaa, alhamdulillah cpet mendarat. Thx Erigooo",
        "sentiment": "positif",
    },
    {
        "comment": "Minta ukuran 28 dikirim 38 mau di retur repot banget. Padahal udah minta ukuran 28 di chat dan di catatan. Niatnya mau di retur tapi kok yah ribet banget permintaan dari toko mesti foto ini itu. Tolong lebih teliti lagi jika ingin kirim barang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Bahannya ndak sesuai yg saya harapkan... tipis, dan dugaan saya luntur... jahitanya buagus... kecewa dibahan, tpi mungkin sesuai dengan harga yaa... hmmm... tingkatkan dikwalitas bahan kak, jahitan sudah okey... 🙏",
        "sentiment": "negatif",
    },
    {
        "comment": "Beli celana sama kaos tapi, celana kekecilan dan kaos kegedean. Ukurannya ga sesuai diskripsi pada tabel size kl di ukur. Kecewa, ditambah lagi pengiriman lambat tidak langsung di proses.",
        "sentiment": "negatif",
    },
    {
        "comment": "Celana kekecilan tidak bisa direktur. Padahal cuman minta tuker size bukan minta duit. Sudah di chat tapi tidak ada respon. Tidak seperti toko yang lain 👎",
        "sentiment": "negatif",
    },
    {
        "comment": "Bahannya sama kayak yang harga 80an kurang rekomended sih kalo menurut aku, ya tapi mau gimana lagi udah saya cancel tapi penjualnya gak mau di cancel upps",
        "sentiment": "negatif",
    },
    {
        "comment": "Ukuran celana yang dikirimkan saya sudah benar, tapi begitu diukur ternyata melewati batas toleransi. alias kegedean jauh.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa karena saya ambil baju ukuran L tapi yang dikirim ukuran XL-_",
        "sentiment": "negatif",
    },
    {
        "comment": "Di karenakan tidak bisa dibatalkan padahal saya salah order tetap saja diproses, mohon pelayanannya yang benar.",
        "sentiment": "negatif",
    },
    {
        "comment": "Terlalu kepanjangan untuk ukuran tinggi pria Indonesia yang rata-rata tinggi badannya 170cm",
        "sentiment": "negatif",
    },
    {"comment": "Jahitannya ga rapih", "sentiment": "negatif"},
    {
        "comment": "Pesan celana dikirimnya kemeja kotak-kotak padahal lagi dibutuhkan banget celananya 😤",
        "sentiment": "negatif",
    },
    {
        "comment": "Sudah beli 3 produk sebelumnya warna navy, cream, dan dark grey. Ukuran semua celana 32 sangat bagus dari bahan dan kualitas. Namun, pesanan terakhir sangat berbeda dari bahan, ukuran, dan kualitas. Kecewa karena ukuran dan bahan berbeda. Tunggu perbaikannya. Terima kasih.",
        "sentiment": "negatif",
    },
    {"comment": "Kualitas produk baik.", "sentiment": "positif"},
    {"comment": "Beda sama yang saya beli kemarin.", "sentiment": "negatif"},
    {"comment": "Respon seller nya jelek.", "sentiment": "negatif"},
    {"comment": "Celana terlalu ketat banget.", "sentiment": "negatif"},
    {"comment": "Warna yang dikirim berbeda.", "sentiment": "negatif"},
]

print("Kuina: ", len(Emerald_Chino))


product_Emerald_pd = pd.DataFrame(Emerald_Chino)

Positif_count_emerald = (product_Emerald_pd["sentiment"] == "positif").sum()
negatif_count_emerald = (product_Emerald_pd["sentiment"] == "negatif").sum()


print("Jumlah ulasan Positif Emerald:", Positif_count_emerald)
print("Jumlah ulasan negatif Emerald:", negatif_count_emerald)


Jogger_Erigo = [
    {
        "comment": "Alhamdulillah akhirnya jogger yang warna hitam restock. Puas banget dengan pelayanan Erigo. Adminnya ramah, pengirimannya cepat meskipun beda pulau. Produk-produknya juga the best. Sukses terus untuk Erigo 👍",
        "sentiment": "positif",
    },
    {
        "comment": "Barangnya bagus, pengirimannya lumayan cepat. Erigo memang sudah gak perlu diragukan lagi. Recommended!",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah pas dengan size 32. Potongan slim membuatnya pas dan bahan bagus. Mungkin akan beli lagi untuk ukuran yang lebih besar. Monggo diborong.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah diterima sesuai deskripsi, bahan lembut, dan pas dipakai. Terima kasih seller, ditunggu diskon berikutnya.",
        "sentiment": "positif",
    },
    {
        "comment": "Pembelian ke-3 selalu sesuai dengan deskripsi. Pengemasan baik dan pengiriman cepat. Semoga muat karena dibeli untuk adik sepupu. Terima kasih Erigo.",
        "sentiment": "positif",
    },
    {
        "comment": "Mantaplah pokoknya, pas banget dan bahan lumayan sesuai dengan harganya. Good!",
        "sentiment": "positif",
    },
    {
        "comment": "Yuhuu~ pesanan jogger Erigo yang kesekian kali datang dengan aman. Paling pas ukuran, harga, dan tentu kualitasnya. Biasanya pakai ukuran 36, tapi rada pas di paha jadi beli yang ukuran 38. Tapi pinggangnya besar banget, sudah ditarik dan diikat tali tetap kedodoran. Tapi yang penting nyaman. InsyaAllah akan jadi langganan terus.",
        "sentiment": "positif",
    },
    {
        "comment": "Celana pas dan nyaman dipakai anak saya, size dan ukuran juga pas. Suka kata anak saya. 👍👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Recommended seller dan barangnya bagus, harganya terjangkau. Semoga awet dan cocok sekali untuk BB 57 TB 158 dengan ukuran 30, nyaman dan stretch.",
        "sentiment": "positif",
    },
    {
        "comment": "Enak dipakai celananya, bahannya gak panas, gak kusut, lembut, ngepas banget, harga flash sale jadi murah banget. Terimakasih ya.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan bagus, warna bagus, ukuran pas tapi di lingkar pinggang agak kebesaran. Tapi gak masalah.",
        "sentiment": "positif",
    },
    {
        "comment": "Belanja kedua x nyh produk Ori kualitas bagus. Pengemasan pengiriman super cepat, packing rapih aman. Terimakasih seller... Gak lupa buat kurir terimakasih juga mau mengantar ke alamat rumah walaupun toko masih tutup.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bagus stylish, warna: black 32. Bahannya enak, bagus, gak terlalu tebal, ringan lagi. Dengan harga segini dan bahan bagus, gak mengecewakan. Packing rapih dan pengiriman cepat.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: pas di badan, warna: hitam. Ukuran 170/80 pas di kaki dan badan. Neks beli lagi.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah sampai, real pict ya cuma pengirimannya agak terlambat, it's ok lah.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas barang bagus. Ini sudah pesan yang kedua kalinya. Nyaman dipakai, resellernya ramah, pengiriman juga cepat sampai. Makasih Erigo.",
        "sentiment": "positif",
    },
    {
        "comment": "Tampilan: bahannya jelek, tipis, bahan kasar\nWarna: warna hitam\nHarga branded tp kualitas kaki lima",
        "sentiment": "negatif",
    },
    {
        "comment": "Pas ke 3x beli yg warna item ini gua pilih nomer 30, dan bener di tag celananya no.30, tapi ukurannya kayak no 32. Bahkan gua samain dengan celana sebelumnya, perbedaanya beberapa CM jauh banget kyak beda size jatohnya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya gk tau hrs komentar apa.. saya cm bingung dgn deskripsi yg tidak sesuai dgn brg, saya beli ukuran 30 = 38cm lingkar pinggang nya. tanya penjual, tp dijawab, ada tim yg akan membantu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Jadi pesennya size 40…pas dibuka langsung copot tagnya krn tulisan sizenya 40 terus dicoba kekecilan setelah dilihat ternyata size nya 34 di celananya…dichat adminnya no response…maaf yaah aku kasih penilaian jelek",
        "sentiment": "negatif",
    },
    {
        "comment": "Jelek kualitas produknya :( sengaja milih beli erigo kirain ntr datangnya bagus. Tau gitu beli merk lain. Celana nya ngepas banget kaya make leging. Kecewa deh sama produk celananya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas: Bahan tipis tidak kayak dulu beli joger di awal yang bahannya tebal, kantongnya juga kain tebal. Yang sekarang bahan model kain nya jelek kasar dan tipis. Karet nya juga sangat melar dan tidak kencang.",
        "sentiment": "negatif",
    },
    {
        "comment": "agak kecewa sih, celana baru aja datang udh sobek dibagian betis nya, padahal sebelumnya saya beli chino disini celana nya bagus bngt mungkin bisa diperbaiki lagi untuk finishing nya",
        "sentiment": "negatif",
    },
    {
        "comment": "Untuk harga segini not worth it, bahan kyk distro pinggir jalan harga 75rb.. di jadikan pengalaman saja ya",
        "sentiment": "negatif",
    },
    {
        "comment": "Kurang bagus dan luntur, ukuran sesuai,waktu pembelian harga 142k sekarang 98k",
        "sentiment": "negatif",
    },
    {
        "comment": "Beli yang kedua kalinya... pertama beli ukuran 32 nya pas.. trus pas beli ke dua ukuran 32 nya besar...dan kainnya agak beda.. pertama yg warna biru navi agak lembut...yg kedua warna hitam agak kasar kain nya...",
        "sentiment": "negatif",
    },
    {
        "comment": "34nya kecil banget, saya bisa pake ukuran 34 gk muat, ade saya coba malah pas di dia yang ukuran 32, tolong di perbaiki customer servicenya saya chat tidak ada tanggapan",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: untuk ukuran 34 ini kekecilan, jadi kaya leging kayaknya bukan product asli deh, Tidak worth it ukurannya tidak standart kekecilan padahal 34 ukurannya",
        "sentiment": "negatif",
    },
    {
        "comment": "Tampilan: jelek, pas dipakai tidak nyaman Warna: warna burik, pudar. Jadiin keset aja kalo bisa. Celana apaan ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pesen tgl 5 dikirim tgl 9 . Lapor shope baru dikirim kecewa. Udah minta batal ga di acc",
        "sentiment": "negatif",
    },
    {
        "comment": "Tolong dong erigo respon nya .. saya chat engga ada di respon ..",
        "sentiment": "negatif",
    },
    {
        "comment": "Udh beli ke 5 kali y bagus semua tapi yg warna item ini kurang puas bagett",
        "sentiment": "negatif",
    },
]

print("Jogger: ", len(Jogger_Erigo))


product_Jogger_pd = pd.DataFrame(Jogger_Erigo)

Positif_count_jogger = (product_Jogger_pd["sentiment"] == "positif").sum()
negatif_count_jogger = (product_Jogger_pd["sentiment"] == "negatif").sum()


print("Jumlah ulasan Positif Emerald:", Positif_count_jogger)
print("Jumlah ulasan negatif Emerald:", negatif_count_jogger)


merge_df = pd.concat(
    [
        product_chino_pd,
        product_fujinkai_pd,
        product_kuina_pd,
        product_Emerald_pd,
        product_Jogger_pd,
    ]
)


Positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan Positif:", Positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_erigo.csv", index=False)

print("Data telah disimpan")
