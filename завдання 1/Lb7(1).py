import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 4)
v = np.sin(10*x)
b = np.sin(3*x)/(x^2)
y = v*b

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()
