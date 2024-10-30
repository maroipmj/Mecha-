import tkinter as tk
from tkinter import ttk, messagebox
from utils import baca_file, tulis_file, tulis_history, keluar, tampilkan_header

# Halaman untuk menampilkan data ikan
def halaman_tampilkan_data_ikan():
    tampil_window = tk.Toplevel()
    tampil_window.title("Tampilkan Data Ikan")
    tampil_window.configure(bg="#003366")
    tampilkan_header(tampil_window, "Tampilkan Data Ikan")

    label_pilihan = tk.Label(tampil_window, text="Pilih Data yang ingin dilihat:", bg="#003366", fg="white")
    label_pilihan.pack(pady=5)

    pilihan = ttk.Combobox(tampil_window)
    pilihan['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    pilihan.pack(pady=5)

    ikan_listbox = tk.Listbox(tampil_window, width=50, height=10)
    ikan_listbox.pack(pady=20)

    def tampil_data():
        ikan_listbox.delete(0, tk.END)
        if pilihan.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Nama: {item[0]}")
            tulis_history("Menampilkan data Nama Ikan")
        elif pilihan.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Jenis: {item[0]}")
            tulis_history("Menampilkan data Jenis Ikan")
        elif pilihan.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Warna: {item[0]}")
            tulis_history("Menampilkan data Warna Ikan")
        elif pilihan.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Waktu: {item[0]} jam, Jarak: {item[1]} km")
            tulis_history("Menampilkan data Jarak Tempuh")

    tombol_tampil = tk.Button(tampil_window, text="Tampilkan Data", command=tampil_data, bg="white", fg="black")
    tombol_tampil.pack(pady=10)

    tombol_keluar = tk.Button(tampil_window, text="Keluar", command=lambda: keluar(tampil_window), bg="red", fg="white")
    tombol_keluar.pack(pady=10)

# Halaman untuk tambah data ikan
def halaman_tambah_data():
    tambah_window = tk.Toplevel()
    tambah_window.title("Tambah Data Ikan")
    tambah_window.configure(bg="#003366")

    label_tambah = tk.Label(tambah_window, text="Pilih Data Ikan yang ingin ditambah:", bg="#003366", fg="white")
    label_tambah.grid(row=0, column=0, padx=10, pady=5)

    dropdown_tambah = ttk.Combobox(tambah_window)
    dropdown_tambah['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_tambah.grid(row=0, column=1, padx=10, pady=5)

    label_data_baru = tk.Label(tambah_window, text="Data Baru:", bg="#003366", fg="white")
    label_data_baru.grid(row=1, column=0, padx=10, pady=5)

    entry_data_baru = tk.Entry(tambah_window)
    entry_data_baru.grid(row=1, column=1, padx=10, pady=5)

    label_waktu = tk.Label(tambah_window, text="Waktu (jam):", bg="#003366", fg="white")
    entry_waktu = tk.Entry(tambah_window)
    label_jarak = tk.Label(tambah_window, text="Jarak (km):", bg="#003366", fg="white")
    entry_jarak = tk.Entry(tambah_window)

    def update_fields(event):
        if dropdown_tambah.get() == "Jarak Tempuh":
            label_data_baru.grid_forget()
            entry_data_baru.grid_forget()

            label_waktu.grid(row=1, column=0, padx=10, pady=5)
            entry_waktu.grid(row=1, column=1, padx=10, pady=5)
            label_jarak.grid(row=2, column=0, padx=10, pady=5)
            entry_jarak.grid(row=2, column=1, padx=10, pady=5)
        else:
            label_waktu.grid_forget()
            entry_waktu.grid_forget()
            label_jarak.grid_forget()
            entry_jarak.grid_forget()

            label_data_baru.grid(row=1, column=0, padx=10, pady=5)
            entry_data_baru.grid(row=1, column=1, padx=10, pady=5)

    dropdown_tambah.bind("<<ComboboxSelected>>", update_fields)

    def tambah_data():
        if dropdown_tambah.get() == "Jarak Tempuh":
            waktu = entry_waktu.get()
            jarak = entry_jarak.get()

            if waktu and jarak:
                jarak_berenang = baca_file('jarak_berenang.txt')
                jarak_berenang.append([waktu, jarak])
                tulis_file('jarak_tempuh.txt', jarak_berenang)
                tulis_history(f"Menambahkan Jarak Tempuh: Waktu {waktu} jam, Jarak {jarak} km")
                messagebox.showinfo("Sukses", "Data jarak tempuh berhasil ditambahkan!")
            else:
                messagebox.showwarning("Peringatan", "Silakan isi waktu dan jarak.")
        else:
            data_baru = entry_data_baru.get()

            if data_baru:
                if dropdown_tambah.get() == "Nama Ikan":
                    nama_ikan = baca_file('nama_ikan.txt')
                    nama_ikan.append([data_baru])
                    tulis_file('nama_ikan.txt', nama_ikan)
                    tulis_history(f"Menambahkan Nama Ikan: {data_baru}")
                elif dropdown_tambah.get() == "Jenis Ikan":
                    jenis_ikan = baca_file('nama_jenis.txt')
                    jenis_ikan.append([data_baru])
                    tulis_file('nama_jenis.txt', jenis_ikan)
                    tulis_history(f"Menambahkan Jenis Ikan: {data_baru}")
                elif dropdown_tambah.get() == "Warna Ikan":
                    warna_ikan = baca_file('nama_warna.txt')
                    warna_ikan.append([data_baru])
                    tulis_file('nama_warna.txt', warna_ikan)
                    tulis_history(f"Menambahkan Warna Ikan: {data_baru}")
                messagebox.showinfo("Sukses", f"Data {dropdown_tambah.get()} berhasil ditambahkan!")
            else:
                messagebox.showwarning("Peringatan", "Silakan isi data baru.")

    tombol_tambah = tk.Button(tambah_window, text="Tambah Data", command=tambah_data, bg="white", fg="black")
    tombol_tambah.grid(row=3, column=1, padx=10, pady=10)

    tombol_keluar = tk.Button(tambah_window, text="Keluar", command=lambda: keluar(tambah_window), bg="red", fg="white")
    tombol_keluar.grid(row=4, column=1, padx=10, pady=10)

def halaman_hapus_data():
    hapus_window = tk.Toplevel()
    hapus_window.title("Hapus Data Ikan")
    hapus_window.configure(bg="#003366")
    tampilkan_header(hapus_window, "Hapus Data Ikan")  # Pastikan header juga menggunakan pack

    # Ubah semua grid menjadi pack
    label_hapus = tk.Label(hapus_window, text="Pilih Data Ikan yang ingin dihapus:", bg="#003366", fg="white")
    label_hapus.pack(pady=5)

    # Misalnya dropdown dan tombol juga harus menggunakan pack
    dropdown_hapus = ttk.Combobox(hapus_window)
    dropdown_hapus['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_hapus.pack(pady=5)

    tombol_hapus = tk.Button(hapus_window, text="Hapus Data", bg="white", fg="black")
    tombol_hapus.pack(pady=10)

    tombol_keluar = tk.Button(hapus_window, text="Keluar", command=lambda: keluar(hapus_window), bg="red", fg="white")
    tombol_keluar.pack(pady=10)

    # Mirip dengan bagian tambahkan data, tetapi untuk menghapus data
    pass

# Halaman untuk melihat history call
def halaman_history_call():
    history_window = tk.Toplevel()
    history_window.title("History Call")
    history_window.configure(bg="#003366")
    tampilkan_header(history_window, "History Call")

    listbox_history = tk.Listbox(history_window, width=50, height=10)
    listbox_history.pack(pady=20)

    with open('history.txt', 'r') as f:
        for line in f.readlines():
            listbox_history.insert(tk.END, line)

    tombol_keluar = tk.Button(history_window, text="Keluar", command=lambda: keluar(history_window), bg="red", fg="white")
    tombol_keluar.pack(pady=10)
