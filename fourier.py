# Import libraries
# -----------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

if __name__ == '__main__':

    # Data to transform
    # -----------------
    t = np.linspace(0, 0.5, 500) # x-data
    s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t) # y-data
    
    # Plot
    # -----------------
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.plot(t, s)
    plt.show()
    
    # Fast Fourier Transform with numpy
    # -----------------
    
    fft = np.fft.fft(s)
    
    for i in range(2):
        print("Value at index {}:\t{}".format(i, fft[i + 1]), "\nValue at index {}:\t{}".format(fft.size -1 - i, fft[-1 - i]))
    
    fft = np.fft.fft(s)
    T = t[1] - t[0]  # sampling interval 
    N = s.size
    
    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    
    # Plot Fourier Transform
    # -----------------
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=1.5)  # 1 / N is a normalization factor
    plt.show()
