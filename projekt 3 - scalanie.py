out = open('data/dane.csv', 'w', encoding='cp1250')

for year in range(2001, 2024):
    for month in ['01','02','03','04','05','06',
                  '07','08','09','10','11','12']:

        file_path = f'data/unpacked/k_d_{month}_{year}.csv'
        file = open(file_path, 'r', encoding='cp1250')

        for line in file:
            out.write(line.replace('"', ''))

        file.close()
        print(f"{file_path} read.")

out.close()