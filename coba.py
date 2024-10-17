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

# Fungsi untuk menampilkan halaman dengan data lengkap (ID, Nama, Warna, Jenis)
def tampilkan_data_ikan():
    tampil_window = tk.Toplevel(root)
    tampil_window.title("Tampilkan Data Ikan")
    tampil_window.configure(bg="#003366")
    
    ikan_listbox = tk.Listbox(tampil_window, width=80, height=10)
    ikan_listbox.pack(pady=20)

    nama_ikan = baca_file('nama_ikan.txt')
    warna_ikan = baca_file('nama_warna.txt')
    jenis_ikan = baca_file('nama_jenis.txt')

    # Tampilkan data secara lengkap
    for i in range(len(nama_ikan)):
        ikan_listbox.insert(tk.END, f"ID: {i + 1}, Nama: {nama_ikan[i]}, Warna: {warna_ikan[i]}, Jenis: {jenis_ikan[i]}")

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

                messagebox.showinfo("Sukses", "Data ikan berhasil diperbarui!")
            else:
                messagebox.showwarning("Peringatan", "ID tidak valid!")
        except ValueError:
            messagebox.showwarning("Peringatan", "Masukkan ID yang valid!")

    simpan_button = tk.Button(edit_window, text="Simpan Perubahan", command=simpan_perubahan, font=("Arial", 12), width=20, bg="white", fg="black")
    simpan_button.grid(row=4, columnspan=2, pady=10)

# Halaman untuk menghitung jarak tempuh ikan
def tulis_jarak_tempuh(file_path, kecepatan, waktu, jarak):
    with open(file_path, 'a') as f:  # 'a' mode untuk append data baru
        f.write(f"Kecepatan: {kecepatan} m/s, Waktu: {waktu} detik, Jarak: {jarak:.2f} meter\n")

def halaman_hitung_jarak():
    jarak_window = tk.Toplevel(root)
    jarak_window.title("Hitung Jarak Tempuh Ikan")
    jarak_window.configure(bg="#003366")

    label_kecepatan = tk.Label(jarak_window, text="Kecepatan Ikan (m/s):", bg="#003366", fg="white")
    label_kecepatan.grid(row=0, column=0, padx=10, pady=5)
    entry_kecepatan = tk.Entry(jarak_window)
    entry_kecepatan.grid(row=0, column=1, padx=10, pady=5)

    label_waktu = tk.Label(jarak_window, text="Waktu Berenang (detik):", bg="#003366", fg="white")
    label_waktu.grid(row=1, column=0, padx=10, pady=5)
    entry_waktu = tk.Entry(jarak_window)
    entry_waktu.grid(row=1, column=1, padx=10, pady=5)

    def hitung_jarak():
        try:
            kecepatan = float(entry_kecepatan.get())
            waktu = float(entry_waktu.get())
            if kecepatan >= 0 and waktu >= 0:
                jarak = kecepatan * waktu
                messagebox.showinfo("Hasil", f"Jarak tempuh ikan: {jarak:.2f} meter")
                
                # Simpan hasil ke file
                tulis_jarak_tempuh('data_jarak_tempuh.txt', kecepatan, waktu, jarak)
            else:
                messagebox.showwarning("Peringatan", "Kecepatan dan waktu harus bernilai positif!")
        except ValueError:
            messagebox.showwarning("Peringatan", "Masukkan nilai numerik yang valid!")

    hitung_button = tk.Button(jarak_window, text="Hitung Jarak", command=hitung_jarak, font=("Arial", 12), width=20, bg="white", fg="black")
    hitung_button.grid(row=2, columnspan=2, pady=10)

# Fungsi untuk menutup aplikasi
def keluar_aplikasi():
    root.quit()

# Setup jendela utama
root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.geometry("400x500")
root.configure(bg="#003366")

headline_label = tk.Label(root, text="Data Ikan", bg="#003366", fg="white", font=("Arial", 20))
headline_label.pack(pady=20)

# Tombol utama
tampil_button = tk.Button(root, text="Tampilkan Data Ikan", command=tampilkan_data_ikan, font=("Arial", 12), width=20, bg="white", fg="black")
tampil_button.pack(pady=10)

tambah_button = tk.Button(root, text="Tambah Data Ikan", command=halaman_tambah_data, font=("Arial", 12), width=20, bg="white", fg="black")
tambah_button.pack(pady=10)

edit_button = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, font=("Arial", 12), width=20, bg="white", fg="black")
edit_button.pack(pady=10)

hitung_button = tk.Button(root, text="Hitung Jarak Tempuh Ikan", command=halaman_hitung_jarak, font=("Arial", 12), width=20, bg="white", fg="black")
hitung_button.pack(pady=10)

# Tombol Keluar
keluar_button = tk.Button(root, text="Keluar", command=keluar_aplikasi, font=("Arial", 12), width=20, bg="red", fg="white")
keluar_button.pack(pady=20)

root.mainloop()
