import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
def plot(fs):
    xt= 2*np.sin( 2 * np.pi * f1 /fs * t) + np.cos( 2 * np.pi * f2 /fs * t )
    yt=scipy.signal.upfirdn(bl,xt,U,D)
    plt.plot(t[0:100],xt[0:100],'b',label="x(n)")
    plt.plot(t[0:100],yt[0:100],'r',label="x(n)prime")
    plt.title("Original")
    plt.ylabel("Magnitude")
    plt.xlim(0, 100)
    plt.ylim(-3, 4)
    plt.legend()
    plt.show()
def plot2(fs):
    xt= 2*np.sin( 2 * np.pi * f1 /fs * t) + np.cos( 2 * np.pi * f2 /fs * t )
    xt1=scipy.signal.decimate(xt,D)
    yt=scipy.signal.resample(xt1,U*1000)
    plt.plot(t[0:100],xt[0:100],'b',label="x(n)")
    plt.plot(t[0:100],yt[20:120],'r',label="x(n)prime")
    plt.title("Original")
    plt.ylabel("Magnitude")
    plt.xlim(0, 100)
    plt.ylim(-3, 4)
    plt.legend()
    plt.show()
t = np.linspace(0, 4999,5000)
f1,f2=500,2000
fs1,fs2,fs3=8000,10000,10000
U,D=4,5
N=24*D
bl = scipy.signal.firwin(N,1/D,window=('kaiser',N+1))
bl=U*bl
plot(fs1)
plot(fs2)
plot2(fs3)