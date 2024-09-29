import os
from file_array import baca_file_array
from file_dict import baca_file_dict

def deteksi_format_dan_baca(file):
    # Membaca file dan mendeteksi formatnya (array atau dictionary)
    with open(file, mode='r', encoding='utf-8') as f:
        content = f.read().strip()

        # Deteksi apakah file berformat dictionary
        if '=>' in content or ':' in content:
            print("Format file terdeteksi sebagai Dictionary.")
            return baca_file_dict(file)
        # Jika tidak ada pemisah dictionary, dianggap format array
        elif ',' in content or '\n' in content:
            print("Format file terdeteksi sebagai Array.")
            return baca_file_array(file)
        else:
            print("Format file tidak dikenali.")
            return None

def main():
    while True:
        filename = input("Masukkan nama file yang akan dibaca (dengan ekstensi): ")

        if not os.path.exists(filename):
            print(f"File '{filename}' tidak ditemukan. Silakan masukkan nama file yang benar.")
            continue

        # Jika file ditemukan, deteksi format dan baca file
        result = deteksi_format_dan_baca(filename)

        if result:
            print("Isi file yang dibaca:")
            print(result)
            break

if __name__ == "__main__":
    main()
