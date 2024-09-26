import csv

def baca_csv_sebagai_dict(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            dict_data = [row for row in csv_reader]
            
            # Jika header ada dan semua baris berbentuk dictionary
            if dict_data:
                print("File dibaca sebagai dictionary (List of Dictionaries):")
                return dict_data
    except Exception as e:
        print(f"Error saat membaca sebagai dictionary: {e}")
    
    # Jika tidak dapat membaca dalam format dictionary
    print("Tidak dapat membaca file sebagai dictionary.")
    return None

# Contoh penggunaan
filename = 'data.csv'
data_baca = baca_csv_sebagai_dict(filename)

# Menampilkan data yang terbaca
if data_baca:
    for row in data_baca:
        print(row)
