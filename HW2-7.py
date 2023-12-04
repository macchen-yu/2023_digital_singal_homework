import numpy as np
import matplotlib.pyplot as plt

N = 250
f_1 = 3000
f_2 = 400
fs_1 = 10000
fs_2 = 5500

n = np.arange(N)
k = np.arange(N)  

def calculate_magXk(f_1, f_2, fs):
    omega_sin = 2 * np.pi * f_1 / fs
    omega_cos = 2 * np.pi * f_2 / fs

    xn = 2 * np.sin(omega_sin * n) + np.cos(omega_cos * n)

    Xk = np.fft.fft(xn, N)
    magXk = 20 * np.log10(np.abs(Xk))
    return (magXk)


plt.plot(k, calculate_magXk(f_1, f_2, fs_1))  
plt.axis([0, N/2, -300, 50])

plt.xlabel('Frequency Index (k)')
plt.ylabel('Magnitude (dB)')
plt.title('DFT Magnitude Spectrum')
plt.grid(True)

plt.figure()  
plt.plot(k, calculate_magXk(f_1, f_2, fs_2))  
plt.axis([0, N/2, 0, 50])

plt.xlabel('Frequency Index (k)')
plt.ylabel('Magnitude (dB)')
plt.title('DFT Magnitude Spectrum')
plt.grid(True)

plt.show()  
