import csv
import random
from datetime import datetime
import pandas as pd

products_erigo = [
    {
        "id": 1,
        "name": "Chino Pants Erigo",
        "image": "https://down-id.img.susercontent.com/file/sg-11134201-23020-l8w1yoqauhnvfd",
        "category_id": 1,
        "description": "Chino Pants Erigo saat ini merupakan salah satu lini pakaian terbaik dan berkualitas tinggi di antara Local Brand Indonesia. Chino Pants are undoubtedly an essential style! Selain serba guna karena modis, celana ini juga merupakan must-have item bagi para pria. Erigo Chino Pants di design dengan warna indah dengan kain pilihan yang membuatmu nyaman sepanjang hari. Memiliki live-button, resleting, belt loop, dan 4 saku simpel pada bagian pinggul.",
        "price": 129000,
        "countInStock": 3900,
        "brand": "Erigo",
        "weight": 1,
        "rating": 4.0,
    },
    {
        "id": 2,
        "name": "Erigo Coach Jacket Fujinkai Black Unisex",
        "image": "https://down-id.img.susercontent.com/file/sg-11134201-23020-2few75h9thnv83",
        "category_id": 1,
        "description": "Coach Jacket Erigo saat ini Mengeluarkan Design terbaru, Coach Jaket Erigo merupakan salah satu lini pakaian terbaik dan berkualitas tinggi di antara Local Brand Indonesia. Jaket berkerah dengan kancing jepret, saku fungsional, dan karet pada ujung lengan. Coach Jacket Erigo memiliki printed design yang unik pada bagian punggung dan dada depan, dengan warna memukau siap menjadikanmu penuh semangat!",
        "price": 155000,
        "countInStock": 260,
        "brand": "Erigo",
        "weight": 1,
        "rating": 5.0,
    },
    {
        "id": 3,
        "name": "Erigo T-Shirt Kuina Navy Unisex",
        "image": "https://down-id.img.susercontent.com/file/id-11134201-7qul7-lh35glotbd2297",
        "category_id": 1,
        "description": "T-Shirt Erigo saat ini merupakan salah satu lini pakaian terbaik dan berkualitas tinggi di antara Local Brand Indonesia. Dibuat dengan bahan cotton yang nyaman untuk menemani harimu dan memiliki print desain yang unik. Dapatkan long lasting tee dengan warna cantik ini untuk merasa muda selamanya!",
        "price": 250000,
        "countInStock": 12,
        "brand": "Erigo",
        "weight": 1,
        "rating": 4.0,
    },
    {
        "id": 4,
        "name": "Erigo Chino Pants Beryl Emerald Unisex",
        "image": "https://down-id.img.susercontent.com/file/sg-11134201-23020-iinhqctbuhnv0e",
        "category_id": 1,
        "description": "Chino Pants Erigo saat ini merupakan salah satu lini pakaian terbaik dan berkualitas tinggi di antara Local Brand Indonesia. Chino Pants are undoubtedly an essential style! Selain serba guna karena modis, celana ini juga merupakan must-have item bagi para pria. Erigo Chino Pants di design dengan warna indah dengan kain pilihan yang membuatmu nyaman sepanjang hari. Memiliki live-button, resleting, belt loop, dan 4 saku simpel pada bagian pinggul.",
        "price": 149000,
        "countInStock": 100,
        "brand": "Erigo",
        "weight": 1,
        "rating": 4.0,
    },
    {
        "id": 5,
        "name": "Erigo Jogger Pants Jessie Black",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qul2-lgbu2l8nkiqw58",
        "category_id": 1,
        "description": "Deskripsi produk 5",
        "price": 149000,
        "countInStock": 300,
        "brand": "Erigo",
        "weight": 1,
        "rating": 5.0,
    },
]

product_robot = [
    {
        "id": 6,
        "name": "ROBOT - Mousepad Anti Slip RP05 Gaming Polos Hitam Murah Rubber Original",
        "image_url": "https://down-id.img.susercontent.com/file/id-11134207-7qukw-lfhtl49y1wr9cb",
        "category_id": 2,
        "description": "Deskripsi produk 6",
        "price": 14900,
        "stock": 150,
        "brand": "Robot",
        "seller_id": 1,
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 7,
        "name": "Mouse Wireless ROBOT M205 2.4G 1600DPI Receiver USB untuk PC Laptop-Garansi Resmi 1 Tahun",
        "image_url": "https://down-id.img.susercontent.com/file/id-11134207-7qul1-lfht2bakt9pefb",
        "category_id": 2,
        "description": "Deskripsi produk 7",
        "price": 89900,
        "stock": 10,
        "brand": "Robot",
        "seller_id": 1,
        "average_rating": 4.0,
        "created_at": "2023-09-18 20:45:11.759205",
        "updated_at": "2023-09-18 20:45:11.759205",
    },
    {
        "id": 8,
        "name": "ROBOT Portable Mini Wireless Set Combo Keyboard and Mouse KM3100 Original Garansi 1 Tahun",
        "image_url": "https://down-id.img.susercontent.com/file/id-11134207-7qukw-lfhsywqw2fbp05",
        "category_id": 2,
        "description": "Deskripsi produk 8",
        "price": 151900,
        "stock": 122,
        "brand": "Robot",
        "seller_id": 1,
        "average_rating": 4.0,
        "created_at": "2023-09-18 20:45:11.759206",
        "updated_at": "2023-09-18 20:45:11.759207",
    },
    {
        "id": 9,
        "name": "Robot TWS Wireless Earphone Airbuds T30 PLUS Original BT 5.3 Original Garansi 1 Tahun",
        "image_url": "https://down-id.img.susercontent.com/file/id-11134207-7qul5-lfjdrexacksta9",
        "category_id": 2,
        "description": "Deskripsi produk 9",
        "price": 134900,
        "stock": 8,
        "brand": "Robot",
        "seller_id": 1,
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759208",
        "updated_at": "2023-09-18 20:45:11.759208",
    },
    {
        "id": 10,
        "name": "ROBOT Stand Holder Laptop Portable Lipat Anti Slip Kompatibel dengan Semua Jenis Laptop dan Tablet RT-LS03 Original",
        "image_url": "https://down-id.img.susercontent.com/file/19bdb45996ce2287637a9dd1a0aedef5",
        "category_id": 2,
        "description": "Deskripsi produk 10",
        "price": 45900,
        "stock": 7,
        "brand": "Robot",
        "seller_id": 1,
        "average_rating": 4.0,
        "created_at": "2023-09-18 20:45:11.759209",
        "updated_at": "2023-09-18 20:45:11.759210",
    },
]

product_sandisk = [
    {
        "id": 11,
        "name": "SanDisk CZ50 Cruzer Blade USB 2.0 - 8 GB",
        "image": "https://down-id.img.susercontent.com/file/4d63a9c676345dd760a19e525270aa45",
        "category_id": 2,
        "description": "Design yang kecil memudahkan koneksi ke perangkat USB apa saja. Meskipun berukuran kecil, SanDisk Cruzer Blade ini mempunyai kapasitas yang cukup untuk menyimpan data-data anda. Didukung aplikasi SanDisk SecureAccess, data anda dapat dilindungi dengan enkripsi 128 bit AES.",
        "price": 38500,
        "countInStock": 200,
        "weight": 1,
        "brand": "Sandisk",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 12,
        "name": "SanDisk Max Endurance 128GB 100MB/s MicroSDXC - 4K Ultra HD",
        "image": "https://down-id.img.susercontent.com/file/ec8169cae5719c666f27a7849f7dd8db",
        "category_id": 2,
        "description": "SanDisk Max Endurance 128GB 100MB/s MicroSDXC",
        "price": 541500,
        "countInStock": 200,
        "weight": 1,
        "brand": "Sandisk",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 13,
        "name": "SanDisk SSD PLUS Solid 240GB SPEED UP/TO 530MB/S",
        "image": "https://down-id.img.susercontent.com/file/20c9f8c7f362e06878d7c5e6ef2eced1",
        "category_id": 2,
        "description": "SANDISK SSD PLUS Solid 240GB SPEED UP/TO 530MB/S",
        "price": 541500,
        "countInStock": 200,
        "weight": 1,
        "brand": "Sandisk",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 14,
        "name": "SANDISK FLASHDISK 128GB / USB FLASH 128GB / SANDISK BLADE CZ50 128GB",
        "image": "https://down-id.img.susercontent.com/file/239f3ebc84461d441f5d9d6a71314c4d",
        "category_id": 2,
        "description": "SANDISK SSD PLUS Solid 240GB SPEED UP/TO 530MB/S",
        "price": 124500,
        "countInStock": 200,
        "weight": 1,
        "brand": "Sandisk",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 15,
        "name": "Sandisk Ultra Micro SDXC UHS I A1 140Mbps 128GB Micro Sd Card Class 10 - QUAB",
        "image": "https://down-id.img.susercontent.com/file/8e55b8ef8ae3644f0ba818614e9ea23b",
        "category_id": 2,
        "description": "SANDISK SSD PLUS Solid 240GB SPEED UP/TO 530MB/S",
        "price": 178000,
        "countInStock": 200,
        "weight": 1,
        "brand": "Sandisk",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
]


product_teamgroup = [
    {
        "id": 16,
        "name": "TEAMGROUP SSD M2 SATA 2280 MS30 2TB ( 2000GB )",
        "image": "https://down-id.img.susercontent.com/file/baccfdd89a536591742b5f8890b6f7d2",
        "category_id": 2,
        "description": "MS30 is a M.2 (NGFF, Next Generation Form Factor) high speed solid state drive of the latest generation. It has the latest SATA III 6Gb/s transfer interface and offers excellent transfer efficiency and compatibility. For different environment usage, MS30 comes in two sizes, 22X80mm and 22X42mm, and the capacity of 22X80mm comes to 2TB, which is capable of satisfying all kinds of specification requirements for motherboards, laptops, mobile devices and developing embedded devices.",
        "price": 3020000,
        "countInStock": 200,
        "weight": 1,
        "brand": "Team-group",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 17,
        "name": "TEAMGROUP SSD 2.5 CX2 Series 256GB Sata3",
        "image": "https://down-id.img.susercontent.com/file/cb0a9527206091fe397a5656f32c1027",
        "category_id": 2,
        "description": "TEAMGROUP SSD 2.5 CX2 Series 256GB Sata3",
        "price": 285000,
        "countInStock": 200,
        "weight": 1,
        "brand": "team-group",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 18,
        "name": "TEAMGROUP SSD 2.5 GX2 128GB Grey",
        "image": "https://down-id.img.susercontent.com/file/62a219eed303ae5ad2a7eaf0430ba763",
        "category_id": 2,
        "description": "TEAMGROUP SSD 2.5 GX2 128GB Grey",
        "price": 220000,
        "countInStock": 200,
        "weight": 1,
        "brand": "team-group",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 19,
        "name": "Teamgroup Elite Plus Memory DDR4 4GB PC 2666Mhz ( 21300 ) Black",
        "image": "https://down-id.img.susercontent.com/file/7ec9c695c7a4c40e3c721a20d00b283c",
        "category_id": 2,
        "description": "Teamgroup Elite Plus Memory DDR4 4GB PC 2666Mhz ( 21300 ) Black",
        "price": 240000,
        "countInStock": 200,
        "weight": 1,
        "brand": "team-group",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
    {
        "id": 20,
        "name": "Teamgroup SSD TEAM MP33 256GB M.2 NVMe (1800MB/s)",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qul2-litxf6olvc0maf",
        "category_id": 2,
        "description": "Teamgroup SSD TEAM MP33 256GB M.2 NVMe (1800MB/s)",
        "price": 297000,
        "countInStock": 200,
        "weight": 1,
        "brand": "team-group",
        "average_rating": 5.0,
        "created_at": "2023-09-18 20:45:11.759203",
        "updated_at": "2023-09-18 20:45:11.759204",
    },
]

product_gm = [
    {
        "id": 21,
        "name": "GM Bear Panci Listrik Fry Pan Electric (2in1) 1692 - Panci Penggorengan Keramik Elektrik Free Steamer",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qul3-lkgg3lx9sb09c1",
        "category_id": 3,
        "description": "GM Bear Panci Listrik Serbaguna hanya dengan satu alat, masak jadi gampang banget! Mengukus, merebus, mamasak mie, membuat hot pot bersama keluarga hingga memanaskan makanan jadi gampang banget loh! Panci ini juga cocok buat anak kost yang nggak mau ribet!  desainnya minimalis memiliki berbagai fungsi dalam satu alat! ",
        "price": 99000,
        "countInStock": 20,
        "weight": 1,
        "brand": "GM",
        "rating": 3.6,
    },
    {
        "id": 22,
        "name": "GM Bear Spatula Set isi 6psc 1073 - Utensil Spatula Sutil Set",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qul4-lfzbuyt1o49f53",
        "category_id": 3,
        "description": "Spatula adalah salah satu alat masak wajib yang harus dimiliki setiap dapur. Namun, untuk memaksimalkan proses memasak, dibutuhkan berbagai jenis spatula. Menghadirkan satu set peralatan masak spatula lengkap yang memiliki fungsi lengkap sehingga memberikan kemudahan dalam menyiapkan makanan untuk keluarga di rumah. ",
        "price": 26010,
        "countInStock": 20,
        "weight": 1,
        "brand": "GM",
        "rating": 3.6,
    },
    {
        "id": 23,
        "name": "GM Bear Wajan 16cm 1072 - Fry Pan Penggorengan Mini",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qukw-lkhtdyk015qs37",
        "category_id": 3,
        "description": "Solusi praktis memasak untuk kamu yang tinggal sendiri atau ngekost maupun suka masak porsi kecil. Simple, ringan dan mudah dibersihkan. Mulai dari menggoreng, menumis, masak telor, dan bikin pancake jadi lebih mudah dengan panci 16cm. Selain itu, design panci dengan warna yang cerah jadi pilihan untuk melengkapi dapurmu. ",
        "price": 34900,
        "countInStock": 20,
        "weight": 1,
        "brand": "GM",
        "rating": 3.5,
    },
    {
        "id": 24,
        "name": "GM Bear Organizer Rak Multifungsi P0177 - Organizer Storage Shelves Space Efficient Drawer",
        "image": "https://down-id.img.susercontent.com/file/7503f4b7c9a700241da64ad1d0caa8e9",
        "category_id": 3,
        "description": "Organizer meja serta lemari serbaguna yang di design untuk menciptakan kerapihan dan memudahkan pengguna dalam mengambil pakaian hingga barang-barang lain supaya tampak lebih rapih dan hemat ruang. Sangat mudah digunakan karena terdapat fitur sliding track yang dapat ditarik dan didorong. Terdapat 2 ukuran kecil dan besar yang bisa disesuaikan dengan kebutuhan.",
        "price": 124500,
        "countInStock": 20,
        "weight": 1,
        "brand": "GM",
        "rating": 3.5,
    },
    {
        "id": 25,
        "name": "GM Bear Alat Pemanggang Daging Hotpot Elektrik (2 in 1) 1247 - Denki BBQ Grill Pan Steamboat Electric",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qul0-lkgh2r96efmc2b",
        "category_id": 3,
        "description": "2 in 1 Grill and Pan elektrik ini bisa Anda gunakan untuk memanggang atau menggoreng BBQ makanan favorit anda dan memasak hot pot sekaligus dalam satu waktu. Panggangan dan Panci electric 2 in 1 akan dangat sempurna untuk acara BBQ bersama keluarga. Alat ini adalah kombinasi dari panggangan(Grill) dan juga Panci (Pan). Memasak berkali-kali dalam satu panci, memenuhi berbagi kebutuhan sekaligus. ",
        "price": 34900,
        "countInStock": 20,
        "weight": 1,
        "brand": "GM",
        "rating": 3.7,
    },
]

product_rinnai = [
    {
        "id": 26,
        "name": "Rinnai Kompor Gas 3 Tungku RI 524 E",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7qukw-lkhtdyk015qs37",
        "category_id": 3,
        "description": "Kompor gas dua tungku dan satu tungku untuk grill pan. Kompor series ini dapat mempermudah Anda untuk memasak dalam jumlah banyak sekaligus. Selain ada beberapa tungku yang bisa Anda gunakan untuk masak sekaligus, kompor ini juga di lengkapi dengan Grill pan dapat digunakan untuk memanggang. kompor ini pun dirancang dengan material body yang kuat.  Karena biasanya kompor gas itu digunakan hingga bertahun-tahun, kompor ini dibuat dengan bahan stainless steel yang terkenal karena kekuatan dan juga tahan karat. Masak akan lebih cepat dan hemat dengan kompor ini karena konsumsi gas yang rendah menggunakan api ekonomis.",
        "price": 874700,
        "countInStock": 20,
        "weight": 1,
        "brand": "Rinnai",
        "rating": 3.5,
    },
    {
        "id": 27,
        "name": "Rinnai Kompor Gas 1 Tungku RI TL 289 / TL289",
        "image": "https://down-id.img.susercontent.com/file/f876123ab77b1d9424e2e39aa17f7a86",
        "category_id": 3,
        "description": "Rinnai Kompor Gas 1 Tungku Low Pressure – TL289F merupakan salah satu kompor terbaik untuk bidang komersial. Bertipe low pressure atau tekanan gas yang rendah, tetapi menghasilkan api yang besar. Cocok untuk dapur rumah makan besar maupun kecil. Tungku yang kokoh dari besi cor mampu diandalkan untuk menompang beban yang berat. Sistem penyaan tanpa korek api yakni berupa piezo ignition. Tungku dengan lima sudut penyangga bisa memberikan penjagaan dengan baik di setiap perabotan memasak, dari panci maupun penggorengan.",
        "price": 696000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Rinnai",
        "rating": 3.7,
    },
    {
        "id": 28,
        "name": "Rinnai Sparepart Burner Head Tornado Kompor Seri 5/6/7",
        "image": "https://down-id.img.susercontent.com/file/e3a0a49c82f2d05f29b0120b467dbd4f",
        "category_id": 3,
        "description": "Kepala Tungku Besar Api Tornado Original Kompor Rinnai. Untuk Tipe berikut : RI-602 BGX, RI-712 BGX, RI-511 T, RI-712 T, RI-712 TG",
        "price": 87100,
        "countInStock": 20,
        "weight": 1,
        "brand": "Rinnai",
        "rating": 3.5,
    },
    {
        "id": 29,
        "name": "Rinnai Kompor Gas 1 Tungku RI 301S / 301S",
        "image": "https://down-id.img.susercontent.com/file/e3a0a49c82f2d05f29b0120b467dbd4f",
        "category_id": 3,
        "description": "Rinnai Kompor 1 Tungku – RI301S merupakan salah satu kompor gas Rinnai yang ekonomis. Memiliki tipe api sun burner yang menjadikan apinya menyala merata dan stabil tanpa pembuangan gas secara besar. Sehingga, masakan matang sempurna dan bahan bakar pun terkondisi. Disempurnakan juga dengan features pilihan, Serta berdiameter 28 cm yang menunjang penggunaan perabotan masak berukuran besar.",
        "price": 220900,
        "countInStock": 20,
        "weight": 1,
        "brand": "Rinnai",
        "rating": 3.9,
    },
    {
        "id": 30,
        "name": "Rinnai Kompor Gas 2 Tungku RI 2 RSP / 2 RSP",
        "image": "https://down-id.img.susercontent.com/file/cb969cae0619a14837f3c34c385875f0",
        "category_id": 3,
        "description": "Rinnai Kompor Gas RI-2RSP dengan desain finishing berwarna menawan membuat dapur Anda terlihat lebih modern dan rapi, cocok untuk Anda yang memperhatikan keindahan dapur Anda. Selain memperhatikan desain, kualitas juga merupakan hal yang diperhatikan oleh Rinnai. Tungku dan material dari kompor gas ini dibuat dari material terbaik.",
        "price": 1859300,
        "countInStock": 20,
        "weight": 1,
        "brand": "Rinnai",
        "rating": 4,
    },
]

product_xiaomi = [
    {
        "id": 31,
        "name": "Xiaomi TV A2 43 [FHD] Smart HD Dolby Audio� Android TV� Google Play Netflix Disney+",
        "image": "https://down-id.img.susercontent.com/file/id-11134201-7qul3-libi6cpmdx92e3",
        "category_id": 4,
        "description": "Memiliki desain layar penuh. Desain bezel ultra-tipis menghadirkan rasio antara layar dan bodi yang jauh lebih baik dibandingkan TV standar.",
        "price": 2790000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Xiaomi",
        "rating": 3.8,
    },
    {
        "id": 32,
        "name": "Xiaomi Redmi Buds 4 Active - Bluetooth® 5.3 IPX4 Baterai Hingga 28 Jam Koneksi Mudah",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7r98o-llkat83vi0yx0d",
        "category_id": 4,
        "description": "Dengan Driver Dinamis 12mm yang lebih besar dari sebelumnya oleh penyetelan ahli oleh Xiaomi Acoustic Lab, Redmi Buds 4 Active dapat menghadirkan bass dan akustik yang ditingkatkan, memberikan pengalaman mendengarkan yang menyenangkan untuk seluruh pengguna.",
        "price": 249000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Xiaomi",
        "rating": 3.8,
    },
    {
        "id": 33,
        "name": "Xiaomi POCO X5 Pro 5G (6GB/128GB) | (8GB/256GB) Snapdragon 778G 5G 120Hz AMOLED 67W 108MP NFC",
        "image": "https://m.media-amazon.com/images/I/61KYeBQgyrL._AC_SX679_.jpg",
        "category_id": 4,
        "description": "Xiaomi POCO X5 Pro 5G (6GB/128GB) | (8GB/256GB) Snapdragon 778G 5G 120Hz AMOLED 67W 108MP NFC",
        "price": 3819000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Xiaomi",
        "rating": 3.8,
    },
    {
        "id": 34,
        "name": "Xiaomi TV Box S (2nd Gen) 4K Ultra HD Streaming Media Player, Google TV Box with 2GB RAM 8GB ROM, 2.4G/5G Dual WiFi, Bluetooth 5.2 & Dolby Audio and DTS-HD, Dolby Vision, HDR10+",
        "image": "https://m.media-amazon.com/images/I/61BEpAFZPxL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "category_id": 4,
        "description": "4K Ultra HD memiliki resolusi 3840 x 2160 piksel, yang empat kali lebih banyak dari resolusi Full HD (1920 x 1080 piksel). ",
        "price": 1044802,
        "countInStock": 20,
        "weight": 1,
        "brand": "Xiaomi",
        "rating": 3.5,
    },
    {
        "id": 35,
        "name": "Xiaomi POCO M5 (4/64GB) | (4/128GB) Helio G99 50MP AI Triple Kamera Layar 90Hz FHD+ 6,58” 5000mAh NFC",
        "image": "https://m.media-amazon.com/images/I/71meiP7FMrL._AC_SL1500_.jpg",
        "category_id": 4,
        "description": "POCO M5 menggunakan prosesor octa-core MediaTek Helio G99 memiliki arsitektur CPU terdepan di industri dan GPU MC2 Mali-G57 tangguh yang mampu menghasilkan performa hebat untuk pengalaman pengguna yang mengesankan. ",
        "price": 1599000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Xiaomi",
        "rating": 3.5,
    },
]

product_bardi = [
    {
        "id": 36,
        "name": "BARDI Smart Indoor PTZ IP Camera CCTV Wifi IoT Home Automation + Micro SD",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7r98u-llijp72tjdm3c9",
        "category_id": 4,
        "description": "BARDI Smart Indoor PTZ IP Camera CCTV Wifi IoT Home Automation + Micro SD",
        "price": 108000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Bardi",
        "rating": 4,
    },
    {
        "id": 37,
        "name": "BARDI Smart LIGHT BULB RGBWW 12W Wifi Wireless IoT - Home Automation (Lampu Tidur Kekinian)",
        "image": "https://down-id.img.susercontent.com/file/id-11134207-7r98t-llijp72tgkh766",
        "category_id": 4,
        "description": "BARDI Smart Light Bulb dapat mengubah suasana dengan pengaturan tingkat keterangan dan warna. Untuk memudahkan pengguna, warna dibagi menjadi 2 pengaturan yaitu ke warm white (2700-6500k), dan beragam warna (RGB). ",
        "price": 120000,
        "countInStock": 20,
        "weight": 1,
        "brand": "Bardi",
        "rating": 4.1,
    },
    {
        "id": 38,
        "name": "BARDI Smart UNIVERSAL IR REMOTE 12M Wifi Wireless IoT For Home Automation",
        "image": "https://down-id.img.susercontent.com/file/0c9ddeb724c18b31aa6eee6ac9d9ce3b",
        "category_id": 4,
        "description": "BARDI Universal IR Remote 12M merupakan remote infrared pintar yang dapat dikendalikan melalui aplikasi selama BARDI Universal IR Remote 12M terhubung ke wifi/hotspot.",
        "price": 135000,
        "countInStock": 40,
        "weight": 1,
        "brand": "Bardi",
        "rating": 3.8,
    },
    {
        "id": 39,
        "name": "BARDI Dual Smart Plug",
        "image": "https://down-id.img.susercontent.com/file/878d142e8bddb22764d7ea57d305485f",
        "category_id": 4,
        "description": "BARDI Dual Smart Plug merupakan steker pintar yang bisa diatur melalui aplikasi. Dengan plug ini, segala perangkat dengan daya listrik 220v dapat diputus atau disambungkan arus listrik sesuai keinginan.",
        "price": 230000,
        "countInStock": 40,
        "weight": 1,
        "brand": "Bardi",
        "rating": 3.9,
    },
    {
        "id": 40,
        "name": "BARDI Bundling Smart IP Camera CCTV Outdoor PTZ + Micro SD",
        "image": "https://down-id.img.susercontent.com/file/sg-11134201-23010-w9jg0ptph7lv4d",
        "category_id": 4,
        "description": "BARDI Universal IR Remote 12M merupakan remote infrared pintar yang dapat dikendalikan melalui aplikasi selama BARDI Universal IR Remote 12M terhubung ke wifi/hotspot.",
        "price": 15000,
        "countInStock": 40,
        "weight": 1,
        "brand": "Bardi",
        "rating": 3.7,
    },
]


user_data_erigo = pd.read_csv("./dataset/user_data_erigo.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_erigo = pd.read_csv("./dataset/sentiment_product_erigo.csv")

# Menghapus \n dari kolom 'comment'
sentiment_product_erigo["comment"] = sentiment_product_erigo["comment"].str.replace(
    "\n", ""
)

# Data ulasan produk Erigo
erigo_product_reviews = []
review_erigo_id = 1  # Menggunakan ulasan ID yang baru untuk produk Bardi
user_id_index = 0
product_id_index = 0

# Menghapus duplikat berdasarkan kolom 'comment'
sentiment_product_erigo.drop_duplicates(subset=["comment"], keep="first", inplace=True)

for i, review_data in sentiment_product_erigo.iterrows():
    user_id = user_data_erigo.iloc[user_id_index]["user_id"]
    product_id = products_erigo[product_id_index]["id"]

    user_name = user_data_erigo.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_erigo_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    erigo_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_erigo)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_erigo_id += 1

# Mengurutkan ulasan berdasarkan user_id
erigo_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_erigo = "./dataset/reviews_erigo.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_erigo, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in erigo_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(f"Data ulasan produk Erigo telah disimpan dalam file CSV: {csv_filename_erigo}")


####### Robot


user_data_robot = pd.read_csv("./dataset/user_data_robot.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_robot = pd.read_csv("./dataset/sentiment_product_robot.csv")


# Data ulasan produk Robot
robot_product_reviews = []
review_robot_id = review_erigo_id  # Menggunakan ulasan ID yang baru untuk produk Bardi
user_id_index = 0
product_id_index = 0


for i, review_data in sentiment_product_robot.iterrows():
    user_id = user_data_robot.iloc[user_id_index]["user_id"]
    product_id = product_robot[product_id_index]["id"]

    user_name = user_data_robot.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_robot_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    robot_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_robot)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_robot_id += 1

# Mengurutkan ulasan berdasarkan user_id
robot_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_robot = "./dataset/reviews_robot.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_robot, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in robot_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(f"Data ulasan produk Robot telah disimpan dalam file CSV: {csv_filename_robot}")


##### Sandisk

user_data_sandisk = pd.read_csv("./dataset/user_data_sandisk.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_sandisk = pd.read_csv("./dataset/sentiment_product_sandisk.csv")


# Data ulasan produk Sandisk
sandisk_product_reviews = []
review_sandisk_id = review_robot_id
user_id_index = 0
product_id_index = 0


for i, review_data in sentiment_product_sandisk.iterrows():
    user_id = user_data_sandisk.iloc[user_id_index]["user_id"]
    product_id = product_sandisk[product_id_index]["id"]

    user_name = user_data_sandisk.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_sandisk_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    sandisk_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_sandisk)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_sandisk_id += 1

# Mengurutkan ulasan berdasarkan user_id
sandisk_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_sandisk = "./dataset/reviews_sandisk.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_sandisk, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in sandisk_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(
    f"Data ulasan produk Sandisk telah disimpan dalam file CSV: {csv_filename_sandisk}"
)


# Teamgroup


user_data_teamgroup = pd.read_csv("./dataset/user_data_teamgroup.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_teamgroup = pd.read_csv("./dataset/sentiment_product_teamgroup.csv")

# Menghapus \n dari kolom 'comment'
sentiment_product_teamgroup["comment"] = sentiment_product_teamgroup[
    "comment"
].str.replace("\n", "")

# Data ulasan produk teamgroup
teamgroup_product_reviews = []
review_teamgroup_id = (
    review_sandisk_id  # Menggunakan ulasan ID yang baru untuk produk Bardi
)
user_id_index = 0
product_id_index = 0


for i, review_data in sentiment_product_teamgroup.iterrows():
    user_id = user_data_teamgroup.iloc[user_id_index]["user_id"]
    product_id = product_teamgroup[product_id_index]["id"]

    user_name = user_data_teamgroup.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_teamgroup_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    teamgroup_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_teamgroup)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_teamgroup_id += 1

# Mengurutkan ulasan berdasarkan user_id
teamgroup_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_teamgroup = "./dataset/reviews_teamgroup.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_teamgroup, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in teamgroup_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(
    f"Data ulasan produk teamgroup telah disimpan dalam file CSV: {csv_filename_teamgroup}"
)


# ### Gm333


user_data_gm = pd.read_csv("./dataset/user_data_gm.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_gm = pd.read_csv("./dataset/sentiment_product_gm.csv")


# Data ulasan produk gm
gm_product_reviews = []
review_gm_id = review_teamgroup_id  # Menggunakan ulasan ID yang baru untuk produk Bardi
user_id_index = 0
product_id_index = 0


for i, review_data in sentiment_product_gm.iterrows():
    user_id = user_data_gm.iloc[user_id_index]["user_id"]
    product_id = product_gm[product_id_index]["id"]

    user_name = user_data_gm.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_gm_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    gm_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_gm)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_gm_id += 1

# Mengurutkan ulasan berdasarkan user_id
gm_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_gm = "./dataset/reviews_gm.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_gm, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in gm_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(f"Data ulasan produk gm telah disimpan dalam file CSV: {csv_filename_gm}")


#### Rinnai

user_data_rinnai = pd.read_csv("./dataset/user_data_rinnai.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_rinnai = pd.read_csv("./dataset/sentiment_product_rinnai.csv")


# Data ulasan produk rinnai
rinnai_product_reviews = []
review_rinnai_id = review_gm_id
user_id_index = 0
product_id_index = 0


for i, review_data in sentiment_product_rinnai.iterrows():
    user_id = user_data_rinnai.iloc[user_id_index]["user_id"]
    product_id = product_rinnai[product_id_index]["id"]

    user_name = user_data_rinnai.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_rinnai_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    rinnai_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_rinnai)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_rinnai_id += 1

# Mengurutkan ulasan berdasarkan user_id
rinnai_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_rinnai = "./dataset/reviews_rinnai.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_rinnai, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in rinnai_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(f"Data ulasan produk rinnai telah disimpan dalam file CSV: {csv_filename_rinnai}")


# #### Xiamoi


user_data_xiaomi = pd.read_csv("./dataset/user_data_xiaomi.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_xiaomi = pd.read_csv("./dataset/sentiment_product_xiaomi.csv")

# Menghapus \n dari kolom 'comment'
sentiment_product_xiaomi["comment"] = sentiment_product_xiaomi["comment"].str.replace(
    "\n", ""
)

# Data ulasan produk xiaomi
xiaomi_product_reviews = []
review_xiaomi_id = (
    review_rinnai_id  # Menggunakan ulasan ID yang baru untuk produk Bardi
)
user_id_index = 0
product_id_index = 0


# sentiment_product_xiaomi.drop_duplicates(subset=["comment"], keep="first", inplace=True)

for i, review_data in sentiment_product_xiaomi.iterrows():
    user_id = user_data_xiaomi.iloc[user_id_index]["user_id"]
    product_id = product_xiaomi[product_id_index]["id"]

    user_name = user_data_xiaomi.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_xiaomi_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    xiaomi_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_xiaomi)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_xiaomi_id += 1

# Mengurutkan ulasan berdasarkan user_id
xiaomi_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_xiaomi = "./dataset/reviews_xiaomi.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_xiaomi, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in xiaomi_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(f"Data ulasan produk xiaomi telah disimpan dalam file CSV: {csv_filename_xiaomi}")


### Bardi

user_data_bardi = pd.read_csv("./dataset/user_data_bardi.csv")

# Memuat data ulasan produk Bardi dari file CSV
sentiment_product_bardi = pd.read_csv("./dataset/sentiment_product_bardi.csv")

# Menghapus \n dari kolom 'comment'
sentiment_product_bardi["comment"] = sentiment_product_bardi["comment"].str.replace(
    "\n", ""
)

# Data ulasan produk xiaomi
bardi_product_reviews = []
review_bardi_id = review_xiaomi_id  # Menggunakan ulasan ID yang baru untuk produk Bardi
user_id_index = 0
product_id_index = 0


# sentiment_product_xiaomi.drop_duplicates(subset=["comment"], keep="first", inplace=True)

for i, review_data in sentiment_product_bardi.iterrows():
    user_id = user_data_xiaomi.iloc[user_id_index]["user_id"]
    product_id = product_bardi[product_id_index]["id"]

    user_name = user_data_bardi.iloc[user_id_index]["nama"]
    random_rating = (
        round(random.uniform(3.9, 4.6), 1)
        if review_data["sentiment"] == "positif"
        else round(random.uniform(2, 3), 1)
    )
    review = {
        "id": review_bardi_id,
        "name": user_name,
        "user_id": user_id,
        "product_id": product_id,
        "comment": review_data["comment"],
        "sentiment": review_data["sentiment"],
        "rating": random_rating,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    bardi_product_reviews.append(review)

    # Pindah ke pengguna berikutnya atau ulasan produk berikutnya
    user_id_index = (user_id_index + 1) % len(user_data_xiaomi)
    product_id_index = (product_id_index + 1) % 5  # Ada 5 produk yang berbeda

    # Tingkatkan nilai ID ulasan
    review_bardi_id += 1

# Mengurutkan ulasan berdasarkan user_id
bardi_product_reviews.sort(key=lambda x: x["user_id"])

csv_filename_bardi = "./dataset/reviews_bardi.csv"

# Membuka file CSV untuk menulis data ulasan produk Bardi
with open(csv_filename_bardi, mode="w", newline="") as csv_file:
    fieldnames = [
        "id",
        "name",
        "comment",
        "rating",
        "sentiment",
        "user_id",
        "product_id",
        "created_at",
        "updated_at",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Menulis header
    writer.writeheader()

    # Menulis data ulasan produk Bardi ke dalam file CSV
    for review in bardi_product_reviews:
        writer.writerow(
            {
                "id": review["id"],
                "name": review["name"],
                "comment": review["comment"],
                "rating": review["rating"],
                "sentiment": review["sentiment"],
                "user_id": review["user_id"],
                "product_id": review["product_id"],
                "created_at": review["created_at"].strftime("%Y-%m-%d %H:%M:S"),
                "updated_at": review["updated_at"].strftime("%Y-%m-%d %H:%M:S"),
            }
        )

print(f"Data ulasan produk bardi telah disimpan dalam file CSV: {csv_filename_bardi}")
