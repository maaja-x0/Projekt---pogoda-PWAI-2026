import os

os.makedirs("data/unpacked", exist_ok=True)

for year in range(2001, 2024):
    for month in ['01','02','03','04','05','06',
                  '07','08','09','10','11','12']:

        zip_path = f"data/raw/{year}_{month}.zip"
        out_dir = "data/unpacked"

        os.system(
            f'unzip -o "{zip_path}" -d "{out_dir}"'
        )
