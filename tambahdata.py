import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import os

def tambah_data():
    def baca_file_data(file_name):
        """Membaca file data dan mengembalikan dictionary."""
        data = {}
        try:
            # Mengecek apakah file ada
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    for line in file:
                        kode, nama = line.strip().split(":")
                        data[int(kode)] = nama
        except Exception as e:
            messagebox.showerror("Error", f"Error saat membaca file {file_name}: {str(e)}")
        return data

    def dapatkan_id_baru(file_name):
        """Mengembalikan ID baru berdasarkan ID terakhir di file."""
        try:
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    lines = file.readlines()
                    if not lines:
                        return 1  # Jika file kosong, mulai dari ID 1
                    last_line = lines[-1]
                    last_id = int(last_line.split(":")[0])
                    return last_id + 1
            else:
                return 1  # Jika file tidak ada, mulai dari ID 1
        except Exception as e:
            messagebox.showerror("Error", f"Error saat mendapatkan ID baru dari file {file_name}: {str(e)}")
            return 1

    def tambah_data_ikan():
        def simpan_ikan():
            try:
                kode = dapatkan_id_baru("nama_ikan.txt")  # ID otomatis
                nama = nama_entry.get().strip()
                warna = warna_var.get()
                jenis = jenis_var.get()

                if not nama or warna == "Pilih Warna" or jenis == "Pilih Jenis":
                    raise ValueError("Semua kolom harus diisi!")

                # Cari ID warna dan jenis dari nama yang dipilih
                id_warna = [k for k, v in data_warna.items() if v == warna][0]
                id_jenis = [k for k, v in data_jenis.items() if v == jenis][0]

                # Simpan data ikan (ID, nama, ID warna, ID jenis) ke file nama_ikan.txt
                with open("nama_ikan.txt", "a") as file:
                    file.write(f"{kode}:{nama},{id_warna},{id_jenis}\n")
                messagebox.showinfo("Sukses", "Data ikan berhasil ditambahkan!")

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

        tk.Button(tambah_window, text="Simpan", command=simpan_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(tambah_window, text="Kembali", command=tambah_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    def tambah_data_warna():
        def simpan_warna():
            try:
                kode = dapatkan_id_baru("nama_warna.txt")
                warna_baru = warna_entry.get().strip()

                if not warna_baru:
                    raise ValueError("Nama warna tidak boleh kosong!")

                # Simpan warna ke file nama_warna.txt
                with open("nama_warna.txt", "a") as file:
                    file.write(f"{kode}:{warna_baru}\n")

                messagebox.showinfo("Sukses", "Data warna berhasil ditambahkan!")

                tambah_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tambah_window = tk.Toplevel()
        tambah_window.title("Tambah Data Warna")
        tambah_window.configure(bg="#87CEFA")

        tk.Label(tambah_window, text="Nama Warna:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        warna_entry = tk.Entry(tambah_window, font=("Arial", 12), width=30)
        warna_entry.pack(pady=5)

        tk.Button(tambah_window, text="Simpan", command=simpan_warna, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(tambah_window, text="Kembali", command=tambah_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    def tambah_data_jenis():
        def simpan_jenis():
            try:
                kode = dapatkan_id_baru("nama_jenis.txt")
                jenis_baru = jenis_entry.get().strip()

                if not jenis_baru:
                    raise ValueError("Nama jenis tidak boleh kosong!")

                # Simpan jenis ke file nama_jenis.txt
                with open("nama_jenis.txt", "a") as file:
                    file.write(f"{kode}:{jenis_baru}\n")

                messagebox.showinfo("Sukses", "Data jenis berhasil ditambahkan!")

                tambah_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tambah_window = tk.Toplevel()
        tambah_window.title("Tambah Data Jenis")
        tambah_window.configure(bg="#87CEFA")

        tk.Label(tambah_window, text="Nama Jenis:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jenis_entry = tk.Entry(tambah_window, font=("Arial", 12), width=30)
        jenis_entry.pack(pady=5)

        tk.Button(tambah_window, text="Simpan", command=simpan_jenis, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(tambah_window, text="Kembali", command=tambah_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    def tambah_data_transaksi():
        def simpan_transaksi():
            try:
                # Ambil ID ikan yang dipilih
                kode_ikan = [k for k, v in data_ikan.items() if v == ikan_var.get()][0]
                tanggal = tanggal_calendar.get_date()  # Sudah dalam format yyyy-mm-dd
                jarak = jarak_entry.get().strip()

                if not jarak:
                    raise ValueError("Jarak tidak boleh kosong!")

                # Mendapatkan ID transaksi baru
                id_transaksi = dapatkan_id_baru("jarak_tempuh.txt")

                # Simpan transaksi ke file
                transaksi_data = f"{id_transaksi}:{tanggal},{kode_ikan},{jarak}\n"
                with open("jarak_tempuh.txt", "a") as file:
                    file.write(transaksi_data)

                messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan!")
                tambah_window.destroy()

            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except KeyError:
                messagebox.showerror("Error", "Ikan tidak valid!")

        # Data ikan dari nama_ikan.txt
        data_ikan = baca_file_data("nama_ikan.txt")

        # Window untuk tambah transaksi
        tambah_window = tk.Toplevel()
        tambah_window.title("Tambah Transaksi")
        tambah_window.configure(bg="#87CEFA")

        tk.Label(tambah_window, text="Pilih Ikan:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        ikan_var = tk.StringVar()
        ikan_var.set("Pilih Ikan")  # Default value
        ikan_dropdown = ttk.OptionMenu(tambah_window, ikan_var, *data_ikan.values())
        ikan_dropdown.pack(pady=5)

        tk.Label(tambah_window, text="Pilih Tanggal:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        tanggal_calendar = Calendar(tambah_window, selectmode="day", date_pattern="yyyy-mm-dd")
        tanggal_calendar.pack(pady=5)

        tk.Label(tambah_window, text="Jarak (km):", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jarak_entry = tk.Entry(tambah_window, font=("Arial", 12), width=30)
        jarak_entry.pack(pady=5)

        tk.Button(tambah_window, text="Simpan", command=simpan_transaksi, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(tambah_window, text="Kembali", command=tambah_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    def menu_tambah_data():
        menu_window = tk.Toplevel()
        menu_window.title("Pilih Data yang Ingin Ditambahkan")
        menu_window.configure(bg="#87CEFA")

        tk.Label(menu_window, text="Pilih Data yang Ingin Ditambahkan", font=("Arial", 16), bg="#87CEFA").pack(pady=10)

        tk.Button(menu_window, text="Tambah Data Ikan", command=lambda: [menu_window.destroy(), tambah_data_ikan()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Tambah Data Warna", command=lambda: [menu_window.destroy(), tambah_data_warna()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Tambah Data Jenis", command=lambda: [menu_window.destroy(), tambah_data_jenis()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Tambah Transaksi", command=lambda: [menu_window.destroy(), tambah_data_transaksi()], bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(menu_window, text="Kembali", command=menu_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    menu_tambah_data()
