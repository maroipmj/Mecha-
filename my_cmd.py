import os

class DataIkan:
    def __init__(self, file_nama, file_jenis, file_warna, file_jarak):
        self.file_nama = file_nama
        self.file_jenis = file_jenis
        self.file_warna = file_warna
        self.file_jarak = file_jarak

    def _load_file(self, file_path):
        """Memuat data dari file dengan format nomor: data."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return [line.strip().split(": ", 1)[1] for line in f if ": " in line]
        return []

    def _append_to_file(self, file_path, data):
        """Menambahkan data ke file dengan format nomor: data."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
            next_index = len(lines) + 1
        else:
            next_index = 1
        with open(file_path, 'a') as f:
            f.write(f"{next_index}: {data}\n")

    def _save_to_file(self, file_path, data):
        """Menyimpan ulang data ke file dengan format nomor: data."""
        with open(file_path, 'w') as f:
            for idx, item in enumerate(data, start=1):
                f.write(f"{idx}: {item}\n")

    # Existing methods for lihat_data_ikan, tambah_data_ikan, edit_data_ikan, hapus_data_ikan remain the same

    def lihat_data_jenis(self):
        """Menampilkan daftar jenis ikan."""
        data_jenis = self._load_file(self.file_jenis)
        if data_jenis:
            print("\nDaftar Jenis Ikan:")
            for idx, jenis in enumerate(data_jenis, start=1):
                print(f"{idx}. {jenis}")
        else:
            print("\nData jenis ikan kosong.")

    def tambah_data_jenis(self):
        """Menambah jenis ikan baru."""
        jenis = input("Masukkan jenis ikan baru: ")
        self._append_to_file(self.file_jenis, jenis)
        print("\nJenis ikan berhasil ditambahkan.")

    def edit_data_jenis(self):
        """Mengedit jenis ikan."""
        data_jenis = self._load_file(self.file_jenis)
        if data_jenis:
            print("\nDaftar Jenis Ikan:")
            for idx, jenis in enumerate(data_jenis, start=1):
                print(f"{idx}. {jenis}")
            try:
                idx = int(input("Masukkan nomor jenis ikan yang ingin diedit: ")) - 1
                if 0 <= idx < len(data_jenis):
                    data_jenis[idx] = input(f"Masukkan jenis baru (sebelumnya: {data_jenis[idx]}): ")
                    self._save_to_file(self.file_jenis, data_jenis)
                    print("Jenis ikan berhasil diperbarui.")
                else:
                    print("Nomor jenis tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData jenis ikan kosong.")

    def hapus_data_jenis(self):
        """Menghapus jenis ikan."""
        data_jenis = self._load_file(self.file_jenis)
        if data_jenis:
            print("\nDaftar Jenis Ikan:")
            for idx, jenis in enumerate(data_jenis, start=1):
                print(f"{idx}. {jenis}")
            try:
                idx = int(input("Masukkan nomor jenis ikan yang ingin dihapus: ")) - 1
                if 0 <= idx < len(data_jenis):
                    del data_jenis[idx]
                    self._save_to_file(self.file_jenis, data_jenis)
                    print("Jenis ikan berhasil dihapus.")
                else:
                    print("Nomor jenis tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData jenis ikan kosong.")

    def lihat_data_warna(self):
        """Menampilkan daftar warna ikan."""
        data_warna = self._load_file(self.file_warna)
        if data_warna:
            print("\nDaftar Warna Ikan:")
            for idx, warna in enumerate(data_warna, start=1):
                print(f"{idx}. {warna}")
        else:
            print("\nData warna ikan kosong.")

    def tambah_data_warna(self):
        """Menambah warna ikan baru."""
        warna = input("Masukkan warna ikan baru: ")
        self._append_to_file(self.file_warna, warna)
        print("\nWarna ikan berhasil ditambahkan.")

    def edit_data_warna(self):
        """Mengedit warna ikan."""
        data_warna = self._load_file(self.file_warna)
        if data_warna:
            print("\nDaftar Warna Ikan:")
            for idx, warna in enumerate(data_warna, start=1):
                print(f"{idx}. {warna}")
            try:
                idx = int(input("Masukkan nomor warna ikan yang ingin diedit: ")) - 1
                if 0 <= idx < len(data_warna):
                    data_warna[idx] = input(f"Masukkan warna baru (sebelumnya: {data_warna[idx]}): ")
                    self._save_to_file(self.file_warna, data_warna)
                    print("Warna ikan berhasil diperbarui.")
                else:
                    print("Nomor warna tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData warna ikan kosong.")

    def hapus_data_warna(self):
        """Menghapus warna ikan."""
        data_warna = self._load_file(self.file_warna)
        if data_warna:
            print("\nDaftar Warna Ikan:")
            for idx, warna in enumerate(data_warna, start=1):
                print(f"{idx}. {warna}")
            try:
                idx = int(input("Masukkan nomor warna ikan yang ingin dihapus: ")) - 1
                if 0 <= idx < len(data_warna):
                    del data_warna[idx]
                    self._save_to_file(self.file_warna, data_warna)
                    print("Warna ikan berhasil dihapus.")
                else:
                    print("Nomor warna tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData warna ikan kosong.")

    def lihat_data_jarak(self):
        """Menampilkan daftar jarak ikan."""
        data_jarak = self._load_file(self.file_jarak)
        if data_jarak:
            print("\nDaftar Jarak Ikan:")
            for idx, jarak in enumerate(data_jarak, start=1):
                print(f"{idx}. {jarak}")
        else:
            print("\nData jarak ikan kosong.")

    def tambah_data_jarak(self):
        """Menambah jarak ikan baru."""
        try:
            jarak = float(input("Masukkan jarak ikan baru (km/jam): "))
            self._append_to_file(self.file_jarak, f"{jarak} km/jam")
            print("\nJarak ikan berhasil ditambahkan.")
        except ValueError:
            print("Input jarak harus berupa angka.")

    def edit_data_jarak(self):
        """Mengedit jarak ikan."""
        data_jarak = self._load_file(self.file_jarak)
        if data_jarak:
            print("\nDaftar Jarak Ikan:")
            for idx, jarak in enumerate(data_jarak, start=1):
                print(f"{idx}. {jarak}")
            try:
                idx = int(input("Masukkan nomor jarak ikan yang ingin diedit: ")) - 1
                if 0 <= idx < len(data_jarak):
                    try:
                        jarak_baru = float(input(f"Masukkan jarak baru (km/jam, sebelumnya: {data_jarak[idx]}): "))
                        data_jarak[idx] = f"{jarak_baru} km/jam"
                        self._save_to_file(self.file_jarak, data_jarak)
                        print("Jarak ikan berhasil diperbarui.")
                    except ValueError:
                        print("Input jarak harus berupa angka.")
                else:
                    print("Nomor jarak tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData jarak ikan kosong.")

    def hapus_data_jarak(self):
        """Menghapus jarak ikan."""
        data_jarak = self._load_file(self.file_jarak)
        if data_jarak:
            print("\nDaftar Jarak Ikan:")
            for idx, jarak in enumerate(data_jarak, start=1):
                print(f"{idx}. {jarak}")
            try:
                idx = int(input("Masukkan nomor jarak ikan yang ingin dihapus: ")) - 1
                if 0 <= idx < len(data_jarak):
                    del data_jarak[idx]
                    self._save_to_file(self.file_jarak, data_jarak)
                    print("Jarak ikan berhasil dihapus.")
                else:
                    print("Nomor jarak tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData jarak ikan kosong.")

def main():
    data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt', 'jarak_tempuh.txt')

    while True:
        print("\nMenu Utama:")
        print("1. Data Ikan")
        print("2. Jenis Ikan")
        print("3. Warna Ikan")
        print("4. Jarak Ikan")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            print("\nMenu Data Ikan:")
            print("1. Lihat data ikan")
            print("2. Tambah data ikan")
            print("3. Edit data ikan")
            print("4. Hapus data ikan")
            sub_pilihan = input("Pilih opsi: ")
            if sub_pilihan == '1':
                data_ikan.lihat_data_ikan()
            elif sub_pilihan == '2':
                data_ikan.tambah_data_ikan()
            elif sub_pilihan == '3':
                data_ikan.edit_data_ikan()
            elif sub_pilihan == '4':
                data_ikan.hapus_data_ikan()

        elif pilihan == '2':
            print("\nMenu Jenis Ikan:")
            print("1. Lihat jenis ikan")
            print("2. Tambah jenis ikan")
            print("3. Edit jenis ikan")
            print("4. Hapus jenis ikan")
            sub_pilihan = input("Pilih opsi: ")
            if sub_pilihan == '1':
                data_ikan.lihat_data_jenis()
            elif sub_pilihan == '2':
                data_ikan.tambah_data_jenis()
            elif sub_pilihan == '3':
                data_ikan.edit_data_jenis()
            elif sub_pilihan == '4':
                data_ikan.hapus_data_jenis()

        elif pilihan == '3':
            print("\nMenu Warna Ikan:")
            print("1. Lihat warna ikan")
            print("2. Tambah warna ikan")
            print("3. Edit warna ikan")
            print("4. Hapus warna ikan")
            sub_pilihan = input("Pilih opsi: ")
            if sub_pilihan == '1':
                data_ikan.lihat_data_warna()
            elif sub_pilihan == '2':
                data_ikan.tambah_data_warna()
            elif sub_pilihan == '3':
                data_ikan.edit_data_warna()
            elif sub_pilihan == '4':
                data_ikan.hapus_data_warna()

        elif pilihan == '4':
            print("\nMenu Jarak Ikan:")
            print("1. Lihat jarak ikan")
            print("2. Tambah jarak ikan")
            print("3. Edit jarak ikan")
            print("4. Hapus jarak ikan")
            sub_pilihan = input("Pilih opsi: ")
            if sub_pilihan == '1':
                data_ikan.lihat_data_jarak()
            elif sub_pilihan == '2':
                data_ikan.tambah_data_jarak()
            elif sub_pilihan == '3':
                data_ikan.edit_data_jarak()
            elif sub_pilihan == '4':
                data_ikan.hapus_data_jarak()

        elif pilihan == '5':
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()