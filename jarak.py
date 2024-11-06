import tkinter as tk
from tkinter import messagebox

class IkanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hitung Jarak Tempuh Ikan Berenang")
        self.root.geometry("400x300")  # Tambahkan ukuran jendela utama agar konsisten
        
        # Label judul
        label_judul = tk.Label(self.root, text="Hitung Jarak Tempuh Ikan", font=("Arial", 16, "bold"))
        label_judul.pack(pady=10)

        # Frame utama
        self.frame_main = tk.Frame(self.root)
        self.frame_main.pack(pady=20)

        # Tombol untuk Input Kecepatan dan Waktu
        btn_input = tk.Button(self.frame_main, text="Masukkan Data", command=self.input_data)
        btn_input.pack(pady=10)

    # Fungsi untuk menampilkan jendela input data
    def input_data(self):
        self.root.attributes('-disabled', True)  # Disable jendela utama saat popup dibuka
        self.popup_input = tk.Toplevel(self.root)
        self.popup_input.title("Input Data")
        self.popup_input.geometry("300x200")

        # Label dan Entry untuk Kecepatan
        lbl_kecepatan = tk.Label(self.popup_input, text="Kecepatan (km/jam):")
        lbl_kecepatan.pack(pady=5)
        self.entry_kecepatan = tk.Entry(self.popup_input)
        self.entry_kecepatan.pack(pady=5)

        # Label dan Entry untuk Waktu
        lbl_waktu = tk.Label(self.popup_input, text="Waktu (jam):")
        lbl_waktu.pack(pady=5)
        self.entry_waktu = tk.Entry(self.popup_input)
        self.entry_waktu.pack(pady=5)

        # Tombol untuk Menghitung Jarak
        btn_hitung = tk.Button(self.popup_input, text="Hitung Jarak Tempuh", command=self.hitung_jarak)
        btn_hitung.pack(pady=10)

        # Tombol untuk Kembali
        btn_kembali = tk.Button(self.popup_input, text="Kembali", command=self.kembali_menu_utama)
        btn_kembali.pack(pady=5)

        # Mengatur aksi ketika tombol "X" ditekan
        self.popup_input.protocol("WM_DELETE_WINDOW", self.kembali_menu_utama)

    # Fungsi untuk menghitung jarak tempuh ikan
    def hitung_jarak(self):
        try:
            # Mengambil input kecepatan dan waktu
            kecepatan = float(self.entry_kecepatan.get())
            waktu = float(self.entry_waktu.get())
            
            # Menghitung jarak tempuh
            jarak = kecepatan * waktu
            
            # Menampilkan hasil jarak tempuh di jendela baru
            self.popup_input.destroy()  # Menutup jendela input setelah hitung
            self.tampilkan_hasil(jarak)
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid. Masukkan angka yang benar.")

    # Fungsi untuk menampilkan hasil perhitungan
    def tampilkan_hasil(self, jarak):
        self.popup_hasil = tk.Toplevel(self.root)
        self.popup_hasil.title("Hasil Perhitungan")
        self.popup_hasil.geometry("300x150")

        # Menampilkan hasil jarak tempuh
        lbl_hasil = tk.Label(self.popup_hasil, text=f"Jarak Tempuh Ikan: {jarak} km")
        lbl_hasil.pack(pady=20)

        # Tombol untuk Kembali
        btn_kembali = tk.Button(self.popup_hasil, text="Kembali", command=self.kembali_menu_utama_hasil)
        btn_kembali.pack(pady=10)

        # Mengatur aksi ketika tombol "X" ditekan
        self.popup_hasil.protocol("WM_DELETE_WINDOW", self.kembali_menu_utama_hasil)

    # Fungsi untuk kembali ke menu utama dari popup input
    def kembali_menu_utama(self):
        self.popup_input.destroy()  # Menutup jendela input
        self.root.attributes('-disabled', False)  # Enable jendela utama

    # Fungsi untuk kembali ke menu utama dari popup hasil
    def kembali_menu_utama_hasil(self):
        self.popup_hasil.destroy()  # Menutup jendela hasil
        self.root.attributes('-disabled', False)  # Enable jendela utama

if __name__ == "__main__":
    root = tk.Tk()
    app = IkanApp(root)
    root.mainloop()
