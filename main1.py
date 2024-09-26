import os
from file_array import baca_file_array
from file_dict import baca_file_dict

def pilih_format_dan_baca(file):
    # Memilih format dan membaca file
    print("Pilih format file yang akan dibaca:")
    print("1. Array")
    print("2. Dictionary")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        # Membaca file sebagai array
        return baca_file_array(file)
    elif pilihan == '2':
        # Membaca file sebagai dictionary
        return baca_file_dict(file)
    else:
        print("Pilihan tidak valid.")
        return None

def main():
    while True:
        filename = input("Masukkan nama file yang akan dibaca (dengan ekstensi): ")

        if not os.path.exists(filename):
            print(f"File '{filename}' tidak ditemukan. Silakan masukkan nama file yang benar.")
            continue

        # Jika file ditemukan, tentukan format dan baca file
        result = pilih_format_dan_baca(filename)

        if result:
            print("Isi file yang dibaca:")
            print(result)
            break

if __name__ == "__main__":
    main()
