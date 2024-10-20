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
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Nama: {item[0]}")
        elif pilihan.get() == "Jenis Ikan":
            data = baca_file('nama_jenis.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Jenis: {item[0]}")
        elif pilihan.get() == "Warna Ikan":
            data = baca_file('nama_warna.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Warna: {item[0]}")
        elif pilihan.get() == "Jarak Tempuh":
            data = baca_file('jarak_tempuh.txt')
            for i, item in enumerate(data):
                ikan_listbox.insert(tk.END, f"ID: {i + 1} | Kecepatan: {item[0]} km/jam, Waktu: {item[1]} jam, Jarak: {item[2]} km")

    tombol_tampil = tk.Button(tampil_window, text="Tampilkan Data", command=tampil_data, bg="white", fg="black")
    tombol_tampil.pack(pady=10)

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

    def update_item_list(event):
        if dropdown_edit.get() == "Nama Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_ikan.txt')]
        elif dropdown_edit.get() == "Jenis Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_jenis.txt')]
        elif dropdown_edit.get() == "Warna Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_warna.txt')]
        elif dropdown_edit.get() == "Jarak Tempuh":
            pilihan_item['values'] = [f"Kecepatan: {item[0]}, Waktu: {item[1]}, Jarak: {item[2]}" for item in baca_file('jarak_tempuh.txt')]

    dropdown_edit.bind("<<ComboboxSelected>>", update_item_list)

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
                kecepatan, waktu, jarak = data_baru.split(',')
                jarak_tempuh[selected_item] = [kecepatan, waktu, jarak]
                tulis_file('jarak_tempuh.txt', jarak_tempuh)

            messagebox.showinfo("Sukses", "Data berhasil diedit!")
        else:
            messagebox.showwarning("Peringatan", "Pilih item dan isi data yang ingin diedit!")

    edit_button = tk.Button(edit_window, text="Edit Data Ikan", command=edit_data, bg="white", fg="black")
    edit_button.grid(row=3, columnspan=2, pady=10)

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

    def update_item_list(event):
        if dropdown_hapus.get() == "Nama Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_ikan.txt')]
        elif dropdown_hapus.get() == "Jenis Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_jenis.txt')]
        elif dropdown_hapus.get() == "Warna Ikan":
            pilihan_item['values'] = [item[0] for item in baca_file('nama_warna.txt')]
        elif dropdown_hapus.get() == "Jarak Tempuh":
            pilihan_item['values'] = [f"Kecepatan: {item[0]}, Waktu: {item[1]}, Jarak: {item[2]}" for item in baca_file('jarak_tempuh.txt')]

    dropdown_hapus.bind("<<ComboboxSelected>>", update_item_list)

    def hapus_data():
        selected_item = pilihan_item.current()

        if selected_item >= 0:
            if dropdown_hapus.get() == "Nama Ikan":
                nama_ikan = baca_file('nama_ikan.txt')
                del nama_ikan[selected_item]
                tulis_file('nama_ikan.txt', nama_ikan)
            elif dropdown_hapus.get() == "Jenis Ikan":
                jenis_ikan = baca_file('nama_jenis.txt')
                del jenis_ikan[selected_item]
                tulis_file('nama_jenis.txt', jenis_ikan)
            elif dropdown_hapus.get() == "Warna Ikan":
                warna_ikan = baca_file('nama_warna.txt')
                del warna_ikan[selected_item]
                tulis_file('nama_warna.txt', warna_ikan)
            elif dropdown_hapus.get() == "Jarak Tempuh":
                jarak_tempuh = baca_file('jarak_tempuh.txt')
                del jarak_tempuh[selected_item]
                tulis_file('jarak_tempuh.txt', jarak_tempuh)

            messagebox.showinfo("Sukses", "Data berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih item yang ingin dihapus!")

    hapus_button = tk.Button(hapus_window, text="Hapus Data Ikan", command=hapus_data, bg="white", fg="black")
    hapus_button.grid(row=2, columnspan=2, pady=10)

# Menginisialisasi aplikasi
root = tk.Tk()
root.title("Aplikasi Data Ikan")
root.configure(bg="#003366")

# Tombol untuk membuka halaman masing-masing
tombol_tampil = tk.Button(root, text="Tampilkan Data Ikan", command=halaman_tampilkan_data_ikan, bg="white", fg="black")
tombol_tampil.pack(pady=10)

tombol_edit = tk.Button(root, text="Edit Data Ikan", command=halaman_edit_data, bg="white", fg="black")
tombol_edit.pack(pady=10)

tombol_hapus = tk.Button(root, text="Hapus Data Ikan", command=halaman_hapus_data, bg="white", fg="black")
tombol_hapus.pack(pady=10)

root.mainloop()