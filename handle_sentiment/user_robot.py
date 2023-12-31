import pandas as pd

user_data_robot = [
    (6, "jufianto henri", "jufianto_henri@gmail.com"),
    (7, "aan nuraini", "aan_nuraini@gmail.com"),
    (8, "abdur rahman", "abdur_rahman@gmail.com"),
    (9, "abdurrahman", "abdurrahman@gmail.com"),
    (10, "ade indra sukma", "ade_indra_sukma@gmail.com"),
    (46, "dede dwi arviyanti", "dede_dwi_arviyanti@gmail.com"),
    (47, "della maulina herianda", "della_maulina_herianda@gmail.com"),
    (48, "deny gustriansyah", "deny_gustriansyah@gmail.com"),
    (49, "desi fitri", "desi_fitri@gmail.com"),
    (50, "edmund andriano", "edmund_andriano@gmail.com"),
    # 11-20
    (86, "desri ardika", "desri_ardika@gmail.com"),
    (87, "dessy masdianata p", "dessy_masdianata_p@gmail.com"),
    (88, "destria membrane", "destria_membrane@gmail.com"),
    (89, "eka nur safitri", "eka_nur_safitri@gmail.com"),
    (90, "fauziah", "fauziah@gmail.com"),
    (126, "hijrah syahputra", "hijrah_syahputra@gmail.com"),
    (127, "indah rahmawati", "indah_rahmawati@gmail.com"),
    (128, "indra firman", "indra_firman@gmail.com"),
    (129, "indri dian pertiwi", "indri_dian_pertiwi@gmail.com"),
    (130, "kemal pasha", "kemal_pasha@gmail.com"),
    # 21-30
    (166, "nony chrisnayanti", "nony_chrisnayanti@gmail.com"),
    (167, "nora ferwati", "nora_ferwati@gmail.com"),
    (168, "nurul gayatri indah reza", "nurul_gayatri_indah_reza@gmail.com"),
    (169, "benny yohanes", "benny_yohanes@gmail.com"),
    (170, "elennuari", "elennuari@gmail.com"),
    (206, "novia kumala sari", "novia_kumala_sari@gmail.com"),
    (207, "padli nofrizal", "padli_nofrizal@gmail.com"),
    (208, "putri wahyuni", "putri_wahyuni@gmail.com"),
    (209, "rahmat hidayat", "rahmat_hidayat@gmail.com"),
    (210, "rahmi andreni", "rahmi_andreni@gmail.com"),
    # 31-40
    (246, "ridho", "ridho@gmail.com"),
    (247, "ridho fajri", "ridho_fajri@gmail.com"),
    (248, "ridho rismayanda", "ridho_rismayanda@gmail.com"),
    (249, "ridwan candra", "ridwan_candra@gmail.com"),
    (250, "rosdina", "rosdina@gmail.com"),
    (286, "rizkie hafizzah", "rizkie_hafizzah@gmail.com"),
    (287, "syaiful akbar", "syaiful_akbar@gmail.com"),
    (288, "nu' in sofyan", "nu'_in_sofyan@gmail.com"),
    (289, "sumirah", "sumirah@gmail.com"),
    (290, "ade surahman", "ade_surahman@gmail.com"),
    ## 41-50
    (326, "riza feri handoko", "riza_feri_handoko@gmail.com"),
    (327, "angga adhy surya", "angga_adhy_surya@gmail.com"),
    (328, "nelvin adhy renata", "nelvin_adhy_renata@gmail.com"),
    (329, "titis brigida silva", "titis_brigida_silva@gmail.com"),
    (330, "suroso", "suroso@gmail.com"),
    (366, "mardiana", "mardiana@gmail.com"),
    (367, "mustika sari", "mustika_sari@gmail.com"),
    (368, "mega mawarni", "mega_mawarni@gmail.com"),
    (369, "muhammad zamzari", "muhammad_zamzari@gmail.com"),
    (370, "air murya", "air_murya@gmail.com"),
    ## 51-60
    (406, "efi sulastri", "efi_sulastri@gmail.com"),
    (407, "wagimun", "wagimun@gmail.com"),
    (408, "girah", "girah@gmail.com"),
    (409, "feni safitri", "feni_safitri@gmail.com"),
    (410, "sumarno", "sumarno@gmail.com"),
    (446, "siti romlah", "siti_romlah@gmail.com"),
    (447, "ricky prayoga", "ricky_prayoga@gmail.com"),
    (448, "shafa mutia nurhaliza", "shafa_mutia_nurhaliza@gmail.com"),
    (449, "abdul malik", "abdul_malik@gmail.com"),
    (450, "kardi", "kardi@gmail.com"),
    ## 61-70
    (486, "mira mustika", "mira_mustika@gmail.com"),
    (487, "edi suyoto", "edi_suyoto@gmail.com"),
    (488, "rikana nurmala desi", "rikana_nurmala_desi@gmail.com"),
    (489, "zidane dhevan pratama", "zidane_dhevan_pratama@gmail.com"),
    (490, "mariyamah", "mariyamah@gmail.com"),
    (526, "setiawan", "setiawan@gmail.com"),
    (527, "sutiono", "sutiono@gmail.com"),
    (528, "nurhayati", "nurhayati@gmail.com"),
    (529, "oki aditia saputra", "oki_aditia_saputra@gmail.com"),
    (530, "hendrio junior", "hendrio_junior@gmail.com"),
    # 71-80
    (566, "wahyu iswan arif", "wahyu_iswan_arif@gmail.com"),
    (567, "ihwanul muslimin", "ihwanul_muslimin@gmail.com"),
    (568, "chomsin", "chomsin@gmail."),
    (569, "mutingah", "mutingah@gmail.com"),
    (570, "muhammad khoiron", "muhammad_khoiron@gmail.com"),
    (606, "widi yanti", "widi_yanti@gmail.com"),
    (607, "fitria lestari", "fitria_lestari@gmail.com"),
    (608, "muji astuti", "muji_astuti@gmail.com"),
    (609, "nurdiana saputri", "nurdiana_saputri@gmail.com"),
    (610, "saim", "saim@gmail.com"),
    # 81-90
    (646, "miseri", "miseri@gmail.com"),
    (647, "wartinah", "wartinah@gmail.com"),
    (648, "agus nuryanto", "agus_nuryanto@gmail.com"),
    (649, "syahrul widianto", "syahrul_widianto@gmail.com"),
    (650, "alif ardana", "alif_ardana@gmail.com"),
    (686, "fajri syahdan naufal", "fajri_syahdan_naufal@gmail.com"),
    (687, "wahidi", "wahidi@gmail.com"),
    (688, "jasiah", "jasiah@gmail.com"),
    (689, "eliyuswisnawaty", "eliyuswisnawaty@gmail.com"),
    (690, "sukijan", "sukijan@gmail.com"),
    # 91-100
    (726, "reni sriyati", "reni_sriyati@gmail.com"),
    (727, "rudi saputra", "rudi_saputra@gmail.com"),
    (728, "ervi lidya wati", "ervi_lidya_wati@gmail.com"),
    (729, "agus setiawan", "agus_setiawan@gmail.com"),
    (730, "tesa rismiani", "tesa_rismiani@gmail.com"),
    (766, "waluyo", "waluyo@gmail.com"),
    (767, "nuraini", "nuraini@gmail.com"),
    (768, "madha leli", "madha_leli@gmail.com"),
    (769, "rudianto", "rudianto@gmail.com"),
    (770, "istiani", "istiani@gmail.com"),
    # 101 - 110
    (806, "dimas dwi fadilah", "dimas_dwi_fadilah@gmail.com"),
    (807, "faiz ahza praditya", "faiz_ahza_praditya@gmail.com"),
    (808, "sudin", "sudin@gmail.com"),
    (809, "miswen", "miswen@gmail.com"),
    (810, "tukijo al rifa' i", "tukijo_al_rifa'_i@gmail.com"),
    (846, "rudi febrianto", "rudi_febrianto@gmail.com"),
    (847, "sugeng pribadi", "sugeng_pribadi@gmail.com"),
    (848, "sutiman", "sutiman@gmail.com"),
    (849, "ngatini", "ngatini@gmail.com"),
    (850, "ahmad nizam alfarizi", "ahmad_nizam_alfarizi@gmail.com"),
    # 111 - 120
    (886, "m. khuza alhasby", "m._khuza_alhasby@gmail.com"),
    (887, "ismail", "ismail@gmail.com"),
    (888, "susiati", "susiati@gmail.com"),
    (889, "qoridhotul mutakin", "qoridhotul_mutakin@gmail.com"),
    (890, "khafidhotus sany", "khafidhotus_sany@gmail.com"),
    (926, "m. tolib syahbarul", "m._tolib_syahbarul@gmail.com"),
    (927, "bela novitasari", "bela_novitasari@gmail.com"),
    (928, "muhammad afdal affandi", "muhammad_afdal_affandi@gmail.com"),
    (929, "dedi iswandi", "dedi_iswandi@gmail.com"),
    (930, "ahmad purwito", "ahmad_purwito@gmail.com"),
    # 121-130
    (966, "muhammad habibullah", "muhammad_habibullah@gmail.com"),
    (967, "ira afrianti", "ira_afrianti@gmail.com"),
    (968, "misbahatussudury", "misbahatussudury@gmail.com"),
    (969, "manto gumes", "manto_gumes@gmail.com"),
    (970, "tumirah", "tumirah@gmail.com"),
    (1006, "umi maslikhah", "umi_maslikhah@gmail.com"),
    (1007, "lilik supriyanto", "lilik_supriyanto@gmail.com"),
    (1008, "sunarti", "sunarti@gmail.com"),
    (1009, "revianita inka hadi", "revianita_inka_hadi@gmail.com"),
    (1010, "agung susilo", "agung_susilo@gmail.com"),
    # 131-140
    (1046, "sutomo", "sutomo@gmail.com"),
    (1047, "mariyem", "mariyem@gmail.com"),
    (1048, "setio purwanto", "setio_purwanto@gmail.com"),
    (1049, "tri tugas", "tri_tugas@gmail.com"),
    (1050, "tumiati", "tumiati@gmail.com"),
    (1086, "shela nur diana sari", "shela_nur_diana_sari@gmail.com"),
    (1087, "lhailatul istamaroh", "lhailatul_istamaroh@gmail."),
    (1088, "sudirman", "sudirman@gmail.com"),
    (1089, "atik winarni", "atik_winarni@gmail.com"),
    (1090, "sofyan ali syahbana", "sofyan_ali_syahbana@gmail.com"),
    # 141-150
    (1126, "tumiati", "tumiati@gmail.com"),
    (1127, "hanifatun nasyroh", "hanifatun_nasyroh@gmail.com"),
    (1128, "sutarman", "sutarman@gmail.com"),
    (1129, "ponirah", "ponirah@gmail.com"),
    (1130, "slamet harianto", "slamet_harianto@gmail.com"),
    (1166, "sofyan ali syahbana", "sofyan_ali_syahbana@gmail.com"),
    (1167, "nur aida dwi ramadhani", "nur_aida_dwi_ramadhani@gmail.com"),
    (1168, "arsy muhammad al habsy", "arsy_muhammad_al_habsy@gmail.com"),
    (1169, "pangidoan", "pangidoan@gmail.com"),
    (1170, "suwarni", "suwarni@gmail.com"),
    # 151-160
    (1206, "hani sali sati", "hani_sali_sati@gmail.com"),
    (1207, "alwan supangat", "alwan_supangat@gmail.com"),
    (1208, "sukirman", "sukirman@gmail.com"),
    (1209, "riyanti", "riyanti@gmail.com"),
    (1210, "rafika oktavianti", "rafika_oktavianti@gmail.com"),
    (1246, "desi ratnasari", "desi_ratnasari@gmail.com"),
    (1247, "abdul hanafi purba", "abdul_hanafi_purba@gmail.com"),
    (1248, "ibnu haris purba", "ibnu_haris_purba@gmail.com"),
    (1249, "arif suesanto purba", "arif_suesanto_purba@gmail.com"),
    (1250, "ade liyanti", "ade_liyanti@gmail.com"),
]

df = pd.DataFrame(user_data_robot, columns=["user_id", "nama", "email"])

df.to_csv("./dataset/user_data_robot.csv", index=False)

print("Data pengguna Robot telah disimpan dalam file CSV.")
