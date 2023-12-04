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

L=61
l = np.linspace(0, 60,61) 
b = 0.4*np.sinc(0.4*(l-30))
a = np.array([1.0])

gain = [1,  1,0,  0]
freq = [0,0.4,0.5,1]

y1 = scipy.signal.firwin(L , cutoff=0.4)
y2 = scipy.signal.firwin2(L,freq = freq,gain = gain)

y1n = scipy.signal.lfilter(y1,a,xn)
y2n = scipy.signal.lfilter(y2, a, xn)


plt.figure(figsize=(8, 3))
plt.subplot(2, 1, 1)
plt.plot(xn,color='b', label='xn')
plt.plot(y1n,color='r', label='yfir1')
plt.plot(sn,color='y', label='sn')
plt.xlim(0, 100)
plt.ylim(-2, 2)
plt.gca().xaxis.set_major_locator(MultipleLocator(10))
plt.gca().yaxis.set_major_locator(MultipleLocator(2))
plt.title('Fir1')
plt.ylabel('Magnitude')
plt.legend(loc='upper right')

plt.subplot(2, 1, 2)
plt.plot(xn,color='b', label='xn')
plt.plot(y2n,color='r', label='yfir2')
plt.plot(sn,color='y', label='sn')
plt.xlim(0, 100)
plt.ylim(-2, 2)
plt.gca().xaxis.set_major_locator(MultipleLocator(10))
plt.gca().yaxis.set_major_locator(MultipleLocator(2))
plt.title('Fir2')
plt.ylabel('Magnitude')
plt.ylabel('100sample')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()