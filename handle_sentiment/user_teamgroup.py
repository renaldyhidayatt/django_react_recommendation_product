import pandas as pd

user_data_teamgroup = [
    (16, "edi kurniawan wibowo", "edi_kurniawan_wibowo@gmail.com"),
    (17, "fadil rahmat andini", "fadil_rahmat_andini@gmail.com"),
    (18, "fahmi iqbal firmananda", "fahmi_iqbal_firmananda@gmail.com"),
    (19, "fairuzi", "fairuzi@gmail.com"),
    (20, "gustian", "gustian@gmail.com"),
    (56, "ikbal gazalba", "ikbal_gazalba@gmail.com"),
    (57, "ikhsan firdaus", "ikhsan_firdaus@gmail.com"),
    (58, "ilda ikhwana lubis", "ilda_ikhwana_lubis@gmail.com"),
    (59, "jayus suryawan", "jayus_suryawan@gmail.com"),
    (60, "muhammad bagoes samaron", "muhammad_bagoes_samaron@gmail.com"),
    (96, "jukhri syahputra", "jukhri_syahputra@gmail.com"),
    (97, "m. muawam", "m._muawam@gmail.com"),
    (98, "m. yassir saputra jamina", "m._yassir_saputra_jamina@gmail.com"),
    (99, "mardiyyat fadliellah", "mardiyyat_fadliellah@gmail.com"),
    (100, "mukhtar lutfi", "mukhtar_lutfi@gmail.com"),
    (136, "nofan widiyarna", "nofan_widiyarna@gmail.com"),
    (137, "nurudin rahman", "nurudin_rahman@gmail.com"),
    (138, "puji astuti", "puji_astuti@gmail.com"),
    (139, "refi delia", "refi_delia@gmail.com"),
    (140, "reno mulia sari", "reno_mulia_sari@gmail.com"),
    (176, "resti yulia", "resti_yulia@gmail.com"),
    (177, "reysa hastarimasuci", "reysa_hastarimasuci@gmail.com"),
    (178, "reza fahlevi", "reza_fahlevi@gmail.com"),
    (179, "rhesma naca", "rhesma_naca@gmail.com"),
    (180, "rudi wijaya", "rudi_wijaya@gmail.com"),
    (216, "ruwadi saputra", "ruwadi_saputra@gmail.com"),
    (217, "sugeng hermawan", "sugeng_hermawan@gmail.com"),
    (218, "suliatun", "suliatun@gmail.com"),
    (219, "tomi ismeidianto", "tomi_ismeidianto@gmail.com"),
    (220, "usthalay putra", "usthalay_putra@gmail.com"),
    (256, "yuni dwi hastuti", "yuni_dwi_hastuti@gmail.com"),
    (257, "aulia rahman", "aulia_rahman@gmail.com"),
    (258, "agung kurniawan", "agung_kurniawan@gmail.com"),
    (259, "ahmad fauzi paturusi", "ahmad_fauzi_paturusi@gmail.com"),
    (260, "arie biola gunti masuko", "arie_biola_gunti_masuko@gmail.com"),
    (296, "laily mufarokah", "laily_mufarokah@gmail.com"),
    (297, "sigit nugroho", "sigit_nugroho@gmail.com"),
    (298, "linda rusmi wardani", "linda_rusmi_wardani@gmail.com"),
    (299, "m. charly iman nugroho", "m._charly_iman_nugroho@gmail.com"),
    (300, "untung sugiono", "untung_sugiono@gmail.com"),
    (336, "muhammad prayoga winata", "muhammad_prayoga_winata@gmail.com"),
    (337, "heru setyono", "heru_setyono@gmail.com"),
    (338, "sri mulyani", "sri_mulyani@gmail.com"),
    (339, "galih subekti", "galih_subekti@gmail.com"),
    (340, "ageng kurniawan", "ageng_kurniawan@gmail.com"),
    (376, "rasman", "rasman@gmail.com"),
    (377, "riya ningsih", "riya_ningsih@gmail.com"),
    (378, "uji ifandy saputra", "uji_ifandy_saputra@gmail.com"),
    (379, "hana aida sahila", "hana_aida_sahila@gmail.com"),
    (380, "mufizar ilyas", "mufizar_ilyas@gmail.com"),
    (416, "rizki pratama", "rizki_pratama@gmail.com"),
    (417, "yanto", "yanto@gmail.com"),
    (418, "puji lestari", "puji_lestari@gmail.com"),
    (419, "dewi wulan ningsih", "dewi_wulan_ningsih@gmail.com"),
    (420, "aril aji alania", "aril_aji_alania@gmail.com"),
    (456, "anin khamidah", "anin_khamidah@gmail.com"),
    (457, "diram", "diram@gmail.com"),
    (458, "muslimah", "muslimah@gmail.com"),
    (459, "eko kurniawan", "eko_kurniawan@gmail.com"),
    (460, "romadon nur hidayat", "romadon_nur_hidayat@gmail.com"),
    (496, "kholipah", "kholipah@gmail.com"),
    (497, "abdul kholik", "abdul_kholik@gmail.com"),
    (498, "dede adiyanto", "dede_adiyanto@gmail.com"),
    (499, "handani nurul hidayah", "handani_nurul_hidayah@gmail.com"),
    (500, "mustofa", "mustofa@gmail.com"),
    (536, "desi susanti", "desi_susanti@gmail.com"),
    (537, "muhyatin", "muhyatin@gmail.com"),
    (538, "astriyah", "astriyah@gmail.com"),
    (539, "ikhsan amirrudin", "ikhsan_amirrudin@gmail.com"),
    (540, "edi susanto", "edi_susanto@gmail.com"),
    (576, "soni haji rifa'i", "soni_haji_rifa'i@gmail.com"),
    (577, "munib alwi abdurohman", "munib_alwi_abdurohman@gmail.com"),
    (578, "aliyatul mu'afa", "aliyatul_mu'afa@gmail.com"),
    (579, "hasim as'ari", "hasim_as'ari@gmail.com"),
    (580, "fathi nur sidiq", "fathi_nur_sidiq@gmail.com"),
    (616, "jurianto", "jurianto@gmail.com"),
    (617, "sri wahyuni", "sri_wahyuni@gmail.com"),
    (618, "pratama ade kurniawan", "pratama_ade_kurniawan@gmail.com"),
    (619, "erianto", "erianto@gmail.com"),
    (620, "tuti rahayu", "tuti_rahayu@gmail.com"),
    (656, "karmidi", "karmidi@gmail.com"),
    (657, "wilmaini", "wilmaini@gmail.com"),
    (658, "debyo widya anggara", "debyo_widya_anggara@gmail.com"),
    (659, "silvi widya pangesti", "silvi_widya_pangesti@gmail.com"),
    (660, "auliya nur syahidah", "auliya_nur_syahidah@gmail.com"),
    (696, "ahmad safi'i", "ahmad_safi'i@gmail.com"),
    (697, "habibi nurrohim", "habibi_nurrohim@gmail.com"),
    (698, "sulasikin nasukah", "sulasikin_nasukah@gmail.com"),
    (699, "jamilatun azizah", "jamilatun_azizah@gmail.com"),
    (700, "suparlan", "suparlan@gmail.com"),
    (736, "darma sahputra", "darma_sahputra@gmail.com"),
    (737, "supriani", "supriani@gmail.com"),
    (738, "rhamasya damar", "rhamasya_damar@gmail.com"),
    (739, "supratman", "supratman@gmail.com"),
    (740, "nanang mujahid", "nanang_mujahid@gmail.com"),
    (776, "solehan", "solehan@gmail.com"),
    (777, "komsidah", "komsidah@gmail.com"),
    (778, "yuli adi putra", "yuli_adi_putra@gmail.com"),
    (779, "ria rasela", "ria_rasela@gmail.com"),
    (780, "solehan", "solehan@gmail.com"),
    (816, "salim", "salim@gmail.com"),
    (817, "tukini", "tukini@gmail.com"),
    (818, "slamet", "slamet@gmail.com"),
    (819, "bini suharyati", "bini_suharyati@gmail.com"),
    (820, "fendi selistiawan", "fendi_selistiawan@gmail.com"),
    (856, "gino", "gino@gmail.com"),
    (857, "nurhayati", "nurhayati@gmail.com"),
    (858, "cici ramadhayanti", "cici_ramadhayanti@gmail.com"),
    (859, "afni dwi lestari", "afni_dwi_lestari@gmail.com"),
    (860, "trisno", "trisno@gmail.com"),
    (896, "aris anggraini", "aris_anggraini@gmail.com"),
    (897, "dian nur artika sari", "dian_nur_artika_sari@gmail.com"),
    (898, "lisa tri yunita", "lisa_tri_yunita@gmail.com"),
    (899, "kasmari", "kasmari@gmail.com"),
    (900, "munik nurhayati", "munik_nurhayati@gmail.com"),
    (936, "seli hapti anggara", "seli_hapti_anggara@gmail.com"),
    (937, "rasidin", "rasidin@gmail.com"),
    (938, "rebo", "rebo@gmail.com"),
    (939, "kasih", "kasih@gmail.com"),
    (940, "ilham setiaji", "ilham_setiaji@gmail.com"),
    (976, "isni", "isni@gmail.com"),
    (977, "suprihatin", "suprihatin@gmail.com"),
    (978, "peni untari", "peni_untari@gmail.com"),
    (979, "tomi ramdani", "tomi_ramdani@gmail.com"),
    (980, "riki supendi", "riki_supendi@gmail.com"),
    (1016, "abdul rahman", "abdul_rahman@gmail.com"),
    (1017, "m. zaenuri", "m._zaenuri@gmail.com"),
    (1018, "tri murtini", "tri_murtini@gmail.com"),
    (1019, "leny faridhotul mutmaini", "leny_faridhotul_mutmaini@gmail.com"),
    (1020, "azizah hanifatur rahma", "azizah_hanifatur_rahma@gmail.com"),
    (1056, "sunarti", "sunarti@gmail.com"),
    (1057, "lukman wibowo. s", "lukman_wibowo._s@gmail.com"),
    (1058, "iman wahyudi", "iman_wahyudi@gmail.com"),
    (1059, "hariyono", "hariyono@gmail.com"),
    (1060, "mami hernawati", "mami_hernawati@gmail.com"),
    (1096, "azizah hanifatur rahma", "azizah_hanifatur_rahma@gmail.com"),
    (1097, "ahmad hasinul fikqih", "ahmad_hasinul_fikqih@gmail.com"),
    (1098, "annida hasnaul atika", "annida_hasnaul_atika@gmail.com"),
    (1099, "jalal", "jalal@gmail.com"),
    (1100, "supri ani", "supri_ani@gmail.com"),
    (1136, "mami hernawati", "mami_hernawati@gmail.com"),
    (1137, "m. irfani", "m._irfani@gmail.com"),
    (1138, "sagiyati", "sagiyati@gmail.com"),
    (1139, "andi sofyan", "andi_sofyan@gmail.com"),
    (1140, "fita eviyana", "fita_eviyana@gmail.com"),
    (1176, "badriah", "badriah@gmail.com"),
    (1177, "harisun", "harisun@gmail.com"),
    (1178, "hali maskur", "hali_maskur@gmail.com"),
    (1179, "yusuf", "yusuf@gmail.com"),
    (1180, "bukhori", "bukhori@gmail.com"),
    (1216, "suliyatin", "suliyatin@gmail.com"),
    (1217, "catur suroso", "catur_suroso@gmail.com"),
    (1218, "rafika dewi sari", "rafika_dewi_sari@gmail.com"),
    (1219, "dian nur assyfa", "dian_nur_assyfa@gmail.com"),
    (1220, "abdul hamid", "abdul_hamid@gmail.com"),
    (1256, "sudarseh", "sudarseh@gmail.com"),
    (1257, "siti juwariyah", "siti_juwariyah@gmail.com"),
    (1258, "munirul ikhwan", "munirul_ikhwan@gmail.com"),
    (1259, "ahmad farid", "ahmad_farid@gmail.com"),
    (1260, "apriyani", "apriyani@gmail.com"),
]

df = pd.DataFrame(user_data_teamgroup, columns=["user_id", "nama", "email"])

df.to_csv("./dataset/user_data_teamgroup.csv", index=False)

print("Data pengguna Teamgroup telah disimpan dalam file CSV.")
