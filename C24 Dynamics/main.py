import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 10, 1000)
x0 = 1
x = t-1 + np.exp(-t)*(x0 + 1)

plt.plot(t,x)
plt.show()