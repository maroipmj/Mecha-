import os

class DataIkan:
    def __init__(self, nama_file, jenis_file, warna_file):
        self.nama_file = nama_file
        self.jenis_file = jenis_file
        self.warna_file = warna_file
        
        # Membaca data dari file saat inisialisasi
        self.nama_data = self.baca_file_dict(self.nama_file)
        self.jenis_data = self.baca_file_dict(self.jenis_file)
        self.warna_data = self.baca_file_dict(self.warna_file)

    # Fungsi untuk membaca data dari file dan mengubahnya menjadi dictionary
    def baca_file_dict(self, file):
        data_dict = {}
        if not os.path.exists(file):
            return data_dict

        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                # Menggunakan .split untuk memisahkan key dan value
                parts = line.strip().split(':', 1)
                if len(parts) == 2:  # Pastikan ada dua bagian
                    key, value = parts
                    data_dict[key.strip()] = value.strip()
        
        return data_dict

    # Fungsi untuk menyimpan dictionary ke file
    def simpan_file_dict(self, file, data):
        with open(file, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}:{value}\n")

    # Fungsi untuk menanyakan data apa yang ingin dilihat
    def lihat_data(self):
        print("Data apa yang ingin Anda lihat?")
        print("1. Nama Ikan")
        print("2. Jenis Ikan")
        print("3. Warna Ikan")
        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == '1':
            print("\nData Nama Ikan:")
            for id_ikan, nama_ikan in self.nama_data.items():
                print(f"{id_ikan}: {nama_ikan}")
        elif pilihan == '2':
            print("\nData Jenis Ikan:")
            for id_ikan, jenis_ikan in self.jenis_data.items():
                print(f"{id_ikan}: {jenis_ikan}")
        elif pilihan == '3':
            print("\nData Warna Ikan:")
            for id_ikan, warna_ikan in self.warna_data.items():
                print(f"{id_ikan}: {warna_ikan}")
        else:
            print("Pilihan tidak valid.")

    # Fungsi untuk menambah data
    def tambah_data(self):
        id_ikan = str(len(self.nama_data) + 1)  # ID baru otomatis
        nama_ikan = input("Masukkan nama ikan: ")

        # Tampilkan pilihan jenis ikan
        print("Kode jenis ikan yang tersedia:")
        for key, value in self.jenis_data.items():
            print(f"{key}: {value}")
        
        jenis_ikan = input("Masukkan kode jenis ikan: ")

        # Tampilkan pilihan warna ikan
        print("Kode warna ikan yang tersedia:")
        for key, value in self.warna_data.items():
            print(f"{key}: {value}")
        
        warna_ikan = input("Masukkan kode warna ikan: ")

        # Validasi input
        if jenis_ikan not in self.jenis_data or warna_ikan not in self.warna_data:
            print("Jenis atau warna ikan tidak valid. Silakan coba lagi.")
            return

        # Simpan data
        self.nama_data[id_ikan] = nama_ikan
        self.jenis_data[id_ikan] = self.jenis_data[jenis_ikan]
        self.warna_data[id_ikan] = self.warna_data[warna_ikan]

        self.simpan_file_dict(self.nama_file, self.nama_data)
        self.simpan_file_dict(self.jenis_file, self.jenis_data)
        self.simpan_file_dict(self.warna_file, self.warna_data)

        print(f"Data ikan dengan ID {id_ikan} berhasil ditambahkan!")

    # Fungsi untuk mengedit data ikan
    def edit_data(self):
        self.lihat_data()
        id_ikan = input("Masukkan ID ikan yang ingin diedit: ")

        if id_ikan in self.nama_data:
            nama_ikan = input(f"Nama baru ({self.nama_data[id_ikan]}): ") or self.nama_data[id_ikan]
            
            print("Kode jenis ikan yang tersedia:")
            for key, value in self.jenis_data.items():
                print(f"{key}: {value}")
            jenis_ikan = input("Masukkan kode jenis ikan baru: ")

            print("Kode warna ikan yang tersedia:")
            for key, value in self.warna_data.items():
                print(f"{key}: {value}")
            warna_ikan = input("Masukkan kode warna ikan baru: ")

            # Validasi input
            if jenis_ikan not in self.jenis_data or warna_ikan not in self.warna_data:
                print("Jenis atau warna ikan tidak valid. Silakan coba lagi.")
                return

            # Perbarui data
            self.nama_data[id_ikan] = nama_ikan
            self.jenis_data[id_ikan] = self.jenis_data[jenis_ikan]
            self.warna_data[id_ikan] = self.warna_data[warna_ikan]

            self.simpan_file_dict(self.nama_file, self.nama_data)
            self.simpan_file_dict(self.jenis_file, self.jenis_data)
            self.simpan_file_dict(self.warna_file, self.warna_data)
            print(f"Data ikan dengan ID {id_ikan} berhasil diperbarui!")
        else:
            print("ID tidak ditemukan.")

    # Fungsi untuk menghapus data ikan
    def hapus_data(self):
        self.lihat_data()
        id_ikan = input("Masukkan ID ikan yang ingin dihapus: ")

        if id_ikan in self.nama_data:
            del self.nama_data[id_ikan]
            del self.jenis_data[id_ikan]
            del self.warna_data[id_ikan]

            self.simpan_file_dict(self.nama_file, self.nama_data)
            self.simpan_file_dict(self.jenis_file, self.jenis_data)
            self.simpan_file_dict(self.warna_file, self.warna_data)
            print(f"Data ikan dengan ID {id_ikan} berhasil dihapus!")
        else:
            print("ID tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    # Membuat instance dari class DataIkan
    data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt')

    while True:
        print("\nMenu:")
        print("1. Lihat data")
        print("2. Tambah data")
        print("3. Edit data")
        print("4. Hapus data")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            data_ikan.lihat_data()
        elif pilihan == '2':
            data_ikan.tambah_data()
        elif pilihan == '3':
            data_ikan.edit_data()
        elif pilihan == '4':
            data_ikan.hapus_data()
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
