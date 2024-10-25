import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Parameter batas integral dan langkah interval
x_start = 0
x_stop = 3.14  # Batas atas adalah pi
x_steps_interval = 0.01

# Membuat array data x dan menghitung nilai f(x)
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = x_values**2 * np.cos(x_values) + 3 * np.sin(2 * x_values)

# Plot kurva fungsi
plt.plot(x_values, y_values, label=r'$x^2 \cos(x) + 3 \sin(2x)$', color='purple')

# Isi area di bawah kurva sebagai hasil integral
plt.fill_between(x_values, y_values, color='pink', alpha=0.8)

# Mendefinisikan fungsi lambda untuk integrasi
integration_function = lambda x: x**2 * np.cos(x) + 3 * np.sin(2 * x)

# Menghitung integral menggunakan quad() (tanpa menampilkan error)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

# Menampilkan hasil integrasi
print("Nilai Integral:", integral)

# Menambahkan label dan judul pada grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik Fungsi $x^2 \cos(x) + 3 \sin(2x)$ dan area di bawah kurva')
plt.legend()

# Menampilkan grafik
plt.show()
