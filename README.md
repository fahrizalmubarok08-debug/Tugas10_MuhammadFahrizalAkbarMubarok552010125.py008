#Tugas10_MuhammadFahrizalAkbarMubarok552010125.py008

# utils.py
# Berisi fungsi-fungsi untuk pengolahan data mahasiswa

# Fungsi menambahkan data mahasiswa ke dalam list
%%writefile utils.py
def tambah_mahasiswa(data, nama, n1, n2, n3):
    data.append({
        "nama": nama,
        "nilai": [n1, n2, n3]
    })


# Fungsi menghitung rata-rata nilai mahasiswa

def hitung_rata(nilai):
    return sum(nilai) / len(nilai)


# Fungsi menentukan status kelulusan

def status_lulus(rata):
    if rata >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus"
9

# Fungsi mencari mahasiswa dengan nilai rata-rata
# tertinggi dan terendah

def cari_max_min(data):
    if not data:
        return None, None

    # Hitung rata-rata untuk setiap mahasiswa
    rekap = [
        (mhs["nama"], hitung_rata(mhs["nilai"]))
        for mhs in data
    ]

    # max dan min berdasarkan rata-rata
    tertinggi = max(rekap, key=lambda x: x[1])
    terendah = min(rekap, key=lambda x: x[1])

    return tertinggi, terendah
