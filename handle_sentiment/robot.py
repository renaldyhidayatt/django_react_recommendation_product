import pandas as pd


Mousepad_product = [
    {
        "comment": "Barang sesuai orderan. Kualitas produk bagus. Baru pertama order disini. Barang belum dicoba. Harga murah. Semoga awet. Packingan safety. Pengiriman cepat. Terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah paket sudah mendarat dengan selamat sesuai pesanan. Thanks buat Seller dan Shopee juga om Kurir tentunya. Sukses untuk kita semua Aamiin.",
        "sentiment": "positif",
    },
    {
        "comment": "bagus juga, sekalian beli mouse pad nya karena ijo ijo makanya aku beli ini terimakasih aku beli yang ukuran medium.",
        "sentiment": "positif",
    },
    {
        "comment": "Ukuran pas untuk dibawa kemana mana, bahan tidak licin.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah produk sampai dengan selamat, packing aman dan pasti berkualitas. Klo ada rejeki pasti bkal order lagi.",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepat 1 hari langsung Sampai respon penjual juga baik dan ramah. Packing aman dan rapi. Bahannya juga tebal. Semoga terus amanah dan semakin berkah.",
        "sentiment": "positif",
    },
    {
        "comment": "Respon penjual cepat dan ramah, pengemasan rapi, dan produk sesuai dengan pesanan. Terima kasih ya...",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman cepet, pengemasan juga aman. Terbaiklah robot, seharusnya beli yang ukuran S, lumayan agak besar sih kalo buat dibawa kemana mana hehe.",
        "sentiment": "positif",
    },
    {
        "comment": "Produknya bagus dan berfungsi dengan baik, harga worth it, pengiriman super cepat, sellernya fast respon.",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah adminnya ramah + pengiriman cepat + kurir ramah + barang sampai dalam kondisi baik. Lumayan worth it kok buat harga diskon dari Rp38.000 jadi Rp12.000 an. Terima kasih yaa ROBOT sudah amanah. Semoga selalu diberikan kesehatan + selalu amanah + berkah, aamiin.",
        "sentiment": "positif",
    },
    {"comment": "Suka bgt. Gak licin lg.", "sentiment": "positif"},
    {
        "comment": "Kualitasnya mantap dengan harga yg sangat terjangkau. Tampilannya juga keren. Makasih Seller.",
        "sentiment": "positif",
    },
    {"comment": "Anti slip. Minimalis. Kualitas OK. Thanks", "sentiment": "positif"},
    {
        "comment": "Alhamdulillah pengiriman cepat dan sesuai dengan gambar dan dipromosikan bagus semoga bertahan lama dan bagus dioperasikan lancar terus. Aamiin allahumma amin",
        "sentiment": "positif",
    },
    {"comment": "Bagus... bahannya juga tebal, Mantap👍", "sentiment": "positif"},
    {
        "comment": "Sangat puas dengan barang yang dikirim, lengkap sesuai pesanan dan sangat keren menurut saya. Jangan ragu membeli produk di toko ini sangat direkomendasikan 👍🏻👍🏻",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Barang yang dikirim sangat buruk, rusak, dan tidak sesuai dengan pesanan. Kualitas produk sangat jelek, dan pengemasan tidak aman. Saya sangat kecewa dengan pelayanan ini!",
        "sentiment": "negatif",
    },
    {
        "comment": "Paket saya hilang dan penjual tidak memberikan respon sama sekali. Ini adalah pengalaman paling buruk yang pernah saya alami. Saya tidak akan pernah membeli dari penjual ini lagi!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya memesan ukuran M, tetapi yang dikirim adalah ukuran S. Ini sungguh menjengkelkan! Penjual sangat tidak profesional dan tidak bisa diandalkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Barang ini hancur begitu saya membukanya. Saya merasa telah membuang uang saya. Saya tidak merekomendasikan produk ini kepada siapa pun!",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan barang yang saya terima dalam keadaan rusak. Saya merasa sangat marah dan kecewa. Ini adalah pemborosan uang!",
        "sentiment": "negatif",
    },
    {
        "comment": "Penjual ini sangat tidak responsif. Saya telah mencoba menghubungi mereka berkali-kali tanpa jawaban. Pelayanan pelanggan buruk sekali!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa ditipu dengan harga produk ini. Kualitas sangat buruk dan tidak sepadan dengan harganya. Jangan pernah membeli dari penjual ini!",
        "sentiment": "negatif",
    },
    {
        "comment": "Ukuran produk tidak konsisten. Saya memesan yang sama sebelumnya dan ukurannya berbeda kali ini. Saya sangat marah!",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat mengecewakan. Tidak sepadan dengan harganya. Saya sangat menyesal membeli ini. Tidak direkomendasikan!",
        "sentiment": "negatif",
    },
    {
        "comment": "Packing sangat buruk. Saya menerima produk dalam keadaan rusak dan penjual tidak memberikan solusi. Ini adalah pengalaman yang sangat buruk!",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah penipuan besar! Saya membayar banyak uang untuk produk ini, tetapi yang saya terima adalah barang palsu yang sangat buruk. Penjual harus ditindak tegas!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat marah dengan pengiriman yang terlalu lambat. Saya memesan ini untuk acara khusus dan barangnya belum tiba. Ini sangat mengganggu!",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan kualitas produk. Tidak sebanding dengan harga yang saya bayar. Ini adalah pemborosan uang!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya memesan barang ini dengan harapan tinggi, tetapi kenyataannya sangat mengecewakan. Kualitas produk sangat rendah, dan penjual tidak responsif!",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat buruk! Saya menerima barang dalam keadaan rusak dan penjual tidak memberikan pengembalian uang. Ini adalah pelanggaran!",
        "sentiment": "negatif",
    },
    {
        "comment": "Kurir sangat tidak ramah. Mereka sangat kasar dalam menangani paket. Barang yang saya terima rusak parah. Saya sangat marah!",
        "sentiment": "negatif",
    },
]


Mouse_wireless = [
    {
        "comment": "Tadi udah coba di leptop berfungsi dengan baik, walau sempat bermasalah di pengiriman tapi datang tepat waktu. Semoga awet di pake 🙏👍👍",
        "sentiment": "positif",
    },
    {
        "comment": "Berfungsi dengan normal. Kualitas oke. Semoga awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang ori, harga murce, pengiriman dan pengemasan cepat aman, thx seller",
        "sentiment": "positif",
    },
    {
        "comment": "Admin fast respon banget. Pas lagi kerja malah rusak.. emang sdh harus diganti.. hahaha.. but sekali lagi makasih utk admin yg fast response dan garcep kirim pas aku bilang bisa kirim kilat soalnya urgent mw lgsg di gunakan",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus sih tapi aku kira include dgn bateraix...ternyata enggak jadi harus keluar dulu cari baterai yg cocok....tapi semuax bagus.... pengiriman cepat....recommended seller ....",
        "sentiment": "positif",
    },
    {
        "comment": "Barang diterima dengan baik, belum dicoba, semoga berfungsi dengan baik. Sekadar saran, packingnya baiknya pakai buble wrap biar lebih aman.",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus optik nya responsibel, mudah²an awet. Rekomend belanja di toko ini. Makasii min",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah, barang sudah diterima, di packing sesuai tambahan, pakai bubble wrap dan kardus, mouse masih segel, sudah dicoba dan berfungsi, semoga barangnya awet",
        "sentiment": "positif",
    },
    {
        "comment": "Belum beli baterai nya sih jadi belum nyoba, dari segi luar bagus sih",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah saya terima. Berfungsi dengan baik. Suka sekali harga hemat berkualitas. Buat daring anak. Karena mouse lama pake kabel jadi mau coba ini tanpa kabel. Ne tanpa baterai ya. Aku pasang sendiri baterainya",
        "sentiment": "positif",
    },
    {
        "comment": "Thanks to pelapak, order jam set 7 malam masih bisa ikut kiriman di hari yang sama. Overall utk barang bagus berfungsi dengan baik. Respon bagus",
        "sentiment": "positif",
    },
    {
        "comment": "Barang ori dan murce , klik nya empuk tapi belum silent klik tapi gpp sesuai harga ini udah bagus bgt, pengiriman juga cepat meski luar kota",
        "sentiment": "positif",
    },
    {
        "comment": "Terima kasih barang nya sudah sampai... pengiriman nya cepat...seller-nya ramah.. kurirnya juga baik ..semoga awet belum dicoba..terima kasih ya",
        "sentiment": "positif",
    },
    {
        "comment": "Alhamdulillah sampai dengan aman dan berfungsi dengan baik. Agak lama install drivernya tapi alhamdulillah bisa. Clicky banget bunyinya, bukan tipe yang silent clicky gitu. Materialnya plastik tapi masih oke, ga terlalu ringkih banget. Warnanya black mate, cakep sih. Packagingnya rapih, kotaknya juga diplastik double, aman.",
        "sentiment": "positif",
    },
    {
        "comment": "Produk sesuai dengan pesanan. Pengemasan dan pengiriman barang cepat rapih aman. Semoga awet. Terima kasih",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman aman dan tepat waktu. Produk sesuai harapan semoga awet. Terima kasih seller terima kasih Shopee",
        "sentiment": "positif",
    },
    {
        "comment": "Pengiriman bermasalah dan sempat terjadi masalah di pengiriman. Tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Berfungsi secara normal, tetapi kualitas tidak sebanding dengan harganya. Kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak cocok, harus mencari baterai yang sesuai. Menyebalkan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang diterima dengan baik tetapi ada kekurangan dalam pengemasan. Harus lebih hati-hati.",
        "sentiment": "negatif",
    },
    {
        "comment": "Belum nyoba karena belum beli baterai. Kurang sesuai ekspektasi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman lambat dan ada masalah dalam proses pengiriman. Tidak puas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sempat rusak saat digunakan, dan tidak mendapat respon yang memadai dari penjual. Kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas tidak sesuai ekspektasi. Barang kurang awet. Tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang dipasang sendiri baterainya. Sepertinya bukan produk yang direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak memuaskan. Berharap bisa lebih baik, tetapi tidak sesuai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang rusak saat tiba dan proses pengembalian sangat merepotkan. Tidak puas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Tidak sesuai dengan gambar yang diiklankan. Kecewa dengan produk ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga tidak sepadan dengan kualitas produk. Terlalu mahal untuk apa yang diberikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kurir pengiriman tidak profesional dan paket tiba dalam kondisi rusak. Tidak direkomendasikan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Admin penjual tidak responsif dan tidak membantu. Komunikasi buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman terlambat dan barang tiba dalam kondisi buruk. Tidak puas dengan layanan ini.",
        "sentiment": "negatif",
    },
]


Kombo_mouse = [
    {
        "comment": "Keyboard empuk, Mouse enak dipegang. Ga ada kendala dan robot ini oke. Tanggapan seller melalui chat juga ramah dan nyaman. Seller update pengiriman melalui chat juga. Thanks a lot.",
        "sentiment": "positif",
    },
    {
        "comment": "Keyboard bagus sesuai harga tanpa lecet. Packingnya aman banget, bubble wrapnya tebal. Seller fast respon saat di chat. Cuman pengirimannya agak lama mungkin karena pesanannya banyak kali ya. Overall mantap.",
        "sentiment": "positif",
    },
    {
        "comment": "Lumayan bagus barangnya, okeelah harga segini mantaap. Belum termasuk baterai ya, gaeesss. Batre-nya AAA 1x dan AA 1x.",
        "sentiment": "positif",
    },
    {
        "comment": "Respon cepat, pelayanan prima, pengemasan aman, produk original. Mouse tidak silent. Sudah termasuk baterai. Mouse cukup baik, keyboard mantap.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang bagus tidak ada yang lecet, berfungsi dengan baik.",
        "sentiment": "positif",
    },
    {"comment": "Harga sesuai, kualitas baik, bonus baterai.", "sentiment": "positif"},
    {
        "comment": "Pengiriman cepat dan barang lengkap serta ada bonus kartu smartfren. Terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Paket sudah sampai dengan selamat karena packing aman. Keyboard dan mouse berfungsi dengan baik. Pengiriman juga lumayan cepat, dapat harga promo juga 😇 dapat baterai sama bonus masker mata 😆",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk original dan baik, sesuai dengan harga yang di bawah harga keyboard wireless lainnya yang lebih mahal. Akan tetapi menurut saya silent keyboardnya lebih ditingkatkan lagi dari segi kualitas bahan keyboardnya. Karena saya pernah pakai silent keyboard merk lain dan merk lain keyboardnya benar-benar silent.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah sampai dengan selamat, maaf baru memberi nilai. Sangat suka dengan keyboardnya, sampai sekarang sangat aman buat kerja di kantor.",
        "sentiment": "positif",
    },
    {"comment": "Simple sudah include baterai.", "sentiment": "positif"},
    {
        "comment": "Bagus banget, teman kerja saya juga puas dengan barangnya. Terima kasih.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sangat memuaskan. Packing juga aman. Meskipun pengiriman ke Semarang lumayan lama tapi sangat memuaskan 🥰 Semoga awet dan nggak rewel ☺",
        "sentiment": "positif",
    },
    {
        "comment": "Bagus, sesuai harga, keyboard dan mouse ada suara, mousenya nyaman di pegang, packaging rapi, dapat batre, 1 batre AA untuk mouse, 1 batre AAA untuk keyboard, semoga awet, semoga ga gampang rusak",
        "sentiment": "positif",
    },
    {
        "comment": "Produk bagus Dan mouse nya bisa lantai juga ok untuk kedepannya tingkatkan lagi",
        "sentiment": "positif",
    },
    {
        "comment": "Wireless keyboard and mouse combo, pesanan terbaik sampai saat ini, tingkat kepekaan atau sensitifnya terhadap gerakan sangat tinggi, sentuhan tangan sangat lembut, bisa kita operasikan sesuka hati..produk memang sangat memuaskan.. pokoknya recommended banget buat produk ini\nTerimakasih buat seller yang sangat luar biasa aktif komunikasi dengan pemesan. Rasanya adem, tenang belanja di seller ini. Maju dan jaya selalu buat seller.\nUntuk jasa kurir sesuai dengan jadwal, cuma kalau boleh memberikan masukan... Mohon info pesanan di update setiap waktu....\nTapi pada akhirnya malah lebih cepat datang nya dari jadwal. Terimakasih banyak buat kurirnya juga.",
        "sentiment": "positif",
    },
    ### Negatif
    {
        "comment": "Keyboard dan mouse ini sangat buruk. Saya kecewa dengan kualitasnya dan mereka tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengemasan sangat buruk dan barang rusak saat sampai. Seller tidak responsif dan tidak membantu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat tertipu dengan pembelian ini. Keyboard dan mouse ini tidak sesuai dengan deskripsi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan barang ini. Keyboard dan mouse sering macet dan tidak nyaman digunakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan tidak sesuai dengan yang dijanjikan. Saya tidak akan membeli dari penjual ini lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga yang saya bayar tidak sebanding dengan kualitas produk ini. Sangat mengecewakan.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini tidak awet sama sekali. Saya merasa seperti saya telah membuang uang dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat rendah. Keyboard dan mouse ini sering error dan membuat saya frustasi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa seperti saya telah ditipu. Keyboard dan mouse ini sangat buruk dan tidak berfungsi dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pelayanan dari penjual sangat buruk. Mereka tidak merespons keluhan saya dengan baik.",
        "sentiment": "negatif",
    },
    {
        "comment": "Keyboard dan mouse ini sangat rapuh dan mudah rusak. Saya merasa seperti saya telah membuang uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sangat kecewa dengan pengiriman yang lama dan produk yang tidak berkualitas. Saya tidak merekomendasikan pembelian dari penjual ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini terlalu tinggi untuk kualitas yang sangat rendah. Saya merasa seperti saya telah tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya tidak akan pernah membeli produk dari penjual ini lagi. Pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Keyboard dan mouse ini tidak sesuai dengan ekspektasi saya. Mereka sering mengalami masalah teknis.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat tidak berguna. Tidak ada manfaatnya sama sekali. Saya menyesal telah membelinya.",
        "sentiment": "negatif",
    },
]


Tws_Robot = [
    {
        "comment": "Suaranya sangat jernih, paket sampai tujuan dalam kondisi baik, admin yang ramah, tampilan barang simpel namun menarik. Pengiriman juga sangat cepat.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sudah sampai dan berfungsi dengan baik. Suaranya jernih, pengemasan rapi, dan pengiriman cepat. Sangat memuaskan!",
        "sentiment": "positif",
    },
    {
        "comment": "Barang bagus, harga terjangkau, suara enak di kuping, tidak sember, sangat mantap. Rekomendasi!",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas produk sangat baik, pengiriman cepat, pelayanan seller memuaskan. Tidak ada kendala, semuanya berfungsi dengan baik. Mantap!",
        "sentiment": "positif",
    },
    {
        "comment": "Robot T30 Plus sudah sampai dengan selamat. Suara bagus, koneksi Bluetooth mudah, sensor sentuhan bagus, model keren, dan earbuds nyaman. Mantaap!",
        "sentiment": "positif",
    },
    {
        "comment": "Paket sudah sampai, respon penjual baik, pengiriman cepat, packing rapi, barang sesuai pesanan, harga murah, kualitas barang bagus, produk asli, dan kurir ramah. Terima kasih buat seller, semoga sukses.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sesuai pesanan dan original, pengiriman juga sangat cepat. Seller juga ramah.",
        "sentiment": "positif",
    },
    {
        "comment": "Tws low budget tapi kualitas TOP BGT, bass keren, noise tidak masuk, seller responsnya cepat dan barang serta packing oke. Best seller!",
        "sentiment": "positif",
    },
    {
        "comment": "Barang bagus, berfungsi dengan baik, suara mantap, seller respons cepat, pengemasan dan pengiriman cepat, kurir juga mantap. Top semuanya.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang sampai dengan selamat dan sesuai pesanan. Bass bagus, baterai tahan lama. Robot memang keren. Terima kasih!",
        "sentiment": "positif",
    },
    {
        "comment": "Dapat bonus brush foundation, sangat sepadan dengan harga, bagus dan mudah dibawa ke mana-mana. Senang!",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas bagus, suara nge-bass banget. Produk yang sangat sepadan dengan harga. Puas!",
        "sentiment": "positif",
    },
    {
        "comment": "Untuk saat ini masih normal, hanya agak bingung pada pemakaian awal. Semoga bisa awet.",
        "sentiment": "positif",
    },
    {
        "comment": "Barang keren abis, asli original, pengiriman juga sangat cepat. Puas banget!",
        "sentiment": "positif",
    },
    {
        "comment": "Suaranya mantap banget, harga juga sepadan. Tinggal menunggu ketahanannya. Puas!",
        "sentiment": "positif",
    },
    {
        "comment": "Akhirnya sampai juga yang ditunggu-tunggu. Packing bagus, semua masih tersegel, sudah dicoba berfungsi dengan baik.",
        "sentiment": "positif",
    },
    {
        "comment": "Kualitas barang baik, sampai dengan aman, respon penjual baik, kurir baik, semoga awet ya. Begitu sampai langsung di chat untuk cara pemakaian. Bagus banget buat orang yang baru mau coba pakai earphone.",
        "sentiment": "negatif",
    },
    {
        "comment": "Baru sehari pakai. Tidak tahu seawet apa. Kualitas suara cukup tidak jelek maupun bagus. Namun kekurangannya fitur bluetooth nya meskipun sudah tersambung bisa disambungkan oleh orang lain. (bisa diganggu)",
        "sentiment": "negatif",
    },
    {
        "comment": "Suara dari Airbuds-nya mantap banget. Cuma Airbuds yang satu tidak bisa hidup sama sekali. Sudah di cas minimal 4 jam tetapi tidak hidup, indikator lampu pairing-nya saja tidak hidup.",
        "sentiment": "negatif",
    },
    {
        "comment": "Udah didalam case kadang nyambung sendiri ke hp jadi baterai cepat habis.",
        "sentiment": "negatif",
    },
    {
        "comment": "Suaranya kurang bagus.... Masih mendingan pake headset Robot-nya. Sambungan-nya putus-putus, jadi tidak nyaman buat dipakai.",
        "sentiment": "negatif",
    },
    {
        "comment": "Suara enak, tapi baterai boros banget, casan tidak bisa dipakai lagi, terasa seperti membeli barang bekas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Salah kirim type produk, pesan T30 PLUS yang dikirim T50 jadi kurang enak dipakai di telinga saya, pengiriman lama males mau tuker karna harus mengembalikan produk",
        "sentiment": "negatif",
    },
    {
        "comment": "Suara aman tapi tidak bisa dipakai telfon org yg ditelfon tidak bisa dengar suara dari mic headset ini",
        "sentiment": "negatif",
    },
    {
        "comment": "Packaging sangat buruk, kotak rusak, kabel charger rusak",
        "sentiment": "negatif",
    },
    {
        "comment": "Suara jernih, cuman di telinga gak enak, bass seperti stereo ambyaar pokoknya dah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saat musik suaranya bagus tapi saat panggilan telepon suara kecil sekali. Ini kalau mau komplain kemana?",
        "sentiment": "negatif",
    },
    {
        "comment": "Jujur, ini kalau ketutupan kupluk/helm/apalah yang menghalangi sedikit saja, lagu langsung ilang... ga ngerti lagi dah nyari cara di yt biar ga missound dari ni airbuds tapi tetap aja kehalang benda bakal mati, DICOBA AJA TUTUP AIRBUDS NYA PAKE TANGAN DI KEKEP PASTI MATI.",
        "sentiment": "negatif",
    },
    {
        "comment": "Udah cas 4 jam tetap lowbat aja, trus yang kanan ga mau. Udah coba reset tetap ga mau, coba manual ga mau juga. Cara klaim garansi gimana ya?",
        "sentiment": "negatif",
    },
    {
        "comment": "Suaranya kurang jelas, lalu baterai nya cepat habis tidak sesuai dengan deskripsi nya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Suara biasa aja. Sensor sentuh ga fungsi. Earbuds diletakan media tidak berhenti.",
        "sentiment": "negatif",
    },
    {
        "comment": "Sebelah kanan gak bisa di cas. Harus di ganjel/diteken dulu baru masuk.",
        "sentiment": "negatif",
    },
]


Stand = [
    {
        "comment": "Bagus, pengiriman aman, bahan dari plastik tapi tebal, warna cute kiyowoo, harga terjangkau:) admin ramah pas barang dikirim diberitahu lewat chat ihiy makasii seller robot",
        "sentiment": "positif",
    },
    {
        "comment": "Warnanya cerah dan cantik, semoga kokoh dan awet dan bisa mempermudah pekerjaan yang biasa dilakukan sehari-hari. Lumayan kuat untuk nahan laptop 14 inch.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: fleksibel dbawa kemana-mana. Sepadan dengan Harga: worth it bangett💞. Ada tempat naruh pen tablet juga, pengirimannya lumayan cepat buat luar jawa makasih kurir 😆 walopun keliatannya agak fragile but actually it's so good mampu bangett nahan laptop love it^^",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: holder laptop. Sepadan dengan Harga: ya. Bahan bagus plastik tebal, kuat nahan laptop 11 inci apa 12 inci yak, lupa 😅 pokoknya bagus gus gus gus. Thanks",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: warna kuningnya baguss dan bahannya kokoh. Sepadan dengan Harga: Ya. Thanks seller barangnya original, bagus, kokoh, dan warna kuningnya cantik bangettt😍 pengiriman cepat, seller responsif! Next time pasti order lagi🙏🥰",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: adminnya super responsif dan enak bangett selalu ngingetin dan ngasih info posisi barang kita by chat. Good Job! Sepadan dengan Harga: mungkin bisa lebih murah lagi🤭 Overall ini cukup sesuai dengan perkiraan saya, bahannya bukan full alumunium / besi gitu ya gaes but ini cukup kokoh. Meskipun bayanganku agak kecil tapi ternyata besar banget.",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bahan plastik tp kokoh. Sepadan dengan Harga: iya. Barangnya sudah sampai, jika dibuka paling lebar emang segitu, pengemasannya aman banget jagi GK perlu khawatir, pokoknya makasih banyak seller dan kurir.... Semoga sukses selalu",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus. Sepadan dengan Harga: worth it. Saya pesen putih kenapa datengnya kuning",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus. Sepadan dengan Harga: sesuai dengan kualitasnya. Mantapp , paling rendah lumayan tinggi juga",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus. Sepadan dengan Harga: Murah. Pesanan diterima dgn baik, pengiriman cepat dan best lah",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: mudah dibawa, menjaga agar punggung tidak pegal ketika lama berhadapan dgn laptop. Sepadan dengan Harga: ya. Pengiriman cepat, thanks seller & shopee",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: simple. Lumayan kokoh, untuk posisi pas dengan mata harus di slot yang paling rendah, tapi gpp tetap enak menggunakan. Makasih",
        "sentiment": "positif",
    },
    {
        "comment": "Untuk laptop 16 inch masih lumayan bisa dipakai. Bagus warnanya dan lumayan tebal",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus bisa utk laptop besar. Sepadan dengan Harga: iya sepadan. Warnanya bagus. Datangnya cepat. Udah dicoba dan memang bisa untuk laptop besar. Semoga awet dan ngga pegel lagi deh sekarang",
        "sentiment": "positif",
    },
    {
        "comment": "Lumayan lah biar laptop ada alasnya kalo dipake",
        "sentiment": "positif",
    },
    {
        "comment": "Fitur Terbaik: bagus bisa utk laptop besar. Sepadan dengan Harga: iya sepadan. Warnanya bagus. Datangnya cepat. Udah dicoba dan memang bisa untuk laptop besar. Semoga awet dan ngga pegel lagi deh sekarang",
        "sentiment": "positif",
    },
    {
        "comment": "Barang ini sangat berguna. Sangat membantu dalam kegiatan sehari-hari saya. Saya sangat puas dengan pembeliannya.",
        "sentiment": "positif",
    },
    # negatif
    {
        "comment": "Barang ini sangat buruk. Tidak sesuai dengan deskripsi dan sangat rapuh. Saya kecewa sekali dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa sangat tertipu. Kualitas produk sangat rendah, dan harga yang saya bayar tidak sebanding dengan barang yang saya terima.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah pemborosan uang. Bahan plastiknya sangat tipis dan rapuh. Saya merasa seperti barang ini akan rusak kapan saja.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan pelayanan dari penjual sangat buruk. Saya tidak akan pernah membeli dari penjual ini lagi.",
        "sentiment": "negatif",
    },
    {
        "comment": "Ini adalah salah satu pembelian terburuk saya. Barang ini tidak awet sama sekali, dan saya merasa telah membuang uang.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Saya merasa seperti saya telah membeli barang palsu. Sangat mengecewakan!",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya sangat kecewa dengan barang ini. Tidak sepadan dengan harganya sama sekali. Saya merasa telah tertipu.",
        "sentiment": "negatif",
    },
    {
        "comment": "Produk ini sangat jelek. Tidak sesuai dengan ekspektasi saya. Saya sangat menyesal telah membelinya.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa seperti saya telah membuang uang dengan pembelian ini. Barangnya tidak tahan lama dan tidak berkualitas.",
        "sentiment": "negatif",
    },
    {
        "comment": "Pengiriman sangat lambat dan penjual tidak responsif. Saya tidak merekomendasikan pembelian dari penjual ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat rapuh dan mudah rusak. Saya merasa seperti saya telah membeli barang sampah.",
        "sentiment": "negatif",
    },
    {
        "comment": "Kualitas produk sangat buruk. Saya sangat kecewa dengan pembelian ini.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya merasa seperti saya telah ditipu. Barang ini tidak sesuai dengan deskripsi dan kualitasnya buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Saya tidak akan pernah membeli dari penjual ini lagi. Pengalaman berbelanja yang sangat buruk.",
        "sentiment": "negatif",
    },
    {
        "comment": "Harga produk ini tidak sepadan dengan kualitasnya. Saya merasa sangat kecewa.",
        "sentiment": "negatif",
    },
    {
        "comment": "Barang ini sangat tidak berguna. Tidak ada manfaatnya sama sekali. Saya menyesal telah membelinya.",
        "sentiment": "negatif",
    },
]


print("Mousepad: ", len(Mousepad_product))


product_mousepad_pd = pd.DataFrame(Mousepad_product)
product_mouse_pd = pd.DataFrame(Mouse_wireless)
product_kombo_pd = pd.DataFrame(Kombo_mouse)
product_tws_pd = pd.DataFrame(Tws_Robot)
product_stand_pd = pd.DataFrame(Stand)


product_mousepad_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_mouse_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_kombo_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_tws_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)
product_stand_pd.drop_duplicates(subset=["comment"], keep="first", inplace=True)


print("Value counts Ke-1: ", product_mousepad_pd["sentiment"].value_counts())
print("Value counts Ke-2: ", product_mouse_pd["sentiment"].value_counts())
print("Value counts Ke-3: ", product_kombo_pd["sentiment"].value_counts())
print("Value counts Ke-4: ", product_tws_pd["sentiment"].value_counts())
print("Value counts Ke-5: ", product_stand_pd["sentiment"].value_counts())


merge_df = pd.concat(
    [
        product_mousepad_pd,
        product_mouse_pd,
        product_kombo_pd,
        product_tws_pd,
        product_stand_pd,
    ]
)

Positif_count = (merge_df["sentiment"] == "positif").sum()
negatif_count = (merge_df["sentiment"] == "negatif").sum()

print("Jumlah ulasan Positif:", Positif_count)
print("Jumlah ulasan negatif:", negatif_count)

print("Jumlah: ", len(merge_df))


merge_df["comment"] = merge_df["comment"].str.replace("\n", " ")


merge_df.to_csv("./dataset/sentiment_product_robot.csv", index=False)

print("Data telah disimpan: ", len(merge_df))
