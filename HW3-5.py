import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from matplotlib.pyplot import MultipleLocator
from fxpmath import Fxp

# Create a simple signal
fs = 5000  
f1 =  500
f2 = 2000
t = np.linspace(0, 99,100)

xn = 2*np.sin( 2 * np.pi * f1 /fs * t) + np.cos( 2 * np.pi * f2 /fs * t )
xnq=Fxp(xn  , signed=True, n_word=16, n_frac=15)
sn = 2*np.sin(2*np.pi*f1*t/fs)

l = np.linspace(0, 60,61) 
b = 0.4*np.sinc(0.4*(l-30))
bl=Fxp(b , signed=True, n_word=16, n_frac=15)
a = np.array([1.0])

w, gd = scipy.signal.group_delay((b, a))
yn = scipy.signal.lfilter(b,a,xn)
ynq=scipy.signal.lfilter(bl,a,xnq)
ynq=Fxp(ynq , signed=True, n_word=16, n_frac=15)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, ynq,color='r', label='yn16n(16bits)')
plt.plot(t, yn,color='b', label='yn')
# plt.plot(t, sn,color='y', label='sn')
plt.xlim(0, 100)
plt.ylim(-2, 2)
plt.gca().xaxis.set_major_locator(MultipleLocator(20))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.5))
plt.title('Original')
plt.ylabel('Magnitude')
plt.legend(loc='upper right')
plt.show()