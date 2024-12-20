import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk membaca file data
def baca_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        return []

# Fungsi untuk menulis ke file data
def tulis_file(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(','.join(item) + '\n')

# Fungsi untuk menampilkan header
def tampilkan_header(window, title):
    header_label = tk.Label(window, text=title, font=("Arial", 16), bg="#003366", fg="white")
    header_label.pack(pady=10)

# Fungsi untuk keluar dari window
def keluar(window):
    window.destroy()

# Halaman untuk menampilkan data ikan
def halaman_tampilkan_data_ikan():
    tampil_window = tk.Toplevel(root)
    tampil_window.title("Tampilkan Data Ikan")
    tampil_window.configure(bg="#003366")
    tampilkan_header(tampil_window, "Tampilkan Data Ikan")

    label_pilihan = tk.Label(tampil_window, text="Pilih Data yang ingin dilihat:", bg="#003366", fg="white")
    label_pilihan.pack(pady=5)

    pilihan = ttk.Combobox(tampil_window)
    pilihan['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    pilihan.pack(pady=5)

    ikan_listbox = tk.Listbox(tampil_window, width=50, height=10)
    ikan_listbox.pack(pady=20)

    def tampil_data():
        ikan_listbox.delete(0, tk.END)
        if pilihan.get() == "Nama Ikan":
            data = baca_file('nama_ikan.txt')
            for item in data:
                ikan_listbox.insert(tk.END, f"Nama: {item[0]}")
        elif pilihan.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            for item in data:
                ikan_listbox.insert(tk.END, f"Jenis: {item[0]}")
        elif pilihan.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            for item in data:
                ikan_listbox.insert(tk.END, f"Warna: {item[0]}")
        elif pilihan.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')
            for item in data:
                ikan_listbox.insert(tk.END, f"Waktu: {item[0]} jam, Jarak: {item[1]} km")

    tombol_tampil = tk.Button(tampil_window, text="Tampilkan Data", command=tampil_data, bg="white", fg="black")
    tombol_tampil.pack(pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(tampil_window, text="Keluar", command=lambda: keluar(tampil_window), bg="red", fg="white")
    tombol_keluar.pack(pady=10)

# Halaman untuk edit data ikan
def halaman_edit_data():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Data Ikan")
    edit_window.configure(bg="#003366")

    label_edit = tk.Label(edit_window, text="Pilih Data Ikan yang ingin diedit:", bg="#003366", fg="white")
    label_edit.grid(row=0, column=0, padx=10, pady=5)

    dropdown_edit = ttk.Combobox(edit_window)
    dropdown_edit['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_edit.grid(row=0, column=1, padx=10, pady=5)

    label_item = tk.Label(edit_window, text="Pilih Item:", bg="#003366", fg="white")
    label_item.grid(row=1, column=0, padx=10, pady=5)

    pilihan_item = ttk.Combobox(edit_window)
    pilihan_item.grid(row=1, column=1, padx=10, pady=5)

    def update_edit_item_list(event):
        if dropdown_edit.get() == "Nama Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_ikan.txt')]
        elif dropdown_edit.get() == "Jenis Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_jenis.txt')]
        elif dropdown_edit.get() == "Warna Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_warna.txt')]
        elif dropdown_edit.get() == "Jarak Tempuh":
            pilihan_item['values'] = [f"Waktu: {item[0]}, Jarak: {item[1]}" for item in baca_file('jarak_tempuh.txt')]

    dropdown_edit.bind("<<ComboboxSelected>>", update_edit_item_list)

    label_edit_value = tk.Label(edit_window, text="Data Baru:", bg="#003366", fg="white")
    label_edit_value.grid(row=2, column=0, padx=10, pady=5)
    entry_edit = tk.Entry(edit_window)
    entry_edit.grid(row=2, column=1, padx=10, pady=5)

    def edit_data():
        selected_item = pilihan_item.current()
        data_baru = entry_edit.get()

        if selected_item >= 0 and data_baru:
            if dropdown_edit.get() == "Nama Ikan":
                nama_ikan = baca_file('nama_ikan.txt')
                nama_ikan[selected_item][0] = data_baru
                tulis_file('nama_ikan.txt', nama_ikan)
            elif dropdown_edit.get() == "Jenis Ikan":
                jenis_ikan = baca_file('nama_jenis.txt')
                jenis_ikan[selected_item][0] = data_baru
                tulis_file('nama_jenis.txt', jenis_ikan)
            elif dropdown_edit.get() == "Warna Ikan":
                warna_ikan = baca_file('nama_warna.txt')
                warna_ikan[selected_item][0] = data_baru
                tulis_file('nama_warna.txt', warna_ikan)
            elif dropdown_edit.get() == "Jarak Tempuh":
                jarak_tempuh = baca_file('jarak_tempuh.txt')
                waktu, jarak = data_baru.split(',')
                jarak_tempuh[selected_item] = [waktu.strip(), jarak.strip()]
                tulis_file('jarak_tempuh.txt', jarak_tempuh)

            messagebox.showinfo("Sukses", "Data berhasil diedit!")
        else:
            messagebox.showwarning("Peringatan", "Pilih item dan isi data yang ingin diedit!")

    edit_button = tk.Button(edit_window, text="Edit Data Ikan", command=edit_data, bg="white", fg="black")
    edit_button.grid(row=3, columnspan=2, pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(edit_window, text="Keluar", command=lambda: keluar(edit_window), bg="red", fg="white")
    tombol_keluar.grid(row=4, columnspan=2, pady=10)

# Halaman untuk hapus data ikan
def halaman_hapus_data():
    hapus_window = tk.Toplevel(root)
    hapus_window.title("Hapus Data Ikan")
    hapus_window.configure(bg="#003366")

    label_hapus = tk.Label(hapus_window, text="Pilih Data Ikan yang ingin dihapus:", bg="#003366", fg="white")
    label_hapus.grid(row=0, column=0, padx=10, pady=5)

    dropdown_hapus = ttk.Combobox(hapus_window)
    dropdown_hapus['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_hapus.grid(row=0, column=1, padx=10, pady=5)

    label_item = tk.Label(hapus_window, text="Pilih Item:", bg="#003366", fg="white")
    label_item.grid(row=1, column=0, padx=10, pady=5)

    pilihan_item = ttk.Combobox(hapus_window)
    pilihan_item.grid(row=1, column=1, padx=10, pady=5)

    def update_hapus_item_list(event):
        if dropdown_hapus.get() == "Nama Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_ikan.txt')]
        elif dropdown_hapus.get() == "Jenis Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_jenis.txt')]
        elif dropdown_hapus.get() == "Warna Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_warna.txt')]
        elif dropdown_hapus.get() == "Jarak Tempuh":
            pilihan_item['values'] = [f"Waktu: {item[0]}, Jarak: {item[1]}" for item in baca_file('jarak_tempuh.txt')]

    dropdown_hapus.bind("<<ComboboxSelected>>", update_hapus_item_list)

    def hapus_data():
        selected_item = pilihan_item.current()
        if selected_item >= 0:
            if dropdown_hapus.get() == "Nama Ikan":
                nama_ikan = baca_file('nama_ikan.txt')
                nama_ikan.pop(selected_item)
                tulis_file('nama_ikan.txt', nama_ikan)
            elif dropdown_hapus.get() == "Jenis Ikan":
                jenis_ikan = baca_file('nama_jenis.txt')
                jenis_ikan.pop(selected_item)
                tulis_file('nama_jenis.txt', jenis_ikan)
            elif dropdown_hapus.get() == "Warna Ikan":
                warna_ikan = baca_file('nama_warna.txt')
                warna_ikan.pop(selected_item)
                tulis_file('nama_warna.txt', warna_ikan)
            elif dropdown_hapus.get() == "Jarak Tempuh":
                jarak_tempuh = baca_file('jarak_tempuh.txt')
                jarak_tempuh.pop(selected_item)
                tulis_file('jarak_tempuh.txt', jarak_tempuh)

            messagebox.showinfo("Sukses", "Data berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih item yang ingin dihapus!")

    hapus_button = tk.Button(hapus_window, text="Hapus Data Ikan", command=hapus_data, bg="white", fg="black")
    hapus_button.grid(row=2, columnspan=2, pady=10)

    # Tombol keluar
    tombol_keluar = tk.Button(hapus_window, text="Keluar", command=lambda: keluar(hapus_window), bg="red", fg="white")
    tombol_keluar.grid(row=3, columnspan=2, pady=10)

# Setup Tkinter Root
root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.geometry("400x400")
root.configure(bg="#003366")

# Label utama
label_utama = tk.Label(root, text="Selamat Datang di Aplikasi Data Ikan", font=("Arial", 16), bg="#003366", fg="white")
label_utama.pack(pady=20)

# Tombol
tombol_tampilkan_data = tk.Button(root, text="Tampilkan Data Ikan", command=halaman_tampilkan_data_ikan, bg="white", fg="black")
tombol_tampilkan_data.pack(pady=5)

tombol_edit_data = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, bg="white", fg="black")
tombol_edit_data.pack(pady=5)

tombol_hapus_data = tk.Button(root, text="Hapus Data Ikan", command=halaman_hapus_data, bg="white", fg="black")
tombol_hapus_data.pack(pady=5)

tombol_keluar = tk.Button(root, text="Keluar", command=root.quit, bg="red", fg="white")
tombol_keluar.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
