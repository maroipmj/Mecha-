import os

class DataIkan:
    def __init__(self, file_nama, file_jenis, file_warna, file_jarak):
        self.file_nama = file_nama
        self.file_jenis = file_jenis
        self.file_warna = file_warna
        self.file_jarak = file_jarak

    def _load_file(self, file_path):
        """Memuat data dari file dengan format ID: data."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return [line.strip().split(":", 1)[1].strip() for line in f if ":" in line]
        return []

    def _append_to_file(self, file_path, data):
        """Menambahkan data ke file dengan format ID: data."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
            next_index = len(lines) + 1
        else:
            next_index = 1

        with open(file_path, 'a') as f:
            f.write(f"{next_index}: {data}\n")

    def _save_to_file(self, file_path, data):
        """Menyimpan ulang data ke file dengan format ID: data."""
        with open(file_path, 'w') as f:
            for idx, item in enumerate(data, start=1):
                f.write(f"{idx}: {item}\n")


class DataIkanExtended(DataIkan):
    def tambah_data_ikan(self):
        """Menambah data ikan baru dengan ID otomatis."""
        # Generate ID baru untuk data ikan
        data_nama = self._load_file(self.file_nama)
        new_id = len(data_nama) + 1

        nama = input("Masukkan nama ikan: ")

        # Pilih jenis ikan
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

        # Pilih warna ikan
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

        # Tambahkan data ke file nama_ikan
        self._append_to_file(self.file_nama, f"{nama},{new_id},{jenis_idx + 1},{warna_idx + 1},{jarak} km/jam")

        print("\nData ikan berhasil ditambahkan.")
        print(f"ID: {new_id}, Nama: {nama}, Jenis: {jenis}, Warna: {warna}, Jarak: {jarak} km/jam")

    def lihat_data_ikan(self):
        """Melihat semua data ikan dengan ID."""
        data_nama = self._load_file(self.file_nama)
        data_jenis = self._load_file(self.file_jenis)
        data_warna = self._load_file(self.file_warna)

        if data_nama:
            print("\nData Ikan:")
            for idx, line in enumerate(data_nama, start=1):
                try:
                    # Parse data
                    nama, fish_id, jenis_idx, warna_idx, jarak = line.split(',')
                    jenis = data_jenis[int(jenis_idx) - 1]
                    warna = data_warna[int(warna_idx) - 1]

                    # Tampilkan data
                    print(f"{fish_id}. Nama: {nama}, Jenis: {jenis}, Warna: {warna}, Jarak: {jarak}")
                except (IndexError, ValueError):
                    print(f"Baris data tidak valid: {line}")
        else:
            print("\nData ikan kosong.")


def main_with_id():
    data_ikan = DataIkanExtended('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt', 'jarak_tempuh.txt')

    while True:
        print("\nMenu Utama:")
        print("1. Data Ikan (CRUD)")
        print("2. Jenis Ikan (Tambah, Edit, Hapus)")
        print("3. Warna Ikan (Tambah, Edit, Hapus)")
        print("4. Lihat Jarak Tempuh")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            while True:
                print("\nMenu Data Ikan:")
                print("1. Lihat data ikan (Read)")
                print("2. Tambah data ikan (Create)")
                print("3. Edit data ikan (Update)")
                print("4. Hapus data ikan (Delete)")
                print("5. Kembali ke menu utama")
                sub_pilihan = input("Pilih opsi: ")

                if sub_pilihan == '1':
                    data_ikan.lihat_data_ikan()
                elif sub_pilihan == '2':
                    data_ikan.tambah_data_ikan()
                elif sub_pilihan == '3':
                    data_ikan.edit_data_ikan()
                elif sub_pilihan == '4':
                    data_ikan.hapus_data_ikan()
                elif sub_pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == '2':
            # Jenis ikan menu
            pass

        elif pilihan == '3':
            # Warna ikan menu
            pass

        elif pilihan == '4':
            data_ikan.lihat_jarak_tempuh()

        elif pilihan == '5':
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main_with_id()
