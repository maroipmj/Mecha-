def baca_file_array(file):

    with open(file, mode='r', encoding='utf-8') as f:
        content = f.read().strip()

        # Jika file CSV dengan pemisah koma
        if ',' in content:
            return content.split(',')
        # Jika file TXT dengan satu elemen per baris
        else:
            return content.splitlines()