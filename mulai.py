import tkinter as tk
from tkinter import messagebox
import threading

# Fungsi untuk menjalankan file Python eksternal di thread terpisah
def buka_file_py(filename):
    def run_file():
        try:
            # Membaca dan menjalankan kode dari file Python eksternal
            with open(filename, "r") as file:
                code = file.read()
                exec(code, globals())  # Menjalankan kode dalam konteks global aplikasi utama
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{filename}' tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka {filename}.\nError: {str(e)}")
        finally:
            # Aktifkan kembali semua tombol setelah selesai menjalankan file Python
            set_tombol_state("normal")

    # Nonaktifkan semua tombol saat file Python sedang diproses
    set_tombol_state("disabled")
    
    # Menjalankan fungsi di thread terpisah
    threading.Thread(target=run_file).start()

# Fungsi untuk menutup aplikasi
def keluar_aplikasi():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        root.destroy()

# Fungsi untuk mengatur status tombol
def set_tombol_state(state):
    btn_ikan.config(state=state)
    btn_jenis.config(state=state)
    btn_warna.config(state=state)
    btn_transaksi.config(state=state)
    btn_keluar.config(state=state)

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
frame_menu.pack(pady=20)

# Gaya tombol
button_style = {
    "width": 20,
    "font": ("Arial", 12, "bold"),
    "relief": "groove",
    "borderwidth": 2,
    "fg": "black",  # Warna teks diubah menjadi hitam
}

# Membuat tombol navigasi di frame menu
btn_ikan = tk.Button(frame_menu, text="Data Ikan", command=lambda: buka_file_py("ikan.py"), bg="#66b3ff", **button_style)
btn_ikan.grid(row=0, column=0, padx=5, pady=10)

btn_jenis = tk.Button(frame_menu, text="Jenis Ikan", command=lambda: buka_file_py("jenis.py"), bg="#66b3ff", **button_style)
btn_jenis.grid(row=1, column=0, padx=5, pady=10)

btn_warna = tk.Button(frame_menu, text="Warna Ikan", command=lambda: buka_file_py("warna.py"), bg="#66b3ff", **button_style)
btn_warna.grid(row=2, column=0, padx=5, pady=10)

btn_transaksi = tk.Button(frame_menu, text="Transaksi", command=lambda: buka_file_py("jarak.py"), bg="#66b3ff", **button_style)
btn_transaksi.grid(row=3, column=0, padx=5, pady=10)

# Membuat tombol Keluar dengan warna berbeda untuk menonjolkan
btn_keluar = tk.Button(frame_menu, text="Keluar", command=keluar_aplikasi, bg="#ff4d4d", **button_style)
btn_keluar.grid(row=4, column=0, padx=5, pady=20)

# Menjalankan aplikasi
root.mainloop()
