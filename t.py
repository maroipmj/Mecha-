import tkinter as tk
from tkinter import messagebox

# Fungsi untuk membaca data dari file
def load_data():
    try:
        with open('nama_ikan.txt', 'r') as file:
            nama_ikan = file.read().splitlines()
        with open('nama_warna.txt', 'r') as file:
            warna_ikan = file.read().splitlines()
        with open('nama_jenis.txt', 'r') as file:
            jenis_ikan = file.read().splitlines()
        return [{"Nama": nama, "Warna": warna, "Jenis": jenis} 
                for nama, warna, jenis in zip(nama_ikan, warna_ikan, jenis_ikan)]
    except FileNotFoundError:
        messagebox.showerror("Error", "File data ikan tidak ditemukan!")
        return []

# Fungsi untuk menyimpan data ikan ke file
def save_data():
    with open('nama_ikan.txt', 'w') as file:
        file.write("\n".join([ikan["Nama"] for ikan in data_ikan]))
    with open('nama_warna.txt', 'w') as file:
        file.write("\n".join([ikan["Warna"] for ikan in data_ikan]))
    with open('nama_jenis.txt', 'w') as file:
        file.write("\n".join([ikan["Jenis"] for ikan in data_ikan]))

# Fungsi untuk membuka window detail ikan
def buka_window_detail():
    selected = list_ikan.curselection()
    if selected:
        index = selected[0]
        ikan = data_ikan[index]
        
        # Membuat window detail
        window_detail = tk.Toplevel(root)
        window_detail.title("Detail Ikan")
        
        tk.Label(window_detail, text=f"Nama Ikan: {ikan['Nama']}").pack()
        tk.Label(window_detail, text=f"Jenis: {ikan['Jenis']}").pack()
        tk.Label(window_detail, text=f"Warna: {ikan['Warna']}").pack()
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan untuk melihat detailnya.")

# Fungsi untuk membuka window tambah ikan
def buka_window_tambah():
    def tambah_ikan():
        nama = entry_nama.get()
        jenis = entry_jenis.get()
        warna = entry_warna.get()
        
        if nama and jenis and warna:
            data_ikan.append({"Nama": nama, "Warna": warna, "Jenis": jenis})
            list_ikan.insert(tk.END, nama)
            save_data()  # Simpan data ke file
            window_tambah.destroy()
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")

    # Membuat window tambah ikan
    window_tambah = tk.Toplevel(root)
    window_tambah.title("Tambah Ikan")
    
    tk.Label(window_tambah, text="Nama").pack()
    entry_nama = tk.Entry(window_tambah)
    entry_nama.pack()
    
    tk.Label(window_tambah, text="Jenis").pack()
    entry_jenis = tk.Entry(window_tambah)
    entry_jenis.pack()
    
    tk.Label(window_tambah, text="Warna").pack()
    entry_warna = tk.Entry(window_tambah)
    entry_warna.pack()
    
    btn_tambah = tk.Button(window_tambah, text="Tambah Ikan", command=tambah_ikan)
    btn_tambah.pack()

# Fungsi untuk membuka window edit ikan
def buka_window_edit():
    selected = list_ikan.curselection()
    if selected:
        global current_edit_index
        current_edit_index = selected[0]
        ikan = data_ikan[current_edit_index]
        
        def simpan_edit():
            data_ikan[current_edit_index] = {
                "Nama": edit_nama_entry.get(),
                "Jenis": edit_jenis_entry.get(),
                "Warna": edit_warna_entry.get()
            }
            save_data()
            list_ikan.delete(current_edit_index)
            list_ikan.insert(current_edit_index, edit_nama_entry.get())
            window_edit.destroy()
        
        # Membuat window edit ikan
        window_edit = tk.Toplevel(root)
        window_edit.title("Edit Ikan")
        
        tk.Label(window_edit, text="Nama").pack()
        edit_nama_entry = tk.Entry(window_edit)
        edit_nama_entry.pack()
        edit_nama_entry.insert(0, ikan["Nama"])
        
        tk.Label(window_edit, text="Jenis").pack()
        edit_jenis_entry = tk.Entry(window_edit)
        edit_jenis_entry.pack()
        edit_jenis_entry.insert(0, ikan["Jenis"])
        
        tk.Label(window_edit, text="Warna").pack()
        edit_warna_entry = tk.Entry(window_edit)
        edit_warna_entry.pack()
        edit_warna_entry.insert(0, ikan["Warna"])
        
        btn_simpan = tk.Button(window_edit, text="Simpan", command=simpan_edit)
        btn_simpan.pack()
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan untuk mengedit.")

# Membaca data awal
data_ikan = load_data()
current_edit_index = None

# Membuat jendela utama
root = tk.Tk()
root.title("Data Ikan")

# Daftar ikan di jendela utama
tk.Label(root, text="List Ikan").pack()
list_ikan = tk.Listbox(root)
list_ikan.pack()

# Menambahkan ikan ke dalam daftar listbox
for ikan in data_ikan:
    list_ikan.insert(tk.END, ikan["Nama"])

# Tombol-tombol untuk membuka window berbeda
btn_detail = tk.Button(root, text="Detail", command=buka_window_detail)
btn_detail.pack()

btn_tambah = tk.Button(root, text="Tambah Ikan", command=buka_window_tambah)
btn_tambah.pack()

btn_edit = tk.Button(root, text="Edit Ikan", command=buka_window_edit)
btn_edit.pack()

# Menjalankan aplikasi
root.mainloop()
