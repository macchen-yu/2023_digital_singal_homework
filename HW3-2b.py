import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

pi=3.14
w = np.arange(0, 6.28, 0.1)    

# 計算頻率響應
X_w =  np.exp(-3j * w)*(6-6*np.cos(w)+4*np.cos(2*w)-2*np.cos(3*w))
H_w=  np.exp(-4j * w) 
Y_w=X_w*H_w
# 計算幅值響應
x_mag = np.abs(X_w)
H_mag=np.abs(H_w)
Y_mag=np.abs(Y_w)
# 計算相位響應
x_phase = np.angle(X_w)
H_phase = np.angle(H_w)
y_phase=np.angle(Y_w)
# y_phase=pi-y_phase
# 繪製幅值響應圖
plt.subplot(2,1,1)
plt.title('magnitude Spectrum')
plt.plot(w/pi, x_mag,linestyle='--', color='b')
plt.plot(w/pi, H_mag,linestyle='--', color='r')
plt.plot(w/pi, Y_mag,linestyle='-.', color='y',alpha=0.6)
plt.ylim(0,20)
plt.xlim(0,2)
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(2.5))

plt.xlabel('w/π')
plt.ylabel('Magnitude')
plt.legend(['X(ejw)','H2(ejw)',"Y2(ejw)"])

# 繪製相位響應圖
plt.subplot(2,1,2) 
plt.title('phase Spectrum')
plt.plot(w/pi, x_phase,linestyle='--', color='b')
plt.plot(w/pi, H_phase,linestyle='--', color='r')
plt.plot(w/pi, y_phase,linestyle='-.', color='y',alpha=0.6)
plt.xlim(0,2)
plt.ylim(-4,4)

plt.xlabel('w/π')
plt.ylabel('x_phase (rad)')
plt.legend(['X(ejw)','H2(ejw)',"Y2(ejw)"])

plt.tight_layout()
plt.show()