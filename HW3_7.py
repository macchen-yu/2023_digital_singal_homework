import scipy.io.wavfile as wav
from scipy import signal
import numpy as np

# 读取wav文件
fs, data = wav.read('./Mixture_Signal(HW3-7).wav')
data= data.astype(np.int16)
# 设置目标采样率
target_fs = 48000

# 上采样
data = signal.resample(data, int(len(data)*target_fs/fs))

# 带阻滤波器
b, a = signal.butter(3, 0.05)
filtered = signal.filtfilt(b,a, data)

# 下采样
filtered = signal.resample(filtered, int(len(filtered)*fs/target_fs))

# 转换类型和写入
filtered = filtered.astype(np.int16)
wav.write('output.wav', fs, filtered)

print(f'Original length: {len(data)/fs}s')
print(f'Filtered length: {len(filtered)/fs}s')