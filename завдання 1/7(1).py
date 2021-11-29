import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 4)
y = np.sin(10*x) * np.sin(3*x) / (x^2)

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()
