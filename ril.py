def tampil_menu():
    print("\nData Ikan")
    print("1.   Tampil data")    
    print("2.   Tambah data")
    print("3.   Edit data")
    print("4.   Hapus data")
    print("5.   Keluar")
    pilih = input("Masukkan pilihan Anda: ")
    return pilih

def tampil_menu_tambah():
    print("\nTambah Data")
    print("1.   Tambah Ikan")    
    print("2.   Tambah Warna")
    print("3.   Tambah Jenis")
    print("4.   Kembali")
    pilih = input("Masukkan pilihan Anda: ")
    return pilih

def tampil_menu_edit():
    print("\nEdit Data")
    print("1.   Edit Ikan")    
    print("2.   Edit Warna")
    print("3.   Edit Jenis")
    print("4.   Kembali")
    pilih = input("Masukkan pilihan Anda: ")
    return pilih

def tampil_menu_hapus():
    print("\nHapus Data")
    print("1.   Hapus Data Ikan")    
    print("2.   Hapus Warna")
    print("3.   Hapus Jenis")
    print("4.   Kembali")
    pilih = input("Masukkan pilihan Anda: ")
    return pilih

def baca_data_ikan(file_name):
    """Fungsi untuk membaca file nama_ikan.txt dengan format 'id:nama,id_warna,id_jenis'."""
    data = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":", 1)
                if len(parts) != 2:
                    print(f"Baris salah di file {file_name}: {line}")
                    continue
                kode = parts[0]
                detail = parts[1].split(",")  
                if len(detail) != 3:
                    print(f"Baris salah di file {file_name}: {line}")
                    continue
                data[kode] = {"nama": detail[0], "id_warna": detail[1], "id_jenis": detail[2]}
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file {file_name}: {e}")
    return data

def baca_data_file(file_name):
    """Fungsi untuk membaca file warna/jenis dengan format 'id:nama'."""
    data = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":", 1)
                if len(parts) != 2:
                    print(f"Baris salah di file {file_name}: {line}")
                    continue
                data[parts[0]] = parts[1].strip()
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file {file_name}: {e}")
    return data

def simpan_data_ke_file(file_name, data_baru):
    """Fungsi untuk menambahkan data ke file."""
    try:
        with open(file_name, "a") as file:
            file.write(data_baru + "\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data ke file {file_name}: {e}")

def tampil_data(data_ikan, data_warna, data_jenis):
    """Fungsi untuk menampilkan data ikan lengkap."""
    print('\nData Ikan')
    print('--------------------------------------------------------------------------------')
    print('|    Kode Ikan   |    Nama Ikan   |   Warna Ikan   |   Jenis Ikan   |')
    print('--------------------------------------------------------------------------------')

    if len(data_ikan) == 0:
        print('             Tidak ada data                       ')
    else:
        for kode, detail in data_ikan.items():
            nama = detail["nama"]
            warna = data_warna.get(detail["id_warna"], "Tidak Diketahui")
            jenis = data_jenis.get(detail["id_jenis"], "Tidak Diketahui")
            print('|', kode.ljust(15), "|", 
                  nama.ljust(15), "|", 
                  warna.ljust(15), "|", 
                  jenis.ljust(15), "|")

    print('--------------------------------------------------------------------------------')
    input("Tekan enter untuk melanjutkan.")

def tambah_data(data_ikan, data_warna, data_jenis):
    """Fungsi untuk menambahkan data ikan baru."""
    print("\n--- Tambah Data Ikan Baru ---")

    # Tentukan kode ikan baru
    if len(data_ikan) == 0:
        kode_baru = "1"
    else:
        kode_baru = str(int(max(data_ikan.keys())) + 1)

    # Input nama ikan
    nama_baru = input("Masukkan nama ikan baru: ")

    # Pilih warna ikan dari daftar yang ada
    print("\nPilih warna ikan dari daftar yang ada:")
    for kode, warna in data_warna.items():
        print(f"{kode}: {warna}")
    kode_warna = input("Masukkan ID warna ikan yang dipilih: ")
    if kode_warna not in data_warna:
        print("ID warna tidak valid, kembali ke menu utama.")
        return

    # Pilih jenis ikan dari daftar yang ada
    print("\nPilih jenis ikan dari daftar yang ada:")
    for kode, jenis in data_jenis.items():
        print(f"{kode}: {jenis}")
    kode_jenis = input("Masukkan ID jenis ikan yang dipilih: ")
    if kode_jenis not in data_jenis:
        print("ID jenis tidak valid, kembali ke menu utama.")
        return

    # Simpan data ke file nama_ikan.txt
    simpan_data_ke_file("nama_ikan.txt", f"{kode_baru}:{nama_baru},{kode_warna},{kode_jenis}")

    # Tambahkan data ke dictionary agar langsung terlihat
    data_ikan[kode_baru] = {"nama": nama_baru, "id_warna": kode_warna, "id_jenis": kode_jenis}

    print(f"\nData ikan berhasil ditambahkan: {kode_baru}:{nama_baru}")
    print(f"Warna: {data_warna[kode_warna]}, Jenis: {data_jenis[kode_jenis]}")

    # Memuat ulang data ikan setelah ditambahkan
    print("\nMemuat ulang data ikan setelah penambahan...")
    tampil_data(data_ikan, data_warna, data_jenis)  # Menampilkan data terbaru

def edit_data_ikan(data_ikan, data_warna, data_jenis):
    """Fungsi untuk mengedit data ikan berdasarkan kode ikan."""
    print("\n--- Edit Data Ikan ---")
    
    # Pilih ikan yang ingin diedit
    print("\nDaftar Ikan: ")
    for kode, detail in data_ikan.items():
        print(f"{kode}: {detail['nama']}")
    
    kode_ikan = input("Masukkan kode ikan yang ingin diedit: ")
    if kode_ikan not in data_ikan:
        print("Kode ikan tidak ditemukan.")
        return
    
def edit_data_warna(data_warna):
    print("\n--- Edit Data Warna ---")
    print("\nDaftar Warna:")
    for kode, warna in data_warna.items():
        print(f"{kode}: {warna}")
    
    kode_warna = input("Masukkan kode warna yang ingin diedit: ")
    if kode_warna not in data_warna:
        print("Kode warna tidak ditemukan.")
        return

    warna_baru = input("Masukkan nama warna baru: ")
    data_warna[kode_warna] = warna_baru
    print(f"Warna dengan kode {kode_warna} berhasil diubah menjadi {warna_baru}.")
    update_file_warna(data_warna)

def edit_data_jenis(data_jenis):
    print("\n--- Edit Data Jenis ---")
    print("\nDaftar Jenis:")
    for kode, jenis in data_jenis.items():
        print(f"{kode}: {jenis}")
    
    kode_jenis = input("Masukkan kode jenis yang ingin diedit: ")
    if kode_jenis not in data_jenis:
        print("Kode jenis tidak ditemukan.")
        return

    jenis_baru = input("Masukkan nama jenis baru: ")
    data_jenis[kode_jenis] = jenis_baru
    print(f"Jenis dengan kode {kode_jenis} berhasil diubah menjadi {jenis_baru}.")
    update_file_jenis(data_jenis)


    # Pilih bagian mana yang akan diedit
    print("\nPilih data yang ingin diedit:")
    print("1. Nama Ikan")
    print("2. Warna Ikan")
    print("3. Jenis Ikan")
    pilih_edit = input("Masukkan pilihan Anda: ")

    if pilih_edit == "1":
        # Edit nama ikan
        nama_baru = input("Masukkan nama ikan yang baru: ")
        data_ikan[kode_ikan]["nama"] = nama_baru
        print(f"Nama ikan dengan kode {kode_ikan} berhasil diubah menjadi {nama_baru}.")
    elif pilih_edit == "2":
        # Edit warna ikan
        print("\nPilih warna ikan dari daftar yang ada:")
        for kode, warna in data_warna.items():
            print(f"{kode}: {warna}")
        kode_warna = input("Masukkan ID warna ikan yang dipilih: ")
        if kode_warna in data_warna:
            data_ikan[kode_ikan]["id_warna"] = kode_warna
            print(f"Warna ikan dengan kode {kode_ikan} berhasil diubah menjadi {data_warna[kode_warna]}.")
        else:
            print("ID warna tidak valid.")
    elif pilih_edit == "3":
        # Edit jenis ikan
        print("\nPilih jenis ikan dari daftar yang ada:")
        for kode, jenis in data_jenis.items():
            print(f"{kode}: {jenis}")
        kode_jenis = input("Masukkan ID jenis ikan yang dipilih: ")
        if kode_jenis in data_jenis:
            data_ikan[kode_ikan]["id_jenis"] = kode_jenis
            print(f"Jenis ikan dengan kode {kode_ikan} berhasil diubah menjadi {data_jenis[kode_jenis]}.")
        else:
            print("ID jenis tidak valid.")
    else:
        print("Pilihan tidak valid.")
        return

    # Memperbarui data di file
    update_file_ikan(data_ikan)

    # Menampilkan data setelah diedit
    print("\nData ikan setelah diedit:")
    tampil_data(data_ikan, data_warna, data_jenis)

def hapus_data_ikan(data_ikan):
    """Fungsi untuk menghapus data ikan berdasarkan kode ikan."""
    print("\n--- Hapus Data Ikan ---")
    
    # Pilih ikan yang ingin dihapus
    print("\nDaftar Ikan:")
    for kode, detail in data_ikan.items():
        print(f"{kode}: {detail['nama']}")

    kode_ikan = input("Masukkan kode ikan yang ingin dihapus: ")
    if kode_ikan not in data_ikan:
        print("Kode ikan tidak ditemukan.")
        return

    # Konfirmasi penghapusan
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus ikan {data_ikan[kode_ikan]['nama']}? (y/n): ")
    if konfirmasi.lower() != 'y':
        print("Penghapusan dibatalkan.")
        return

    # Hapus data ikan dari dictionary
    del data_ikan[kode_ikan]
    print(f"Data ikan dengan kode {kode_ikan} telah dihapus.")

    # Memperbarui data di file
    update_file_ikan(data_ikan)

    # Menampilkan data setelah dihapus
    print("\nData ikan setelah dihapus:") 
    tampil_data(data_ikan, data_warna, data_jenis)

def hapus_data_warna(data_warna):
    """Fungsi untuk menghapus data warna berdasarkan kode warna."""
    print("\n--- Hapus Data Warna ---")
    
    # Tampilkan daftar warna
    print("\nDaftar Warna:")
    for kode, warna in data_warna.items():
        print(f"{kode}: {warna}")

    # Meminta input kode warna
    kode_warna = input("Masukkan kode warna yang ingin dihapus: ")
    if kode_warna not in data_warna:
        print("Kode warna tidak ditemukan.")
        return

    # Konfirmasi penghapusan
    warna_terpilih = data_warna[kode_warna]
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus warna '{warna_terpilih}'? (y/n): ")
    if konfirmasi.lower() != 'y':
        print("Penghapusan dibatalkan.")
        return

    # Hapus data warna dari dictionary
    del data_warna[kode_warna]
    print(f"Data warna dengan kode '{kode_warna}' dan nama '{warna_terpilih}' telah dihapus.")

    # Memperbarui data di file
    update_file_warna(data_warna)



def hapus_data_jenis(data_jenis):
    """Fungsi untuk menghapus data jenis berdasarkan kode jenis."""
    print("\n--- Hapus Data Jenis ---")
    
    # Pilih jenis yang ingin dihapus
    print("\nDaftar Jenis:")
    for kode, jenis in data_jenis.items():
        print(f"{kode}: {jenis}")

    kode_jenis = input("Masukkan kode jenis yang ingin dihapus: ")
    if kode_jenis not in data_jenis:
        print("Kode jenis tidak ditemukan.")
        return

    # Konfirmasi penghapusan
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus jenis {data_jenis[kode_jenis]}? (y/n): ")
    if konfirmasi.lower() != 'y':
        print("Penghapusan dibatalkan.")
        return

    # Hapus data jenis dari dictionary
    del data_jenis[kode_jenis]
    print(f"Data jenis dengan kode {kode_jenis} telah dihapus.")

    # Memperbarui data di file
    update_file_jenis(data_jenis)

def update_file_warna(data_warna):
    """Memperbarui file nama_warna.txt setelah perubahan data warna."""
    try:
        with open("nama_warna.txt", "w") as file:
            for kode, warna in data_warna.items():
                file.write(f"{kode}:{warna}\n")
        print("File warna berhasil diperbarui.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memperbarui file warna: {e}")

def update_file_jenis(data_jenis):
    """Memperbarui file nama_jenis.txt setelah perubahan data jenis."""
    try:
        with open("nama_jenis.txt", "w") as file:
            for kode, jenis in data_jenis.items():
                file.write(f"{kode}:{jenis}\n")
        print("File jenis berhasil diperbarui.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memperbarui file jenis: {e}")


# Main Program
while True:
    print("\nMembaca data dari file...")
    data_ikan = baca_data_ikan("nama_ikan.txt")
    data_warna = baca_data_file("nama_warna.txt")
    data_jenis = baca_data_file("nama_jenis.txt")

    pilih = tampil_menu()

    match pilih:
        case "1":
            tampil_data(data_ikan, data_warna, data_jenis)
        case "2":
            while True:
                pilih_tambah = tampil_menu_tambah()
                match pilih_tambah:
                    case "1":
                        tambah_data(data_ikan, data_warna, data_jenis)
                    case "2":
                        tambah_warna(data_warna)
                    case "3":
                        tambah_jenis(data_jenis)
                    case "4":
                        break
                    case _:
                        print("Pilihan tidak valid.")
        case "3":
            while True:
                pilih_edit = tampil_menu_edit()
                match pilih_edit:
                    case "1":
                        edit_data_ikan(data_ikan, data_warna, data_jenis)
                    case "2":
                        edit_data_warna(data_warna)
                        pass
                    case "3":
                        edit_data_jenis(data_jenis)
                        pass
                    case "4":
                        break
                    case _:
                        print("Pilihan tidak valid.")
        case "4":
            while True:
                pilih_hapus = tampil_menu_hapus()
                match pilih_hapus:
                    case "1":
                        hapus_data_ikan(data_ikan)
                    case "2":
                        hapus_data_warna(data_warna)
                        pass
                    case "3":
                        hapus_data_jenis(data_jenis)
                        pass
                    case "4":
                        break
                    case _:
                        print("Pilihan tidak valid.")
        case "5":
            print("Keluar dari program.")
            break
        case _:
            print("Pilihan tidak valid, coba lagi.")
            