import matplotlib.pyplot as plt
import numpy as fft
import numpy as np
from scipy.fftpack import fft
noise_size = 1400
noise_array =  np.random.normal(0, 2, noise_size)
    
        
adc_value=[]
    
for i in range(noise_size):
        
    adc_value.append(0)
  
y= np.array(adc_value) + noise_array

yy=fft(y)                     #快速傅里叶变换
yf=abs(fft(y))                # 取模
yf1=abs(fft(y))/((len(y)/2))           #归一化处理
yf2 = yf1[range(int(len(y)/2))]  #由于对称性，只取一半区间
#混合波的FFT（双边频率范围）
xf = np.arange(len(y)) 
plt.figure(1)
plt.plot(xf,yf,'r') #显示原始信号的FFT模值
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表

yy=fft(y)                     #快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分
test_y =yy
for i in range(len(yy)):
    if i <=1200 and i>=200:
        test_y[i]=0
test = np.fft.ifft(test_y)  #对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
y=test
yy=fft(y)                     #快速傅里叶变换
yf=abs(fft(y))                # 取模
yf1=abs(fft(y))/((len(y)/2))           #归一化处理
yf2 = yf1[range(int(len(y)/2))]  #由于对称性，只取一半区间
#混合波的FFT（双边频率范围）
xf = np.arange(len(y)) 
plt.figure(2)
plt.plot(xf,yf,'r') #显示原始信号的FFT模值
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表
