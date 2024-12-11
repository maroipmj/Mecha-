import tkinter as tk
from tkinter import messagebox


def baca_data_file(file_name):
    """Membaca data dari file (format kode:nama) dan mengembalikan dictionary."""
    data = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":", 1)
                if len(parts) == 2:
                    kode, nama = parts
                    data[nama] = kode  # Balik: Nama sebagai kunci, ID sebagai nilai
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data


def update_file(file_name, data):
    """Memperbarui file dengan data baru."""
    try:
        with open(file_name, "w") as file:
            for nama, kode in data.items():
                file.write(f"{kode}:{nama}\n")
    except Exception as e:
        print(f"Kesalahan memperbarui file {file_name}: {e}")


def baca_data_ikan(file_name):
    """Membaca data ikan dari file nama_ikan.txt."""
    data = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":", 1)
                if len(parts) == 2:
                    kode, detail = parts[0], parts[1].split(",")
                    if len(detail) == 3:
                        data[detail[0]] = {"kode": kode, "id_warna": detail[1], "id_jenis": detail[2]}  # Nama sebagai kunci
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data


def update_file_ikan(file_name, data_ikan):
    """Memperbarui file nama_ikan.txt."""
    try:
        with open(file_name, "w") as file:
            for nama, detail in data_ikan.items():
                file.write(f"{detail['kode']}:{nama},{detail['id_warna']},{detail['id_jenis']}\n")
    except Exception as e:
        print(f"Kesalahan memperbarui file {file_name}: {e}")


def edit_data():
    def configure_window(window, title):
        """Konfigurasi awal untuk jendela dengan background biru langit."""
        window.title(title)
        window.geometry("400x300")
        window.configure(bg="#87CEFA")  # Warna biru langit

    def edit_data_ikan():
        def simpan_perubahan_ikan():
            pilihan = ikan_var.get()
            if pilihan == "Pilih Ikan":
                messagebox.showerror("Error", "Pilih ikan untuk diedit.")
                return
            nama_baru = entry_nama.get()
            if not nama_baru:
                messagebox.showerror("Error", "Nama baru tidak boleh kosong.")
                return
            # Ubah nama ikan
            data_ikan[nama_baru] = data_ikan.pop(pilihan)
            update_file_ikan("nama_ikan.txt", data_ikan)
            messagebox.showinfo("Info", f"Nama ikan berhasil diperbarui menjadi {nama_baru}.")
            edit_window.destroy()

        data_ikan = baca_data_ikan("nama_ikan.txt")

        # Window untuk edit data ikan
        edit_window = tk.Toplevel()
        configure_window(edit_window, "Edit Data Ikan")

        tk.Label(edit_window, text="Pilih Ikan", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        ikan_var = tk.StringVar(edit_window)
        ikan_var.set("Pilih Ikan")
        options = list(data_ikan.keys())
        tk.OptionMenu(edit_window, ikan_var, *options).pack(pady=5)

        tk.Label(edit_window, text="Nama Baru:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        entry_nama = tk.Entry(edit_window, width=30)
        entry_nama.pack(pady=5)

        tk.Button(edit_window, text="Simpan", command=simpan_perubahan_ikan, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(edit_window, text="Kembali", command=edit_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    def edit_data_warna():
        def simpan_perubahan_warna():
            pilihan = warna_var.get()
            if pilihan == "Pilih Warna":
                messagebox.showerror("Error", "Pilih warna untuk diedit.")
                return
            nama_baru = entry_nama.get()
            if not nama_baru:
                messagebox.showerror("Error", "Nama baru tidak boleh kosong.")
                return
            # Ubah nama warna
            data_warna[nama_baru] = data_warna.pop(pilihan)
            update_file("nama_warna.txt", data_warna)
            messagebox.showinfo("Info", f"Nama warna berhasil diperbarui menjadi {nama_baru}.")
            edit_window.destroy()

        data_warna = baca_data_file("nama_warna.txt")

        # Window untuk edit data warna
        edit_window = tk.Toplevel()
        configure_window(edit_window, "Edit Data Warna")

        tk.Label(edit_window, text="Pilih Warna", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        warna_var = tk.StringVar(edit_window)
        warna_var.set("Pilih Warna")
        options = list(data_warna.keys())
        tk.OptionMenu(edit_window, warna_var, *options).pack(pady=5)

        tk.Label(edit_window, text="Nama Baru:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        entry_nama = tk.Entry(edit_window, width=30)
        entry_nama.pack(pady=5)

        tk.Button(edit_window, text="Simpan", command=simpan_perubahan_warna, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(edit_window, text="Kembali", command=edit_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    def edit_data_jenis():
        def simpan_perubahan_jenis():
            pilihan = jenis_var.get()
            if pilihan == "Pilih Jenis":
                messagebox.showerror("Error", "Pilih jenis untuk diedit.")
                return
            nama_baru = entry_nama.get()
            if not nama_baru:
                messagebox.showerror("Error", "Nama baru tidak boleh kosong.")
                return
            # Ubah nama jenis
            data_jenis[nama_baru] = data_jenis.pop(pilihan)
            update_file("nama_jenis.txt", data_jenis)
            messagebox.showinfo("Info", f"Nama jenis berhasil diperbarui menjadi {nama_baru}.")
            edit_window.destroy()

        data_jenis = baca_data_file("nama_jenis.txt")

        # Window untuk edit data jenis
        edit_window = tk.Toplevel()
        configure_window(edit_window, "Edit Data Jenis")

        tk.Label(edit_window, text="Pilih Jenis", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jenis_var = tk.StringVar(edit_window)
        jenis_var.set("Pilih Jenis")
        options = list(data_jenis.keys())
        tk.OptionMenu(edit_window, jenis_var, *options).pack(pady=5)

        tk.Label(edit_window, text="Nama Baru:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        entry_nama = tk.Entry(edit_window, width=30)
        entry_nama.pack(pady=5)

        tk.Button(edit_window, text="Simpan", command=simpan_perubahan_jenis, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(edit_window, text="Kembali", command=edit_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    def edit_jarak_tempuh():
        def simpan_perubahan_jarak():
            pilihan = jarak_var.get()
            if pilihan == "Pilih Jarak Tempuh":
                messagebox.showerror("Error", "Pilih jarak tempuh untuk diedit.")
                return
            nama_baru = entry_nama.get()
            if not nama_baru:
                messagebox.showerror("Error", "Nama baru tidak boleh kosong.")
                return
            # Ubah nama jarak tempuh
            data_jarak[nama_baru] = data_jarak.pop(pilihan)
            update_file("jarak_tempuh.txt", data_jarak)
            messagebox.showinfo("Info", f"Nama jarak tempuh berhasil diperbarui menjadi {nama_baru}.")
            edit_window.destroy()

        data_jarak = baca_data_file("jarak_tempuh.txt")

        # Window untuk edit data jarak tempuh
        edit_window = tk.Toplevel()
        configure_window(edit_window, "Edit Data Jarak Tempuh")

        tk.Label(edit_window, text="Pilih Jarak Tempuh", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        jarak_var = tk.StringVar(edit_window)
        jarak_var.set("Pilih Jarak Tempuh")
        options = list(data_jarak.keys())
        tk.OptionMenu(edit_window, jarak_var, *options).pack(pady=5)

        tk.Label(edit_window, text="Nama Baru:", bg="#87CEFA", font=("Arial", 12)).pack(pady=5)
        entry_nama = tk.Entry(edit_window, width=30)
        entry_nama.pack(pady=5)

        tk.Button(edit_window, text="Simpan", command=simpan_perubahan_jarak, bg="#4682B4", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(edit_window, text="Kembali", command=edit_window.destroy, bg="#4682B4", fg="white", font=("Arial", 12)).pack()

    # Main window
    root = tk.Tk()
    configure_window(root, "Edit Data")

    tk.Label(root, text="Pilih Data yang Ingin Diedit", bg="#87CEFA", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Edit Data Ikan", command=edit_data_ikan, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Edit Data Warna", command=edit_data_warna, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Edit Data Jenis", command=edit_data_jenis, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)
    tk.Button(root, text="Edit Data Jarak Tempuh", command=edit_jarak_tempuh, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=5)

    tk.Button(root, text="Kembali", command=root.destroy, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    root.mainloop()
    