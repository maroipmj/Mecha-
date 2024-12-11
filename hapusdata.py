import tkinter as tk
from tkinter import messagebox

def baca_data_file(file_name):
    """Membaca data dari file (format ID: nama) dan mengembalikan dictionary."""
    data = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":", 1)  # Memisahkan ID dan nama
                if len(parts) == 2:
                    id_item, nama_item = parts
                    data[nama_item] = id_item  # Nama sebagai key, ID sebagai value
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data

def update_file(file_name, data):
    """Memperbarui file dengan data baru."""
    try:
        with open(file_name, "w") as file:
            for nama_item, id_item in data.items():
                file.write(f"{id_item}: {nama_item}\n")
    except Exception as e:
        print(f"Kesalahan memperbarui file {file_name}: {e}")

def hapus_data():
    def configure_window(window, title):
        """Konfigurasi awal untuk jendela dengan background biru langit."""
        window.title(title)
        window.geometry("400x300")
        window.configure(bg="#87CEFA")  # Warna biru langit

    def hapus_data_ikan():
        def konfirmasi_hapus():
            pilihan = ikan_var.get()
            if pilihan == "Pilih Ikan":
                messagebox.showerror("Error", "Pilih ikan untuk dihapus.")
                return
            # Cari ID ikan berdasarkan nama ikan yang dipilih
            id_ikan = data_ikan[pilihan]  # Ambil ID berdasarkan nama ikan yang dipilih
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus ikan '{pilihan}'?")
            if konfirmasi:
                del data_ikan[pilihan]  # Hapus berdasarkan nama ikan
                update_file("nama_ikan.txt", data_ikan)  # Update file
                messagebox.showinfo("Info", f"Data ikan '{pilihan}' berhasil dihapus.")
                hapus_window.destroy()

        data_ikan = baca_data_file("nama_ikan.txt")

        hapus_window = tk.Toplevel()
        configure_window(hapus_window, "Hapus Data Ikan")

        tk.Label(hapus_window, text="Pilih Ikan", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        ikan_var = tk.StringVar(hapus_window)
        ikan_var.set("Pilih Ikan")
        
        # Menampilkan hanya nama ikan di dropdown (tanpa angka ID)
        options = list(data_ikan.keys())  # Ambil hanya nama ikan sebagai pilihan
        tk.OptionMenu(hapus_window, ikan_var, *options).pack(pady=5)

        tk.Button(hapus_window, text="Hapus", command=konfirmasi_hapus, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(hapus_window, text="Kembali", command=hapus_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    def hapus_data_warna():
        def konfirmasi_hapus():
            pilihan = warna_var.get()
            if pilihan == "Pilih Warna":
                messagebox.showerror("Error", "Pilih warna untuk dihapus.")
                return
            # Cari ID warna berdasarkan nama warna yang dipilih
            id_warna = data_warna[pilihan]  # Ambil ID berdasarkan nama warna yang dipilih
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus warna '{pilihan}'?")
            if konfirmasi:
                del data_warna[pilihan]  # Hapus berdasarkan nama warna
                update_file("nama_warna.txt", data_warna)  # Update file
                messagebox.showinfo("Info", f"Data warna '{pilihan}' berhasil dihapus.")
                hapus_window.destroy()

        data_warna = baca_data_file("nama_warna.txt")

        hapus_window = tk.Toplevel()
        configure_window(hapus_window, "Hapus Data Warna")

        tk.Label(hapus_window, text="Pilih Warna", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        warna_var = tk.StringVar(hapus_window)
        warna_var.set("Pilih Warna")
        
        # Menampilkan hanya nama warna di dropdown (tanpa angka ID)
        options = list(data_warna.keys())  # Ambil hanya nama warna sebagai pilihan
        tk.OptionMenu(hapus_window, warna_var, *options).pack(pady=5)

        tk.Button(hapus_window, text="Hapus", command=konfirmasi_hapus, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(hapus_window, text="Kembali", command=hapus_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    def hapus_data_jenis():
        def konfirmasi_hapus():
            pilihan = jenis_var.get()
            if pilihan == "Pilih Jenis":
                messagebox.showerror("Error", "Pilih jenis untuk dihapus.")
                return
            # Cari ID jenis berdasarkan nama jenis yang dipilih
            id_jenis = data_jenis[pilihan]  # Ambil ID berdasarkan nama jenis yang dipilih
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus jenis '{pilihan}'?")
            if konfirmasi:
                del data_jenis[pilihan]  # Hapus berdasarkan nama jenis
                update_file("nama_jenis.txt", data_jenis)  # Update file
                messagebox.showinfo("Info", f"Data jenis '{pilihan}' berhasil dihapus.")
                hapus_window.destroy()

        data_jenis = baca_data_file("nama_jenis.txt")

        hapus_window = tk.Toplevel()
        configure_window(hapus_window, "Hapus Data Jenis")

        tk.Label(hapus_window, text="Pilih Jenis", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jenis_var = tk.StringVar(hapus_window)
        jenis_var.set("Pilih Jenis")
        
        # Menampilkan hanya nama jenis di dropdown (tanpa angka ID)
        options = list(data_jenis.keys())  # Ambil hanya nama jenis sebagai pilihan
        tk.OptionMenu(hapus_window, jenis_var, *options).pack(pady=5)

        tk.Button(hapus_window, text="Hapus", command=konfirmasi_hapus, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(hapus_window, text="Kembali", command=hapus_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    def hapus_jarak_tempuh():
        def konfirmasi_hapus():
            pilihan = jarak_var.get()
            if pilihan == "Pilih Jarak Tempuh":
                messagebox.showerror("Error", "Pilih jarak tempuh untuk dihapus.")
                return
            # Cari ID jarak berdasarkan detail jarak yang dipilih
            id_jarak = data_jarak[pilihan]  # Ambil ID berdasarkan detail yang dipilih
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus jarak tempuh '{pilihan}'?")
            if konfirmasi:
                del data_jarak[pilihan]  # Hapus berdasarkan detail jarak
                update_file("jarak_tempuh.txt", data_jarak)  # Update file
                messagebox.showinfo("Info", f"Jarak tempuh '{pilihan}' berhasil dihapus.")
                hapus_window.destroy()

        data_jarak = baca_data_file("jarak_tempuh.txt")

        hapus_window = tk.Toplevel()
        configure_window(hapus_window, "Hapus Jarak Tempuh")

        tk.Label(hapus_window, text="Pilih Jarak Tempuh", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jarak_var = tk.StringVar(hapus_window)
        jarak_var.set("Pilih Jarak Tempuh")
        
        # Menampilkan hanya detail jarak tempuh di dropdown (tanpa ID)
        options = list(data_jarak.keys())  # Ambil hanya detail jarak sebagai pilihan
        tk.OptionMenu(hapus_window, jarak_var, *options).pack(pady=5)

        tk.Button(hapus_window, text="Hapus", command=konfirmasi_hapus, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(hapus_window, text="Kembali", command=hapus_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    # Main window
    root = tk.Tk()
    configure_window(root, "Hapus Data")

    tk.Label(root, text="Pilih Data yang Ingin Dihapus", bg="#87CEFA", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Hapus Data Ikan", command=hapus_data_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Hapus Data Warna", command=hapus_data_warna, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Hapus Data Jenis", command=hapus_data_jenis, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Hapus Jarak Tempuh", command=hapus_jarak_tempuh, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    tk.Button(root, text="Kembali", command=root.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    root.mainloop()
    