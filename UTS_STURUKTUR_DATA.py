# ==========================================
# Nama : Candra Winata
# NIM  : 20255520007
# Prodi : Informatika 
# ==========================================

# Array/List untuk menyimpan data mahasiswa
mahasiswa = [
    {"nim": "001", "nama": "Andi", "nilai": 85},
    {"nim": "002", "nama": "Budi", "nilai": 90},
    {"nim": "003", "nama": "Citra", "nilai": 75},
    {"nim": "004", "nama": "Dimas", "nilai": 95},
    {"nim": "005", "nama": "Eka", "nilai": 80}
]

# Tambah data mahasiswa
def tambah_data():
    print("\n========== TAMBAH DATA ==========")

    nim = input("Masukkan NIM   : ")

    # Validasi NIM agar tidak sama
    for mhs in mahasiswa:
        if mhs["nim"] == nim:
            print("NIM tersebut sudah digunakan.")
            return

    nama = input("Masukkan Nama  : ")

    try:
        nilai = int(input("Masukkan Nilai : "))

        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0 sampai 100.")
            return

    except ValueError:
        print("Nilai harus berupa angka.")
        return

    data_baru = {
        "nim": nim,
        "nama": nama,
        "nilai": nilai
    }

    mahasiswa.append(data_baru)
    print("Data mahasiswa berhasil ditambahkan.")

# Tampilan semua data mahasiswa
def tampilkan_data():
    print("\n========== DATA MAHASISWA ==========")

    if len(mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
        return

    print("------------------------------------------")
    print("NIM\tNama\t\tNilai")
    print("------------------------------------------")

    for mhs in mahasiswa:
        print(f"{mhs['nim']}\t{mhs['nama']}\t\t{mhs['nilai']}")
    print("------------------------------------------")

# Searching Linear Search untuk mencari mahasiswa berdasarkan NIM atau Nama
def cari_mahasiswa(kunci, berdasarkan):
    # Memeriksa data satu per satu
    for mhs in mahasiswa:
        if mhs[berdasarkan].lower() == kunci.lower():
            return mhs
    return None


def menu_pencarian():
    print("\n========== CARI MAHASISWA ==========")
    print("1. Cari berdasarkan NIM")
    print("2. Cari berdasarkan Nama")

    pilihan = input("Pilih pencarian: ")

    if pilihan == "1":
        nim = input("Masukkan NIM: ")
        hasil = cari_mahasiswa(nim, "nim")
    elif pilihan == "2":
        nama = input("Masukkan Nama: ")
        hasil = cari_mahasiswa(nama, "nama")
    else:
        print("Pilihan tidak valid.")
        return
    if hasil is not None:
        print("\nData ditemukan!")
        print("NIM   :", hasil["nim"])
        print("Nama  :", hasil["nama"])
        print("Nilai :", hasil["nilai"])
    else:
        print("Data mahasiswa tidak ditemukan.")

# Binary Search untuk mencari mahasiswa berdasarkan NIM
def binary_search_nim(target):
    # Membuat salinan data mahasiswa
    data = mahasiswa.copy()
    # Mengurutkan data berdasarkan NIM
    # menggunakan Bubble Sort
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]["nim"] > data[j + 1]["nim"]:
                data[j], data[j + 1] = (
                    data[j + 1],
                    data[j]
                )
                
    # Proses Binary Search
    kiri = 0
    kanan = len(data) - 1
    while kiri <= kanan:
        # Menentukan posisi tengah
        tengah = (kiri + kanan) // 2
        # Jika NIM ditemukan
        if data[tengah]["nim"] == target:
            return data[tengah]

        # Jika target lebih besar
        elif data[tengah]["nim"] < target:
            kiri = tengah + 1

        # Jika target lebih kecil
        else:
            kanan = tengah - 1
    return None

def menu_binary_search():
    print("\n========== BINARY SEARCH ==========")
    nim = input("Masukkan NIM yang dicari: ")
    hasil = binary_search_nim(nim)
    if hasil is not None:
        print("\nData ditemukan!")
        print("NIM   :", hasil["nim"])
        print("Nama  :", hasil["nama"])
        print("Nilai :", hasil["nilai"])

    else:
        print("Data mahasiswa tidak ditemukan.")
# Bubble Sort untuk mengurutkan data mahasiswa berdasarkan nilai
def bubble_sort(descending=True):
    n = len(mahasiswa)
    # Perulangan Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if descending:
                # Nilai terbesar ke terkecil
                if mahasiswa[j]["nilai"] < mahasiswa[j + 1]["nilai"]:
                    mahasiswa[j], mahasiswa[j + 1] = (
                        mahasiswa[j + 1],
                        mahasiswa[j]
                    )
            else:
                # Nilai terkecil ke terbesar
                if mahasiswa[j]["nilai"] > mahasiswa[j + 1]["nilai"]:
                    mahasiswa[j], mahasiswa[j + 1] = (
                        mahasiswa[j + 1],
                        mahasiswa[j]
                    )

def menu_sorting():
    print("\n========== URUTKAN NILAI ==========")
    print("1. Nilai tertinggi ke terendah")
    print("2. Nilai terendah ke tertinggi")

    pilihan = input("Pilih pengurutan: ")

    if pilihan == "1":
        bubble_sort(True)
        print("Data berhasil diurutkan dari nilai tertinggi.")
        tampilkan_data()  # ← TAMBAHKAN INI

    elif pilihan == "2":
        bubble_sort(False)
        print("Data berhasil diurutkan dari nilai terendah.")
        tampilkan_data()  # ← TAMBAHKAN INI

    else:
        print("Pilihan tidak valid.")
        
# 5. Rekursif: Hitung total nilai mahasiswa
def total_nilai(index=0):
    # Base case
    if index == len(mahasiswa):
        return 0
    # Recursive case
    return mahasiswa[index]["nilai"] + total_nilai(index + 1)

def tampilkan_total_nilai():
    print("\n========== TOTAL NILAI ==========")
    if len(mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
        return
    total = total_nilai()
    print("Total seluruh nilai mahasiswa:", total)

# Menu utama
def menu():
    while True:
        print("\n======================================")
        print("       SISTEM DAFTAR NILAI MAHASISWA")
        print("======================================")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data")
        print("3. Cari Mahasiswa")
        print("4. Urutkan Nilai")
        print("5. Hitung Total Nilai (Rekursif)")
        print("6. Keluar")
        print("======================================")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            menu_pencarian()
        elif pilihan == "4":
            menu_sorting()
        elif pilihan == "5":
            tampilkan_total_nilai()
        elif pilihan == "6":
            print("\nProgram selesai.")
            break
        else:
            print("Pilihan tidak valid.")

# Menjalankan program
menu()