import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class DataIkan:
    def _init_(self, nama_file, jenis_file, warna_file):
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
            return data_dict

        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    data_dict[key.strip()] = value.strip()
        return data_dict

    def simpan_file_dict(self, file, data):
        with open(file, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}:{value}\n")

class TambahDataDialog(simpledialog.Dialog):
    def _init_(self, parent, title, jenis_options, warna_options):
        self.nama_ikan = None
        self.jenis_ikan = None
        self.warna_ikan = None
        self.jenis_options = jenis_options
        self.warna_options = warna_options
        super()._init_(parent, title)

    def body(self, master):
        tk.Label(master, text="Nama Ikan:").grid(row=0, column=0)
        tk.Label(master, text="Jenis Ikan:").grid(row=1, column=0)
        tk.Label(master, text="Warna Ikan:").grid(row=2, column=0)

        self.entry_nama = tk.Entry(master)
        self.entry_nama.grid(row=0, column=1)

        self.jenis_var = tk.StringVar(master)
        self.jenis_var.set(self.jenis_options[0])
        self.optionmenu_jenis = tk.OptionMenu(master, self.jenis_var, *self.jenis_options)
        self.optionmenu_jenis.grid(row=1, column=1)

        self.warna_var = tk.StringVar(master)
        self.warna_var.set(self.warna_options[0])
        self.optionmenu_warna = tk.OptionMenu(master, self.warna_var, *self.warna_options)
        self.optionmenu_warna.grid(row=2, column=1)

    def apply(self):
        self.nama_ikan = self.entry_nama.get()
        self.jenis_ikan = self.jenis_var.get()
        self.warna_ikan = self.warna_var.get()

class EditDataDialog(simpledialog.Dialog):
    def _init_(self, parent, title, nama_ikan, jenis_ikan, warna_ikan, jenis_options, warna_options):
        self.nama_ikan = nama_ikan
        self.jenis_ikan = jenis_ikan
        self.warna_ikan = warna_ikan
        self.jenis_options = jenis_options
        self.warna_options = warna_options
        super()._init_(parent, title)

    def body(self, master):
        tk.Label(master, text="Nama Ikan:").grid(row=0, column=0)
        tk.Label(master, text="Jenis Ikan:").grid(row=1, column=0)
        tk.Label(master, text="Warna Ikan:").grid(row=2, column=0)

        self.entry_nama = tk.Entry(master)
        self.entry_nama.insert(0, self.nama_ikan)
        self.entry_nama.grid(row=0, column=1)

        self.jenis_var = tk.StringVar(master)
        self.jenis_var.set(self.jenis_ikan)
        self.optionmenu_jenis = tk.OptionMenu(master, self.jenis_var, *self.jenis_options)
        self.optionmenu_jenis.grid(row=1, column=1)

        self.warna_var = tk.StringVar(master)
        self.warna_var.set(self.warna_ikan)
        self.optionmenu_warna = tk.OptionMenu(master, self.warna_var, *self.warna_options)
        self.optionmenu_warna.grid(row=2, column=1)

    def apply(self):
        self.nama_ikan = self.entry_nama.get()
        self.jenis_ikan = self.jenis_var.get()
        self.warna_ikan = self.warna_var.get()

class GUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Data Ikan")
        self.root.geometry("500x600")  # Adjusted size

        # Create a canvas to set the background color
        self.canvas = tk.Canvas(root, width=500, height=600, bg='lightblue')  # Latar belakang biru seperti akuarium
        self.canvas.pack(fill="both", expand=True)

        self.data_ikan = DataIkan('nama_ikan.txt', 'nama_jenis.txt', 'nama_warna.txt')

        # Add title text with black color
        self.canvas.create_text(250, 40, text="Data Ikan", font=("Arial", 16, "bold"), fill="black")

        # Create listbox to view data
        self.buat_listbox_data()

        # Create buttons for adding, editing, and deleting fish
        self.btn_tambah = tk.Button(root, text="Tambah Data Ikan", command=self.tambah_data, bg='white')
        self.canvas.create_window(250, 400, window=self.btn_tambah)

        self.btn_edit = tk.Button(root, text="Edit Data Ikan", command=self.edit_data, bg='white')
        self.canvas.create_window(250, 450, window=self.btn_edit)

        self.btn_hapus = tk.Button(root, text="Hapus Data Ikan", command=self.hapus_data, bg='white')
        self.canvas.create_window(250, 500, window=self.btn_hapus)

        # Create exit button
        self.btn_keluar = tk.Button(root, text="Keluar", command=root.quit, bg='white')
        self.canvas.create_window(250, 550, window=self.btn_keluar)

    def buat_listbox_data(self):
        # Buat listbox untuk menampilkan data ikan
        self.listbox = tk.Listbox(self.root, width=70, height=15)
        self.listbox.pack()

        # Mengisi listbox dengan data ikan
        self.isi_listbox()

    def isi_listbox(self):
        self.listbox.delete(0, tk.END)  # Bersihkan listbox
        for id_ikan in self.data_ikan.nama_data.keys():
            nama = self.data_ikan.nama_data.get(id_ikan, "N/A")
            jenis = self.data_ikan.jenis_data.get(id_ikan, "N/A")
            warna = self.data_ikan.warna_data.get(id_ikan, "N/A")
            self.listbox.insert(tk.END, f"ID: {id_ikan}, Nama: {nama}, Jenis: {jenis}, Warna: {warna}")

    def tambah_data(self):
        jenis_options = list(set(self.data_ikan.jenis_data.values()))
        if not jenis_options:
            messagebox.showwarning("Peringatan", "Data jenis ikan kosong.")
            return
        warna_options = list(set(self.data_ikan.warna_data.values()))
        if not warna_options:
            messagebox.showwarning("Peringatan", "Data warna ikan kosong.")
            return

        dialog = TambahDataDialog(self.root, "Tambah Data Ikan", jenis_options, warna_options)
        if dialog.nama_ikan:
            id_ikan = str(len(self.data_ikan.nama_data) + 1)
            self.data_ikan.nama_data[id_ikan] = dialog.nama_ikan
            self.data_ikan.jenis_data[id_ikan] = dialog.jenis_ikan
            self.data_ikan.warna_data[id_ikan] = dialog.warna_ikan

            self.data_ikan.simpan_file_dict(self.data_ikan.nama_file, self.data_ikan.nama_data)
            self.data_ikan.simpan_file_dict(self.data_ikan.jenis_file, self.data_ikan.jenis_data)
            self.data_ikan.simpan_file_dict(self.data_ikan.warna_file, self.data_ikan.warna_data)

            messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil ditambahkan!")
            self.isi_listbox()
        else:
            messagebox.showwarning("Peringatan", "Data ikan tidak lengkap atau dibatalkan.")

    def hapus_data(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data ikan yang ingin dihapus.")
            return
        
        selected_index = selected[0]
        id_ikan = list(self.data_ikan.nama_data.keys())[selected_index]

        result = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus data ikan dengan ID {id_ikan}?")
        if result:
            del self.data_ikan.nama_data[id_ikan]
            del self.data_ikan.jenis_data[id_ikan]
            del self.data_ikan.warna_data[id_ikan]

            self.data_ikan.simpan_file_dict(self.data_ikan.nama_file, self.data_ikan.nama_data)
            self.data_ikan.simpan_file_dict(self.data_ikan.jenis_file, self.data_ikan.jenis_data)
            self.data_ikan.simpan_file_dict(self.data_ikan.warna_file, self.data_ikan.warna_data)

            messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil dihapus!")
            self.isi_listbox()

    def edit_data(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data ikan yang ingin diedit.")
            return
        
        selected_index = selected[0]
        id_ikan = list(self.data_ikan.nama_data.keys())[selected_index]
        nama_ikan = self.data_ikan.nama_data[id_ikan]
        jenis_ikan = self.data_ikan.jenis_data[id_ikan]
        warna_ikan = self.data_ikan.warna_data[id_ikan]

        jenis_options = list(set(self.data_ikan.jenis_data.values()))
        if not jenis_options:
            messagebox.showwarning("Peringatan", "Data jenis ikan kosong.")
            return
        warna_options = list(set(self.data_ikan.warna_data.values()))
        if not warna_options:
            messagebox.showwarning("Peringatan", "Data warna ikan kosong.")
            return

        dialog = EditDataDialog(self.root, "Edit Data Ikan", nama_ikan, jenis_ikan, warna_ikan, jenis_options, warna_options)
        if dialog.nama_ikan:
            self.data_ikan.nama_data[id_ikan] = dialog.nama_ikan
            self.data_ikan.jenis_data[id_ikan] = dialog.jenis_ikan
            self.data_ikan.warna_data[id_ikan] = dialog.warna_ikan

            self.data_ikan.simpan_file_dict(self.data_ikan.nama_file, self.data_ikan.nama_data)
            self.data_ikan.simpan_file_dict(self.data_ikan.jenis_file, self.data_ikan.jenis_data)
            self.data_ikan.simpan_file_dict(self.data_ikan.warna_file, self.data_ikan.warna_data)

            messagebox.showinfo("Info", f"Data ikan dengan ID {id_ikan} berhasil diperbarui!")
            self.isi_listbox()
        else:
            messagebox.showwarning("Peringatan", "Perubahan data ikan dibatalkan.")

if __name__ == "_main_":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()