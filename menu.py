import tkinter as tk
from tkinter import messagebox

# Variabel global untuk menyimpan jendela tambahan yang dibuka
jendela_tambahan = None

# Fungsi untuk menampilkan jendela konten sesuai menu yang dipilih
def buka_jendela(konten):
    global jendela_tambahan
    
    # Jika ada jendela tambahan yang sudah terbuka, tutup dulu
    if jendela_tambahan is not None:
        jendela_tambahan.destroy()

    # Membuat jendela tambahan baru
    jendela_tambahan = tk.Toplevel(root)
    jendela_tambahan.title(f"Halaman {konten.capitalize()}")
    jendela_tambahan.geometry("300x200")

    # Menambahkan konten yang sesuai di dalam jendela tambahan
    if konten == "ikan":
        tk.Label(jendela_tambahan, text="Halaman Data Ikan", font=("Arial", 14)).pack(pady=20)
    elif konten == "jenis":
        tk.Label(jendela_tambahan, text="Halaman Data Jenis Ikan", font=("Arial", 14)).pack(pady=20)
    elif konten == "warna":
        tk.Label(jendela_tambahan, text="Halaman Data Warna Ikan", font=("Arial", 14)).pack(pady=20)
    elif konten == "transaksi":
        tk.Label(jendela_tambahan, text="Halaman Data Transaksi", font=("Arial", 14)).pack(pady=20)

    # Menambahkan tombol kembali untuk menutup jendela
    tk.Button(jendela_tambahan, text="Kembali", command=jendela_tambahan.destroy).pack(pady=10)

# Fungsi untuk menutup aplikasi
def keluar_aplikasi():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Menu Utama - Data Ikan")
root.geometry("400x300")

# Membuat label judul
label_judul = tk.Label(root, text="Menu Data Ikan", font=("Arial", 16, "bold"))
label_judul.pack(pady=10)

# Membuat frame untuk tombol navigasi
frame_menu = tk.Frame(root)
frame_menu.pack(pady=20)

# Membuat tombol navigasi di frame menu
btn_ikan = tk.Button(frame_menu, text="Ikan", command=lambda: buka_jendela("ikan"), width=20)
btn_ikan.grid(row=0, column=0, padx=5, pady=5)

btn_jenis = tk.Button(frame_menu, text="Jenis", command=lambda: buka_jendela("jenis"), width=20)
btn_jenis.grid(row=1, column=0, padx=5, pady=5)

btn_warna = tk.Button(frame_menu, text="Warna", command=lambda: buka_jendela("warna"), width=20)
btn_warna.grid(row=2, column=0, padx=5, pady=5)

btn_transaksi = tk.Button(frame_menu, text="Transaksi", command=lambda: buka_jendela("transaksi"), width=20)
btn_transaksi.grid(row=3, column=0, padx=5, pady=5)

# Membuat tombol Keluar dengan background merah
btn_keluar = tk.Button(frame_menu, text="Keluar", command=keluar_aplikasi, width=20, bg="red", fg="white")
btn_keluar.grid(row=4, column=0, padx=5, pady=20)

# Menjalankan aplikasi
root.mainloop()
