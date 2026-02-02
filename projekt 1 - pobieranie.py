import os
import time

os.makedirs("data/raw", exist_ok=True)

for year in range(2001, 2024):
    for month in ['01','02','03','04','05','06',
                  '07','08','09','10','11','12']:

        url = f"https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/klimat/{year}/{year}_{month}_k.zip"
        output = f"data/raw/{year}_{month}.zip"

        os.system(
            f'curl -L "{url}" -o "{output}"'
        )

        time.sleep(1)
