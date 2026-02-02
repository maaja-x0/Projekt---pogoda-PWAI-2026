import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/dane.csv", delimiter=',', dtype=str, encoding="cp1250")

s1_id = '253170210'
s2_id = '249190090'

s1 = data[data[:,0] == s1_id]
s2 = data[data[:,0] == s2_id]

dates_s1 = {(r,m,d): temp for r,m,d,temp in s1[:,2:6]}
dates_s2 = {(r,m,d): temp for r,m,d,temp in s2[:,2:6]}

common_dates = sorted(set(dates_s1.keys()) & set(dates_s2.keys()))

diff = np.array([
    float(dates_s1[d]) - float(dates_s2[d])
    for d in common_dates
])

x = np.arange(len(diff))

plt.figure(figsize=(12,5))
plt.plot(x, diff)
plt.title("Różnica średnich temperatur: s1(t) − s2(t)")
plt.xlabel("Dzień")
plt.ylabel("Różnica temperatur [°C]")
plt.grid(True)
plt.show()

idx_max_diff = np.argmax(np.abs(diff))
print("Największa różnica temperatur:")
print(f"{diff[idx_max_diff]:.2f} °C, data: {common_dates[idx_max_diff]}")
