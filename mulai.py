import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Fungsi untuk membaca file data
def baca_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        return []

# Fungsi untuk menulis ke file data
def tulis_file(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(','.join(item) + '\n')

# Fungsi untuk menulis history ke file
def tulis_history(aksi):
    with open('history.txt', 'a') as f:
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{waktu_sekarang}] {aksi}\n")

# Fungsi untuk menampilkan header
def tampilkan_header(window, title):
    header_label = tk.Label(window, text=title, font=("Arial", 16), bg="#003366", fg="white")
    header_label.pack(pady=10)

# Fungsi untuk keluar dari window
def keluar(window):
    window.destroy()

# Halaman untuk menampilkan data ikan
def halaman_tampilkan_data_ikan():
    tampil_window = tk.Toplevel(root)
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
                ikan_listbox.insert(tk.END, f"Nama: {item[0]}")
            tulis_history("Menampilkan data Nama Ikan")
        elif pilihan.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"Jenis: {item[0]}")
            tulis_history("Menampilkan data Jenis Ikan")
        elif pilihan.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"Warna: {item[0]}")
            tulis_history("Menampilkan data Warna Ikan")
        elif pilihan.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"Waktu: {item[0]} jam, Jarak: {item[0]} km")
            tulis_history("Menampilkan data Jarak Tempuh")

    tombol_tampil = tk.Button(tampil_window, text="Tampilkan Data", command=tampil_data, bg="white", fg="black")
    tombol_tampil.pack(pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(tampil_window, text="Keluar", command=lambda: keluar(tampil_window), bg="red", fg="white")
    tombol_keluar.pack(pady=10)

# Halaman untuk tambah data ikan
def halaman_tambah_data():
    tambah_window = tk.Toplevel(root)
    tambah_window.title("Tambah Data Ikan")
    tambah_window.configure(bg="#003366")

    label_tambah = tk.Label(tambah_window, text="Pilih Data Ikan yang ingin ditambah:", bg="#003366", fg="white")
    label_tambah.grid(row=0, column=0, padx=10, pady=5)

    dropdown_tambah = ttk.Combobox(tambah_window)
    dropdown_tambah['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_tambah.grid(row=0, column=1, padx=10, pady=5)

    # Label dan Entry untuk data baru (dinamis)
    label_data_baru = tk.Label(tambah_window, text="Data Baru:", bg="#003366", fg="white")
    label_data_baru.grid(row=1, column=0, padx=10, pady=5)

    # Entry untuk input data (dinamis)
    entry_data_baru = tk.Entry(tambah_window)
    entry_data_baru.grid(row=1, column=1, padx=10, pady=5)

    # Tambahan khusus untuk jarak tempuh: waktu, jarak
    label_waktu = tk.Label(tambah_window, text="Waktu (jam):", bg="#003366", fg="white")
    entry_waktu = tk.Entry(tambah_window)
    label_jarak = tk.Label(tambah_window, text="Jarak (km):", bg="#003366", fg="white")
    entry_jarak = tk.Entry(tambah_window)

    def update_fields(event):
        # Mengatur visibilitas field berdasarkan jenis data yang dipilih
        if dropdown_tambah.get() == "Jarak Tempuh":
            label_data_baru.grid_forget()
            entry_data_baru.grid_forget()
            
            # Tampilkan input khusus untuk jarak tempuh
            label_waktu.grid(row=1, column=0, padx=10, pady=5)
            entry_waktu.grid(row=1, column=1, padx=10, pady=5)
            label_jarak.grid(row=2, column=0, padx=10, pady=5)
            entry_jarak.grid(row=2, column=1, padx=10, pady=5)
        else:
            label_waktu.grid_forget()
            entry_waktu.grid_forget()
            label_jarak.grid_forget()
            entry_jarak.grid_forget()
            
            # Tampilkan input biasa
            label_data_baru.grid(row=1, column=0, padx=10, pady=5)
            entry_data_baru.grid(row=1, column=1, padx=10, pady=5)

    dropdown_tambah.bind("<<ComboboxSelected>>", update_fields)

    def tambah_data():
        # Tambah data untuk jarak tempuh secara khusus
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
                messagebox.showwarning("Peringatan", "Isi semua data waktu dan jarak!")
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

                messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
            else:
                messagebox.showwarning("Peringatan", "Isi data yang ingin ditambah!")

    tambah_button = tk.Button(tambah_window, text="Tambah Data Ikan", command=tambah_data, bg="white", fg="black")
    tambah_button.grid(row=4, columnspan=2, pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(tambah_window, text="Keluar", command=lambda: keluar(tambah_window), bg="red", fg="white")
    tombol_keluar.grid(row=5, columnspan=2, pady=10)

def halaman_edit_data():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Data Ikan")
    edit_window.configure(bg="#003366")

    label_edit = tk.Label(edit_window, text="Pilih Data Ikan yang ingin diedit:", bg="#003366", fg="white")
    label_edit.grid(row=0, column=0, padx=10, pady=5)

    dropdown_edit = ttk.Combobox(edit_window)
    dropdown_edit['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_edit.grid(row=0, column=1, padx=10, pady=5)

    # Label dan Entry untuk data yang ingin diedit (dinamis)
    label_data_edit = tk.Label(edit_window, text="Data yang ingin diedit:", bg="#003366", fg="white")
    label_data_edit.grid(row=1, column=0, padx=10, pady=5)

    entry_data_edit = tk.Entry(edit_window)
    entry_data_edit.grid(row=1, column=1, padx=10, pady=5)

    # Label dan Entry untuk data baru
    label_data_baru = tk.Label(edit_window, text="Data Baru:", bg="#003366", fg="white")
    label_data_baru.grid(row=2, column=0, padx=10, pady=5)

    entry_data_baru = tk.Entry(edit_window)
    entry_data_baru.grid(row=2, column=1, padx=10, pady=5)

    # Listbox untuk menampilkan data yang ada
    data_listbox = tk.Listbox(edit_window, width=50, height=10)
    data_listbox.grid(row=3, columnspan=2, padx=10, pady=10)

    def update_data_listbox():
        data_listbox.delete(0, tk.END)
        data = []
        if dropdown_edit.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
        elif dropdown_edit.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
        elif dropdown_edit.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
        elif dropdown_edit.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')

        for item in data:
            data_listbox.insert(tk.END, item[0])

    dropdown_edit.bind("<<ComboboxSelected>>", lambda e: update_data_listbox())

    def select_data(event):
        # Menampilkan data yang dipilih di entry
        selected_index = data_listbox.curselection()
        if selected_index:
            data = data_listbox.get(selected_index)
            entry_data_edit.delete(0, tk.END)
            entry_data_edit.insert(0, data)

    data_listbox.bind("<<ListboxSelect>>", select_data)

    def edit_data():
        data_edit = entry_data_edit.get()
        data_baru = entry_data_baru.get()
        if not data_edit or not data_baru:
            messagebox.showwarning("Peringatan", "Isi data yang ingin diedit dan data baru!")
            return
        
        if dropdown_edit.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
            updated_data = [[data_baru] if item[0] == data_edit else item for item in data]
            tulis_file('nama_ikan.txt', updated_data)
            tulis_history(f"Mengedit Nama Ikan: {data_edit} menjadi {data_baru}")
        elif dropdown_edit.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            updated_data = [[data_baru] if item[0] == data_edit else item for item in data]
            tulis_file('nama_jenis.txt', updated_data)
            tulis_history(f"Mengedit Jenis Ikan: {data_edit} menjadi {data_baru}")
        elif dropdown_edit.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            updated_data = [[data_baru] if item[0] == data_edit else item for item in data]
            tulis_file('nama_warna.txt', updated_data)
            tulis_history(f"Mengedit Warna Ikan: {data_edit} menjadi {data_baru}")
        elif dropdown_edit.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')
            updated_data = [[data_baru] if item[0] == data_edit else item for item in data]
            tulis_file('jarak_tempuh.txt', updated_data)
            tulis_history(f"Mengedit Jarak Tempuh: {data_edit} menjadi {data_baru}")

        messagebox.showinfo("Sukses", "Data berhasil diedit!")
        entry_data_edit.delete(0, tk.END)
        entry_data_baru.delete(0, tk.END)
        update_data_listbox()

    edit_button = tk.Button(edit_window, text="Edit Data Ikan", command=edit_data, bg="white", fg="black")
    edit_button.grid(row=4, columnspan=2, pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(edit_window, text="Keluar", command=lambda: keluar(edit_window), bg="red", fg="white")
    tombol_keluar.grid(row=5, columnspan=2, pady=10)

# Halaman untuk menghapus data ikan
def halaman_hapus_data():
    hapus_window = tk.Toplevel(root)
    hapus_window.title("Hapus Data Ikan")
    hapus_window.configure(bg="#003366")

    label_hapus = tk.Label(hapus_window, text="Pilih Data Ikan yang ingin dihapus:", bg="#003366", fg="white")
    label_hapus.grid(row=0, column=0, padx=10, pady=5)

    dropdown_hapus = ttk.Combobox(hapus_window)
    dropdown_hapus['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_hapus.grid(row=0, column=1, padx=10, pady=5)

    # Listbox untuk menampilkan data yang ada
    data_listbox = tk.Listbox(hapus_window, width=50, height=10)
    data_listbox.grid(row=1, columnspan=2, padx=10, pady=10)

    def update_data_listbox():
        # Kosongkan Listbox dan tampilkan data berdasarkan pilihan user
        data_listbox.delete(0, tk.END)
        data = []
        if dropdown_hapus.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
        elif dropdown_hapus.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
        elif dropdown_hapus.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
        elif dropdown_hapus.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')

        for item in data:
            data_listbox.insert(tk.END, item[0])

    # Update listbox saat combobox dipilih
    dropdown_hapus.bind("<<ComboboxSelected>>", lambda e: update_data_listbox())

    def hapus_data():
        # Ambil data yang dipilih dari Listbox
        selected_index = data_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return

        data_hapus = data_listbox.get(selected_index)

        if dropdown_hapus.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
            updated_data = [item for item in data if item[0] != data_hapus]
            tulis_file('nama_ikan.txt', updated_data)
            tulis_history(f"Menghapus Nama Ikan: {data_hapus}")
        elif dropdown_hapus.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            updated_data = [item for item in data if item[0] != data_hapus]
            tulis_file('nama_jenis.txt', updated_data)
            tulis_history(f"Menghapus Jenis Ikan: {data_hapus}")
        elif dropdown_hapus.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            updated_data = [item for item in data if item[0] != data_hapus]
            tulis_file('nama_warna.txt', updated_data)
            tulis_history(f"Menghapus Warna Ikan: {data_hapus}")
        elif dropdown_hapus.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')
            updated_data = [item for item in data if item[0] != data_hapus]
            tulis_file('jarak_tempuh.txt', updated_data)
            tulis_history(f"Menghapus Jarak Tempuh: {data_hapus}")

        # Update Listbox setelah penghapusan
        messagebox.showinfo("Sukses", "Data berhasil dihapus!")
        update_data_listbox()

    hapus_button = tk.Button(hapus_window, text="Hapus Data Ikan", command=hapus_data, bg="white", fg="black")
    hapus_button.grid(row=4, columnspan=2, pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(hapus_window, text="Keluar", command=lambda: keluar(hapus_window), bg="red", fg="white")
    tombol_keluar.grid(row=5, columnspan=2, pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button( text="Keluar", command=lambda: keluar, bg="red", fg="white")
    tombol_keluar.pack(pady=10)

# Setup main window
root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.geometry("400x400")
root.configure(bg="#003366")

# Header aplikasi
header_label = tk.Label(root, text="Aplikasi Data Ikan", font=("Arial", 24), bg="#003366", fg="white")
header_label.pack(pady=20)

# Tombol untuk menampilkan data
tampilkan_button = tk.Button(root, text="Tampilkan Data Ikan", command=halaman_tampilkan_data_ikan, bg="white", fg="black")
tampilkan_button.pack(pady=10)

# Tombol untuk menambah data ikan
tambah_button = tk.Button(root, text="Tambah Data Ikan", command=halaman_tambah_data, bg="white", fg="black")
tambah_button.pack(pady=10)

# Tombol untuk mengedit data ikan
edit_button = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, bg="white", fg="black")
edit_button.pack(pady=10)

# Tombol untuk menghapus data ikan
hapus_button = tk.Button(root, text="Hapus Data Ikan", command=halaman_hapus_data, bg="white", fg="black")
hapus_button.pack(pady=10)

# Tombol untuk keluar aplikasi
keluar_button = tk.Button(root, text="Keluar", command=root.quit, bg="red", fg="white")
keluar_button.pack(pady=20)

root.mainloop()
