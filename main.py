
# main.py
# Program utama memanggil fungsi dari modul utils

import utils

# List untuk menyimpan data mahasiswa
database = []

print("=== PROGRAM SISTEM NILAI MAHASISWA (MODULAR) ===")

# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Input data mahasiswa
for i in range(jumlah):
    print(f"\nData ke-{i+1}")
    nama = input("Nama mahasiswa : ")
    n1 = float(input("Nilai 1 : "))
    n2 = float(input("Nilai 2 : "))
    n3 = float(input("Nilai 3 : "))

    # Memanggil fungsi tambah_mahasiswa
    utils.tambah_mahasiswa(database, nama, n1, n2, n3)


# Tampilkan hasil
print("\n=== HASIL REKAP NILAI ===")

for mhs in database:
    rata = utils.hitung_rata(mhs["nilai"])
    status = utils.status_lulus(rata)

    print(f"\nNama        : {mhs['nama']}")
    print(f"Nilai       : {mhs['nilai']}")
    print(f"Rata-rata   : {rata:.2f}")
    print(f"Status      : {status}")


# Mencari nilai tertinggi & terendah
max_mhs, min_mhs = utils.cari_max_min(database)

print("\n=== NILAI TERTINGGI & TERENDAH ===")
print(f"Nilai Tertinggi : {max_mhs[0]} (Rata-rata {max_mhs[1]:.2f})")
print(f"Nilai Terendah  : {min_mhs[0]} (Rata-rata {min_mhs[1]:.2f})")

print("\nProgram Selesai.")
