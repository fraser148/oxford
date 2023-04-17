import matplotlib.pyplot as plt

x1 = [1,2,-3]
y1 = [2, -4, -1]

x2 = [2,-1,5]
y2 = [4,-5,0]

plt.scatter(x1, y1, c='r', label="S1")
plt.scatter(x2, y2, c='g', label="S2")
plt.legend()
plt.grid()
plt.show()