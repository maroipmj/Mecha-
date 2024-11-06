import tkinter as tk
from tkinter import messagebox

class IkanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Ikan")

        self.jenis_ikan = ["Koi", "Lele"]  # Daftar jenis ikan awal
        
        # Frame utama
        self.frame_main = tk.Frame(self.root)
        self.frame_main.pack()

        # Tombol Jenis
        self.btn_jenis = tk.Button(self.frame_main, text="Jenis", command=self.menu_jenis)
        self.btn_jenis.pack(pady=10)
        
    def menu_jenis(self):
        self.frame_main.pack_forget()
        self.frame_jenis = tk.Frame(self.root)
        self.frame_jenis.pack()

        # Daftar jenis ikan
        self.listbox_jenis = tk.Listbox(self.frame_jenis)
        self.update_jenis_listbox()
        self.listbox_jenis.pack()

        # Tombol Tambah, Hapus, dan Edit
        btn_tambah = tk.Button(self.frame_jenis, text="+", command=self.tambah_jenis)
        btn_tambah.pack(side=tk.LEFT, padx=5)
        
        btn_hapus = tk.Button(self.frame_jenis, text="-", command=self.hapus_jenis)
        btn_hapus.pack(side=tk.LEFT, padx=5)

        btn_edit = tk.Button(self.frame_jenis, text="Edit", command=self.edit_jenis)
        btn_edit.pack(side=tk.LEFT, padx=5)

        # Tombol kembali
        btn_kembali = tk.Button(self.frame_jenis, text="Kembali", command=self.kembali_menu_utama)
        btn_kembali.pack(pady=10)
        
    def update_jenis_listbox(self):
        self.listbox_jenis.delete(0, tk.END)
        for idx, jenis in enumerate(self.jenis_ikan, start=1):
            self.listbox_jenis.insert(tk.END, f"{idx}: {jenis}")
    
    def tambah_jenis(self):
        self.frame_jenis.pack_forget()
        self.frame_tambah = tk.Frame(self.root)
        self.frame_tambah.pack()

        self.entry_tambah = tk.Entry(self.frame_tambah)
        self.entry_tambah.pack()

        btn_tambah = tk.Button(self.frame_tambah, text="Tambah", command=self.simpan_tambah_jenis)
        btn_tambah.pack(pady=5)

        btn_kembali = tk.Button(self.frame_tambah, text="Kembali", command=self.kembali_menu_jenis)
        btn_kembali.pack(pady=5)

    def simpan_tambah_jenis(self):
        jenis_baru = self.entry_tambah.get()
        if jenis_baru:
            self.jenis_ikan.append(jenis_baru)
            self.kembali_menu_jenis()

    def hapus_jenis(self):
        selected = self.listbox_jenis.curselection()
        if selected:
            jenis = self.jenis_ikan[selected[0]]
            confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus {jenis}?")
            if confirm:
                self.jenis_ikan.pop(selected[0])
                self.update_jenis_listbox()
    
    def edit_jenis(self):
        selected = self.listbox_jenis.curselection()
        if selected:
            self.jenis_index = selected[0]
            self.jenis_edit = self.jenis_ikan[self.jenis_index]
            self.frame_jenis.pack_forget()
            self.frame_edit = tk.Frame(self.root)
            self.frame_edit.pack()

            self.entry_edit = tk.Entry(self.frame_edit)
            self.entry_edit.insert(0, self.jenis_edit)
            self.entry_edit.pack()

            btn_simpan = tk.Button(self.frame_edit, text="Simpan", command=self.simpan_edit_jenis)
            btn_simpan.pack(pady=5)

            btn_kembali = tk.Button(self.frame_edit, text="Kembali", command=self.kembali_menu_jenis)
            btn_kembali.pack(pady=5)

    def simpan_edit_jenis(self):
        jenis_baru = self.entry_edit.get()
        if jenis_baru:
            self.jenis_ikan[self.jenis_index] = jenis_baru
            self.kembali_menu_jenis()

    def kembali_menu_utama(self):
        self.frame_jenis.pack_forget()
        self.frame_main.pack()

    def kembali_menu_jenis(self):
        self.frame_tambah.pack_forget() if hasattr(self, 'frame_tambah') else None
        self.frame_edit.pack_forget() if hasattr(self, 'frame_edit') else None
        self.frame_jenis.pack()
        self.update_jenis_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = IkanApp(root)
    root.mainloop()
