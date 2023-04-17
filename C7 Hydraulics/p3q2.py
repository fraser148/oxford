import numpy as np
import matplotlib.pyplot as plt

n = 1.5
phi_0 = 0.25

z_wt1 = -3
z_wt2 = -4
z_wt3 = -5

z = np.linspace(0, -8, 1000)
S_1 =  np.power((1 + np.power(((z-z_wt1)/phi_0), n)), (1-n)/n)
S_2 =  np.power((1 + np.power(((z-z_wt2)/phi_0), n)), (1-n)/n)
S_3 =  np.power((1 + np.power(((z-z_wt3)/phi_0), n)), (1-n)/n)

plt.plot(S_1, z, label="z_wt=-3m")
plt.plot(S_2, z, label="z_wt=-4m")
plt.plot(S_3, z, label="z_wt=-5m")
plt.legend()
plt.title("Van Genuchten")
plt.xlabel("Saturation")
plt.ylabel("z[m]")
plt.show()