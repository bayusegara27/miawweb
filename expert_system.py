class ExpertSystem:
    def __init__(self):
        # Daftar gejala dan penyakit dalam dictionary
        self.symptoms = {
            "G1": "Ruam merah pada kepala/punggung/ekor",
            "G2": "Ruam merah pada telinga",
            "G3": "Ruam bentuk abstrak",
            "G4": "Ruam bentuk bulat",
            "G5": "Bulu rontok pada seluruh tubuh",
            "G6": "Bulu rontok pada bagian terjangkit",
            "G7": "Gatal (menggaruk seluruh tubuh)",
            "G8": "Gatal (menggaruk punggung tengah)",
            "G9": "Gatal (menggaruk punggung ekor)",
            "G10": "Gatal (menggaruk telinga)",
            "G11": "Gatal (menggaruk kepala/kaki/ekor)",
            "G12": "Diare",
            "G13": "Diare disertai darah",
            "G14": "Diare berlendir",
            "G15": "Diare disertai cacing",
            "G16": "Pup normal disertai cacing",
            "G17": "Demam",
            "G18": "Demam tinggi",
            "G19": "Tidak mau makan/nafsu makan turun",
            "G20": "Berat badan turun",
            "G21": "Lemas",
            "G22": "Muntah",
            "G23": "Dehidrasi/gusi putih",
            "G24": "Pucat",
            "G25": "Nyeri di bagian perut",
            "G26": "Sesak napas",
            "G27": "Ikterus",
            "G28": "Radang mata",
            "G29": "Bulu kusam",
            "G30": "Selaput putih pada mata",
            "G31": "Telinga radang",
            "G32": "Sariawan",
            "G33": "Ngiler/ngeces",
            "G34": "Anemia",
            "G35": "Keropeng pada bagian tubuh",
            "G36": "Keropeng pada telinga",
            "G37": "Terdapat bintik merah",
            "G38": "Infeksi pada luka",
            "G39": "Terdapat banyak kutu",
            "G40": "Sering mengigit/menjilat tubuh",
            "G41": "Sering menggoyangkan kepala",
            "G42": "Kotoran telinga berwarna coklat kehitaman",
            "G43": "Terdapat luka lembab/basah",
            "G44": "Terdapat luka mengandung nanah"
        }

        # Aturan yang menghubungkan gejala dengan penyakit
        self.diseases_rules = {
            "P1": {"name": "Ringworm / kurap / dermathopysis",
                   "symptoms": ["G1", "G4", "G6", "G11"],
                   "solution": "a. Diberi obat jamur, bisa dalam bentuk salep atau minum (oral)\n"
                               "b. Grooming (dimandikan) secara rutin menggunakan sampo anti jamur\n"
                               "c. Hindari menempatkan kucing pada tempat yang lembab\n"
                               "d. Dipisah dari kucing yang lain agar tidak menular\n"
                               "e. Diberi pakan kucing khusus untuk kesehatan kulit\n"
                               "f. Apabila sudah parah lebih baik dibawa ke pengobatan dokter hewan"},
            "P2": {"name": "Salmonellosis / Tifus Kucing",
                   "symptoms": ["G12", "G17", "G19", "G21", "G22", "G23", "G24", "G25"],
                   "solution": "a. Diberi antibiotik dan penanganan sesuai gejala yang muncul\n"
                               "b. Diberikan makan berupa pakan kucing khusus untuk saluran pencernaan, bisa dibeli di petshop\n"
                               "c. Apabila sudah parah lebih baik dibawa ke pengobatan dokter hewan"},
            "P3": {"name": "Toxoplasmosis",
                   "symptoms": ["G12", "G17", "G18", "G19", "G21", "G22", "G23", "G26", "G27", "G28", "G29"],
                   "solution": "a. Dapat dilakukan terapi cairan (infus) jika kucing mengalami dehidrasi\n"
                               "b. Pemberian antibiotic/anti radang\n"
                               "c. Diberikan pakan kucing khusus recovery, bisa dibeli di petshop\n"
                               "d. Apabila sudah parah lebih baik dibawa ke pengobatan dokter hewan"},
            "P4": {"name": "Toxocara",
                   "symptoms": ["G5", "G12", "G13", "G14", "G15", "G16", "G17", "G19", "G22", "G23", "G29", "G30"],
                   "solution": "a. Diberikan obat cacing sesuai dengan dosis\n"
                               "b. Apabila sudah parah lebih baik dibawa ke pengobatan dokter hewan"},
            "P5": {"name": "FPV (Feline Panleukopenia Virus)",
                   "symptoms": ["G12", "G13", "G17", "G19", "G21", "G22", "G24", "G27", "G31", "G32", "G33"],
                   "solution": "a. Diberi infus, antibiotik, obat sesuai gejalanya, seperti obat anti muntah, anti diare\n"
                               "b. Diberi vaksin, vitamin tambahan\n"
                               "c. Dibawa ke dokter hewan"},
            "P6": {"name": "Kutuan / Infeksi Kutu",
                   "symptoms": ["G5", "G11", "G19", "G21", "G24", "G29", "G34", "G37", "G39", "G40"],
                   "solution": "a. Digrooming (dimandikan) dengan sampo kutu\n"
                               "b. Diberi obat anti parasite bisa dalam bentuk suntik atau tetes tengkuk (spot on)\n"
                               "c. Kucing disisir menggunakan sisir anti kutu\n"
                               "d. Apabila sudah parah lebih baik dibawa ke pengobatan dokter hewan"},
            "P7": {"name": "Scabies",
                   "symptoms": ["G1", "G5", "G11", "G35", "G36", "G37"],
                   "solution": "a. Diberikan anti parasite dalam bentuk suntik atau spot on\n"
                               "b. Kalau sudah parah, kucing jangan dimandikan, karena dapat membuatnya lebih parah\n"
                               "c. Dapat diberi vitamin / nutrisi kulit / bulu untuk kucing\n"
                               "d. Diberi makan pakan terapi khusus\n"
                               "e. Apabila sudah parah lebih baik dibawa ke pengobatan dokter hewan"},
            "P8": {"name": "Scabies Akut",
                   "symptoms": ["G1", "G5", "G11", "G35", "G36", "G37", "G38"],
                   "solution": "a. Diberi antibiotic\n"
                               "b. Dibawa kedokter"},
            "P9": {"name": "Feline Demodecosis",
                   "symptoms": ["G5", "G8", "G37", "G38", "G39", "G40"],
                   "solution": "a. Mandi ddengan obat antiekstoparasit"},
            "P10": {"name": "Feline Demodecosis Akut",
                    "symptoms": ["G5", "G8", "G19", "G20", "G37", "G38", "G39", "G40"],
                    "solution": "a. Dibawa kedokter hewan"},
            "P11": {"name": "Alopecia",
                    "symptoms": ["G5"],
                    "solution": "a. Diberi penyubur rambut"},
            "P12": {"name": "Flea Allergy Derma",
                    "symptoms": ["G5", "G9", "G38"],
                    "solution": "a. Dimandikan\n"
                                "b. Luka dibersihkan"},
            "P13": {"name": "Pruritus",
                    "symptoms": ["G7"],
                    "solution": "a. Pemberian obat anti radang"},
            "P14": {"name": "Ear Mite",
                    "symptoms": ["G2", "G10", "G38", "G41", "G42"],
                    "solution": "a. Pemberian obat antiekstoparasit"},
            "P15": {"name": "Pyoderma",
                    "symptoms": ["G3", "G6", "G38", "G43", "G44"],
                    "solution": "a. Luka dibershkan\n"
                                "b. Nanah dibersihkan"},
            "P16": {"name": "Hotspot",
                    "symptoms": ["G4", "G5", "G40", "G43"],
                    "solution": "a. Diberikan salep"},
                        "P17": {"name": "Feline Infectious Peritonitis (FIP)",
                    "symptoms": ["G18", "G19", "G21", "G22", "G23", "G27", "G28"],
                    "solution": "a. Terapi cairan untuk dehidrasi\n"
                                "b. Obat anti-inflamasi dan penguatan sistem imun\n"
                                "c. Segera konsultasi ke dokter hewan untuk perawatan intensif"},
            "P18": {"name": "Feline Lower Urinary Tract Disease (FLUTD)",
                    "symptoms": ["G19", "G21", "G25", "G26"],
                    "solution": "a. Diberi makanan khusus untuk kesehatan saluran kemih\n"
                                "b. Pastikan kucing memiliki akses air bersih\n"
                                "c. Segera bawa ke dokter hewan untuk perawatan jika gejala memburuk"},
            "P19": {"name": "Conjunctivitis",
                    "symptoms": ["G28", "G30"],
                    "solution": "a. Bersihkan mata dengan cairan khusus pembersih mata\n"
                                "b. Obat tetes mata antibiotik atau anti-radang\n"
                                "c. Jika kondisi memburuk, konsultasikan ke dokter hewan"},
            "P20": {"name": "Feline Leukemia Virus (FeLV)",
                    "symptoms": ["G17", "G18", "G19", "G24", "G34"],
                    "solution": "a. Berikan terapi suportif untuk meningkatkan kualitas hidup\n"
                                "b. Isolasi kucing dari kucing lain untuk mencegah penularan\n"
                                "c. Konsultasikan dengan dokter hewan untuk terapi lanjutan"},
            "P21": {"name": "Gastroenteritis",
                    "symptoms": ["G12", "G14", "G17", "G21", "G22"],
                    "solution": "a. Berikan makanan rendah serat yang mudah dicerna\n"
                                "b. Terapi cairan untuk mengatasi dehidrasi\n"
                                "c. Jika gejala menetap, bawa ke dokter hewan"},
            "P22": {"name": "Hyperthyroidism",
                    "symptoms": ["G19", "G20", "G21", "G33"],
                    "solution": "a. Berikan makanan khusus untuk mengontrol tiroid\n"
                                "b. Obat pengontrol tiroid yang diresepkan dokter hewan\n"
                                "c. Pemeriksaan rutin untuk memantau kondisi kesehatan"},
            "P23": {"name": "Otitis Externa",
                    "symptoms": ["G10", "G41", "G42", "G31"],
                    "solution": "a. Bersihkan telinga dengan cairan khusus pembersih telinga\n"
                                "b. Obat tetes telinga antibiotik atau antijamur\n"
                                "c. Konsultasikan ke dokter hewan jika kondisi tidak membaik"},
            "P24": {"name": "Lymphoma",
                    "symptoms": ["G17", "G19", "G20", "G21", "G27"],
                    "solution": "a. Kemoterapi untuk mengurangi perkembangan penyakit\n"
                                "b. Terapi suportif seperti vitamin tambahan\n"
                                "c. Konsultasikan dengan dokter hewan spesialis onkologi"},
            "P25": {"name": "Conjunctivitis",
                    "symptoms": ["G28", "G30"],
                    "solution": "a. Mata dibersihkan dengan cairan antiseptik\nb. Pemberian tetes mata antibiotik\nc. Dibawa ke dokter hewan untuk pemeriksaan lebih lanjut"
                    },
            "P26": {"name": "Cholangiohepatitis",
                    "symptoms": ["G17", "G18", "G25", "G27"],
                    "solution": "a. Pemberian terapi cairan\nb. Antibiotik\nc. Vitamin tambahan"
                    },
            "P27": {"name": "Feline Rhinotracheitis",
                    "symptoms": ["G18", "G26", "G31", "G33"],
                    "solution": "a. Pemberian obat antivirus\nb. Vitamin penambah daya tahan tubuh\nc. Dibawa ke dokter hewan"
                    },
            "P28": {"name": "Chronic Kidney Disease (CKD)",
                    "symptoms": ["G19", "G20", "G21", "G22", "G23"],
                    "solution": "a. Pemberian makanan renal diet\nb. Terapi cairan (infus)\nc. Obat sesuai gejala"
                    },
            "P29": {"name": "Otitis Externa",
                    "symptoms": ["G2", "G10", "G31", "G41", "G42"],
                    "solution": "a. Pembersihan telinga\nb. Obat tetes antiradang\nc. Antibiotik"
                },
            "P30": {"name": "Feline Asthma",
                    "symptoms": ["G26", "G33"],
                    "solution": "a. Pemberian obat bronkodilator\nb. Obat antiradang\nc. Hindari pemicu asma"
                },
            "P31": {"name": "Feline Hyperthyroidism",
                    "symptoms": ["G17", "G19", "G20", "G21"],
                    "solution": "a. Pemberian obat antitiroid\nb. Diet khusus\nc. Pemeriksaan rutin"
                },
            "P32": {"name": "Feline Diabetes",
                    "symptoms": ["G20", "G21", "G23", "G24"],
                    "solution": "a. Pemberian insulin\nb. Diet rendah karbohidrat\nc. Pemeriksaan kadar gula darah"
                },
            "P33": {"name": "Feline Infectious Peritonitis (FIP)",
                    "symptoms": ["G17", "G18", "G21", "G25", "G27", "G28"],
                    "solution": "a. Terapi cairan\nb. Vitamin tambahan\nc. Perawatan suportif"
                },
            "P34": {"name": "Feline Leukemia Virus (FeLV)",
                    "symptoms": ["G18", "G19", "G21", "G34"],
                    "solution": "a. Pemberian vitamin\nb. Antibiotik untuk infeksi sekunder\nc. Vaksinasi"
                },
            "P35": {"name": "Feline Calicivirus",
                    "symptoms": ["G32", "G33", "G28", "G18"],
                    "solution": "a. Pemberian antibiotik\nb. Obat antiinflamasi\nc. Terapi cairan"
                },
            "P36": {"name": "Feline Chlamydia",
                    "symptoms": ["G28", "G33"],
                    "solution": "a. Pemberian antibiotik\nb. Mata dibersihkan\nc. Obat tetes mata"
                },
            "P37": {"name": "Feline Bartonellosis",
                    "symptoms": ["G17", "G19", "G22"],
                    "solution": "a. Pemberian antibiotik\nb. Pemeriksaan darah\nc. Obat sesuai gejala"
                },
            "P38": {"name": "Feline Giardia",
                    "symptoms": ["G12", "G14", "G22"],
                    "solution": "a. Obat antiparasit\nb. Diet khusus\nc. Kebersihan lingkungan"
                },
            "P39": {"name": "Feline Cryptosporidiosis",
                    "symptoms": ["G13", "G22", "G23"],
                    "solution": "a. Obat antiparasit\nb. Terapi cairan\nc. Kebersihan lingkungan"
                },
            "P40": {"name": "Feline Mycoplasma",
                    "symptoms": ["G17", "G21", "G22", "G34"],
                    "solution": "a. Pemberian antibiotik\nb. Vitamin\nc. Pemeriksaan darah"
                },
            "P41": {"name": "Feline Hemobartonellosis",
                    "symptoms": ["G17", "G21", "G23", "G34"],
                    "solution": "a. Obat antibakteri\nb. Vitamin\nc. Terapi cairan"
                },
            "P42": {"name": "Feline Eosinophilic Granuloma Complex",
                    "symptoms": ["G35", "G36"],
                    "solution": "a. Obat antiradang\nb. Obat antibiotik\nc. Diet eliminasi"
                },
            "P43": {"name": "Feline Pododermatitis",
                    "symptoms": ["G43", "G44"],
                    "solution": "a. Pemberian antibiotik\nb. Obat antiradang\nc. Luka dibersihkan"
                },
            "P44": {"name": "Feline Gastritis",
                    "symptoms": ["G22", "G25"],
                    "solution": "a. Obat antiradang\nb. Diet khusus\nc. Terapi cairan"
                },
            "P45": {"name": "Feline Colitis",
                    "symptoms": ["G12", "G14", "G25"],
                    "solution": "a. Obat antiradang\nb. Diet khusus\nc. Terapi cairan"
                },
            "P46": {"name": "Feline Hepatic Lipidosis",
                    "symptoms": ["G19", "G20", "G21", "G25"],
                    "solution": "a. Terapi cairan\nb. Obat suportif\nc. Diet khusus"
                },
            "P47": {"name": "Feline Hypertrophic Cardiomyopathy",
                    "symptoms": ["G26", "G24"],
                    "solution": "a. Obat jantung\nb. Pemeriksaan rutin\nc. Hindari stres"
                },
            "P48": {"name": "Feline Lower Urinary Tract Disease (FLUTD)",
                    "symptoms": ["G25", "G22", "G24"],
                    "solution": "a. Obat antiradang\nb. Diet khusus\nc. Terapi cairan"
                },
            "P49": {"name": "Feline Lymphoma",
                    "symptoms": ["G17", "G18", "G21", "G19"],
                    "solution": "a. Kemoterapi\nb. Terapi cairan\nc. Obat suportif"
                },
            "P50": {"name": "Feline Infectious Anemia",
                    "symptoms": ["G17", "G34"],
                    "solution": "a. Pemberian antibiotik\nb. Transfusi darah\nc. Terapi cairan"
                }          
        }



    def diagnose(self, user_symptoms):
        # Melakukan pencocokan gejala dengan aturan penyakit
        possible_diseases = []
        for code, disease in self.diseases_rules.items():
            # Hitung berapa banyak gejala yang cocok dengan gejala penyakit
            matched_symptoms = [symptom for symptom in disease["symptoms"] if symptom in user_symptoms]
            # Jika semua gejala terpenuhi atau lebih dari 5 gejala terpenuhi, tambahkan ke hasil
            if len(matched_symptoms) == len(disease["symptoms"]) or len(matched_symptoms) >= 2:
                possible_diseases.append((disease["name"], disease, len(matched_symptoms)))

    # Hasil diagnosis
        if possible_diseases:
            print("Kemungkinan penyakit berdasarkan gejala yang diberikan:\n")
            # Urutkan penyakit berdasarkan jumlah gejala yang cocok
            possible_diseases.sort(key=lambda x: x[2], reverse=True)
            for disease_name, disease_info, count in possible_diseases:
                print(f"- {disease_name} (cocok dengan {count} gejala)")
                print("Solusi:")
                print(f"{disease_info['solution']}\n")
        else:
            print("Tidak ada penyakit yang cocok dengan gejala yang diberikan.")


# Contoh penggunaan sistem pakar
if __name__ == "__main__":
    # Instansiasi sistem pakar
    system = ExpertSystem()
