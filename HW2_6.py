import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

b = np.array([0.008, -0.033, 0.05, -0.033, 0.008])
a = np.array([1, 2.37, 2.7, 1.6, 0.41])
w, h = signal.freqz(b,a)

phase = np.unwrap(np.angle(h))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(w / 3.14, 10 * np.log10(abs(h)**2))
plt.title('Square Magnitude Spectrum')
plt.xlabel('Normalized Frequency [xπ rad/sample]')
plt.ylabel('Square Magnitude [dB]')
plt.margins(0, 0.1)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(w / 3.14, phase*57.3, 'g')
plt.title('Phase (degrees)')
plt.xlabel('Normalized Frequency [xπ rad/sample]')
plt.ylabel('Phase (radians)')
plt.grid()

plt.tight_layout()
plt.show()