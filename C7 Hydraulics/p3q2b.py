import numpy as np
import matplotlib.pyplot as plt

n = 1.5
phi_0 = 0.25

z_wt = np.linspace(0, -100, 1000)
S_1 =  np.power((1 + np.power(((-z_wt)/phi_0), n)), (1-n)/n)

plt.plot(S_1, z_wt)
plt.legend()
plt.title("Van Genuchten")
plt.xlabel("Saturation")
plt.ylabel("z[m]")
plt.show()