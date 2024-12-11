import tkinter as tk
from tkinter import messagebox


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
                    # Abaikan baris yang tidak sesuai format
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
                    # Abaikan baris yang tidak sesuai format
                    continue
    return data


# Fungsi untuk membaca data jarak_tempuh dari file (format string)
def baca_data_jarak_tempuh(file_path):
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    kode, jarak = line.split(":")
                    data[int(kode)] = jarak.strip()  # Simpan dalam bentuk string
                except ValueError:
                    # Abaikan baris yang tidak sesuai format
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
            label.grid(row=0, column=col, sticky="nsew")  # Menambahkan sticky untuk perataan

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
                    label.grid(row=row, column=col, sticky="nsew")  # Menambahkan sticky untuk perataan
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
            data_jenis.get(detail.get("id_jenis", -1), "Tidak Diketahui"),
            data_jarak.get(kode, "Tidak Diketahui")  # Menambahkan jarak tempuh dalam format string
        ])

    def tampilkan_data_warna():
        tampilkan_tabel("Data Warna", data_warna, headers_warna, lambda kode, nama: [kode, nama])

    def tampilkan_data_jenis():
        tampilkan_tabel("Data Jenis", data_jenis, headers_jenis, lambda kode, nama: [kode, nama])

    # Load data
    try:
        data_ikan = baca_data_ikan("nama_ikan.txt")
        data_warna = baca_data_file("nama_warna.txt")
        data_jenis = baca_data_file("nama_jenis.txt")
        data_jarak = baca_data_jarak_tempuh("jarak_tempuh.txt")  # Membaca data jarak tempuh (dalam format string)
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"File tidak ditemukan: {e.filename}")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat membaca file: {e}")
        return

    headers_ikan = ["Kode Ikan", "Nama Ikan", "Warna Ikan", "Jenis Ikan", "Jarak Tempuh"]  # Menambahkan header untuk jarak tempuh
    headers_warna = ["Kode Warna", "Nama Warna"]
    headers_jenis = ["Kode Jenis", "Nama Jenis"]

    # Main GUI
    root = tk.Toplevel()
    root.title("Lihat Data")
    root.configure(bg='#87CEFA')  # Latar belakang biru langit

    tk.Label(root, text="Pilih Data yang Ingin Ditampilkan", bg="#87CEFA", font=("Arial", 16)).pack(pady=10)

    # Tombol untuk memilih jenis data
    tk.Button(root, text="Data Ikan", command=tampilkan_data_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Warna", command=tampilkan_data_warna, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Jenis", command=tampilkan_data_jenis, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    # Tombol kembali
    tk.Button(root, text="Kembali", command=root.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    root.mainloop()
