import tkinter as tk
from tkinter import messagebox
import os

# Nama file
filename_nama = "nama_ikan.txt"
filename_jenis = "nama_jenis.txt"
filename_warna = "nama_warna.txt"

# Mengecek apakah file ada; jika tidak, membuat file baru
for file in [filename_nama, filename_jenis, filename_warna]:
    if not os.path.exists(file):
        with open(file, "w") as f:
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

# Load data dari file eksternal
data_nama_ikan = load_data(filename_nama)
data_jenis_ikan = load_data(filename_jenis)
data_warna_ikan = load_data(filename_warna)

# Fungsi untuk menampilkan jendela tambah jenis baru
def tambah_jenis():
    def simpan_jenis():
        nama = entry_nama.get()
        jenis = entry_jenis.get()
        warna = entry_warna.get()
        if nama and jenis and warna:
            data_nama_ikan.append(nama)
            data_jenis_ikan.append(jenis)
            data_warna_ikan.append(warna)
            save_data(filename_nama, data_nama_ikan)
            save_data(filename_jenis, data_jenis_ikan)
            save_data(filename_warna, data_warna_ikan)
            messagebox.showinfo("Berhasil", "Data berhasil ditambahkan!")
            update_list_ikan()
            tambah_jendela.destroy()
            root.attributes('-disabled', False)
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")

    root.attributes('-disabled', True)
    tambah_jendela = tk.Toplevel(root)
    tambah_jendela.title("Tambah Data Baru")
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

    tk.Button(tambah_jendela, text="Tambah Data", command=simpan_jenis).pack(pady=10)

# Fungsi untuk menampilkan detail ikan
def detail_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        nama_ikan = data_nama_ikan[index] if index < len(data_nama_ikan) else "Tidak diketahui"
        jenis_ikan = data_jenis_ikan[index] if index < len(data_jenis_ikan) else "Tidak diketahui"
        warna_ikan = data_warna_ikan[index] if index < len(data_warna_ikan) else "Tidak diketahui"

        root.attributes('-disabled', True)
        detail_jendela = tk.Toplevel(root)
        detail_jendela.title("Detail Data Ikan")
        detail_jendela.geometry("300x200")

        tk.Label(detail_jendela, text=f"Nama Ikan : {nama_ikan}").pack()
        tk.Label(detail_jendela, text=f"Jenis : {jenis_ikan}").pack()
        tk.Label(detail_jendela, text=f"Warna : {warna_ikan}").pack()

        def kembali():
            detail_jendela.destroy()
            root.attributes('-disabled', False)

        tk.Button(detail_jendela, text="Kembali", command=kembali).pack(pady=10)
        detail_jendela.protocol("WM_DELETE_WINDOW", kembali)
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan terlebih dahulu.")

# Fungsi untuk menghapus data yang dipilih
def hapus_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus data ikan '{data_nama_ikan[index]}'?")
        if konfirmasi:
            data_nama_ikan.pop(index)
            if index < len(data_jenis_ikan):
                data_jenis_ikan.pop(index)
            if index < len(data_warna_ikan):
                data_warna_ikan.pop(index)
            
            save_data(filename_nama, data_nama_ikan)
            save_data(filename_jenis, data_jenis_ikan)
            save_data(filename_warna, data_warna_ikan)
            
            update_list_ikan()
            messagebox.showinfo("Berhasil", "Data berhasil dihapus.")
    else:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus.")

# Fungsi untuk memperbarui daftar ikan di listbox
def update_list_ikan():
    listbox_ikan.delete(0, tk.END)
    for i, ikan in enumerate(data_nama_ikan, start=1):
        listbox_ikan.insert(tk.END, f"{i}: {ikan}")

# Fungsi untuk mengedit hanya warna ikan
def edit_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]

        def simpan_perubahan():
            warna = entry_warna.get()
            if warna:
                # Memperbarui warna ikan yang dipilih
                data_warna_ikan[index] = warna
                save_data(filename_warna, data_warna_ikan)
                messagebox.showinfo("Berhasil", "Warna berhasil diperbarui!")
                update_list_ikan()  # Memperbarui listbox
                edit_jendela.destroy()  # Menutup jendela edit
                root.attributes('-disabled', False)  # Mengaktifkan kembali jendela utama
            else:
                messagebox.showwarning("Peringatan", "Kolom warna harus diisi.")

        def kembali():
            edit_jendela.destroy()
            root.attributes('-disabled', False)

        # Membuat jendela untuk mengedit warna ikan
        root.attributes('-disabled', True)
        edit_jendela = tk.Toplevel(root)
        edit_jendela.title("Edit Warna Ikan")
        edit_jendela.geometry("300x200")

        tk.Label(edit_jendela, text="Warna Ikan").pack()
        entry_warna = tk.Entry(edit_jendela)
        entry_warna.pack()
        entry_warna.insert(0, data_warna_ikan[index])  # Menampilkan warna ikan yang dipilih

        tk.Button(edit_jendela, text="Simpan Perubahan", command=simpan_perubahan).pack(pady=10)
        tk.Button(edit_jendela, text="Kembali", command=kembali).pack(pady=5)

        edit_jendela.protocol("WM_DELETE_WINDOW", kembali)  # Menangani penutupan jendela edit
    else:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin diedit.")

# Fungsi untuk kembali ke menu utama
def kembali_ke_menu():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Data Jenis Ikan")
root.geometry("400x400")
root.configure(bg="#E8EAF6")

# Label judul
label_judul = tk.Label(root, text="Data Jenis Ikan", font=("Arial", 16, "bold"), bg="#5E35B1", fg="white")
label_judul.pack(pady=10)

# Daftar ikan
frame_list = tk.Frame(root, bg="#E8EAF6")
frame_list.pack()

listbox_ikan = tk.Listbox(frame_list, width=30, height=10)
listbox_ikan.pack(side="left")

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")
listbox_ikan.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_ikan.yview)

# Tombol tambah, detail, edit, hapus
frame_buttons = tk.Frame(root, bg="#E8EAF6")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Tambah", command=tambah_jenis, bg="#4CAF50", fg="white", width=8).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Detail", command=detail_ikan, bg="#FFEB3B", fg="black", width=8).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Edit Warna", command=edit_ikan, bg="#FF9800", fg="white", width=8).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Hapus", command=hapus_ikan, bg="#F44336", fg="white", width=8).grid(row=0, column=2, padx=5, pady=5)

# Tombol kembali
tk.Button(root, text="Kembali", command=kembali_ke_menu, bg="#B0BEC5", fg="black", width=15).pack(pady=8)

# Memuat daftar ikan ke listbox
update_list_ikan()

# Menjalankan aplikasi
root.mainloop()
