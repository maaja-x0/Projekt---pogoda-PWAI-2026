import csv
import numpy as np

rows = []

with open("data/dane.csv", encoding="cp1250") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] != '' and row[7] != '':
            rows.append(row)

data_clean = np.array(rows, dtype=object)

tmax = data_clean[:,5].astype(float)
tmin = data_clean[:,7].astype(float)

idx_min = np.argmin(tmin)
idx_max = np.argmax(tmax)

min_info = data_clean[idx_min]
max_info = data_clean[idx_max]

print("Najniższa temperatura minimalna:")
print(f"{tmin[idx_min]} °C, data: {min_info[4]}-{min_info[3]}-{min_info[2]}, "
      f"stacja: {min_info[1]} ({min_info[0]})")

print("\nNajwyższa temperatura maksymalna:")
print(f"{tmax[idx_max]} °C, data: {max_info[4]}-{max_info[3]}-{max_info[2]}, "
      f"stacja: {max_info[1]} ({max_info[0]})")
