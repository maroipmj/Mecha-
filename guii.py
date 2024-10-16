import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk membaca file data
def baca_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Fungsi untuk menulis ke file data
def tulis_file(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(item + '\n')

# Fungsi untuk menampilkan header
def tampilkan_header(window):
    header_label = tk.Label(window, text="Data Ikan", font=("Arial", 16), bg="#003366", fg="white")
    header_label.pack(pady=10)

# Fungsi untuk menampilkan halaman dengan data ikan
def tampilkan_data_ikan():
    tampil_window = tk.Toplevel(root)
    tampil_window.title("Tampilkan Data Ikan")
    tampil_window.configure(bg="#003366")

    tampilkan_header(tampil_window)

    label_pilihan = tk.Label(tampil_window, text="Pilih Data yang ingin dilihat:", bg="#003366", fg="white")
    label_pilihan.pack(pady=5)

    pilihan = ttk.Combobox(tampil_window)
    pilihan['values'] = ["Nama Ikan", "Warna Ikan", "Jenis Ikan"]
    pilihan.pack(pady=5)

    ikan_listbox = tk.Listbox(tampil_window, width=50, height=10)
    ikan_listbox.pack(pady=20)

    def tampil_data():
        ikan_listbox.delete(0, tk.END)  # Kosongkan listbox sebelum menampilkan data
        if pilihan.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Nama: {item}")
        elif pilihan.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Warna: {item}")
        elif pilihan.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Jenis: {item}")

    tombol_tampil = tk.Button(tampil_window, text="Tampilkan Data", command=tampil_data, font=("Arial", 12), bg="white", fg="black")
    tombol_tampil.pack(pady=10)

# Halaman untuk menambah data ikan
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

# Halaman untuk edit data ikan
def halaman_edit_data():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Data Ikan")
    edit_window.configure(bg="#003366")

    label_edit = tk.Label(edit_window, text="Pilih Ikan:", bg="#003366", fg="white")
    label_edit.grid(row=0, column=0, padx=10, pady=5)
    dropdown_edit = ttk.Combobox(edit_window)
    dropdown_edit['values'] = baca_file('nama_ikan.txt')
    dropdown_edit.grid(row=0, column=1, padx=10, pady=5)

    label_bagian = tk.Label(edit_window, text="Bagian yang ingin diubah:", bg="#003366", fg="white")
    label_bagian.grid(row=1, column=0, padx=10, pady=5)
    dropdown_bagian = ttk.Combobox(edit_window)
    dropdown_bagian['values'] = ["Nama", "Warna", "Jenis"]
    dropdown_bagian.grid(row=1, column=1, padx=10, pady=5)

    label_edit_value = tk.Label(edit_window, text="Data Baru:", bg="#003366", fg="white")
    label_edit_value.grid(row=2, column=0, padx=10, pady=5)
    entry_edit = tk.Entry(edit_window)
    entry_edit.grid(row=2, column=1, padx=10, pady=5)

    def edit_data():
        selected_id = dropdown_edit.current()
        bagian = dropdown_bagian.current()
        data_baru = entry_edit.get()

        if selected_id >= 0 and data_baru:
            nama_ikan = baca_file('nama_ikan.txt')
            warna_ikan = baca_file('nama_warna.txt')
            jenis_ikan = baca_file('nama_jenis.txt')

            if bagian == 0:  # Nama
                nama_ikan[selected_id] = data_baru
                tulis_file('nama_ikan.txt', nama_ikan)
            elif bagian == 1:  # Warna
                warna_ikan[selected_id] = data_baru
                tulis_file('nama_warna.txt', warna_ikan)
            elif bagian == 2:  # Jenis
                jenis_ikan[selected_id] = data_baru
                tulis_file('nama_jenis.txt', jenis_ikan)

            messagebox.showinfo("Sukses", "Data ikan berhasil diedit!")
        else:
            messagebox.showwarning("Peringatan", "Pilih ikan dan isi data yang ingin diedit!")

    edit_button = tk.Button(edit_window, text="Edit Data Ikan", command=edit_data, font=("Arial", 12), width=20, bg="white", fg="black")
    edit_button.grid(row=3, columnspan=2, pady=10)

# Halaman untuk hapus data ikan
def halaman_hapus_data():
    hapus_window = tk.Toplevel(root)
    hapus_window.title("Hapus Data Ikan")
    hapus_window.configure(bg="#003366")

    label_hapus = tk.Label(hapus_window, text="Pilih Ikan untuk Dihapus:", bg="#003366", fg="white")
    label_hapus.grid(row=0, column=0, padx=10, pady=5)
    dropdown_hapus = ttk.Combobox(hapus_window)
    dropdown_hapus['values'] = baca_file('nama_ikan.txt')
    dropdown_hapus.grid(row=0, column=1, padx=10, pady=5)

    def hapus_data():
        selected_id = dropdown_hapus.current()

        if selected_id >= 0:
            nama_ikan = baca_file('nama_ikan.txt')
            warna_ikan = baca_file('nama_warna.txt')
            jenis_ikan = baca_file('nama_jenis.txt')

            del nama_ikan[selected_id]
            del warna_ikan[selected_id]
            del jenis_ikan[selected_id]

            tulis_file('nama_ikan.txt', nama_ikan)
            tulis_file('nama_warna.txt', warna_ikan)
            tulis_file('nama_jenis.txt', jenis_ikan)

            messagebox.showinfo("Sukses", "Data ikan berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih ikan yang ingin dihapus!")

    hapus_button = tk.Button(hapus_window, text="Hapus Data Ikan", command=hapus_data, font=("Arial", 12), width=20, bg="white", fg="black")
    hapus_button.grid(row=1, columnspan=2, pady=10)

# Fungsi untuk menampilkan data jarak berenang
def tampilkan_data_jarak():
    tampil_window = tk.Toplevel(root)
    tampil_window.title("Tampilkan Jarak Berenang Ikan")
    tampil_window.configure(bg="#003366")

    tampilkan_header(tampil_window)

    label_jarak = tk.Label(tampil_window, text="Jarak Berenang Ikan (meter):", bg="#003366", fg="white")
    label_jarak.pack(pady=5)

    jarak_listbox = tk.Listbox(tampil_window, width=50, height=10)
    jarak_listbox.pack(pady=20)

    data_jarak = baca_file('jarak_berenang.txt')
    for i, jarak in enumerate(data_jarak):
        jarak_listbox.insert(tk.END, f"ID: {i + 1} | Jarak: {jarak} meter")

# Halaman untuk tambah jarak berenang
def halaman_tambah_jarak():
    tambah_window = tk.Toplevel(root)
    tambah_window.title("Tambah Jarak Berenang Ikan")
    tambah_window.configure(bg="#003366")

    label_jarak = tk.Label(tambah_window, text="Jarak Berenang (meter):", bg="#003366", fg="white")
    label_jarak.grid(row=0, column=0, padx=10, pady=5)
    entry_jarak = tk.Entry(tambah_window)
    entry_jarak.grid(row=0, column=1, padx=10, pady=5)

    def tambah_jarak():
        jarak = entry_jarak.get()

        if jarak.isdigit():
            jarak_berenang = baca_file('jarak_berenang.txt')
            jarak_berenang.append(jarak)

            tulis_file('jarak_berenang.txt', jarak_berenang)

            messagebox.showinfo("Sukses", "Jarak berenang berhasil ditambah!")
        else:
            messagebox.showwarning("Peringatan", "Jarak harus berupa angka!")

    tambah_button = tk.Button(tambah_window, text="Tambah Jarak Berenang", command=tambah_jarak, font=("Arial", 12), width=20, bg="white", fg="black")
    tambah_button.grid(row=1, columnspan=2, pady=10)

# Halaman untuk edit jarak berenang
def halaman_edit_jarak():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Jarak Berenang Ikan")
    edit_window.configure(bg="#003366")

    label_edit = tk.Label(edit_window, text="Pilih Jarak untuk Diedit:", bg="#003366", fg="white")
    label_edit.grid(row=0, column=0, padx=10, pady=5)
    dropdown_edit = ttk.Combobox(edit_window)
    dropdown_edit['values'] = baca_file('jarak_berenang.txt')
    dropdown_edit.grid(row=0, column=1, padx=10, pady=5)

    label_edit_value = tk.Label(edit_window, text="Jarak Baru (meter):", bg="#003366", fg="white")
    label_edit_value.grid(row=1, column=0, padx=10, pady=5)
    entry_edit = tk.Entry(edit_window)
    entry_edit.grid(row=1, column=1, padx=10, pady=5)

    def edit_jarak():
        selected_id = dropdown_edit.current()
        jarak_baru = entry_edit.get()

        if selected_id >= 0 and jarak_baru.isdigit():
            jarak_berenang = baca_file('jarak_berenang.txt')
            jarak_berenang[selected_id] = jarak_baru

            tulis_file('jarak_berenang.txt', jarak_berenang)

            messagebox.showinfo("Sukses", "Jarak berenang berhasil diedit!")
        else:
            messagebox.showwarning("Peringatan", "Pilih jarak dan isi data yang ingin diedit!")

    edit_button = tk.Button(edit_window, text="Edit Jarak Berenang", command=edit_jarak, font=("Arial", 12), width=20, bg="white", fg="black")
    edit_button.grid(row=2, columnspan=2, pady=10)

# Halaman untuk hapus jarak berenang
def halaman_hapus_jarak():
    hapus_window = tk.Toplevel(root)
    hapus_window.title("Hapus Jarak Berenang Ikan")
    hapus_window.configure(bg="#003366")

    label_hapus = tk.Label(hapus_window, text="Pilih Jarak untuk Dihapus:", bg="#003366", fg="white")
    label_hapus.grid(row=0, column=0, padx=10, pady=5)
    dropdown_hapus = ttk.Combobox(hapus_window)
    dropdown_hapus['values'] = baca_file('jarak_berenang.txt')
    dropdown_hapus.grid(row=0, column=1, padx=10, pady=5)

    def hapus_jarak():
        selected_id = dropdown_hapus.current()

        if selected_id >= 0:
            jarak_berenang = baca_file('jarak_berenang.txt')

            del jarak_berenang[selected_id]

            tulis_file('jarak_berenang.txt', jarak_berenang)

            messagebox.showinfo("Sukses", "Jarak berenang berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih jarak yang ingin dihapus!")

    hapus_button = tk.Button(hapus_window, text="Hapus Jarak Berenang", command=hapus_jarak, font=("Arial", 12), width=20, bg="white", fg="black")
    hapus_button.grid(row=1, columnspan=2, pady=10)

# Fungsi utama
root = tk.Tk()
root.title("Data Ikan")
root.configure(bg="#003366")

# Tombol untuk membuka setiap halaman
button_tampil = tk.Button(root, text="Tampilkan Data Ikan", command=tampilkan_data_ikan, font=("Arial", 12), width=30, bg="white", fg="black")
button_tampil.pack(pady=10)

button_tambah = tk.Button(root, text="Tambah Data Ikan", command=halaman_tambah_data, font=("Arial", 12), width=30, bg="white", fg="black")
button_tambah.pack(pady=10)

button_edit = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, font=("Arial", 12), width=30, bg="white", fg="black")
button_edit.pack(pady=10)

button_hapus = tk.Button(root, text="Hapus Data Ikan", command=halaman_hapus_data, font=("Arial", 12), width=30, bg="white", fg="black")
button_hapus.pack(pady=10)

button_tampil_jarak = tk.Button(root, text="Tampilkan Jarak Berenang", command=tampilkan_data_jarak, font=("Arial", 12), width=30, bg="white", fg="black")
button_tampil_jarak.pack(pady=10)

button_tambah_jarak = tk.Button(root, text="Tambah Jarak Berenang", command=halaman_tambah_jarak, font=("Arial", 12), width=30, bg="white", fg="black")
button_tambah_jarak.pack(pady=10)

button_edit_jarak = tk.Button(root, text="Edit Jarak Berenang", command=halaman_edit_jarak, font=("Arial", 12), width=30, bg="white", fg="black")
button_edit_jarak.pack(pady=10)

button_hapus_jarak = tk.Button(root, text="Hapus Jarak Berenang", command=halaman_hapus_jarak, font=("Arial", 12), width=30, bg="white", fg="black")
button_hapus_jarak.pack(pady=10)

root.mainloop()
