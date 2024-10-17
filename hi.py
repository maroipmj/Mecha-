import tkinter as tk
from tkinter import ttk, messagebox
import os

# Fungsi untuk membaca file data ikan
def baca_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Fungsi untuk menulis ke file data ikan
def tulis_file(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(item + '\n')

# Fungsi untuk menampilkan data ikan
def tampilkan_data_ikan():
    pilih_window = tk.Toplevel(root)
    pilih_window.title("Tampilkan Data Ikan")
    pilih_window.configure(bg="#003366")

    # Label Pilihan
    label_pilihan = tk.Label(pilih_window, text="Pilih Data yang Ingin Dilihat:", bg="#003366", fg="white")
    label_pilihan.pack(pady=10)

    # Dropdown pilihan data
    pilihan_data = ttk.Combobox(pilih_window, values=["Nama Ikan", "Warna Ikan", "Jenis Ikan"])
    pilihan_data.pack(pady=10)

    # Fungsi untuk membuka jendela berdasarkan pilihan
    def buka_jendela():
        pilihan = pilihan_data.get()
        if pilihan == "Nama Ikan":
            tampilkan_nama_ikan()
        elif pilihan == "Warna Ikan":
            tampilkan_warna_ikan()
        elif pilihan == "Jenis Ikan":
            tampilkan_jenis_ikan()

    # Tombol untuk menampilkan jendela sesuai pilihan
    tampilkan_button = tk.Button(pilih_window, text="Tampilkan", command=buka_jendela, font=("Arial", 12), width=20, bg="white", fg="black")
    tampilkan_button.pack(pady=10)

# Fungsi untuk menampilkan Nama Ikan di jendela terpisah
def tampilkan_nama_ikan():
    nama_window = tk.Toplevel(root)
    nama_window.title("Nama Ikan")
    nama_window.configure(bg="#003366")

    nama_ikan = baca_file('nama_ikan.txt')
    jarak_tempuh = baca_file('jarak_tempuh.txt')
    nama_listbox = tk.Listbox(nama_window, width=50, height=10)
    nama_listbox.pack(pady=20)

    for i, (nama, jarak) in enumerate(zip(nama_ikan, jarak_tempuh), 1):
        nama_listbox.insert(tk.END, f"ID: {i} - Nama: {nama} - Jarak Tempuh: {jarak} meter")

# Fungsi untuk menampilkan Warna Ikan di jendela terpisah
def tampilkan_warna_ikan():
    warna_window = tk.Toplevel(root)
    warna_window.title("Warna Ikan")
    warna_window.configure(bg="#003366")

    warna_ikan = baca_file('warna_ikan.txt')
    warna_listbox = tk.Listbox(warna_window, width=50, height=10)
    warna_listbox.pack(pady=20)

    for i, warna in enumerate(warna_ikan, 1):
        warna_listbox.insert(tk.END, f"ID: {i} - Warna: {warna}")

# Fungsi untuk menampilkan Jenis Ikan di jendela terpisah
def tampilkan_jenis_ikan():
    jenis_window = tk.Toplevel(root)
    jenis_window.title("Jenis Ikan")
    jenis_window.configure(bg="#003366")

    jenis_ikan = baca_file('jenis_ikan.txt')
    jenis_listbox = tk.Listbox(jenis_window, width=50, height=10)
    jenis_listbox.pack(pady=20)

    for i, jenis in enumerate(jenis_ikan, 1):
        jenis_listbox.insert(tk.END, f"ID: {i} - Jenis: {jenis}")

# Fungsi untuk menambah data ikan
def halaman_tambah_data():
    tambah_window = tk.Toplevel(root)
    tambah_window.title("Tambah Data Ikan")
    tambah_window.configure(bg="#003366")

    label_nama = tk.Label(tambah_window, text="Nama Ikan:", bg="#003366", fg="white")
    label_nama.grid(row=0, column=0, padx=10, pady=5)
    entry_nama = tk.Entry(tambah_window)
    entry_nama.grid(row=0, column=1, padx=10, pady=5)

    label_warna = tk.Label(tambah_window, text="Warna Ikan:", bg="#003366", fg="white")
    label_warna.grid(row=1, column=0, padx=10, pady=5)
    dropdown_warna = ttk.Combobox(tambah_window)
    dropdown_warna['values'] = baca_file('warna_ikan.txt')
    dropdown_warna.grid(row=1, column=1, padx=10, pady=5)

    label_jenis = tk.Label(tambah_window, text="Jenis Ikan:", bg="#003366", fg="white")
    label_jenis.grid(row=2, column=0, padx=10, pady=5)
    dropdown_jenis = ttk.Combobox(tambah_window)
    dropdown_jenis['values'] = baca_file('jenis_ikan.txt')
    dropdown_jenis.grid(row=2, column=1, padx=10, pady=5)

    label_kecepatan = tk.Label(tambah_window, text="Kecepatan (m/s):", bg="#003366", fg="white")
    label_kecepatan.grid(row=3, column=0, padx=10, pady=5)
    entry_kecepatan = tk.Entry(tambah_window)
    entry_kecepatan.grid(row=3, column=1, padx=10, pady=5)

    label_waktu = tk.Label(tambah_window, text="Waktu (detik):", bg="#003366", fg="white")
    label_waktu.grid(row=4, column=0, padx=10, pady=5)
    entry_waktu = tk.Entry(tambah_window)
    entry_waktu.grid(row=4, column=1, padx=10, pady=5)

    def tambah_data():
        nama = entry_nama.get()
        warna = dropdown_warna.get()
        jenis = dropdown_jenis.get()
        try:
            kecepatan = float(entry_kecepatan.get())
            waktu = float(entry_waktu.get())
            if kecepatan < 0 or waktu < 0:
                messagebox.showwarning("Peringatan", "Kecepatan dan waktu harus bernilai positif!")
                return
            jarak = kecepatan * waktu
        except ValueError:
            messagebox.showwarning("Peringatan", "Masukkan nilai numerik yang valid!")
            return

        if nama and warna and jenis:
            nama_ikan = baca_file('nama_ikan.txt')
            warna_ikan = baca_file('warna_ikan.txt')
            jenis_ikan = baca_file('jenis_ikan.txt')
            jarak_tempuh = baca_file('jarak_tempuh.txt')

            nama_ikan.append(nama)
            warna_ikan.append(warna)
            jenis_ikan.append(jenis)
            jarak_tempuh.append(f"{jarak:.2f}")

            tulis_file('nama_ikan.txt', nama_ikan)
            tulis_file('warna_ikan.txt', warna_ikan)
            tulis_file('jenis_ikan.txt', jenis_ikan)
            tulis_file('jarak_tempuh.txt', jarak_tempuh)

            messagebox.showinfo("Sukses", f"Data ikan berhasil ditambah dengan ID: {len(nama_ikan)}")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")

    tambah_button = tk.Button(tambah_window, text="Tambah Data Ikan", command=tambah_data, font=("Arial", 12), width=20, bg="white", fg="black")
    tambah_button.grid(row=5, columnspan=2, pady=10)

# Fungsi untuk menutup aplikasi
def keluar_aplikasi():
    root.quit()

# Fungsi untuk halaman edit data
def halaman_edit_data():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Data Ikan")
    edit_window.configure(bg="#003366")

    label_id = tk.Label(edit_window, text="Masukkan ID Ikan:", bg="#003366", fg="white")
    label_id.grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(edit_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    label_nama = tk.Label(edit_window, text="Nama Baru:", bg="#003366", fg="white")
    label_nama.grid(row=1, column=0, padx=10, pady=5)
    entry_nama = tk.Entry(edit_window)
    entry_nama.grid(row=1, column=1, padx=10, pady=5)

    label_warna = tk.Label(edit_window, text="Warna Baru:", bg="#003366", fg="white")
    label_warna.grid(row=2, column=0, padx=10, pady=5)
    entry_warna = tk.Entry(edit_window)
    entry_warna.grid(row=2, column=1, padx=10, pady=5)

    label_jenis = tk.Label(edit_window, text="Jenis Baru:", bg="#003366", fg="white")
    label_jenis.grid(row=3, column=0, padx=10, pady=5)
    entry_jenis = tk.Entry(edit_window)
    entry_jenis.grid(row=3, column=1, padx=10, pady=5)

    label_kecepatan = tk.Label(edit_window, text="Kecepatan Baru (m/s):", bg="#003366", fg="white")
    label_kecepatan.grid(row=4, column=0, padx=10, pady=5)
    entry_kecepatan = tk.Entry(edit_window)
    entry_kecepatan.grid(row=4, column=1, padx=10, pady=5)

    def edit_data():
        try:
            id_ikan = int(entry_id.get())
            nama_baru = entry_nama.get()
            warna_baru = entry_warna.get()
            jenis_baru = entry_jenis.get()
            kecepatan_baru = float(entry_kecepatan.get())
            
            # Validasi ID
            nama_ikan = baca_file('nama_ikan.txt')
            if id_ikan < 1 or id_ikan > len(nama_ikan):
                messagebox.showwarning("Peringatan", "ID tidak valid!")
                return

            # Update data
            if nama_baru:
                nama_ikan[id_ikan - 1] = nama_baru
            if warna_baru:
                warna_ikan = baca_file('warna_ikan.txt')
                warna_ikan[id_ikan - 1] = warna_baru
                tulis_file('warna_ikan.txt', warna_ikan)
            if jenis_baru:
                jenis_ikan = baca_file('jenis_ikan.txt')
                jenis_ikan[id_ikan - 1] = jenis_baru
                tulis_file('jenis_ikan.txt', jenis_ikan)
            if kecepatan_baru >= 0:
                jarak_tempuh = baca_file('jarak_tempuh.txt')
                waktu = 1  # Ganti dengan waktu yang sesuai jika perlu
                jarak_tempuh[id_ikan - 1] = f"{kecepatan_baru * waktu:.2f}"
                tulis_file('jarak_tempuh.txt', jarak_tempuh)

            tulis_file('nama_ikan.txt', nama_ikan)
            messagebox.showinfo("Sukses", "Data ikan berhasil diperbarui!")
        except ValueError:
            messagebox.showwarning("Peringatan", "Masukkan ID dan kecepatan yang valid!")

    edit_button = tk.Button(edit_window, text="Edit Data Ikan", command=edit_data, font=("Arial", 12), width=20, bg="white", fg="black")
    edit_button.grid(row=5, columnspan=2, pady=10)

# Fungsi untuk halaman hapus data
def halaman_hapus_data():
    hapus_window = tk.Toplevel(root)
    hapus_window.title("Hapus Data Ikan")
    hapus_window.configure(bg="#003366")

    label_id = tk.Label(hapus_window, text="Masukkan ID Ikan untuk Dihapus:", bg="#003366", fg="white")
    label_id.pack(pady=10)
    entry_id = tk.Entry(hapus_window)
    entry_id.pack(pady=5)

    def hapus_data():
        try:
            id_ikan = int(entry_id.get())
            nama_ikan = baca_file('nama_ikan.txt')

            # Validasi ID
            if id_ikan < 1 or id_ikan > len(nama_ikan):
                messagebox.showwarning("Peringatan", "ID tidak valid!")
                return

            confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus data ikan dengan ID: {id_ikan}?")
            if confirm:
                # Hapus data dari semua file
                del nama_ikan[id_ikan - 1]
                warna_ikan = baca_file('warna_ikan.txt')
                del warna_ikan[id_ikan - 1]
                jenis_ikan = baca_file('jenis_ikan.txt')
                del jenis_ikan[id_ikan - 1]
                jarak_tempuh = baca_file('jarak_tempuh.txt')
                del jarak_tempuh[id_ikan - 1]

                # Tulis kembali data ke file
                tulis_file('nama_ikan.txt', nama_ikan)
                tulis_file('warna_ikan.txt', warna_ikan)
                tulis_file('jenis_ikan.txt', jenis_ikan)
                tulis_file('jarak_tempuh.txt', jarak_tempuh)

                messagebox.showinfo("Sukses", "Data ikan berhasil dihapus!")
                hapus_window.destroy()
        except ValueError:
            messagebox.showwarning("Peringatan", "Masukkan ID yang valid!")

    hapus_button = tk.Button(hapus_window, text="Hapus Data Ikan", command=hapus_data, font=("Arial", 12), width=20, bg="white", fg="black")
    hapus_button.pack(pady=10)

# Inisialisasi window utama
root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.configure(bg="#003366")

# Tombol untuk menambah data
tambah_button = tk.Button(root, text="Tambah Data Ikan", command=halaman_tambah_data, font=("Arial", 12), width=20, bg="white", fg="black")
tambah_button.pack(pady=10)

# Tombol untuk menampilkan data ikan
tampilkan_button = tk.Button(root, text="Tampilkan Data Ikan", command=tampilkan_data_ikan, font=("Arial", 12), width=20, bg="white", fg="black")
tampilkan_button.pack(pady=10)

# Tombol untuk mengedit data ikan
edit_button = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, font=("Arial", 12), width=20, bg="white", fg="black")
edit_button.pack(pady=10)

# Tombol untuk menghapus data ikan
hapus_button = tk.Button(root, text="Hapus Data Ikan", command=halaman_hapus_data, font=("Arial", 12), width=20, bg="white", fg="black")
hapus_button.pack(pady=10)

# Tombol untuk keluar aplikasi
keluar_button = tk.Button(root, text="Keluar", command=keluar_aplikasi, font=("Arial", 12), width=20, bg="white", fg="black")
keluar_button.pack(pady=10)

# Buat file jika belum ada
for file in ['nama_ikan.txt', 'warna_ikan.txt', 'jenis_ikan.txt', 'jarak_tempuh.txt']:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write('')  # Create empty files if they don't exist

# Jalankan aplikasi
root.mainloop()
