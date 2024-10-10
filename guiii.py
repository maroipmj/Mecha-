<<<<<<< HEAD
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class DataIkan:
    def __init__(self, nama_file, jenis_file, warna_file):
        self.nama_file = nama_file
        self.jenis_file = jenis_file
        self.warna_file = warna_file
        
        # Read data from files at initialization
        self.nama_data = self.baca_file_dict(self.nama_file)
        self.jenis_data = self.baca_file_dict(self.jenis_file)
        self.warna_data = self.baca_file_dict(self.warna_file)

    def baca_file_dict(self, file):
        data_dict = {}
        if not os.path.exists(file):
            # File tidak ditemukan
            print(f"File {file} tidak ditemukan.")
            return data_dict

        print(f"Membaca file {file}...")  # Debugging: memastikan file dibaca
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:  # Pastikan format yang diharapkan (ID:Value)
                    key, value = line.strip().split(':', 1)
                    data_dict[key.strip()] = value.strip()
                    print(f"Baris dibaca: {key.strip()} -> {value.strip()}")  # Debugging
                else:
                    print(f"Format salah di baris: {line.strip()}")  # Debugging: Format tidak sesuai

        print(f"Data dari file {file}: {data_dict}")  # Debugging: melihat data yang terbaca
        return data_dict

    def simpan_file_dict(self, file, data):
        with open(file, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}:{value}\n")

    def get_fish_data(self, data_type):
        data = ""
        if data_type == "nama":
            data_dict = self.nama_data
        elif data_type == "jenis":
            data_dict = self.jenis_data
        elif data_type == "warna":
            data_dict = self.warna_data
        else:
            return "Invalid data type."

        for id_ikan in data_dict.keys():
            data += f"ID: {id_ikan}, Data: {data_dict[id_ikan]}\n"
        return data.strip() or "Tidak ada data."

    def tambah_data(self):
        id_ikan = str(len(self.nama_data) + 1)
        nama_ikan = simpledialog.askstring("Input", "Masukkan nama ikan:")
        if not nama_ikan:
            return

        jenis_ikan = self.get_choice("Jenis Ikan", self.jenis_data)
        if not jenis_ikan:
            return

        warna_ikan = self.get_choice("Warna Ikan", self.warna_data)
        if not warna_ikan:
            return

        self.nama_data[id_ikan] = nama_ikan
        self.jenis_data[id_ikan] = self.jenis_data[jenis_ikan]
        self.warna_data[id_ikan] = self.warna_data[warna_ikan]

        self.simpan_file_dict(self.nama_file, self.nama_data)
        self.simpan_file_dict(self.jenis_file, self.jenis_data)
        self.simpan_file_dict(self.warna_file, self.warna_data)

        messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil ditambahkan!")

    def edit_data(self):
        all_data = self.get_fish_data("nama")
        if all_data == "Tidak ada data.":
            messagebox.showwarning("Peringatan", "Tidak ada data untuk diedit.")
            return

        id_ikan = simpledialog.askstring("Input", f"Data ikan yang tersedia:\n{all_data}\n\nMasukkan ID ikan yang ingin diedit:")
        if id_ikan not in self.nama_data:
            messagebox.showwarning("Peringatan", "ID tidak ditemukan.")
            return

        current_data = (
            f"ID: {id_ikan}\n"
            f"Nama: {self.nama_data[id_ikan]}\n"
            f"Jenis: {self.jenis_data[id_ikan]}\n"
            f"Warna: {self.warna_data[id_ikan]}"
        )
        messagebox.showinfo("Data Saat Ini", current_data)

        edit_choice = simpledialog.askstring("Edit Data", "Apa yang ingin Anda edit?\n1. Nama\n2. Jenis\n3. Warna\nMasukkan pilihan (1-3):")
        
        if edit_choice == '1':
            nama_ikan = simpledialog.askstring("Input", f"Nama baru ({self.nama_data[id_ikan]}):")
            if nama_ikan:
                self.nama_data[id_ikan] = nama_ikan
        elif edit_choice == '2':
            jenis_ikan = self.get_choice("Jenis Ikan", self.jenis_data)
            if jenis_ikan:
                self.jenis_data[id_ikan] = self.jenis_data[jenis_ikan]
        elif edit_choice == '3':
            warna_ikan = self.get_choice("Warna Ikan", self.warna_data)
            if warna_ikan:
                self.warna_data[id_ikan] = self.warna_data[warna_ikan]
        else:
            messagebox.showwarning("Peringatan", "Pilihan tidak valid.")
            return

        self.simpan_file_dict(self.nama_file, self.nama_data)
        self.simpan_file_dict(self.jenis_file, self.jenis_data)
        self.simpan_file_dict(self.warna_file, self.warna_data)

        messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil diperbarui!")

    def hapus_data(self):
        all_data = self.get_fish_data("nama")
        if all_data == "Tidak ada data.":
            messagebox.showwarning("Peringatan", "Tidak ada data untuk dihapus.")
            return

        id_ikan = simpledialog.askstring("Input", f"Data ikan yang tersedia:\n{all_data}\n\nMasukkan ID ikan yang ingin dihapus:")
        if id_ikan in self.nama_data:
            del self.nama_data[id_ikan]
            del self.jenis_data[id_ikan]
            del self.warna_data[id_ikan]

            self.simpan_file_dict(self.nama_file, self.nama_data)
            self.simpan_file_dict(self.jenis_file, self.jenis_data)
            self.simpan_file_dict(self.warna_file, self.warna_data)

            messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "ID tidak ditemukan.")

    def get_choice(self, title, data_dict):
        choices = "\n".join(f"{key}: {value}" for key, value in data_dict.items())
        return simpledialog.askstring("Input", f"{title} yang tersedia:\n{choices}\nMasukkan kode:")

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Ikan")
        self.root.geometry("400x400")

        # Create a canvas to set the background color
        self.canvas = tk.Canvas(root, width=400, height=400, bg='lightblue')  # Latar belakang biru seperti akuarium
        self.canvas.pack(fill="both", expand=True)

        self.data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt')

        # Add title text with black color
        self.canvas.create_text(200, 40, text="Data Ikan", font=("Arial", 16, "bold"), fill="black")

        # Create buttons and place them on the canvas
        self.btn_lihat = tk.Button(root, text="Lihat Data", command=self.show_data, bg='white')
        self.btn_lihat_window = self.canvas.create_window(200, 100, window=self.btn_lihat)

        self.btn_tambah = tk.Button(root, text="Tambah Data", command=self.data_ikan.tambah_data, bg='white')
        self.btn_tambah_window = self.canvas.create_window(200, 150, window=self.btn_tambah)

        self.btn_edit = tk.Button(root, text="Edit Data", command=self.data_ikan.edit_data, bg='white')
        self.btn_edit_window = self.canvas.create_window(200, 200, window=self.btn_edit)

        self.btn_hapus = tk.Button(root, text="Hapus Data", command=self.data_ikan.hapus_data, bg='white')
        self.btn_hapus_window = self.canvas.create_window(200, 250, window=self.btn_hapus)

        self.btn_keluar = tk.Button(root, text="Keluar", command=root.quit, bg='white')
        self.btn_keluar_window = self.canvas.create_window(200, 300, window=self.btn_keluar)

    def show_data(self):
        pilihan = simpledialog.askstring("Pilih Data", "Apa yang ingin Anda lihat?\n1. Nama Ikan\n2. Jenis Ikan\n3. Warna Ikan\nMasukkan pilihan (1-3):")
        
        if pilihan == '1':
            data = self.data_ikan.get_fish_data("nama")
        elif pilihan == '2':
            data = self.data_ikan.get_fish_data("jenis")
        elif pilihan == '3':
            data = self.data_ikan.get_fish_data("warna")
        else:
            messagebox.showwarning("Peringatan", "Pilihan tidak valid.")
            return
            
        messagebox.showinfo("Data Ikan", data)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
=======
import os

class DataIkan:
    def init(self, nama_file, jenis_file, warna_file):
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

if __name__ == "main":
    main()
>>>>>>> a8f1979205642224fd411a9dec0b95c0f4a499c8
