import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

x = np.arange (0, 3.14*2, 0.01)
print x

noise = np.random.uniform(-0.1, 0.1, len(x))
y = np.sin(x)
y_with_noise = y + noise


#numbers = [1,2,3, 10,5,1,-1,3, 0, 3]
smoothing_kernel = [0.0044318484119380075, 0.05399096651318806, 0.24197072451914337,
                   0.3989422804014327,
                   0.24197072451914337, 0.05399096651318806, 0.0044318484119380075]

#kernel = [1,2,1]


from math import pi, sqrt, exp

def gauss(n=11,sigma=1):
    r = range(-int(n/2),int(n/2)+1)
    return [1 / (sigma * sqrt(2*pi)) * exp(-float(x)**2/(2*sigma**2)) for x in r]

#print gauss(n=7)


def convolution(x, kernel):
    y = 0
    list_a = []
    for offset in range(len(x)-len(kernel)+1):
        for i in range(len(kernel)):
            y += x[i+offset]*kernel[i]
        list_a.append(y)
        y = 0
    return list_a

width = 17
y_smoothed = convolution(y_with_noise, gauss(n=width, sigma = 3))


plt.plot(x, y_with_noise, color = "r")
plt.plot(x[width/2:-width/2+1], y_smoothed, color = "b")
plt.show()