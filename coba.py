import tkinter as tk
from tkinter import ttk, messagebox

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

# Fungsi untuk menampilkan halaman dengan data sesuai pilihan dari dropdown (Nama, Warna, Jenis)
def tampilkan_data_ikan():
    # Membuat jendela baru untuk menampilkan data ikan
    tampil_window = tk.Toplevel(root)
    tampil_window.title("Tampilkan Data Ikan")
    tampil_window.configure(bg="#003366")
    
    # Label untuk pilihan filter data
    label_pilih = tk.Label(tampil_window, text="Pilih Data yang Ingin Dilihat:", bg="#003366", fg="white")
    label_pilih.pack(pady=10)
    
    # Dropdown untuk memilih data yang ingin ditampilkan
    dropdown_pilihan = ttk.Combobox(tampil_window, state="readonly")
    dropdown_pilihan['values'] = ["Semua Data", "Nama Ikan", "Warna Ikan", "Jenis Ikan"]
    dropdown_pilihan.current(0)  # Set pilihan default ke "Semua Data"
    dropdown_pilihan.pack(pady=5)
    
    # Listbox untuk menampilkan hasil data ikan
    ikan_listbox = tk.Listbox(tampil_window, width=80, height=10)
    ikan_listbox.pack(pady=20)

    # Fungsi untuk menampilkan data sesuai pilihan dropdown
    def tampilkan_berdasarkan_pilihan():
        pilihan = dropdown_pilihan.get()

        # Kosongkan listbox sebelum menampilkan data baru
        ikan_listbox.delete(0, tk.END)

        # Membaca file data ikan
        nama_ikan = baca_file('nama_ikan.txt')
        warna_ikan = baca_file('nama_warna.txt')
        jenis_ikan = baca_file('nama_jenis.txt')

        # Tampilkan data sesuai pilihan pengguna
        if pilihan == "Semua Data":
            for i in range(len(nama_ikan)):
                ikan_listbox.insert(tk.END, f"ID: {i + 1}, Nama: {nama_ikan[i]}, Warna: {warna_ikan[i]}, Jenis: {jenis_ikan[i]}")
        elif pilihan == "Nama Ikan":
            for i in range(len(nama_ikan)):
                ikan_listbox.insert(tk.END, f"ID: {i + 1}, Nama: {nama_ikan[i]}")
        elif pilihan == "Warna Ikan":
            for i in range(len(warna_ikan)):
                ikan_listbox.insert(tk.END, f"ID: {i + 1}, Warna: {warna_ikan[i]}")
        elif pilihan == "Jenis Ikan":
            for i in range(len(jenis_ikan)):
                ikan_listbox.insert(tk.END, f"ID: {i + 1}, Jenis: {jenis_ikan[i]}")

    # Tombol untuk memulai penampilan data sesuai pilihan dropdown
    tampilkan_button = tk.Button(tampil_window, text="Tampilkan Data", command=tampilkan_berdasarkan_pilihan, font=("Arial", 12), width=20, bg="white", fg="black")
    tampilkan_button.pack(pady=10)

# Halaman untuk menambah data ikan dengan auto increment
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
    dropdown_warna['values'] = baca_file('nama_warna.txt')
    dropdown_warna.grid(row=1, column=1, padx=10, pady=5)

    label_jenis = tk.Label(tambah_window, text="Jenis Ikan:", bg="#003366", fg="white")
    label_jenis.grid(row=2, column=0, padx=10, pady=5)

    dropdown_jenis = ttk.Combobox(tambah_window)
    dropdown_jenis['values'] = baca_file('nama_jenis.txt')
    dropdown_jenis.grid(row=2, column=1, padx=10, pady=5)

    def tambah_data():
        nama = entry_nama.get()
        warna = dropdown_warna.get()
        jenis = dropdown_jenis.get()

        if nama and warna and jenis:
            nama_ikan = baca_file('nama_ikan.txt')
            warna_ikan = baca_file('nama_warna.txt')
            jenis_ikan = baca_file('nama_jenis.txt')

            nama_ikan.append(nama)
            warna_ikan.append(warna)
            jenis_ikan.append(jenis)

            tulis_file('nama_ikan.txt', nama_ikan)
            tulis_file('nama_warna.txt', warna_ikan)
            tulis_file('nama_jenis.txt', jenis_ikan)

            messagebox.showinfo("Sukses", f"Data ikan berhasil ditambah dengan ID: {len(nama_ikan)}")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")

    tambah_button = tk.Button(tambah_window, text="Tambah Data Ikan", command=tambah_data, font=("Arial", 12), width=20, bg="white", fg="black")
    tambah_button.grid(row=3, columnspan=2, pady=10)

# Fungsi untuk mengedit data ikan
def halaman_edit_data():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Data Ikan")
    edit_window.configure(bg="#003366")

    label_id = tk.Label(edit_window, text="Masukkan ID Ikan yang akan diedit:", bg="#003366", fg="white")
    label_id.grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(edit_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    label_nama = tk.Label(edit_window, text="Nama Baru:", bg="#003366", fg="white")
    label_nama.grid(row=1, column=0, padx=10, pady=5)
    entry_nama = tk.Entry(edit_window)
    entry_nama.grid(row=1, column=1, padx=10, pady=5)

    label_warna = tk.Label(edit_window, text="Warna Baru:", bg="#003366", fg="white")
    label_warna.grid(row=2, column=0, padx=10, pady=5)

    dropdown_warna = ttk.Combobox(edit_window)
    dropdown_warna['values'] = baca_file('nama_warna.txt')
    dropdown_warna.grid(row=2, column=1, padx=10, pady=5)

    label_jenis = tk.Label(edit_window, text="Jenis Baru:", bg="#003366", fg="white")
    label_jenis.grid(row=3, column=0, padx=10, pady=5)

    dropdown_jenis = ttk.Combobox(edit_window)
    dropdown_jenis['values'] = baca_file('nama_jenis.txt')
    dropdown_jenis.grid(row=3, column=1, padx=10, pady=5)

    def simpan_perubahan():
        try:
            id_ikan = int(entry_id.get()) - 1
            nama_baru = entry_nama.get()
            warna_baru = dropdown_warna.get()
            jenis_baru = dropdown_jenis.get()

            nama_ikan = baca_file('nama_ikan.txt')
            warna_ikan = baca_file('nama_warna.txt')
            jenis_ikan = baca_file('nama_jenis.txt')

            if 0 <= id_ikan < len(nama_ikan):
                # Periksa apakah input kosong, jika kosong gunakan data lama
                if nama_baru:
                    nama_ikan[id_ikan] = nama_baru
                if warna_baru:
                    warna_ikan[id_ikan] = warna_baru
                if jenis_baru:
                    jenis_ikan[id_ikan] = jenis_baru

                # Simpan perubahan ke file
                tulis_file('nama_ikan.txt', nama_ikan)
                tulis_file('nama_warna.txt', warna_ikan)
                tulis_file('nama_jenis.txt', jenis_ikan)

                messagebox.showinfo("Sukses", f"Data ikan ID {id_ikan + 1} berhasil diperbarui!")
            else:
                messagebox.showerror("Error", "ID Ikan tidak valid!")
        except ValueError:
            messagebox.showerror("Error", "Masukkan ID yang valid!")

    simpan_button = tk.Button(edit_window, text="Simpan Perubahan", command=simpan_perubahan, font=("Arial", 12), width=20, bg="white", fg="black")
    simpan_button.grid(row=4, columnspan=2, pady=10)

# Halaman Utama
root = tk.Tk()
root.title("Sistem Manajemen Data Ikan")
root.geometry("500x400")
root.configure(bg="#003366")

label_title = tk.Label(root, text="Sistem Manajemen Data Ikan", bg="#003366", fg="white", font=("Arial", 16))
label_title.pack(pady=20)

tambah_button = tk.Button(root, text="Tambah Data Ikan", command=halaman_tambah_data, font=("Arial", 12), width=30, bg="white", fg="black")
tambah_button.pack(pady=10)

tampil_button = tk.Button(root, text="Tampilkan Data Ikan", command=tampilkan_data_ikan, font=("Arial", 12), width=30, bg="white", fg="black")
tampil_button.pack(pady=10)

edit_button = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, font=("Arial", 12), width=30, bg="white", fg="black")
edit_button.pack(pady=10)

root.mainloop()
