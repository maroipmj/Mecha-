import tkinter as tk
from tkinter import messagebox
import os

# Fungsi untuk memuat data ikan dari file txt
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

# Load data dari file eksternal
data_nama_ikan = load_data("nama_ikan.txt")
data_jenis_ikan = load_data("nama_jenis.txt")
data_warna_ikan = load_data("nama_warna.txt")

# Fungsi untuk menampilkan jendela tambah ikan baru
def tambah_ikan():
    def simpan_ikan():
        nama = entry_nama.get()
        jenis = entry_jenis.get()
        warna = entry_warna.get()
        if nama and jenis and warna:
            data_nama_ikan.append(nama)
            data_jenis_ikan.append(jenis)
            data_warna_ikan.append(warna)
            save_data("nama_ikan.txt", data_nama_ikan)
            save_data("nama_jenis.txt", data_jenis_ikan)
            save_data("nama_warna.txt", data_warna_ikan)
            messagebox.showinfo("Berhasil", "Ikan berhasil ditambahkan!")
            update_list_ikan()
            tambah_jendela.destroy()
            root.attributes('-disabled', False)
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")

    root.attributes('-disabled', True)
    tambah_jendela = tk.Toplevel(root)
    tambah_jendela.title("Tambah Ikan Baru")
    tambah_jendela.geometry("300x200")

    tk.Label(tambah_jendela, text="Nama Ikan").pack()
    entry_nama = tk.Entry(tambah_jendela)
    entry_nama.pack()

    tk.Label(tambah_jendela, text="Jenis Ikan").pack()
    entry_jenis = tk.Entry(tambah_jendela)
    entry_jenis.pack()

    tk.Label(tambah_jendela, text="Warna Ikan").pack()
    entry_warna = tk.Entry(tambah_jendela)
    entry_warna.pack()

    tk.Button(tambah_jendela, text="Tambah Ikan", command=simpan_ikan).pack(pady=10)

# Fungsi untuk menampilkan detail ikan
def detail_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        nama_ikan = data_nama_ikan[index]
        jenis_ikan = data_jenis_ikan[index] if index < len(data_jenis_ikan) else "Tidak diketahui"
        warna_ikan = data_warna_ikan[index] if index < len(data_warna_ikan) else "Tidak diketahui"

        root.attributes('-disabled', True)
        detail_jendela = tk.Toplevel(root)
        detail_jendela.title("Detail Ikan")
        detail_jendela.geometry("300x200")

        tk.Label(detail_jendela, text=f"Nama Ikan : {nama_ikan}").pack()
        tk.Label(detail_jendela, text=f"Jenis : {jenis_ikan}").pack()
        tk.Label(detail_jendela, text=f"Warna : {warna_ikan}").pack()

        # Fungsi untuk kembali ke jendela utama (menu ikan)
        def kembali():
            detail_jendela.destroy()
            root.attributes('-disabled', False)

        # Tombol Kembali untuk menutup jendela detail
        tk.Button(detail_jendela, text="Kembali", command=kembali).pack(pady=10)

        # Menangani event jika user menutup jendela detail dengan tombol "X"
        detail_jendela.protocol("WM_DELETE_WINDOW", kembali)
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan terlebih dahulu.")

# Fungsi untuk mengedit data ikan
def edit_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]

        def simpan_perubahan():
            nama = entry_nama.get()
            jenis = entry_jenis.get()
            warna = entry_warna.get()
            if nama and jenis and warna:
                data_nama_ikan[index] = nama
                data_jenis_ikan[index] = jenis
                data_warna_ikan[index] = warna
                save_data("nama_ikan.txt", data_nama_ikan)
                save_data("nama_jenis.txt", data_jenis_ikan)
                save_data("nama_warna.txt", data_warna_ikan)
                messagebox.showinfo("Berhasil", "Data ikan berhasil diperbarui!")
                update_list_ikan()
                edit_jendela.destroy()
                root.attributes('-disabled', False)
            else:
                messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")

        # Fungsi untuk kembali ke jendela utama (menu ikan)
        def kembali():
            edit_jendela.destroy()
            root.attributes('-disabled', False)

        root.attributes('-disabled', True)
        edit_jendela = tk.Toplevel(root)
        edit_jendela.title("Edit Ikan")
        edit_jendela.geometry("300x200")

        tk.Label(edit_jendela, text="Nama Ikan").pack()
        entry_nama = tk.Entry(edit_jendela)
        entry_nama.pack()
        entry_nama.insert(0, data_nama_ikan[index])

        tk.Label(edit_jendela, text="Jenis Ikan").pack()
        entry_jenis = tk.Entry(edit_jendela)
        entry_jenis.pack()
        entry_jenis.insert(0, data_jenis_ikan[index] if index < len(data_jenis_ikan) else "")

        tk.Label(edit_jendela, text="Warna Ikan").pack()
        entry_warna = tk.Entry(edit_jendela)
        entry_warna.pack()
        entry_warna.insert(0, data_warna_ikan[index] if index < len(data_warna_ikan) else "")

        tk.Button(edit_jendela, text="Simpan Perubahan", command=simpan_perubahan).pack(pady=10)
        tk.Button(edit_jendela, text="Kembali", command=kembali).pack(pady=5)

        # Menangani event jika user menutup jendela edit dengan tombol "X"
        edit_jendela.protocol("WM_DELETE_WINDOW", kembali)
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan yang ingin diedit.")

# Fungsi untuk menghapus ikan yang dipilih
def hapus_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus ikan '{data_nama_ikan[index]}'?")
        if konfirmasi:
            data_nama_ikan.pop(index)
            if index < len(data_jenis_ikan):
                data_jenis_ikan.pop(index)
            if index < len(data_warna_ikan):
                data_warna_ikan.pop(index)
            
            save_data("nama_ikan.txt", data_nama_ikan)
            save_data("nama_jenis.txt", data_jenis_ikan)
            save_data("nama_warna.txt", data_warna_ikan)
            
            update_list_ikan()
            messagebox.showinfo("Berhasil", "Ikan berhasil dihapus.")
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan yang ingin dihapus.")

# Fungsi untuk memperbarui daftar ikan di listbox
def update_list_ikan():
    listbox_ikan.delete(0, tk.END)
    for i, ikan in enumerate(data_nama_ikan, start=1):
        listbox_ikan.insert(tk.END, f"{i}: {ikan}")

# Fungsi untuk kembali ke menu utama
def kembali_ke_menu():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Data Ikan")
root.geometry("400x400")

# Label judul
label_judul = tk.Label(root, text="Data Ikan", font=("Arial", 16, "bold"))
label_judul.pack(pady=10)

# List Ikan
frame_list = tk.Frame(root)
frame_list.pack()

listbox_ikan = tk.Listbox(frame_list, width=30, height=10)
listbox_ikan.pack(side="left")

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")
listbox_ikan.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_ikan.yview)

# Tombol Tambah, Hapus, Detail, Edit
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="+", command=tambah_ikan).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="-", command=hapus_ikan).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Detail", command=detail_ikan).grid(row=3, column=1, padx=5)
tk.Button(frame_buttons, text="Edit", command=edit_ikan).grid(row=0, column=1, padx=5)

# Tombol kembali
tk.Button(root, text="Kembali", command=kembali_ke_menu).pack(pady=8)

# Load daftar ikan ke listbox
update_list_ikan()

# Menjalankan aplikasi
root.mainloop()
