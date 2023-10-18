import numpy as np
import matplotlib.pyplot as plt
#length of signal
L = 50
#discrete time variable
n = np.arange(L)
#clean signal
sn = np.cos(2*np.pi*n/10)
#plot clean signal
plt.stem(sn)
plt.show()


#noise with sigma = 0.01
d = .01*np.random.rand(L)
#disturbed signal
xn = sn + d
#plot disturbed signal
plt.stem(xn)
plt.show()

#ratio variable
M = []
for i in range(10):
    M.append(1/(2*(i + 1) + 1))
    
def time_shifting(xn: np.array, time: int):
    if(time == 0):
        return xn
    elif(time > 0):
        x = np.zeros(xn.size)
        for i in range(L - time):
            x[i] = xn[i + time]
        return x
    else:
        x = np.zeros(xn.size)
        for i in range(L + time):
            x[i - time] = xn[i]
        return x
#signal after denoise with M
y = []
for i in range(1, 11):
    yn = np.zeros(L)
    for j in range(-i,i+1):
        yn += time_shifting(xn, j)
    y.append(yn)
def diff(yn: np.array, sn: np.array):
    return sum((yn - sn)**2)
SSE = []
for yn in y:
    SSE.append(diff(yn, sn))
plt.plot(SSE)
plt.show()