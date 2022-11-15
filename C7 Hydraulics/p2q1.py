import numpy as np
import matplotlib.pyplot as plt

w = 0.4
d = 40
g = 9.81

k_estimate = w**2/g*(1/np.tanh((w*np.sqrt(d/g))**(3/2)))**(2/3)

RHS = w**2
LHS = k_estimate*g*np.tanh(k_estimate*d)

print("{} = {}".format(RHS, LHS))

k = np.linspace(0, 0.1, 10000)
w = np.sqrt(k*g*np.tanh(k*d))

solid = np.full(len(k), 0.4)

best_index = 0
best_diff = 1000

for i in range(0, len(k)):
  diff = np.abs(solid[i] - w[i])
  if diff < best_diff and w[i] != 0:
    best_index = i
    best_diff = diff
    error = diff/w[i]*100

error = (k[best_index]-k_estimate)/k[best_index]

print("Estimate for k is: {:.5f}".format(k_estimate))
print("Best k is: {:.5f}".format(k[best_index]))
print("Error: {:.3f}%".format(error))

plt.plot(k, w)
plt.plot(k, solid)
plt.text(k[best_index], w[best_index], "Best point")
plt.show()