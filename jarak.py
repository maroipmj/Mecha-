import tkinter as tk
from tkinter import messagebox

def tampilkan_transaksi():
    # Membuat jendela transaksi
    transaksi_root = tk.Tk()
    transaksi_root.title("Transaksi Jarak")
    transaksi_root.geometry("400x300")
    transaksi_root.configure(bg="#f9f9f9")

    # Label judul
    label_judul = tk.Label(transaksi_root, text="Halaman Transaksi Jarak", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333")
    label_judul.pack(pady=20)

    # Label info
    label_info = tk.Label(transaksi_root, text="Tampilkan data jarak, waktu, dan kecepatan di sini.", font=("Arial", 12), bg="#f9f9f9", fg="#666")
    label_info.pack(pady=10)

    # Tombol kembali
    btn_kembali = tk.Button(transaksi_root, text="Kembali", command=transaksi_root.destroy, bg="#4CAF50", fg="white", width=10)
    btn_kembali.pack(pady=20)

    transaksi_root.mainloop()

# Pastikan kode ini hanya berjalan jika file ini dijalankan langsung
if __name__ == "__main__":
    tampilkan_transaksi()
