import os

class DataIkan:
    def __init__(self, file_nama, file_jenis, file_warna):
        self.file_nama = file_nama
        self.file_jenis = file_jenis
        self.file_warna = file_warna
        self.data_ikan = []
        self.jenis_ikan = []
        self.warna_ikan = []
        self.load_data()

    def load_data(self):
        """Memuat data dari file."""
        # Memuat nama ikan
        if os.path.exists(self.file_nama):
            with open(self.file_nama, 'r') as f:
                self.data_ikan = [line.strip() for line in f if line.strip()]

        # Memuat jenis ikan
        if os.path.exists(self.file_jenis):
            with open(self.file_jenis, 'r') as f:
                self.jenis_ikan = [line.strip() for line in f if line.strip()]

        # Memuat warna ikan
        if os.path.exists(self.file_warna):
            with open(self.file_warna, 'r') as f:
                self.warna_ikan = [line.strip() for line in f if line.strip()]

    def simpan_data_ikan(self):
        """Simpan nama ikan ke file."""
        with open(self.file_nama, 'w') as f:
            for nama in self.data_ikan:
                f.write(f"{nama}\n")

    def lihat_data_ikan(self):
        """Menampilkan semua data ikan dengan jenis dan warna."""
        if self.data_ikan:
            print("\nData Ikan:")
            for idx, nama in enumerate(self.data_ikan, start=1):
                jenis = self.jenis_ikan[idx % len(self.jenis_ikan)]  # Pilihan jenis secara berurutan
                warna = self.warna_ikan[idx % len(self.warna_ikan)]  # Pilihan warna secara berurutan
                print(f"{idx}. Nama: {nama}, Jenis: {jenis}, Warna: {warna}")
        else:
            print("\nData ikan kosong.")

    def tambah_data_ikan(self):
        """Menambah nama ikan baru."""
        nama = input("Masukkan nama ikan: ")
        
        # Pilih jenis ikan
        print("\nPilih jenis ikan:")
        for idx, jenis in enumerate(self.jenis_ikan, start=1):
            print(f"{idx}. {jenis}")
        try:
            jenis_idx = int(input("Masukkan nomor jenis ikan: ")) - 1
            if not (0 <= jenis_idx < len(self.jenis_ikan)):
                print("Pilihan jenis tidak valid.")
                return
        except ValueError:
            print("Input harus berupa angka.")
            return
        jenis = self.jenis_ikan[jenis_idx]

        # Pilih warna ikan
        print("\nPilih warna ikan:")
        for idx, warna in enumerate(self.warna_ikan, start=1):
            print(f"{idx}. {warna}")
        try:
            warna_idx = int(input("Masukkan nomor warna ikan: ")) - 1
            if not (0 <= warna_idx < len(self.warna_ikan)):
                print("Pilihan warna tidak valid.")
                return
        except ValueError:
            print("Input harus berupa angka.")
            return
        warna = self.warna_ikan[warna_idx]

        # Tambahkan data ikan
        self.data_ikan.append(f"{nama} - {jenis} - {warna}")
        self.simpan_data_ikan()
        print("\nData ikan berhasil ditambahkan.")

    def hapus_data_ikan(self):
        """Menghapus data ikan berdasarkan nomor."""
        self.lihat_data_ikan()
        if self.data_ikan:
            try:
                idx = int(input("Masukkan nomor ikan yang ingin dihapus: ")) - 1
                if 0 <= idx < len(self.data_ikan):
                    self.data_ikan.pop(idx)
                    self.simpan_data_ikan()
                    print("Data ikan berhasil dihapus.")
                else:
                    print("Nomor ikan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    def menu_jenis_ikan(self):
        """Menu untuk jenis ikan."""
        while True:
            print("\nMenu Jenis Ikan:")
            print("1. Lihat jenis ikan")
            print("2. Tambah jenis ikan")
            print("3. Hapus jenis ikan")
            print("4. Kembali")
            pilihan = input("Pilih opsi: ")
            if pilihan == '1':
                print("\nJenis Ikan:")
                for idx, jenis in enumerate(self.jenis_ikan, start=1):
                    print(f"{idx}. {jenis}")
            elif pilihan == '2':
                jenis_baru = input("Masukkan jenis ikan baru: ")
                if jenis_baru not in self.jenis_ikan:
                    self.jenis_ikan.append(jenis_baru)
                    with open(self.file_jenis, 'a') as f:
                        f.write(f"{jenis_baru}\n")
                    print("Jenis ikan berhasil ditambahkan.")
                else:
                    print("Jenis ikan sudah ada.")
            elif pilihan == '3':
                self.hapus_jenis_ikan()
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid.")

    def hapus_jenis_ikan(self):
        """Menghapus jenis ikan berdasarkan nomor."""
        print("\nJenis Ikan:")
        for idx, jenis in enumerate(self.jenis_ikan, start=1):
            print(f"{idx}. {jenis}")
        try:
            idx = int(input("Masukkan nomor jenis ikan yang ingin dihapus: ")) - 1
            if 0 <= idx < len(self.jenis_ikan):
                self.jenis_ikan.pop(idx)
                with open(self.file_jenis, 'w') as f:
                    for jenis in self.jenis_ikan:
                        f.write(f"{jenis}\n")
                print("Jenis ikan berhasil dihapus.")
            else:
                print("Nomor jenis ikan tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    def menu_warna_ikan(self):
        """Menu untuk warna ikan."""
        while True:
            print("\nMenu Warna Ikan:")
            print("1. Lihat warna ikan")
            print("2. Tambah warna ikan")
            print("3. Hapus warna ikan")
            print("4. Kembali")
            pilihan = input("Pilih opsi: ")
            if pilihan == '1':
                print("\nWarna Ikan:")
                for idx, warna in enumerate(self.warna_ikan, start=1):
                    print(f"{idx}. {warna}")
            elif pilihan == '2':
                warna_baru = input("Masukkan warna ikan baru: ")
                if warna_baru not in self.warna_ikan:
                    self.warna_ikan.append(warna_baru)
                    with open(self.file_warna, 'a') as f:
                        f.write(f"{warna_baru}\n")
                    print("Warna ikan berhasil ditambahkan.")
                else:
                    print("Warna ikan sudah ada.")
            elif pilihan == '3':
                self.hapus_warna_ikan()
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid.")

    def hapus_warna_ikan(self):
        """Menghapus warna ikan berdasarkan nomor."""
        print("\nWarna Ikan:")
        for idx, warna in enumerate(self.warna_ikan, start=1):
            print(f"{idx}. {warna}")
        try:
            idx = int(input("Masukkan nomor warna ikan yang ingin dihapus: ")) - 1
            if 0 <= idx < len(self.warna_ikan):
                self.warna_ikan.pop(idx)
                with open(self.file_warna, 'w') as f:
                    for warna in self.warna_ikan:
                        f.write(f"{warna}\n")
                print("Warna ikan berhasil dihapus.")
            else:
                print("Nomor warna ikan tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

def main():
    data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt')

    while True:
        print("\nMenu Utama:")
        print("1. Data Ikan")
        print("2. Jenis Ikan")
        print("3. Warna Ikan")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")
        if pilihan == '1':
            print("\nMenu Data Ikan:")
            print("1. Lihat data ikan")
            print("2. Tambah data ikan")
            print("3. Hapus data ikan")
            print("4. Kembali")
            sub_pilihan = input("Pilih opsi: ")
            if sub_pilihan == '1':
                data_ikan.lihat_data_ikan()
            elif sub_pilihan == '2':
                data_ikan.tambah_data_ikan()
            elif sub_pilihan == '3':
                data_ikan.hapus_data_ikan()
            elif sub_pilihan == '4':
                continue
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '2':
            data_ikan.menu_jenis_ikan()
        elif pilihan == '3':
            data_ikan.menu_warna_ikan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
