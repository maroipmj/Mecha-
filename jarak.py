import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# Nama file untuk menyimpan data jenis ikan, transaksi, dan jarak tempuh + waktu
FILE_JENIS_IKAN = "nama_jenis.txt"
FILE_TRANSAKSI = "transaksi.txt"
FILE_JARAK_TEMPUH = "jarak_tempuh.txt"

# Fungsi untuk memastikan file data ada
def ensure_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            pass  # Membuat file kosong jika belum ada

# Fungsi untuk memuat data dari file txt
def load_data(filename):
    data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                item = line.strip()
                if item:
                    data.append(item)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' tidak ditemukan.")
    return data

# Fungsi untuk menyimpan data ke file txt
def save_data(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")

# Pastikan file ada
ensure_file_exists(FILE_JENIS_IKAN)
ensure_file_exists(FILE_TRANSAKSI)
ensure_file_exists(FILE_JARAK_TEMPUH)

# Load data jenis ikan, transaksi, dan jarak tempuh + waktu
data_jenis_ikan = load_data(FILE_JENIS_IKAN)
data_transaksi = load_data(FILE_TRANSAKSI)
data_jarak_waktu = load_data(FILE_JARAK_TEMPUH)

# Fungsi untuk memperbarui daftar transaksi di listbox
def update_list_transaksi():
    listbox_transaksi.delete(0, tk.END)
    for transaksi, jarak_waktu in zip(data_transaksi, data_jarak_waktu):
        jarak, waktu = map(float, jarak_waktu.split(","))
        try:
            kecepatan = round(jarak / waktu, 2)
        except ZeroDivisionError:
            kecepatan = 0
        listbox_transaksi.insert(tk.END, f"{transaksi} - {jarak} km - {waktu} jam - {kecepatan} km/jam")

# Fungsi untuk menampilkan jendela tambah transaksi
def tambah_transaksi():
    def simpan_transaksi():
        ikan = combo_ikan.get()
        jarak = entry_jarak.get()
        waktu = entry_waktu.get()

        if not ikan or not jarak or not waktu:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")
            return

        transaksi = f"{ikan}"
        data_transaksi.append(transaksi)
        data_jarak_waktu.append(f"{jarak},{waktu}")

        save_data(FILE_TRANSAKSI, data_transaksi)
        save_data(FILE_JARAK_TEMPUH, data_jarak_waktu)

        messagebox.showinfo("Berhasil", "Transaksi berhasil ditambahkan!")
        update_list_transaksi()
        tambah_jendela.destroy()
        root.attributes('-disabled', False)

    root.attributes('-disabled', True)
    tambah_jendela = tk.Toplevel(root)
    tambah_jendela.title("Tambah Transaksi")
    tambah_jendela.geometry("300x300")
    tambah_jendela.configure(bg="#E8EAF6")

    # Label Judul
    tk.Label(tambah_jendela, text="Tambah Transaksi", font=("Arial", 14, "bold"), bg="#E8EAF6").pack(pady=10)

    # Pilih ikan
    tk.Label(tambah_jendela, text="Pilih Ikan", bg="#E8EAF6").pack(pady=5)
    combo_ikan = ttk.Combobox(tambah_jendela, values=data_jenis_ikan, state='readonly')
    combo_ikan.pack(pady=5)
    
    # Input jarak
    tk.Label(tambah_jendela, text="Jarak (km)", bg="#E8EAF6").pack(pady=5)
    entry_jarak = tk.Entry(tambah_jendela)
    entry_jarak.pack(pady=5)

    # Input waktu
    tk.Label(tambah_jendela, text="Waktu (jam)", bg="#E8EAF6").pack(pady=5)
    entry_waktu = tk.Entry(tambah_jendela)
    entry_waktu.pack(pady=5)

    # Tombol Simpan dan Kembali
    tk.Button(tambah_jendela, text="Simpan", command=simpan_transaksi, bg="#4CAF50", fg="white", width=10).pack(pady=10)
    tk.Button(tambah_jendela, text="Kembali", command=lambda: tambah_jendela.destroy(), bg="#B0BEC5", fg="black", width=10).pack(pady=5)

# Fungsi untuk kembali ke menu utama
def kembali():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Data Transaksi Ikan")
root.geometry("600x400")
root.configure(bg="#E8EAF6")

# Label judul
label_judul = tk.Label(root, text="Transaksi Ikan", font=("Arial", 16, "bold"), bg="#5E35B1", fg="white")
label_judul.pack(pady=10)

# Frame untuk List Transaksi
frame_list = tk.Frame(root, bg="#E8EAF6")
frame_list.pack(pady=10, padx=10)

tk.Label(frame_list, text="Ikan       Jarak    Waktu    Kecepatan", font=("Arial", 10, "bold"), bg="#E8EAF6").pack()

# List Transaksi
listbox_transaksi = tk.Listbox(frame_list, width=60, height=10)
listbox_transaksi.pack(side="left", padx=5)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")
listbox_transaksi.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_transaksi.yview)

# Tombol Tambah Transaksi
tk.Button(root, text="Tambah Transaksi", command=tambah_transaksi, bg="#4CAF50", fg="white", width=15).pack(pady=10)

# Tombol Kembali
tk.Button(root, text="Kembali", command=kembali, bg="#B0BEC5", fg="black", width=15).pack(pady=10)

# Load daftar transaksi ke listbox
update_list_transaksi()

# Menjalankan aplikasi
root.mainloop()
