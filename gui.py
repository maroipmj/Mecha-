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

    # Function to read data from file and convert to dictionary
    def baca_file_dict(self, file):
        data_dict = {}
        if not os.path.exists(file):
            return data_dict

        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split(':', 1)
                data_dict[key.strip()] = value.strip()
        
        return data_dict

    # Function to save dictionary to file
    def simpan_file_dict(self, file, data):
        with open(file, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}:{value}\n")

    # Function to get fish data as string
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

    # Function to add fish data
    def tambah_data(self):
        id_ikan = str(len(self.nama_data) + 1)  # Automatically generate new ID
        nama_ikan = simpledialog.askstring("Input", "Masukkan nama ikan:")
        if not nama_ikan:
            return

        # Display available types of fish
        jenis_ikan = self.get_choice("Jenis Ikan", self.jenis_data)
        if not jenis_ikan:
            return

        # Display available colors of fish
        warna_ikan = self.get_choice("Warna Ikan", self.warna_data)
        if not warna_ikan:
            return

        # Save data
        self.nama_data[id_ikan] = nama_ikan
        self.jenis_data[id_ikan] = self.jenis_data[jenis_ikan]
        self.warna_data[id_ikan] = self.warna_data[warna_ikan]

        self.simpan_file_dict(self.nama_file, self.nama_data)
        self.simpan_file_dict(self.jenis_file, self.jenis_data)
        self.simpan_file_dict(self.warna_file, self.warna_data)

        messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil ditambahkan!")

    # Function to edit fish data
    def edit_data(self):
        # Display all fish data for user to select
        all_data = self.get_fish_data("nama")
        if all_data == "Tidak ada data.":
            messagebox.showwarning("Peringatan", "Tidak ada data untuk diedit.")
            return

        id_ikan = simpledialog.askstring("Input", f"Data ikan yang tersedia:\n{all_data}\n\nMasukkan ID ikan yang ingin diedit:")
        if id_ikan not in self.nama_data:
            messagebox.showwarning("Peringatan", "ID tidak ditemukan.")
            return

        # Show current data to edit
        current_data = (
            f"ID: {id_ikan}\n"
            f"Nama: {self.nama_data[id_ikan]}\n"
            f"Jenis: {self.jenis_data[id_ikan]}\n"
            f"Warna: {self.warna_data[id_ikan]}"
        )
        messagebox.showinfo("Data Saat Ini", current_data)

        # Ask user what they want to edit
        edit_choice = simpledialog.askstring("Edit Data", "Apa yang ingin Anda edit?\n1. Nama\n2. Jenis\n3. Warna\nMasukkan pilihan (1-3):")
        
        if edit_choice == '1':  # Edit Nama
            nama_ikan = simpledialog.askstring("Input", f"Nama baru ({self.nama_data[id_ikan]}):")
            if nama_ikan:
                self.nama_data[id_ikan] = nama_ikan
        elif edit_choice == '2':  # Edit Jenis
            jenis_ikan = self.get_choice("Jenis Ikan", self.jenis_data)
            if jenis_ikan:
                self.jenis_data[id_ikan] = self.jenis_data[jenis_ikan]
        elif edit_choice == '3':  # Edit Warna
            warna_ikan = self.get_choice("Warna Ikan", self.warna_data)
            if warna_ikan:
                self.warna_data[id_ikan] = self.warna_data[warna_ikan]
        else:
            messagebox.showwarning("Peringatan", "Pilihan tidak valid.")
            return

        # Save updated data back to files
        self.simpan_file_dict(self.nama_file, self.nama_data)
        self.simpan_file_dict(self.jenis_file, self.jenis_data)
        self.simpan_file_dict(self.warna_file, self.warna_data)

        messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil diperbarui!")

    # Function to delete fish data
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

    # Function to display choices and get user's choice
    def get_choice(self, title, data_dict):
        choices = "\n".join(f"{key}: {value}" for key, value in data_dict.items())
        return simpledialog.askstring("Input", f"{title} yang tersedia:\n{choices}\nMasukkan kode:")

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Ikan")
        self.root.geometry("400x400")
        self.root.configure(bg='lightblue')

        self.data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt')

        # Create buttons
        tk.Button(root, text="Lihat Data", command=self.show_data, bg='white').pack(pady=10)
        tk.Button(root, text="Tambah Data", command=self.data_ikan.tambah_data, bg='white').pack(pady=10)
        tk.Button(root, text="Edit Data", command=self.data_ikan.edit_data, bg='white').pack(pady=10)
        tk.Button(root, text="Hapus Data", command=self.data_ikan.hapus_data, bg='white').pack(pady=10)
        tk.Button(root, text="Keluar", command=root.quit, bg='white').pack(pady=10)

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
