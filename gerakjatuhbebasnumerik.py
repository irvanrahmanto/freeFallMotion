# Gerak Jatuh Bebas Numerik

import pandas as pd
from matplotlib import pyplot as plt

# inisialisasi
g = -9.8
v0 = 0
y0 = 5

# timestap
dt = 0.2

# iterasi
t = 0
y = y0
v = v0
while y >= 0:
    t = t + dt
    v = v + (g*dt)
    y = y + (v*dt)
    # print("Hasil t : ", t)
    # print("Hasil y :", y)

    # Print plot didalem while + definisi warna nya
    plt.plot(t, y, 'ro')

# Show diluar iterasi / perulangan nya
plt.show()
