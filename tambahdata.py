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
        print(f"Data berhasil ditambahkan ke {file_name}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data ke file {file_name}: {e}")

def tambah_data_ikan(data_ikan, data_warna, data_jenis):
    """Fungsi untuk menambahkan data ikan baru."""
    print("\n--- Tambah Data Ikan Baru ---")

    # Tentukan kode ikan baru
    if len(data_ikan) == 0:
        kode_baru = "1"
    else:
        kode_baru = str(int(max(data_ikan.keys())) + 1)

    # Input nama ikan
    while True:
        nama_baru = input("Masukkan nama ikan baru: ").strip()
        if nama_baru:
            break
        print("Nama ikan tidak boleh kosong.")

    # Pilih warna ikan dari daftar yang ada
    while True:
        print("\nPilih warna ikan dari daftar yang ada:")
        for kode, warna in data_warna.items():
            print(f"{kode}: {warna}")
        kode_warna = input("Masukkan ID warna ikan yang dipilih: ").strip()
        if kode_warna in data_warna:
            break
        print("ID warna tidak valid. Silakan coba lagi.")

    # Pilih jenis ikan dari daftar yang ada
    while True:
        print("\nPilih jenis ikan dari daftar yang ada:")
        for kode, jenis in data_jenis.items():
            print(f"{kode}: {jenis}")
        kode_jenis = input("Masukkan ID jenis ikan yang dipilih: ").strip()
        if kode_jenis in data_jenis:
            break
        print("ID jenis tidak valid. Silakan coba lagi.")

    # Konfirmasi penambahan data
    print("\nKonfirmasi Data Baru:")
    print(f"Kode Ikan: {kode_baru}")
    print(f"Nama Ikan: {nama_baru}")
    print(f"Warna Ikan: {data_warna[kode_warna]}")
    print(f"Jenis Ikan: {data_jenis[kode_jenis]}")
    konfirmasi = input("Apakah data sudah benar? (y/n): ")
    
    if konfirmasi.lower() != 'y':
        print("Penambahan data dibatalkan.")
        return None

    # Simpan data ke file nama_ikan.txt
    data_untuk_disimpan = f"{kode_baru}:{nama_baru},{kode_warna},{kode_jenis}"
    simpan_data_ke_file("nama_ikan.txt", data_untuk_disimpan)

    # Tambahkan data ke dictionary
    data_ikan[kode_baru] = {
        "nama": nama_baru, 
        "id_warna": kode_warna, 
        "id_jenis": kode_jenis
    }

    print(f"\nData ikan berhasil ditambahkan: {kode_baru}:{nama_baru}")
    return data_ikan

def tambah_warna(data_warna):
    """Fungsi untuk menambahkan data warna baru."""
    print("\n--- Tambah Warna Baru ---")

    # Tentukan kode warna baru
    if len(data_warna) == 0:
        kode_baru = "1"
    else:
        kode_baru = str(int(max(data_warna.keys(), key=int)) + 1)

    # Input nama warna baru
    while True:
        warna_baru = input("Masukkan nama warna baru: ").strip()
        if warna_baru:
            break
        print("Nama warna tidak boleh kosong.")

    # Konfirmasi penambahan data
    print("\nKonfirmasi Data Baru:")
    print(f"Kode Warna: {kode_baru}")
    print(f"Nama Warna: {warna_baru}")
    konfirmasi = input("Apakah data sudah benar? (y/n): ")
    
    if konfirmasi.lower() != 'y':
        print("Penambahan data dibatalkan.")
        return None

    # Simpan data ke file nama_warna.txt
    simpan_data_ke_file("nama_warna.txt", f"{kode_baru}:{warna_baru}")

    # Tambahkan data ke dictionary
    data_warna[kode_baru] = warna_baru
    print(f"\nData warna berhasil ditambahkan: {kode_baru}:{warna_baru}")
    return data_warna

def tambah_jenis(data_jenis):
    """Fungsi untuk menambahkan data jenis baru."""
    print("\n--- Tambah Jenis Baru ---")

    # Tentukan kode jenis baru
    if len(data_jenis) == 0:
        kode_baru = "1"
    else:
        kode_baru = str(int(max(data_jenis.keys(), key=int)) + 1)

    # Input nama jenis baru
    while True:
        jenis_baru = input("Masukkan nama jenis baru: ").strip()
        if jenis_baru:
            break
        print("Nama jenis tidak boleh kosong.")

    # Konfirmasi penambahan data
    print("\nKonfirmasi Data Baru:")
    print(f"Kode Jenis: {kode_baru}")
    print(f"Nama Jenis: {jenis_baru}")
    konfirmasi = input("Apakah data sudah benar? (y/n): ")
    
    if konfirmasi.lower() != 'y':
        print("Penambahan data dibatalkan.")
        return None

    # Simpan data ke file nama_jenis.txt
    simpan_data_ke_file("nama_jenis.txt", f"{kode_baru}:{jenis_baru}")

    # Tambahkan data ke dictionary
    data_jenis[kode_baru] = jenis_baru
    print(f"\nData jenis berhasil ditambahkan: {kode_baru}:{jenis_baru}")
    return data_jenis

# Contoh cara menggunakan fungsi-fungsi di atas
if __name__ == "__main__":
    # Baca data awal
    data_ikan = baca_data_ikan("nama_ikan.txt")
    data_warna = baca_data_file("nama_warna.txt")
    data_jenis = baca_data_file("nama_jenis.txt")

    # Contoh penggunaan fungsi tambah data
    tambah_data_ikan(data_ikan, data_warna, data_jenis)
    tambah_warna(data_warna)
    tambah_jenis(data_jenis)
