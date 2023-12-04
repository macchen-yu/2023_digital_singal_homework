import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from matplotlib.pyplot import MultipleLocator
# Create a simple signal
fs = 5000  
f1 =  500
f2 = 2000
t = np.linspace(0, 99,100)

xn = 2*np.sin( 2 * np.pi * f1 /fs * t) + np.cos( 2 * np.pi * f2 /fs * t )
sn = 2*np.sin(2*np.pi*f1*t/fs)

l = np.linspace(0, 60,61) 
b = 0.4*np.sinc(0.4*(l-30))
a = np.array([1.0])

w, gd = scipy.signal.group_delay((b, a))
yn = scipy.signal.lfilter(b,a,xn)
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
# plt.plot(t, xn,color='b', label='xn')
plt.plot(t, yn,color='r', label='yn')
# plt.plot(t, sn,color='y', label='sn')
plt.xlim(0, 100)
plt.ylim(-2, 2)
plt.gca().xaxis.set_major_locator(MultipleLocator(10))
plt.gca().yaxis.set_major_locator(MultipleLocator(2))
plt.title('Original')
plt.ylabel('Magnitude')
plt.legend(loc='upper right')
plt.show()