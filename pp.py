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
        # Jika file tidak ada, kembalikan data kosong dan tampilkan pesan
        if not os.path.exists(file):
            print(f"File {file} tidak ditemukan.")
            return data_dict

        # Baca file dan simpan dalam dictionary
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    data_dict[key.strip()] = value.strip()
                else:
                    print(f"Format salah pada baris: {line.strip()}")
        return data_dict

    def simpan_file_dict(self, file, data):
        with open(file, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}:{value}\n")

    def get_fish_data(self, data_type):
        data = ""
        # Pilih tipe data berdasarkan input pengguna
        if data_type == "nama":
            data_dict = self.nama_data
        elif data_type == "jenis":
            data_dict = self.jenis_data
        elif data_type == "warna":
            data_dict = self.warna_data
        else:
            return "Invalid data type."

        # Format data menjadi string untuk ditampilkan
        for id_ikan in data_dict.keys():
            data += f"ID: {id_ikan}, Data: {data_dict[id_ikan]}\n"
        return data.strip() or "Tidak ada data."

    def tambah_data(self):
        id_ikan = str(len(self.nama_data) + 1)  # Auto-generate ID ikan
        nama_ikan = simpledialog.askstring("Input", "Masukkan nama ikan:")
        if not nama_ikan:
            return

        # Pilih jenis ikan dari daftar yang ada
        jenis_ikan = self.get_choice("Jenis Ikan", self.jenis_data)
        if not jenis_ikan:
            return

        # Pilih warna ikan dari daftar yang ada
        warna_ikan = self.get_choice("Warna Ikan", self.warna_data)
        if not warna_ikan:
            return

        # Tambahkan data ikan baru
        self.nama_data[id_ikan] = nama_ikan
        self.jenis_data[id_ikan] = jenis_ikan  # Menggunakan key (bukan value) dari data jenis
        self.warna_data[id_ikan] = warna_ikan  # Menggunakan key (bukan value) dari data warna

        # Simpan data ke file
        self.simpan_file_dict(self.nama_file, self.nama_data)
        self.simpan_file_dict(self.jenis_file, self.jenis_data)
        self.simpan_file_dict(self.warna_file, self.warna_data)

        messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil ditambahkan!")

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
        # Tampilkan pilihan yang tersedia dan minta input pengguna
        choices = "\n".join(f"{key}: {value}" for key, value in data_dict.items())
        return simpledialog.askstring("Input", f"{title} yang tersedia:\n{choices}\nMasukkan kode:")

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Ikan")
        self.root.geometry("400x550")  # Perbesar ukuran jendela agar tombol dan accordion muat

        # Create a canvas to set the background color
        self.canvas = tk.Canvas(root, width=400, height=550, bg='lightblue')  # Latar belakang biru seperti akuarium
        self.canvas.pack(fill="both", expand=True)

        self.data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt')

        # Add title text with black color
        self.canvas.create_text(200, 40, text="Data Ikan", font=("Arial", 16, "bold"), fill="black")

        # Create accordion frames
        self.accordion_frame = tk.Frame(root)
        self.accordion_frame.place(x=50, y=100)

        self.create_accordion("Nama Ikan", "nama")
        self.create_accordion("Jenis Ikan", "jenis")
        self.create_accordion("Warna Ikan", "warna")

        # Create buttons for adding and deleting fish
        self.btn_tambah = tk.Button(root, text="Tambah Data Ikan", command=self.data_ikan.tambah_data, bg='white')
        self.canvas.create_window(200, 400, window=self.btn_tambah)

        self.btn_hapus = tk.Button(root, text="Hapus Data Ikan", command=self.data_ikan.hapus_data, bg='white')
        self.canvas.create_window(200, 450, window=self.btn_hapus)

        # Create exit button
        self.btn_keluar = tk.Button(root, text="Keluar", command=root.quit, bg='white')
        self.canvas.create_window(200, 500, window=self.btn_keluar)

    def create_accordion(self, title, data_type):
        # Create a button to serve as the accordion header
        btn_accordion = tk.Button(self.accordion_frame, text=title, width=30, command=lambda: self.toggle_dropdown(data_type))
        btn_accordion.pack()

        # Create a frame that will act as the dropdown content
        frame_dropdown = tk.Frame(self.accordion_frame, bd=1, relief="sunken")
        frame_dropdown.pack(fill="both", expand=True)
        frame_dropdown.pack_forget()  # Initially hide it

        # Store frame in a dictionary for later reference
        setattr(self, f"frame_{data_type}", frame_dropdown)

    def toggle_dropdown(self, data_type):
        frame = getattr(self, f"frame_{data_type}")
        if frame.winfo_viewable():
            frame.pack_forget()  # Hide the dropdown
        else:
            self.show_data(data_type)
            frame.pack(fill="both", expand=True)  # Show the dropdown

    def show_data(self, data_type):
        # Clear any previous content
        frame = getattr(self, f"frame_{data_type}")
        for widget in frame.winfo_children():
            widget.destroy()

        # Get data and display in labels
        data = self.data_ikan.get_fish_data(data_type)
        if data == "Invalid data type.":
            messagebox.showwarning("Peringatan", "Pilihan tidak valid.")
            return

        label_data = tk.Label(frame, text=data, anchor="w", justify="left")
        label_data.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
