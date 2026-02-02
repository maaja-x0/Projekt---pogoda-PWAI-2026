import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/dane.csv", delimiter=',', dtype=str, encoding="cp1250")

data.shape
print(data.shape[0])

id_stacji = data[:,0]
id_stacji = np.unique(id_stacji)
id_stacji.shape[0]

daty = data[:,2:5]
daty = np.unique(daty, axis = 0)
full_dates_number = daty.shape[0]
print(full_dates_number)

stacje_z_data = data[:,0:5]
stacje_z_data = np.unique(stacje_z_data, axis = 0)

id_pomiary_dict = {id : stacje_z_data[stacje_z_data[:,0] == id].shape[0] for id in id_stacji}

list(id_pomiary_dict.items())

id_pomiary = np.array(list(id_pomiary_dict.items()))
pelna_historia = id_pomiary[id_pomiary[:,1] == '8400']
pelna_historia.shape[0]

stacja_z_pelna_historia = '253170210'
dane_stacji_z_pelna_historia = stacje_z_data[stacje_z_data[:,0]==stacja_z_pelna_historia]

rok_miesiac = np.unique(dane_stacji_z_pelna_historia[:,2:4], axis = 0)
rok_miesiac

wybrana_stacja = '254180060'

dane_wybranej_stacji = stacje_z_data[stacje_z_data[:,0]==wybrana_stacja]

liczba_pomiarow = {
    (rok, miesiac) : dane_wybranej_stacji[(dane_wybranej_stacji[:,2] == rok) &
    (dane_wybranej_stacji[:,3] == miesiac)].shape[0]
    for (rok, miesiac) in rok_miesiac
    }
liczba_pomiarow

y = list(liczba_pomiarow.values())
x = list(range(len(y)))

etykiety = [f"{rok}-{miesiac}" for (rok, miesiac) in liczba_pomiarow.keys()]

plt.title('Pomiary Wybranej Stacji W Danym Miesiącu')
plt.xlabel('Miesiąc i Rok')
plt.ylabel('Liczba pomiarów')
plt.bar(x, y)
krok = 48
plt.xticks(x[::krok], etykiety[::krok])
# plt.xticks(x, list(liczba_pomiarow.keys()))
plt.show()