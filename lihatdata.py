import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from tkcalendar import DateEntry
import datetime

# Fungsi untuk membaca data ikan dari file
def baca_data_ikan(file_path):
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    kode, detail = line.split(":")
                    nama, id_warna, id_jenis = detail.split(",")
                    data[int(kode)] = {
                        "nama": nama.strip(),
                        "id_warna": int(id_warna.strip()),
                        "id_jenis": int(id_jenis.strip()),
                    }
                except ValueError:
                    continue
    return data

# Fungsi untuk membaca data umum (warna/jenis) dari file
def baca_data_file(file_path):
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    kode, nama = line.split(":")
                    data[int(kode)] = nama.strip()
                except ValueError:
                    continue
    return data

# Fungsi untuk membaca data transaksi (jarak tempuh) dari file
def baca_data_transaksi(file_path):
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    kode, detail = line.split(":")
                    tanggal, id_ikan, jarak = detail.split(",")
                    data[int(kode)] = {
                        "tanggal": tanggal.strip(),
                        "id_ikan": int(id_ikan.strip()),
                        "jarak": jarak.strip()
                    }
                except ValueError:
                    continue
    return data

# Fungsi utama untuk menampilkan data
def lihat_data():
    def tampilkan_tabel(judul, data, headers, row_formatter):
        if not data:
            messagebox.showerror("Error", f"Tidak ada {judul} yang ditemukan!")
            return

        tabel_window = tk.Toplevel()
        tabel_window.title(judul)
        tabel_window.configure(bg='#87CEFA')  # Latar belakang biru langit

        # Judul
        tk.Label(tabel_window, text=judul, font=("Arial", 18, "bold"), bg='#87CEFA').pack(pady=10)

        # Header tabel
        header_frame = tk.Frame(tabel_window, bg='#87CEFA')
        header_frame.pack(pady=5)

        # Membuat header rata tengah
        for col, header in enumerate(headers):
            label = tk.Label(header_frame, text=header, borderwidth=1, relief="solid", width=20, bg='#87CEFA', font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, sticky="nsew")

        # Mengatur konfigurasi kolom agar rata
        for col in range(len(headers)):
            header_frame.grid_columnconfigure(col, weight=1, uniform="equal")

        # Isi tabel
        data_frame = tk.Frame(tabel_window, bg='#87CEFA')
        data_frame.pack(pady=5)

        for row, (kode, detail) in enumerate(data.items(), start=1):
            try:
                values = row_formatter(kode, detail)
                for col, value in enumerate(values):
                    label = tk.Label(data_frame, text=value, borderwidth=1, relief="solid", width=20, bg='#87CEFA', font=("Arial", 12))
                    label.grid(row=row, column=col, sticky="nsew")
            except KeyError as e:
                label = tk.Label(data_frame, text=f"Error: {e}", borderwidth=1, relief="solid", width=20, bg='#87CEFA', font=("Arial", 12))
                label.grid(row=row, column=0, sticky="nsew")

        # Mengatur konfigurasi kolom agar rata
        for col in range(len(headers)):
            data_frame.grid_columnconfigure(col, weight=1, uniform="equal")

        # Tombol kembali
        tk.Button(tabel_window, text="Kembali", command=tabel_window.destroy, width=20, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=10)

    def tampilkan_data_ikan():
        tampilkan_tabel("Data Ikan", data_ikan, headers_ikan, lambda kode, detail: [
            kode,
            detail.get("nama", "Tidak Diketahui"),
            data_warna.get(detail.get("id_warna", -1), "Tidak Diketahui"),
            data_jenis.get(detail.get("id_jenis", -1), "Tidak Diketahui")
        ])

    def tampilkan_data_warna():
        tampilkan_tabel("Data Warna", data_warna, headers_warna, lambda kode, nama: [kode, nama])

    def tampilkan_data_jenis():
        tampilkan_tabel("Data Jenis", data_jenis, headers_jenis, lambda kode, nama: [kode, nama])

    def tampilkan_data_transaksi():
        # Sorting Transaksi berdasarkan tanggal
        sorted_data = sorted(data_transaksi.items(), key=lambda x: x[1]['tanggal'])

        # Menampilkan tabel transaksi
        tampilkan_tabel("Data Transaksi", dict(sorted_data), headers_transaksi, lambda kode, detail: [
            kode,
            detail.get("tanggal", "Tidak Diketahui"),
            data_ikan.get(detail.get("id_ikan", -1), {}).get("nama", "Tidak Diketahui"),
            detail.get("jarak", "Tidak Diketahui")
        ])

    def tampilkan_data_transaksi_urutkan():
        def ambil_tanggal():
            start_date = cal_mulai.get_date()
            end_date = cal_selesai.get_date()

            if start_date > end_date:
                messagebox.showerror("Error", "Tanggal mulai tidak boleh lebih besar dari tanggal selesai!")
                return

            # Filter transaksi berdasarkan rentang tanggal
            filtered_data = {kode: detail for kode, detail in data_transaksi.items()
                             if start_date <= datetime.datetime.strptime(detail['tanggal'], "%Y-%m-%d").date() <= end_date}

            # Menampilkan hasil filter
            if filtered_data:
                tampilkan_tabel("Filtered by Date", filtered_data, headers_transaksi, lambda kode, detail: [
                    kode,
                    detail.get("tanggal", "Tidak Diketahui"),
                    data_ikan.get(detail.get("id_ikan", -1), {}).get("nama", "Tidak Diketahui"),
                    detail.get("jarak", "Tidak Diketahui")
                ])
            else:
                messagebox.showinfo("Informasi", "Tidak ada transaksi dalam rentang tanggal yang dipilih.")

        # GUI untuk memilih tanggal
        date_window = tk.Toplevel()
        date_window.title("Pilih Rentang Tanggal")
        date_window.configure(bg="#87CEFA")

        tk.Label(date_window, text="Pilih Tanggal Mulai", font=("Arial", 12), bg="#87CEFA").pack(pady=5)
        cal_mulai = DateEntry(date_window, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-MM-dd")
        cal_mulai.pack(pady=5)

        tk.Label(date_window, text="Pilih Tanggal Selesai", font=("Arial", 12), bg="#87CEFA").pack(pady=5)
        cal_selesai = DateEntry(date_window, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-MM-dd")
        cal_selesai.pack(pady=5)

        # Tombol konfirmasi
        tk.Button(date_window, text="Filter Data", command=ambil_tanggal, bg="#4682B4", fg="white", font=("Arial", 12), width=15).pack(pady=10)
        tk.Button(date_window, text="Kembali", command=date_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=15).pack(pady=5)

    # Load data
    try:
        data_ikan = baca_data_ikan("nama_ikan.txt")
        data_warna = baca_data_file("nama_warna.txt")
        data_jenis = baca_data_file("nama_jenis.txt")
        data_transaksi = baca_data_transaksi("jarak_tempuh.txt")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"File tidak ditemukan: {e.filename}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat membaca file: {e}")
        return

    headers_ikan = ["Kode Ikan", "Nama Ikan", "Warna Ikan", "Jenis Ikan"]
    headers_warna = ["Kode Warna", "Nama Warna"]
    headers_jenis = ["Kode Jenis", "Nama Jenis"]
    headers_transaksi = ["Kode Transaksi", "Tanggal", "Nama Ikan", "Jarak Tempuh"]

    # Main GUI
    root = tk.Toplevel()
    root.title("Lihat Data")
    root.configure(bg='#87CEFA')

    tk.Label(root, text="Pilih Data yang Ingin Ditampilkan", bg="#87CEFA", font=("Arial", 16)).pack(pady=10)

    # Tombol untuk memilih jenis data
    tk.Button(root, text="Data Ikan", command=tampilkan_data_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Warna", command=tampilkan_data_warna, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Jenis", command=tampilkan_data_jenis, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Transaksi", command=tampilkan_data_transaksi, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Filtered by Date", command=tampilkan_data_transaksi_urutkan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    # Tombol kembali
    tk.Button(root, text="Kembali", command=root.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    root.mainloop()
