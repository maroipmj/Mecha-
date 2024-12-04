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

    def lihat_data_ikan(self):
        """Membaca semua file dan menampilkan data ikan."""
        data_nama = self._load_file(self.file_nama)
        data_jenis = self._load_file(self.file_jenis)
        data_warna = self._load_file(self.file_warna)
        data_jarak = self._load_file(self.file_jarak)

        if data_nama and data_jenis and data_warna and data_jarak:
            print("\nData Ikan:")
            for idx, (nama, jenis, warna, jarak) in enumerate(zip(data_nama, data_jenis, data_warna, data_jarak), start=1):
                print(f"{idx}. Nama: {nama}, Jenis: {jenis}, Warna: {warna}, Jarak: {jarak}")
        else:
            print("\nData ikan kosong atau file tidak lengkap.")

    def tambah_data_ikan(self):
        """Menambah data ikan baru."""
        nama = input("Masukkan nama ikan: ")

        # Pilih jenis ikan dari file yang sudah ada
        data_jenis = self._load_file(self.file_jenis)
        print("\nPilih jenis ikan:")
        for idx, jenis in enumerate(data_jenis, start=1):
            print(f"{idx}. {jenis}")
        try:
            jenis_idx = int(input("Masukkan nomor jenis ikan: ")) - 1
            if not (0 <= jenis_idx < len(data_jenis)):
                print("Pilihan jenis tidak valid.")
                return
        except ValueError:
            print("Input harus berupa angka.")
            return
        jenis = data_jenis[jenis_idx]

        # Pilih warna ikan dari file yang sudah ada
        data_warna = self._load_file(self.file_warna)
        print("\nPilih warna ikan:")
        for idx, warna in enumerate(data_warna, start=1):
            print(f"{idx}. {warna}")
        try:
            warna_idx = int(input("Masukkan nomor warna ikan: ")) - 1
            if not (0 <= warna_idx < len(data_warna)):
                print("Pilihan warna tidak valid.")
                return
        except ValueError:
            print("Input harus berupa angka.")
            return
        warna = data_warna[warna_idx]

        # Input jarak ikan
        try:
            jarak = float(input("Masukkan jarak ikan (dalam km/jam): "))
        except ValueError:
            print("Input jarak harus berupa angka.")
            return

        # Tambahkan data baru ke file nama_ikan.txt dan jarak_tempuh.txt (jenis dan warna tidak ditambahkan)
        self._append_to_file(self.file_nama, nama)
        self._append_to_file(self.file_jarak, f"{jarak} km/jam")

        print("\nData ikan berhasil ditambahkan.")

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

    def edit_data_ikan(self):
        """Mengedit data ikan berdasarkan nomor."""
        data_nama = self._load_file(self.file_nama)
        data_jarak = self._load_file(self.file_jarak)
        data_jenis = self._load_file(self.file_jenis)
        data_warna = self._load_file(self.file_warna)

        if data_nama and data_jarak:
            print("\nData Ikan:")
            for idx, (nama, jenis, warna, jarak) in enumerate(zip(data_nama, data_jenis, data_warna, data_jarak), start=1):
                print(f"{idx}. Nama: {nama}, Jenis: {jenis}, Warna: {warna}, Jarak: {jarak}")
            try:
                idx = int(input("Masukkan nomor ikan yang ingin diedit: ")) - 1
                if 0 <= idx < len(data_nama):
                    # Edit nama ikan
                    data_nama[idx] = input(f"Nama baru (sebelumnya: {data_nama[idx]}): ") or data_nama[idx]

                    # Pilih jenis baru
                    print("\nPilih jenis ikan:")
                    for jdx, jenis in enumerate(data_jenis, start=1):
                        print(f"{jdx}. {jenis}")
                    try:
                        jenis_idx = int(input("Masukkan nomor jenis ikan: ")) - 1
                        if 0 <= jenis_idx < len(data_jenis):
                            data_jenis[idx] = data_jenis[jenis_idx]
                        else:
                            print("Pilihan jenis tidak valid.")
                            return
                    except ValueError:
                        print("Input harus berupa angka.")
                        return

                    # Pilih warna baru
                    print("\nPilih warna ikan:")
                    for wdx, warna in enumerate(data_warna, start=1):
                        print(f"{wdx}. {warna}")
                    try:
                        warna_idx = int(input("Masukkan nomor warna ikan: ")) - 1
                        if 0 <= warna_idx < len(data_warna):
                            data_warna[idx] = data_warna[warna_idx]
                        else:
                            print("Pilihan warna tidak valid.")
                            return
                    except ValueError:
                        print("Input harus berupa angka.")
                        return

                    # Edit jarak ikan
                    try:
                        data_jarak[idx] = f"{float(input(f'Jarak baru (km/jam, sebelumnya: {data_jarak[idx]}): '))} km/jam"
                    except ValueError:
                        print("Input jarak harus berupa angka.")
                        return

                    # Simpan ulang file
                    self._save_to_file(self.file_nama, data_nama)
                    self._save_to_file(self.file_jarak, data_jarak)
                    self._save_to_file(self.file_jenis, data_jenis)
                    self._save_to_file(self.file_warna, data_warna)

                    print("Data ikan berhasil diperbarui.")
                else:
                    print("Nomor ikan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData ikan kosong.")

    def _save_to_file(self, file_path, data):
        """Menyimpan ulang data ke file dengan format nomor: data."""
        with open(file_path, 'w') as f:
            for idx, item in enumerate(data, start=1):
                f.write(f"{idx}: {item}\n")

    def hapus_data_ikan(self):
        """Menghapus data ikan berdasarkan nomor."""
        data_nama = self._load_file(self.file_nama)
        data_jarak = self._load_file(self.file_jarak)
        data_jenis = self._load_file(self.file_jenis)
        data_warna = self._load_file(self.file_warna)

        if data_nama and data_jarak:
            print("\nData Ikan:")
            for idx, (nama, jenis, warna, jarak) in enumerate(zip(data_nama, data_jenis, data_warna, data_jarak), start=1):
                print(f"{idx}. Nama: {nama}, Jenis: {jenis}, Warna: {warna}, Jarak: {jarak}")
            try:
                idx = int(input("Masukkan nomor ikan yang ingin dihapus: ")) - 1
                if 0 <= idx < len(data_nama):
                    # Hapus data ikan dengan menghapus data pada masing-masing list
                    del data_nama[idx]
                    del data_jenis[idx]
                    del data_warna[idx]
                    del data_jarak[idx]

                    # Simpan ulang file tanpa data yang dihapus
                    self._save_to_file(self.file_nama, data_nama)
                    self._save_to_file(self.file_jarak, data_jarak)
                    self._save_to_file(self.file_jenis, data_jenis)
                    self._save_to_file(self.file_warna, data_warna)

                    print("Data ikan berhasil dihapus.")
                else:
                    print("Nomor ikan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        else:
            print("\nData ikan kosong.")

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
            # Implementasi untuk menu jenis ikan di sini

        elif pilihan == '3':
            print("\nMenu Warna Ikan:")
            # Implementasi untuk menu warna ikan di sini

        elif pilihan == '4':
            print("\nMenu Jarak Ikan:")
            # Implementasi untuk menu jarak ikan di sini

        elif pilihan == '5':
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
