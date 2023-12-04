import numpy as np
from scipy import signal
b = np.array([ 1,3.3,-71.1,22,630])
a = np.array([1, 5,-5,-28,30])
z, p, k = signal.tf2zpk(b, a)
print(z)
print(p)
print(k)