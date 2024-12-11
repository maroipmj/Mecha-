import tkinter as tk
from tkinter import messagebox, ttk

def tambah_data():
    def baca_file_data(file_name):
        """Membaca file data dan mengembalikan dictionary."""
        data = {}
        try:
            with open(file_name, "r") as file:
                for line in file:
                    kode, nama = line.strip().split(":")
                    data[int(kode)] = nama
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {file_name} tidak ditemukan!")
        return data

    def dapatkan_id_baru(file_name):
        """Mengembalikan ID baru berdasarkan ID terakhir di file."""
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                if not lines:
                    return 1  # Jika file kosong, mulai dari ID 1
                last_line = lines[-1]
                last_id = int(last_line.split(":")[0])
                return last_id + 1
        except FileNotFoundError:
            return 1  # Jika file tidak ada, mulai dari ID 1

    def tambah_data_ikan():
        def simpan_ikan():
            try:
                kode = dapatkan_id_baru("nama_ikan.txt")  # ID otomatis
                nama = nama_entry.get().strip()
                warna = warna_var.get()
                jenis = jenis_var.get()
                jarak_tempuh = jarak_entry.get().strip()

                if not nama or warna == "Pilih Warna" or jenis == "Pilih Jenis" or not jarak_tempuh:
                    raise ValueError("Semua kolom harus diisi!")

                # Cari ID warna dan jenis dari nama yang dipilih
                id_warna = [k for k, v in data_warna.items() if v == warna][0]
                id_jenis = [k for k, v in data_jenis.items() if v == jenis][0]

                # Simpan data ikan (ID, nama, ID warna, ID jenis) ke file nama_ikan.txt
                with open("nama_ikan.txt", "a") as file:
                    file.write(f"{kode}:{nama},{id_warna},{id_jenis}\n")

                # Simpan data jarak tempuh (ID ikan dan jarak tempuh) ke file jarak_tempuh.txt
                with open("jarak_tempuh.txt", "a") as file:
                    file.write(f"{kode}: {jarak_tempuh}\n")

                messagebox.showinfo("Sukses", "Data ikan berhasil ditambahkan!")

                # Memperbarui tabel Lihat Data setelah data ditambahkan
                lihat_data()

                tambah_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except KeyError:
                messagebox.showerror("Error", "Warna atau jenis tidak valid!")

        # Data warna dan jenis
        data_warna = baca_file_data("nama_warna.txt")
        data_jenis = baca_file_data("nama_jenis.txt")

        # Window untuk tambah data ikan
        tambah_window = tk.Toplevel()
        tambah_window.title("Tambah Data Ikan")
        tambah_window.configure(bg="#87CEFA")

        tk.Label(tambah_window, text="Nama Ikan:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        nama_entry = tk.Entry(tambah_window, font=("Arial", 12), width=30)
        nama_entry.pack(pady=5)

        tk.Label(tambah_window, text="Pilih Warna:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        warna_var = tk.StringVar()
        warna_var.set("Pilih Warna")  # Default value
        warna_dropdown = ttk.OptionMenu(tambah_window, warna_var, *data_warna.values())
        warna_dropdown.pack(pady=5)

        tk.Label(tambah_window, text="Pilih Jenis:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jenis_var = tk.StringVar()
        jenis_var.set("Pilih Jenis")  # Default value
        jenis_dropdown = ttk.OptionMenu(tambah_window, jenis_var, *data_jenis.values())
        jenis_dropdown.pack(pady=5)

        tk.Label(tambah_window, text="Jarak Tempuh (km):", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jarak_entry = tk.Entry(tambah_window, font=("Arial", 12), width=30)
        jarak_entry.pack(pady=5)

        tk.Button(tambah_window, text="Simpan", command=simpan_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(tambah_window, text="Kembali", command=tambah_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    def menu_tambah_data():
        menu_window = tk.Toplevel()
        menu_window.title("Pilih Data yang Ingin Ditambahkan")
        menu_window.configure(bg="#87CEFA")

        tk.Label(menu_window, text="Pilih Data yang Ingin Ditambahkan", font=("Arial", 16), bg="#87CEFA").pack(pady=10)

        tk.Button(menu_window, text="Tambah Data Ikan", command=lambda: [menu_window.destroy(), tambah_data_ikan()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Tambah Data Warna", command=lambda: [menu_window.destroy(), tambah_data_warna()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Tambah Data Jenis", command=lambda: [menu_window.destroy(), tambah_data_jenis()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Kembali", command=menu_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    menu_tambah_data()
