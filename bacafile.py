import csv

def baca_csv(filename):
    # Mencoba membaca file sebagai Dictionary (List of Dictionaries)
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            dict_data = [row for row in csv_reader]
            
            # Jika header ada dan semua baris berbentuk dictionary
            if dict_data and all(isinstance(row, dict) for row in dict_data):
                print("File dibaca sebagai dictionary (List of Dictionaries):")
                return dict_data
    except Exception as e:
        print(f"Error saat membaca sebagai dictionary: {e}")
    
    # Jika gagal sebagai dictionary, mencoba membaca sebagai Array (List of Lists)
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            array_data = [row for row in csv_reader]
            
            # Jika berhasil membaca baris
            if array_data:
                print("File dibaca sebagai array (List of Lists):")
                return array_data
    except Exception as e:
        print(f"Error saat membaca sebagai array: {e}")
    
    # Jika tidak dapat membaca dalam format apapun
    print("Tidak dapat membaca file dalam format array atau dictionary.")
    return None

# Contoh penggunaan
filename = 'data.csv'
data_baca = baca_csv(filename)

# Menampilkan data yang terbaca
if data_baca:
    for row in data_baca:
        print(row)
