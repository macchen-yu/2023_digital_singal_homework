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

l = np.linspace(0, 60,61) 
b = 0.4*np.sinc(0.4*(l-30))
a = np.array([1.0])


hamming_values = 0.54 - 0.46 * np.cos((2 * np.pi * l) / (61 - 1))
yn = scipy.signal.lfilter(b,a,xn)
c= b*hamming_values
sn = scipy.signal.lfilter(c, a, xn)

#plt.figure(figsize=(10, 6))
#plt.subplot(2, 1, 1)
plt.plot(t, yn,color='b', label='yn')
plt.plot(t, sn,color='r',linestyle='--', label='yhamming(n)')
plt.xlim(0, 100)
plt.ylim(-2, 2)
plt.gca().xaxis.set_major_locator(MultipleLocator(10))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.5))
plt.title('Original')
plt.ylabel('Magnitude')
plt.legend(loc='upper right')
plt.show()