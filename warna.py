import tkinter as tk
from tkinter import messagebox

class IkanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Ikan - Warna")
        self.root.geometry("400x300")  # Menambahkan ukuran default untuk jendela utama

        self.warna_ikan = ["kuning", "biru"]  # Daftar warna ikan awal
        
        # Label judul
        label_judul = tk.Label(self.root, text="Kelola Warna Ikan", font=("Arial", 16, "bold"))
        label_judul.pack(pady=10)
        
        # Frame utama
        self.frame_main = tk.Frame(self.root)
        self.frame_main.pack(pady=20)

        # Tombol Warna
        self.btn_warna = tk.Button(self.frame_main, text="Warna", command=self.menu_warna)
        self.btn_warna.pack(pady=10)
        
    def menu_warna(self):
        self.frame_main.pack_forget()
        self.frame_warna = tk.Frame(self.root)
        self.frame_warna.pack(pady=20)

        # Daftar warna ikan
        self.listbox_warna = tk.Listbox(self.frame_warna)
        self.update_warna_listbox()
        self.listbox_warna.pack(pady=10)

        # Tombol Tambah, Hapus, dan Edit
        btn_tambah = tk.Button(self.frame_warna, text="+", command=self.tambah_warna)
        btn_tambah.pack(side=tk.LEFT, padx=5)
        
        btn_hapus = tk.Button(self.frame_warna, text="-", command=self.hapus_warna)
        btn_hapus.pack(side=tk.LEFT, padx=5)

        btn_edit = tk.Button(self.frame_warna, text="Edit", command=self.edit_warna)
        btn_edit.pack(side=tk.LEFT, padx=5)

        # Tombol kembali
        btn_kembali = tk.Button(self.frame_warna, text="Kembali", command=self.kembali_menu_utama)
        btn_kembali.pack(pady=10)
        
    def update_warna_listbox(self):
        self.listbox_warna.delete(0, tk.END)
        for idx, warna in enumerate(self.warna_ikan, start=1):
            self.listbox_warna.insert(tk.END, f"{idx}: {warna}")
    
    def tambah_warna(self):
        self.root.attributes('-disabled', True)  # Disable jendela utama
        self.popup_tambah = tk.Toplevel(self.root)
        self.popup_tambah.title("Tambah Warna Ikan")
        self.popup_tambah.geometry("300x150")

        self.entry_tambah = tk.Entry(self.popup_tambah)
        self.entry_tambah.pack(pady=10)

        btn_tambah = tk.Button(self.popup_tambah, text="Tambah", command=self.simpan_tambah_warna)
        btn_tambah.pack(pady=5)

        btn_kembali = tk.Button(self.popup_tambah, text="Kembali", command=self.kembali_menu_warna)
        btn_kembali.pack(pady=5)

        self.popup_tambah.protocol("WM_DELETE_WINDOW", self.kembali_menu_warna)

    def simpan_tambah_warna(self):
        warna_baru = self.entry_tambah.get()
        if warna_baru:
            self.warna_ikan.append(warna_baru)
            self.kembali_menu_warna()

    def hapus_warna(self):
        selected = self.listbox_warna.curselection()
        if selected:
            warna = self.warna_ikan[selected[0]]
            confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus warna {warna}?")
            if confirm:
                self.warna_ikan.pop(selected[0])
                self.update_warna_listbox()
    
    def edit_warna(self):
        selected = self.listbox_warna.curselection()
        if selected:
            self.warna_index = selected[0]
            self.warna_edit = self.warna_ikan[self.warna_index]
            self.root.attributes('-disabled', True)  # Disable jendela utama
            self.popup_edit = tk.Toplevel(self.root)
            self.popup_edit.title("Edit Warna Ikan")
            self.popup_edit.geometry("300x150")

            self.entry_edit = tk.Entry(self.popup_edit)
            self.entry_edit.insert(0, self.warna_edit)
            self.entry_edit.pack(pady=10)

            btn_simpan = tk.Button(self.popup_edit, text="Simpan", command=self.simpan_edit_warna)
            btn_simpan.pack(pady=5)

            btn_kembali = tk.Button(self.popup_edit, text="Kembali", command=self.kembali_menu_warna)
            btn_kembali.pack(pady=5)

            self.popup_edit.protocol("WM_DELETE_WINDOW", self.kembali_menu_warna)

    def simpan_edit_warna(self):
        warna_baru = self.entry_edit.get()
        if warna_baru:
            self.warna_ikan[self.warna_index] = warna_baru
            self.kembali_menu_warna()

    def kembali_menu_utama(self):
        self.frame_warna.pack_forget()
        self.frame_main.pack(pady=20)

    def kembali_menu_warna(self):
        if hasattr(self, 'popup_tambah'):
            self.popup_tambah.destroy()
        if hasattr(self, 'popup_edit'):
            self.popup_edit.destroy()
        self.root.attributes('-disabled', False)  # Enable jendela utama
        self.update_warna_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = IkanApp(root)
    root.mainloop()
