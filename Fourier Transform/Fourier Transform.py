# import the usual libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftfreq # Fourier transform package 

# create a time signal with frequency 0.01 in the range [0,5)
dt = 0.01
time = np.arange(0,5.,dt)

### calculate wave with frequency f_1 and amplitude a_1, changeable values
f_1 = 1.
a_1 = 1.
y = a_1*np.sin(2.*np.pi*time*f_1)

# plot wave as funtion of time
plt.plot(time,y)
plt.xlabel("Time t [s]")
plt.ylabel("Amplitude")
plt.title("Wave Signal")
plt.show()

# calculate the fourier transform -- spectral amplitude over frequencies
n = time.shape[-1]
transform = (fft(y)[:n/2]) * 2./n
frequency = fftfreq(n,time[1]-time[0])[:n/2]
## n is the amount of time data points
## transform is the normalized fourier transform in the positive frequency range - [:n/2]
## frequency is the positive frequency range based on the given time data

# plot the fourier transform
plt.plot(frequency,np.abs(transform))
plt.xlabel("Frequency f [Hz]")
plt.ylabel("Amplitude")
plt.title("Fourier Transform")