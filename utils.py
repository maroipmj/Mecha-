import datetime
import tkinter as tk


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

# Fungsi untuk menulis history ke file
def tulis_history(aksi):
    with open('history.txt', 'a') as f:
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{waktu_sekarang}] {aksi}\n")

# Fungsi untuk keluar dari window
def keluar(window):
    window.destroy()

# Fungsi untuk menampilkan header
def tampilkan_header(window, title):
    header_label = tk.Label(window, text=title, font=("Arial", 16), bg="#003366", fg="white")
    header_label.pack(pady=10)
