def baca_file_dict(file):
    
    dict_data = {}
    
    with open(file, mode='r', encoding='utf-8') as f:
        content = f.read().strip()

        # Mengidentifikasi format
        if ',' in content:
            pairs = content.split(',')
            for pair in pairs:
                if '=>' in pair:
                    key, value = pair.split('=>')
                else:
                    key, value = pair.split(':')
                dict_data[key.strip()] = value.strip()
        # Jika format dengan titik koma (key:value)
        elif ';' in content:
            pairs = content.split(';')
            for pair in pairs:
                key, value = pair.split(':')
                dict_data[key.strip()] = value.strip()
        
    return dict_data

