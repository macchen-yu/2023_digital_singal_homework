import scipy.signal
import numpy as np
input=np.array([1,-1,0.5])
#轉移函數係數
B=[0,1,-1.2,1]
A=[1,-1.3,1.04,-0.222]
filteredSignal=scipy.signal.lfilter(B,A,input)
print(filteredSignal)