import tkinter as tk
from tkinter import messagebox
<<<<<<< HEAD
from tkinter import ttk  # Untuk Treeview

# Fungsi untuk membaca data dari file teks dan mengabaikan angka di awal baris
def baca_data_dari_file(filename):
    try:
        with open(filename, "r") as file:
            # Membaca setiap baris, memisahkan berdasarkan spasi, dan mengabaikan angka pertama
            return [line.strip().split(" ", 1)[-1] for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' tidak ditemukan.")
        return []
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka {filename}.\nError: {str(e)}")
        return []

# Fungsi untuk melihat data seluruhnya
def lihat_data_seluruhnya():
    # Membaca data dari file
    nama_ikan = baca_data_dari_file("nama_ikan.txt")
    jenis_ikan = baca_data_dari_file("nama_jenis.txt")
    warna_ikan = baca_data_dari_file("nama_warna.txt")
    jarak_tempuh = baca_data_dari_file("jarak_tempuh.txt")

    # Memeriksa apakah jumlah data konsisten
    if len(nama_ikan) != len(jenis_ikan) or len(jenis_ikan) != len(warna_ikan) or len(warna_ikan) != len(jarak_tempuh):
        messagebox.showerror("Error", "Jumlah data di file-file tidak konsisten.\nPeriksa jumlah baris pada setiap file.")
        return

    # Membuat jendela baru untuk menampilkan data
    window_data = tk.Toplevel(root)
    window_data.title("Data Keseluruhan Ikan")
    window_data.geometry("700x400")

    # Membuat label judul
    label_judul = tk.Label(window_data, text="Data Keseluruhan Ikan", font=("Arial", 16, "bold"))
    label_judul.pack(pady=10)

    # Membuat frame untuk Treeview (tabel)
    frame_data = tk.Frame(window_data)
    frame_data.pack(pady=10, fill="both", expand=True)

    # Membuat Treeview untuk menampilkan data
    tree = ttk.Treeview(frame_data, columns=("Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"), show="headings")
    tree.pack(fill="both", expand=True)

    # Menambahkan header untuk setiap kolom
    tree.heading("Nama Ikan", text="Nama Ikan")
    tree.heading("Jenis Ikan", text="Jenis Ikan")
    tree.heading("Warna Ikan", text="Warna Ikan")
    tree.heading("Jarak Tempuh", text="Jarak Tempuh")

    # Menambahkan lebar kolom
    tree.column("Nama Ikan", width=150, anchor="w")
    tree.column("Jenis Ikan", width=150, anchor="w")
    tree.column("Warna Ikan", width=150, anchor="w")
    tree.column("Jarak Tempuh", width=150, anchor="w")

    # Menambahkan data ke dalam Treeview
    for (nama, jenis, warna, jarak) in zip(nama_ikan, jenis_ikan, warna_ikan, jarak_tempuh):
        tree.insert("", "end", values=(nama, jenis, warna, jarak))

    # Menambahkan scrollbar vertikal untuk Treeview
    scrollbar = tk.Scrollbar(frame_data, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Membuat tombol Kembali untuk kembali ke menu utama
    btn_kembali = tk.Button(window_data, text="Kembali", command=window_data.destroy, bg="#ff6666", font=("Arial", 12, "bold"))
    btn_kembali.pack(side="bottom", pady=10)

=======

>>>>>>> 20c38400cb29301d776868643be0b238d7fc32b8
# Fungsi untuk menjalankan file Python eksternal
def buka_file_py(filename):
    try:
        # Membaca dan menjalankan kode dari file Python eksternal
        with open(filename, "r") as file:
            code = file.read()
            exec(code, globals())  # Menjalankan kode dalam konteks global aplikasi utama
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka {filename}.\nError: {str(e)}")

# Fungsi untuk menutup aplikasi
def keluar_aplikasi():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Menu Utama - Data Ikan")
root.geometry("400x400")
root.configure(bg="#e6f2ff")  # Warna latar belakang utama yang lembut

# Membuat label judul
label_judul = tk.Label(root, text="Menu Data Ikan", font=("Arial", 20, "bold"), fg="#004080", bg="#e6f2ff")
label_judul.pack(pady=20)

# Membuat frame untuk tombol navigasi
frame_menu = tk.Frame(root, bg="#e6f2ff")
frame_menu.pack(pady=20, fill="both", expand=True)  # Gunakan fill dan expand agar frame bisa mengisi ruang

# Gaya tombol
button_style = {
    "width": 20,
    "font": ("Arial", 12, "bold"),
    "relief": "groove",
    "borderwidth": 2,
    "fg": "black",  # Warna teks diubah menjadi hitam
}

# Membuat tombol navigasi di frame menu dengan urutan yang diinginkan
btn_lihat_data = tk.Button(frame_menu, text="Lihat Data Keseluruhan", command=lihat_data_seluruhnya, bg="#66b3ff", **button_style)
btn_lihat_data.pack(side="top", pady=10)  # Tombol "Lihat Data Seluruhnya" akan berada di bagian atas

btn_ikan = tk.Button(frame_menu, text="Data Ikan", command=lambda: buka_file_py("ikan.py"), bg="#66b3ff", **button_style)
btn_ikan.pack(pady=10)

btn_jenis = tk.Button(frame_menu, text="Jenis Ikan", command=lambda: buka_file_py("jenis.py"), bg="#66b3ff", **button_style)
btn_jenis.pack(pady=10)

btn_warna = tk.Button(frame_menu, text="Warna Ikan", command=lambda: buka_file_py("warna.py"), bg="#66b3ff", **button_style)
btn_warna.pack(pady=10)

# Membuat tombol Keluar dengan warna berbeda untuk menonjolkan
btn_keluar = tk.Button(frame_menu, text="Keluar", command=keluar_aplikasi, bg="#ff4d4d", **button_style)
btn_keluar.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
