import pandas as pd


user_data_sandisk = [
    (11, "ade irmayani", "ade_irmayani@gmail.com"),
    (12, "bakti yoga fiyandana", "bakti_yoga_fiyandana@gmail.com"),
    (13, "daniel sepra fatama", "daniel_sepra_fatama@gmail.com"),
    (14, "dayu m sandro", "dayu_m_sandro@gmail.com"),
    (15, "dean mareti hariani", "dean_mareti_hariani@gmail.com"),
    (51, "fajar aulia rahman", "fajar_aulia_rahman@gmail.com"),
    (52, "fathiya hasyifah sibarani", "fathiya_hasyifah_sibarani@gmail.com"),
    (53, "fauzar", "fauzar@gmail.com"),
    (54, "habzer maisera", "habzer_maisera@gmail.com"),
    (55, "herzavina", "herzavina@gmail.com"),
    (91, "feny afrisilia", "feny_afrisilia@gmail.com"),
    (92, "hesty afriani srg", "hesty_afriani_srg@gmail.com"),
    (93, "ilham afandi aziz", "ilham_afandi_aziz@gmail.com"),
    (94, "ilham fajri", "ilham_fajri@gmail.com"),
    (95, "indah permata sari", "indah_permata_sari@gmail.com"),
    (131, "muhammad sayuti nur nasution", "muhammad_sayuti_nur_nasution@gmail.com"),
    (132, "miftahur ridho", "miftahur_ridho@gmail.com"),
    (133, "mila yuli yanti", "mila_yuli_yanti@gmail.com"),
    (134, "muhammad wendi hidayat", "muhammad_wendi_hidayat@gmail.com"),
    (135, "nikawati", "nikawati@gmail.com"),
    (171, "harika vaizal", "harika_vaizal@gmail.com"),
    (172, "hildayanti oktaviana", "hildayanti_oktaviana@gmail.com"),
    (173, "khairul fahmi purba", "khairul_fahmi_purba@gmail.com"),
    (174, "muhammad triyoga sp", "muhammad_triyoga_sp@gmail.com"),
    (175, "putri lia lestari", "putri_lia_lestari@gmail.com"),
    (211, "rian aries fani", "rian_aries_fani@gmail.com"),
    (212, "riandi selvi", "riandi_selvi@gmail.com"),
    (213, "rianto", "rianto@gmail.com"),
    (214, "ridha ulva", "ridha_ulva@gmail.com"),
    (215, "rizqi wahyuningsih", "rizqi_wahyuningsih@gmail.com"),
    (251, "supriadi", "supriadi@gmail.com"),
    (252, "suriyani", "suriyani@gmail.com"),
    (253, "tommy zul hidayat", "tommy_zul_hidayat@gmail.com"),
    (254, "umi riyani", "umi_riyani@gmail.com"),
    (255, "wiwik sumarmi", "wiwik_sumarmi@gmail.com"),
    (291, "kasnanto", "kasnanto@gmail.com"),
    (292, "sumirah", "sumirah@gmail.com"),
    (293, "teguh wahyudi", "teguh_wahyudi@gmail.com"),
    (294, "sakiyo", "sakiyo@gmail.com"),
    (295, "dwi kasmini", "dwi_kasmini@gmail.com"),
    (331, "sukati", "sukati@gmail.com"),
    (332, "depri selamet ariadi", "depri_selamet_ariadi@gmail.com"),
    (333, "isti nurjanah", "isti_nurjanah@gmail.com"),
    (334, "ruswantoro", "ruswantoro@gmail.com"),
    (335, "juli anggraeni", "juli_anggraeni@gmail.com"),
    (371, "sumardi", "sumardi@gmail.com"),
    (372, "surni", "surni@gmail.com"),
    (373, "wahid suprayitno", "wahid_suprayitno@gmail.com"),
    (374, "sutramiati", "sutramiati@gmail.com"),
    (375, "susanti lestari", "susanti_lestari@gmail.com"),
    (411, "nurimah", "nurimah@gmail.com"),
    (412, "noviana anggraeni", "noviana_anggraeni@gmail.com"),
    (413, "aissyah dwi zhaskia", "aissyah_dwi_zhaskia@gmail.com"),
    (414, "hariri", "hariri@gmail.com"),
    (415, "ida budiani", "ida_budiani@gmail.com"),
    (451, "sumini", "sumini@gmail.com"),
    (452, "andika saputra", "andika_saputra@gmail.com"),
    (453, "habib hidayaturrohman", "habib_hidayaturrohman@gmail.com"),
    (454, "wiwik wulandari", "wiwik_wulandari@gmail.com"),
    (455, "m. souvil anam", "m._souvil_anam@gmail.com"),
    (491, "giatno", "giatno@gmail.com"),
    (492, "siti ngaisah", "siti_ngaisah@gmail.com"),
    (493, "ahmad rasyid", "ahmad_rasyid@gmail.com"),
    (494, "gilang nur bekti", "gilang_nur_bekti@gmail.com"),
    (495, "abas suyatno", "abas_suyatno@gmail.com"),
    (531, "masinah", "masinah@gmail.com"),
    (532, "d. maulana", "d._maulana@gmail.com"),
    (533, "kasri", "kasri@gmail.com"),
    (534, "salami", "salami@gmail.com"),
    (535, "eko rudiyanto", "eko_rudiyanto@gmail.com"),
    (571, "zen mahrom", "zen_mahrom@gmail.com"),
    (572, "m. husmudin", "m._husmudin@gmail.com"),
    (573, "siti nur azijah", "siti_nur_azijah@gmail.com"),
    (574, "agus sugianto", "agus_sugianto@gmail.com"),
    (575, "siti umayah", "siti_umayah@gmail.com"),
    (611, "supingatun", "supingatun@gmail.com"),
    (612, "indra yani", "indra_yani@gmail.com"),
    (613, "munawaroh", "munawaroh@gmail.com"),
    (614, "sanadi saleh", "sanadi_saleh@gmail.com"),
    (615, "musaadah", "musaadah@gmail.com"),
    (651, "mujianto", "mujianto@gmail.com"),
    (652, "puji astuti", "puji_astuti@gmail.com"),
    (653, "ahmad aji supriono", "ahmad_aji_supriono@gmail.com"),
    (654, "rifa'i dwi cahyo", "rifa'i_dwi_cahyo@gmail.com"),
    (655, "ayla amelia nur", "ayla_amelia_nur@gmail.com"),
    (691, "sudarmi", "sudarmi@gmail.com"),
    (692, "siti zaenap", "siti_zaenap@gmail.com"),
    (693, "sodikin", "sodikin@gmail.com"),
    (694, "mas' ud", "mas'_ud@gmail.com"),
    (695, "sutinem", "sutinem@gmail.com"),
    (731, "ellenna yuliani putri. s", "ellenna_yuliani_putri._s@gmail.com"),
    (732, "saiman", "saiman@gmail.com"),
    (733, "surti", "surti@gmail.com"),
    (734, "pirawati", "pirawati@gmail.com"),
    (735, "triani", "triani@gmail.com"),
    (771, "vega miftaqul rizka", "vega_miftaqul_rizka@gmail.com"),
    (772, "meilany putri sakinah", "meilany_putri_sakinah@gmail.com"),
    (773, "akbar rizki saputra", "akbar_rizki_saputra@gmail.com"),
    (774, "safira cantika fitriani", "safira_cantika_fitriani@gmail.com"),
    (775, "slamet teguh santoso", "slamet_teguh_santoso@gmail.com"),
    (811, "winarti", "winarti@gmail.com"),
    (812, "irvan maulana", "irvan_maulana@gmail.com"),
    (813, "alfin akbar rifa'i", "alfin_akbar_rifa'i@gmail.com"),
    (814, "samidi", "samidi@gmail.com"),
    (815, "paijem", "paijem@gmail.com"),
    (851, "syahrul", "syahrul@gmail.com"),
    (852, "ngadinem", "ngadinem@gmail.com"),
    (853, "elly kumala sari", "elly_kumala_sari@gmail.com"),
    (854, "nanda ayu nur halizzah", "nanda_ayu_nur_halizzah@gmail.com"),
    (855, "muksin", "muksin@gmail.com"),
    (891, "syafia zahra aprelia", "syafia_zahra_aprelia@gmail.com"),
    (892, "slamet", "slamet@gmail.com"),
    (893, "eka restiawati", "eka_restiawati@gmail.com"),
    (894, "m. aditya hatta", "m._aditya_hatta@gmail.com"),
    (895, "sumarno", "sumarno@gmail.com"),
    (931, "agustina muntikawati", "agustina_muntikawati@gmail.com"),
    (932, "ali hamzah", "ali_hamzah@gmail.com"),
    (933, "dewi", "dewi@gmail.com"),
    (934, "evi alisma", "evi_alisma@gmail.com"),
    (935, "egi aulia pirdaus", "egi_aulia_pirdaus@gmail.com"),
    (971, "ali mustopo", "ali_mustopo@gmail.com"),
    (972, "siti maemunah", "siti_maemunah@gmail.com"),
    (973, "aisah", "aisah@gmail.com"),
    (974, "sapin", "sapin@gmail.com"),
    (975, "nur khalim", "nur_khalim@gmail.com"),
    (1011, "ira susanti", "ira_susanti@gmail.com"),
    (1012, "silvia ayu nadira rahmawati", "silvia_ayu_nadira_rahmawati@gmail.com"),
    (1013, "ngadiman", "ngadiman@gmail.com"),
    (1014, "sriyatun", "sriyatun@gmail.com"),
    (1015, "een romlah", "een_romlah@gmail.com"),
    (1051, "hanifatun nasyroh", "hanifatun_nasyroh@gmail.com"),
    (1052, "sutarman", "sutarman@gmail.com"),
    (1053, "ponirah", "ponirah@gmail.com"),
    (1054, "slamet harianto", "slamet_harianto@gmail.com"),
    (1055, "sumarno", "sumarno@gmail.com"),
    (1091, "nur aida dwi ramadhani", "nur_aida_dwi_ramadhani@gmail.com"),
    (1092, "arsy muhammad al habsy", "arsy_muhammad_al_habsy@gmail.com"),
    (1093, "m. zaenuri", "m._zaenuri@gmail.com"),
    (1094, "tri murtini", "tri_murtini@gmail.com"),
    (1095, "leny faridhotul mutmaini", "leny_faridhotul_mutmaini@gmail.com"),
    (1131, "santi susanti", "santi_susanti@gmail.com"),
    (1132, "nyaman", "nyaman@gmail.com"),
    (1133, "rusmiyati", "rusmiyati@gmail.com"),
    (1134, "taufik usman", "taufik_usman@gmail.com"),
    (1135, "suci melia putri", "suci_melia_putri@gmail.com"),
    (1171, "nurliani", "nurliani@gmail.com"),
    (1172, "safiq heryanto", "safiq_heryanto@gmail.com"),
    (1173, "rahmat", "rahmat@gmail.com"),
    (1174, "yunersen", "yunersen@gmail.com"),
    (1175, "ahmad muttakin", "ahmad_muttakin@gmail.com"),
    (1211, "dwi kurniasih", "dwi_kurniasih@gmail.com"),
    (1212, "m. tri ananta anugrah", "m._tri_ananta_anugrah@gmail.com"),
    (1213, "rajiman", "rajiman@gmail.com"),
    (1214, "leginem", "leginem@gmail.com"),
    (1215, "suparjo", "suparjo@gmail.com"),
    (1251, "jubadi", "jubadi@gmail.com"),
    (1252, "citra ayu wulandari", "citra_ayu_wulandari@gmail.com"),
    (1253, "surya dwi syahputra", "surya_dwi_syahputra@gmail.com"),
    (1254, "jumali", "jumali@gmail.com"),
    (1255, "adi widjoyo", "adi_widjoyo@gmail.com"),
]

df = pd.DataFrame(user_data_sandisk, columns=["user_id", "nama", "email"])

df.to_csv("./dataset/user_data_sandisk.csv", index=False)

print("Data pengguna Sandisk telah disimpan dalam file CSV.")
