import os

# Fungsi untuk membaca data dari file dan mengubahnya menjadi dictionary
def baca_file_dict(file):
    data_dict = {}
    if not os.path.exists(file):
        return data_dict

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.strip().split(':', 1)
            data_dict[key.strip()] = value.strip()
    
    return data_dict

# Fungsi untuk menyimpan dictionary ke file
def simpan_file_dict(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}:{value}\n")

# Fungsi untuk melihat data dari ketiga file
def lihat_data(nama_data, jenis_data, warna_data):
    ids = nama_data.keys()
    for id_ikan in ids:
        nama_ikan = nama_data.get(id_ikan, "Tidak Ditemukan")
        jenis_ikan = jenis_data.get(id_ikan, "Tidak Ditemukan")
        warna_ikan = warna_data.get(id_ikan, "Tidak Ditemukan")

        # Menampilkan output dalam format yang diinginkan
        print(f"{id_ikan}.{nama_ikan}:{jenis_ikan}:{warna_ikan}")

# Fungsi untuk menambah data ke tiga file
def tambah_data(nama_file, jenis_file, warna_file, nama_data, jenis_data, warna_data):
    id_ikan = str(len(nama_data) + 1)  # ID baru otomatis
    nama_ikan = input("Masukkan nama ikan: ")

    # Tampilkan pilihan jenis ikan
    print("Kode jenis ikan yang tersedia:")
    for key, value in jenis_data.items():
        print(f"{key}: {value}")
    
    jenis_ikan = input("Masukkan kode jenis ikan: ")

    # Tampilkan pilihan warna ikan
    print("Kode warna ikan yang tersedia:")
    for key, value in warna_data.items():
        print(f"{key}: {value}")
    
    warna_ikan = input("Masukkan kode warna ikan: ")

    # Validasi input
    if jenis_ikan not in jenis_data or warna_ikan not in warna_data:
        print("Jenis atau warna ikan tidak valid. Silakan coba lagi.")
        return

    # Simpan data
    nama_data[id_ikan] = nama_ikan
    jenis_data[id_ikan] = jenis_data[jenis_ikan]
    warna_data[id_ikan] = warna_data[warna_ikan]

    simpan_file_dict(nama_file, nama_data)
    simpan_file_dict(jenis_file, jenis_data)
    simpan_file_dict(warna_file, warna_data)

    print(f"Data ikan dengan ID {id_ikan} berhasil ditambahkan!")

# Fungsi untuk mengedit data yang sudah ada
def edit_data(nama_file, jenis_file, warna_file, nama_data, jenis_data, warna_data):
    lihat_data(nama_data, jenis_data, warna_data)
    id_ikan = input("Masukkan ID ikan yang ingin diedit: ")

    if id_ikan in nama_data:
        nama_ikan = input(f"Nama baru ({nama_data[id_ikan]}): ") or nama_data[id_ikan]
        
        print("Kode jenis ikan yang tersedia:")
        for key, value in jenis_data.items():
            print(f"{key}: {value}")
        jenis_ikan = input("Masukkan kode jenis ikan baru: ")

        print("Kode warna ikan yang tersedia:")
        for key, value in warna_data.items():
            print(f"{key}: {value}")
        warna_ikan = input("Masukkan kode warna ikan baru: ")

        # Validasi input
        if jenis_ikan not in jenis_data or warna_ikan not in warna_data:
            print("Jenis atau warna ikan tidak valid. Silakan coba lagi.")
            return

        # Perbarui data
        nama_data[id_ikan] = nama_ikan
        jenis_data[id_ikan] = jenis_data[jenis_ikan]
        warna_data[id_ikan] = warna_data[warna_ikan]

        simpan_file_dict(nama_file, nama_data)
        simpan_file_dict(jenis_file, jenis_data)
        simpan_file_dict(warna_file, warna_data)
        print(f"Data ikan dengan ID {id_ikan} berhasil diperbarui!")
    else:
        print("ID tidak ditemukan.")

# Fungsi untuk menghapus data berdasarkan ID
def hapus_data(nama_file, jenis_file, warna_file, nama_data, jenis_data, warna_data):
    lihat_data(nama_data, jenis_data, warna_data)
    id_ikan = input("Masukkan ID ikan yang ingin dihapus: ")

    if id_ikan in nama_data:
        del nama_data[id_ikan]
        del jenis_data[id_ikan]
        del warna_data[id_ikan]

        simpan_file_dict(nama_file, nama_data)
        simpan_file_dict(jenis_file, jenis_data)
        simpan_file_dict(warna_file, warna_data)
        print(f"Data ikan dengan ID {id_ikan} berhasil dihapus!")
    else:
        print("ID tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    nama_file = 'nama_ikan.txt'
    jenis_file = 'jenis_ikan.txt'
    warna_file = 'warna_ikan.txt'

    # Baca data dari file
    nama_data = baca_file_dict(nama_file)
    jenis_data = baca_file_dict(jenis_file)
    warna_data = baca_file_dict(warna_file)

    while True:
        print("\nMenu:")
        print("1. Lihat data")
        print("2. Tambah data")
        print("3. Edit data")
        print("4. Hapus data")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            lihat_data(nama_data, jenis_data, warna_data)
        elif pilihan == '2':
            tambah_data(nama_file, jenis_file, warna_file, nama_data, jenis_data, warna_data)
        elif pilihan == '3':
            edit_data(nama_file, jenis_file, warna_file, nama_data, jenis_data, warna_data)
        elif pilihan == '4':
            hapus_data(nama_file, jenis_file, warna_file, nama_data, jenis_data, warna_data)
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
