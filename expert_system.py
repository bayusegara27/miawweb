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
                    "solution": "a. Diberikan salep"}
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