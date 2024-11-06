import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memuat data jenis ikan dari file txt
def load_data(filename):
    data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                item = line.strip()
                if item:
                    data.append(item)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' tidak ditemukan.")
    return data

# Fungsi untuk menyimpan data ke file txt
def save_data(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")

# Load data jenis dari file eksternal
data_jenis_ikan = load_data("jenis_ikan.txt")

# Fungsi untuk menampilkan jendela tambah jenis baru
def tambah_jenis():
    def simpan_jenis():
        jenis = entry_jenis.get()
        if jenis:
            data_jenis_ikan.append(jenis)
            save_data("jenis_ikan.txt", data_jenis_ikan)
            messagebox.showinfo("Berhasil", "Jenis ikan berhasil ditambahkan!")
            update_list_jenis()
            tambah_jendela.destroy()
            root.attributes('-disabled', False)
        else:
            messagebox.showwarning("Peringatan", "Kolom jenis ikan harus diisi.")

    root.attributes('-disabled', True)
    tambah_jendela = tk.Toplevel(root)
    tambah_jendela.title("Tambah Jenis Ikan")
    tambah_jendela.geometry("300x150")

    tk.Label(tambah_jendela, text="Jenis Ikan").pack(pady=5)
    entry_jenis = tk.Entry(tambah_jendela)
    entry_jenis.pack(pady=5)

    tk.Button(tambah_jendela, text="Tambah Jenis", command=simpan_jenis).pack(pady=10)

# Fungsi untuk menampilkan detail jenis ikan
def detail_jenis():
    selected_index = listbox_jenis.curselection()
    if selected_index:
        index = selected_index[0]
        jenis_ikan = data_jenis_ikan[index]

        root.attributes('-disabled', True)
        detail_jendela = tk.Toplevel(root)
        detail_jendela.title("Detail Jenis Ikan")
        detail_jendela.geometry("300x150")

        tk.Label(detail_jendela, text=f"Jenis Ikan: {jenis_ikan}").pack(pady=20)

        # Fungsi untuk kembali ke jendela utama (menu jenis)
        def kembali():
            detail_jendela.destroy()
            root.attributes('-disabled', False)

        # Tombol Kembali untuk menutup jendela detail
        tk.Button(detail_jendela, text="Kembali", command=kembali).pack(pady=10)

        # Menangani event jika user menutup jendela detail dengan tombol "X"
        detail_jendela.protocol("WM_DELETE_WINDOW", kembali)
    else:
        messagebox.showwarning("Peringatan", "Pilih jenis ikan terlebih dahulu.")

# Fungsi untuk mengedit data jenis ikan
def edit_jenis():
    selected_index = listbox_jenis.curselection()
    if selected_index:
        index = selected_index[0]

        def simpan_perubahan():
            jenis = entry_jenis.get()
            if jenis:
                data_jenis_ikan[index] = jenis
                save_data("jenis_ikan.txt", data_jenis_ikan)
                messagebox.showinfo("Berhasil", "Jenis ikan berhasil diperbarui!")
                update_list_jenis()
                edit_jendela.destroy()
                root.attributes('-disabled', False)
            else:
                messagebox.showwarning("Peringatan", "Kolom jenis ikan harus diisi.")

        # Fungsi untuk kembali ke jendela utama (menu jenis)
        def kembali():
            edit_jendela.destroy()
            root.attributes('-disabled', False)

        root.attributes('-disabled', True)
        edit_jendela = tk.Toplevel(root)
        edit_jendela.title("Edit Jenis Ikan")
        edit_jendela.geometry("300x150")

        tk.Label(edit_jendela, text="Jenis Ikan").pack(pady=5)
        entry_jenis = tk.Entry(edit_jendela)
        entry_jenis.pack(pady=5)
        entry_jenis.insert(0, data_jenis_ikan[index])

        tk.Button(edit_jendela, text="Simpan Perubahan", command=simpan_perubahan).pack(pady=10)
        tk.Button(edit_jendela, text="Kembali", command=kembali).pack(pady=5)

        # Menangani event jika user menutup jendela edit dengan tombol "X"
        edit_jendela.protocol("WM_DELETE_WINDOW", kembali)
    else:
        messagebox.showwarning("Peringatan", "Pilih jenis ikan yang ingin diedit.")

# Fungsi untuk menghapus jenis ikan yang dipilih
def hapus_jenis():
    selected_index = listbox_jenis.curselection()
    if selected_index:
        index = selected_index[0]
        
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus jenis ikan '{data_jenis_ikan[index]}'?")
        if konfirmasi:
            data_jenis_ikan.pop(index)
            save_data("jenis_ikan.txt", data_jenis_ikan)
            
            update_list_jenis()
            messagebox.showinfo("Berhasil", "Jenis ikan berhasil dihapus.")
    else:
        messagebox.showwarning("Peringatan", "Pilih jenis ikan yang ingin dihapus.")

# Fungsi untuk memperbarui daftar jenis ikan di listbox
def update_list_jenis():
    listbox_jenis.delete(0, tk.END)
    for i, jenis in enumerate(data_jenis_ikan, start=1):
        listbox_jenis.insert(tk.END, f"{i}: {jenis}")

# Fungsi untuk kembali ke menu utama
def kembali_ke_menu():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Data Jenis Ikan")
root.geometry("400x400")

# Label judul
label_judul = tk.Label(root, text="Data Jenis Ikan", font=("Arial", 16, "bold"))
label_judul.pack(pady=10)

# List Jenis Ikan
frame_list = tk.Frame(root)
frame_list.pack()

listbox_jenis = tk.Listbox(frame_list, width=30, height=10)
listbox_jenis.pack(side="left")

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")
listbox_jenis.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_jenis.yview)

# Tombol Tambah, Hapus, Detail, Edit
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="+", command=tambah_jenis).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="-", command=hapus_jenis).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Detail", command=detail_jenis).grid(row=3, column=1, padx=5)
tk.Button(frame_buttons, text="Edit", command=edit_jenis).grid(row=0, column=1, padx=5)

# Tombol kembali
tk.Button(root, text="Kembali", command=kembali_ke_menu).pack(pady=8)

# Load daftar jenis ikan ke listbox
update_list_jenis()

# Menjalankan aplikasi
root.mainloop()