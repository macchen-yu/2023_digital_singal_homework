import scipy.signal
import numpy as np
input=np.array([-1,2,-3,6,-3,2,-1])
#轉移函數係數

#H1(z)=1
B1=[1.0]
A1=[1.0]
#H2(z)=z^-4
B2=[0,0,0,0,1.0]
A2=[1.0]
#H3(z)=(0.4-z^-1)/(1-0.4*z^-1)
B3=[0.4,-1.0]
A3=[1.0,-0.4]
filteredSignal1=scipy.signal.lfilter(            B1,A1,input)
filteredSignal2=scipy.signal.lfilter(B2,A2,input)
filteredSignal3=scipy.signal.lfilter(B3,A3,input)

print("X(n):",input)
print("y1(n):",filteredSignal1)
print("y2(n):",filteredSignal2)
print("y3(n):",filteredSignal3)