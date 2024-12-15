import tkinter as tk
from tkinter import messagebox

# Fungsi untuk membaca data ikan dari file
def baca_data_ikan(file_path):
    data = {}
    try:
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
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} tidak ditemukan!")
    return data

# Fungsi untuk membaca data umum (warna/jenis) dari file
def baca_data_file(file_path):
    data = {}
    try:
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
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} tidak ditemukan!")
    return data

# Fungsi untuk membaca data jarak_tempuh dari file (format string)
def baca_data_jarak_tempuh(file_path):
    data = {}
    try:
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
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} tidak ditemukan!")
    return data

def lihat_data():
    def tampilkan_tabel(judul, data, headers, row_formatter):
        if not data:
            messagebox.showerror("Error", f"Tidak ada {judul} yang ditemukan!")
            return

        tabel_window = tk.Toplevel()
        tabel_window.title(judul)
        tabel_window.configure(bg='#87CEFA')  # Latar belakang biru langit
        tabel_window.geometry("800x600")  # Ukuran jendela yang lebih besar

        # Judul
        tk.Label(tabel_window, text=judul, font=("Arial", 18, "bold"), bg='#87CEFA').pack(pady=10)

        # Membuat Treeview untuk tampilan tabel yang lebih baik
        import tkinter.ttk as ttk

        # Membuat Frame untuk Treeview
        tree_frame = tk.Frame(tabel_window)
        tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview
        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=headers, show='headings')
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Konfigurasi scrollbar
        tree_scroll.config(command=tree.yview)

        # Konfigurasi header
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, width=100, anchor='center')

        # Isi data
        for kode, detail in data.items():
            try:
                values = row_formatter(kode, detail)
                tree.insert('', 'end', values=values)
            except KeyError as e:
                tree.insert('', 'end', values=[f"Error: {e}"])

        # Tombol kembali
        tk.Button(tabel_window, text="Kembali", command=tabel_window.destroy, 
                  width=20, font=("Arial", 12), bg="#4682B4", fg="white").pack(pady=10)

    def tampilkan_data_ikan():
        tampilkan_tabel("Data Ikan", data_ikan, headers_ikan, lambda kode, detail: [
            kode,
            detail.get("nama", "Tidak Diketahui"),
            data_warna.get(detail.get("id_warna", -1), "Tidak Diketahui"),
            data_jenis.get(detail.get("id_jenis", -1), "Tidak Diketahui"),
            data_jarak.get(kode, "Tidak Diketahui")
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
        data_jarak = baca_data_jarak_tempuh("jarak_tempuh.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat membaca file: {e}")
        return

    headers_ikan = ["Kode Ikan", "Nama Ikan", "Warna Ikan", "Jenis Ikan", "Jarak Tempuh"]
    headers_warna = ["Kode Warna", "Nama Warna"]
    headers_jenis = ["Kode Jenis", "Nama Jenis"]

    # Main GUI
    root = tk.Toplevel()
    root.title("Lihat Data")
    root.configure(bg='#87CEFA')
    root.geometry("400x300")

    tk.Label(root, text="Pilih Data yang Ingin Ditampilkan", bg="#87CEFA", font=("Arial", 16)).pack(pady=10)

    # Tombol untuk memilih jenis data
    tk.Button(root, text="Data Ikan", command=tampilkan_data_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Warna", command=tampilkan_data_warna, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Data Jenis", command=tampilkan_data_jenis, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    # Tombol kembali
    tk.Button(root, text="Kembali", command=root.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)
