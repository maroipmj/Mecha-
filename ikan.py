import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memuat data ikan dari file txt
def load_data_with_id(filename):
    data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                item = line.strip()
                if ":" in item:
                    data.append(item)
    except FileNotFoundError:
        open(filename, "w").close()  # Buat file kosong jika tidak ditemukan
    return data

# Fungsi untuk menyimpan data ke file txt
def save_data_with_id(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")

# Fungsi untuk mendapatkan ID baru
def generate_id(data):
    if data:
        last_id = max(int(line.split(":")[0]) for line in data)
        return str(last_id + 1)
    return "1"

# Load data dari file eksternal
data_nama_ikan_with_id = load_data_with_id("nama_ikan.txt")
data_jenis_ikan = load_data_with_id("nama_jenis.txt")
data_warna_ikan = load_data_with_id("nama_warna.txt")
data_jarak_ikan = load_data_with_id("jarak_tempuh.txt")

# Pilihan dropdown berdasarkan file
jenis_ikan_options = [line.split(":")[1] for line in data_jenis_ikan]
warna_ikan_options = [line.split(":")[1] for line in data_warna_ikan]

# Fungsi untuk menampilkan jendela tambah ikan baru
def tambah_ikan():
    def simpan_ikan():
        nama = entry_nama.get()
        jenis = jenis_var.get()
        warna = warna_var.get()
        jarak = entry_jarak.get()
        if nama and jenis and warna and jarak:
            try:
                jarak = float(jarak)  # Pastikan jarak adalah angka
                new_id = generate_id(data_nama_ikan_with_id)
                data_nama_ikan_with_id.append(f"{new_id}:{nama}")
                data_jenis_ikan.append(f"{new_id}:{jenis}")
                data_warna_ikan.append(f"{new_id}:{warna}")
                data_jarak_ikan.append(f"{new_id}:{jarak}")
                save_data_with_id("nama_ikan.txt", data_nama_ikan_with_id)
                save_data_with_id("nama_jenis.txt", data_jenis_ikan)
                save_data_with_id("nama_warna.txt", data_warna_ikan)
                save_data_with_id("jarak_tempuh.txt", data_jarak_ikan)
                messagebox.showinfo("Berhasil", "Ikan berhasil ditambahkan!")
                update_list_ikan()
                tambah_jendela.destroy()
                root.attributes('-disabled', False)
            except ValueError:
                messagebox.showerror("Error", "Jarak harus berupa angka.")
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")

    root.attributes('-disabled', True)
    tambah_jendela = tk.Toplevel(root)
    tambah_jendela.title("Tambah Ikan Baru")
    tambah_jendela.geometry("300x300")
    tambah_jendela.configure(bg="#e6e6fa")

    tk.Label(tambah_jendela, text="Nama Ikan", bg="#e6e6fa").pack()
    entry_nama = tk.Entry(tambah_jendela)
    entry_nama.pack()

    tk.Label(tambah_jendela, text="Jenis Ikan", bg="#e6e6fa").pack()
    jenis_var = tk.StringVar(tambah_jendela)
    jenis_var.set(jenis_ikan_options[0] if jenis_ikan_options else "")
    jenis_menu = tk.OptionMenu(tambah_jendela, jenis_var, *jenis_ikan_options)
    jenis_menu.pack()

    tk.Label(tambah_jendela, text="Warna Ikan", bg="#e6e6fa").pack()
    warna_var = tk.StringVar(tambah_jendela)
    warna_var.set(warna_ikan_options[0] if warna_ikan_options else "")
    warna_menu = tk.OptionMenu(tambah_jendela, warna_var, *warna_ikan_options)
    warna_menu.pack()

    tk.Label(tambah_jendela, text="Jarak Ikan (meter)", bg="#e6e6fa").pack()
    entry_jarak = tk.Entry(tambah_jendela)
    entry_jarak.pack()

    tk.Button(tambah_jendela, text="Tambah Ikan", command=simpan_ikan, bg="#66cdaa", fg="white").pack(pady=10)
    tambah_jendela.protocol("WM_DELETE_WINDOW", lambda: [tambah_jendela.destroy(), root.attributes('-disabled', False)])

# Fungsi untuk menampilkan detail ikan
def detail_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        id_ikan, nama_ikan = data_nama_ikan_with_id[index].split(":", 1)
        jenis_ikan = data_jenis_ikan[index].split(":")[1] if index < len(data_jenis_ikan) else "Tidak diketahui"
        warna_ikan = data_warna_ikan[index].split(":")[1] if index < len(data_warna_ikan) else "Tidak diketahui"
        jarak_ikan = data_jarak_ikan[index].split(":")[1] if index < len(data_jarak_ikan) else "Tidak diketahui"

        messagebox.showinfo(
            "Detail Ikan",
            f"ID: {id_ikan}\nNama: {nama_ikan}\nJenis: {jenis_ikan}\nWarna: {warna_ikan}\nJarak: {jarak_ikan} "
        )
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan terlebih dahulu.")

# Fungsi untuk mengedit ikan
def edit_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        id_ikan, nama_ikan = data_nama_ikan_with_id[index].split(":", 1)

        def simpan_perubahan():
            nama = entry_nama.get()
            jenis = jenis_var.get()
            warna = warna_var.get()
            jarak = entry_jarak.get()
            if nama and jenis and warna and jarak:
                try:
                    jarak = float(jarak)  # Pastikan jarak adalah angka
                    # Perbarui data
                    data_nama_ikan_with_id[index] = f"{id_ikan}:{nama}"
                    data_jenis_ikan[index] = f"{id_ikan}:{jenis}"
                    data_warna_ikan[index] = f"{id_ikan}:{warna}"
                    data_jarak_ikan[index] = f"{id_ikan}:{jarak}"
                    save_data_with_id("nama_ikan.txt", data_nama_ikan_with_id)
                    save_data_with_id("nama_jenis.txt", data_jenis_ikan)
                    save_data_with_id("nama_warna.txt", data_warna_ikan)
                    save_data_with_id("jarak_tempuh.txt", data_jarak_ikan)
                    messagebox.showinfo("Berhasil", "Data ikan berhasil diperbarui!")
                    update_list_ikan()
                    edit_jendela.destroy()
                    root.attributes('-disabled', False)
                except ValueError:
                    messagebox.showerror("Error", "Jarak harus berupa angka.")
            else:
                messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")

        root.attributes('-disabled', True)
        edit_jendela = tk.Toplevel(root)
        edit_jendela.title("Edit Ikan")
        edit_jendela.geometry("300x300")
        edit_jendela.configure(bg="#e6e6fa")

        tk.Label(edit_jendela, text="Nama Ikan", bg="#e6e6fa").pack()
        entry_nama = tk.Entry(edit_jendela)
        entry_nama.insert(0, nama_ikan)
        entry_nama.pack()

        tk.Label(edit_jendela, text="Jenis Ikan", bg="#e6e6fa").pack()
        jenis_var = tk.StringVar(edit_jendela, value=data_jenis_ikan[index].split(":")[1])
        jenis_menu = tk.OptionMenu(edit_jendela, jenis_var, *jenis_ikan_options)
        jenis_menu.pack()

        tk.Label(edit_jendela, text="Warna Ikan", bg="#e6e6fa").pack()
        warna_var = tk.StringVar(edit_jendela, value=data_warna_ikan[index].split(":")[1])
        warna_menu = tk.OptionMenu(edit_jendela, warna_var, *warna_ikan_options)
        warna_menu.pack()

        tk.Label(edit_jendela, text="Jarak Ikan (meter)", bg="#e6e6fa").pack()
        entry_jarak = tk.Entry(edit_jendela)
        entry_jarak.insert(0, data_jarak_ikan[index].split(":")[1])
        entry_jarak.pack()

        tk.Button(edit_jendela, text="Simpan", command=simpan_perubahan, bg="#66cdaa", fg="white").pack(pady=10)
        edit_jendela.protocol("WM_DELETE_WINDOW", lambda: [edit_jendela.destroy(), root.attributes('-disabled', False)])
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan terlebih dahulu.")

# Fungsi untuk menghapus ikan
def hapus_ikan():
    selected_index = listbox_ikan.curselection()
    if selected_index:
        index = selected_index[0]
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ikan ini?")
        if confirm:
            del data_nama_ikan_with_id[index]
            del data_jenis_ikan[index]
            del data_warna_ikan[index]
            #del data_jarak_ikan[index]
            save_data_with_id("nama_ikan.txt", data_nama_ikan_with_id)
            save_data_with_id("nama_jenis.txt", data_jenis_ikan)
            save_data_with_id("nama_warna.txt", data_warna_ikan)
            save_data_with_id("jarak_tempuh.txt", data_jarak_ikan)
            messagebox.showinfo("Berhasil", "Data ikan berhasil dihapus.")
            update_list_ikan()
    else:
        messagebox.showwarning("Peringatan", "Pilih ikan terlebih dahulu.")

# Fungsi untuk memperbarui daftar ikan di listbox
def update_list_ikan():
    listbox_ikan.delete(0, tk.END)
    for item in data_nama_ikan_with_id:
        id_ikan, nama_ikan = item.split(":", 1)
        listbox_ikan.insert(tk.END, f"{id_ikan}. {nama_ikan}")

# Membuat jendela utama
root = tk.Tk()
root.title("Data Ikan")
root.geometry("400x400")
root.configure(bg="#e6e6fa")

# Label judul
label_judul = tk.Label(root, text="Data Ikan", font=("Arial", 16, "bold"), bg="#e6e6fa", fg="#6a0dad")
label_judul.pack(pady=10)

# List Ikan
frame_list = tk.Frame(root, bg="#e6e6fa")
frame_list.pack()

listbox_ikan = tk.Listbox(frame_list, width=40, height=10, bg="white", fg="black", highlightbackground="#d3d3d3")
listbox_ikan.pack(side="left")

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")
listbox_ikan.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_ikan.yview)

# Tombol Tambah, Edit, Detail, Hapus
frame_buttons = tk.Frame(root, bg="#e6e6fa")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Tambah", command=tambah_ikan, bg="#66cdaa", fg="white", width=8).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Detail", command=detail_ikan, bg="#87ceeb", fg="white", width=8).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Edit", command=edit_ikan, bg="#ffa07a", fg="white", width=8).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Hapus", command=hapus_ikan, bg="#ff6347", fg="white", width=8).grid(row=0, column=3, padx=5)

# Load daftar ikan ke listbox
update_list_ikan()

<<<<<<< HEAD
# Menjalankan aplikasi
root.mainloop()
=======
root.mainloop()
>>>>>>> 20c38400cb29301d776868643be0b238d7fc32b8
