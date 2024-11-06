import tkinter as tk
from tkinter import ttk, messagebox
from utils import baca_file, tulis_file, tulis_history

def halaman_edit_data(root):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Data Ikan")
    edit_window.configure(bg="#003366")

    label_edit = tk.Label(edit_window, text="Pilih Data yang ingin diedit:", bg="#003366", fg="white")
    label_edit.grid(row=0, column=0, padx=10, pady=5)

    dropdown_edit = ttk.Combobox(edit_window)
    dropdown_edit['values'] = ["Nama Ikan", "Jenis Ikan", "Warna Ikan", "Jarak Tempuh"]
    dropdown_edit.grid(row=0, column=1, padx=10, pady=5)

    # Dropdown untuk memilih data lama
    label_data_lama = tk.Label(edit_window, text="Pilih Data Lama:", bg="#003366", fg="white")
    label_data_lama.grid(row=1, column=0, padx=10, pady=5)

    dropdown_data_lama = ttk.Combobox(edit_window)
    dropdown_data_lama.grid(row=1, column=1, padx=10, pady=5)

    # Label dan entry untuk data baru
    label_data_baru = tk.Label(edit_window, text="Data Baru:", bg="#003366", fg="white")
    label_data_baru.grid(row=2, column=0, padx=10, pady=5)

    entry_data_baru = tk.Entry(edit_window)
    entry_data_baru.grid(row=2, column=1, padx=10, pady=5)

    # Label untuk menampilkan semua data secara horizontal
    label_semua_data = tk.Label(edit_window, text="", bg="#003366", fg="white", wraplength=400, justify=tk.LEFT)
    label_semua_data.grid(row=5, columnspan=2, padx=10, pady=10)

    def update_fields(event):
        data_file_mapping = {
            "Nama Ikan": 'nama_ikan.txt',
            "Jenis Ikan": 'nama_jenis.txt',
            "Warna Ikan": 'nama_warna.txt',
            "Jarak Tempuh": 'jarak_tempuh.txt'
        }
        
        # Ambil data dari file berdasarkan pilihan dropdown
        data = baca_file(data_file_mapping[dropdown_edit.get()])
        if data:
            # Mengisi dropdown untuk memilih data lama
            dropdown_data_lama['values'] = [item[0] for item in data]
            dropdown_data_lama.set('')  # Reset pilihan dropdown data lama
            entry_data_baru.delete(0, tk.END)  # Reset entry data baru

            # Menampilkan semua data secara horizontal
            all_data = []
            nama_ikan = baca_file('nama_ikan.txt')
            jenis_ikan = baca_file('nama_jenis.txt')
            warna_ikan = baca_file('nama_warna.txt')
            jarak_tempuh = baca_file('jarak_tempuh.txt')

            # Menggabungkan semua data
            for i in range(max(len(nama_ikan), len(jenis_ikan), len(warna_ikan), len(jarak_tempuh))):
                data_str = ""
                if i < len(nama_ikan):
                    data_str += f"Nama: {nama_ikan[i][0]}, "
                if i < len(jenis_ikan):
                    data_str += f"Jenis: {jenis_ikan[i][0]}, "
                if i < len(warna_ikan):
                    data_str += f"Warna: {warna_ikan[i][0]}, "
                if i < len(jarak_tempuh):
                    data_str += f"Waktu: {jarak_tempuh[i][0]} jam, Jarak: {jarak_tempuh[i][1]} km"
                all_data.append(data_str.strip(", "))  # Menghapus trailing comma jika ada

            label_semua_data.config(text="Data Tersimpan:\n" + "\n".join(all_data))

    dropdown_edit.bind("<<ComboboxSelected>>", update_fields)

    def edit_data():
        data_baru = entry_data_baru.get()
        data_lama = dropdown_data_lama.get()
        data_file_mapping = {
            "Nama Ikan": 'nama_ikan.txt',
            "Jenis Ikan": 'nama_jenis.txt',
            "Warna Ikan": 'nama_warna.txt',
            "Jarak Tempuh": 'jarak_tempuh.txt'
        }

        if data_baru and data_lama:
            data = baca_file(data_file_mapping[dropdown_edit.get()])
            for i, item in enumerate(data):
                if item[0] == data_lama:
                    data[i] = [data_baru]
                    tulis_file(data_file_mapping[dropdown_edit.get()], data)
                    tulis_history(f"Edit {dropdown_edit.get()}: {data_lama} menjadi {data_baru}")
                    messagebox.showinfo("Sukses", f"Data {dropdown_edit.get()} berhasil diedit!")
                    return

            messagebox.showwarning("Peringatan", "Data tidak ditemukan!")
        else:
            messagebox.showwarning("Peringatan", "Pilih data lama dan isi data baru!")

    edit_button = tk.Button(edit_window, text="Edit Data", command=edit_data, bg="white", fg="black")
    edit_button.grid(row=3, columnspan=2, pady=10)

    tombol_keluar = tk.Button(edit_window, text="Keluar", command=edit_window.destroy, bg="red", fg="white")
    tombol_keluar.grid(row=4, columnspan=2, pady=10)
