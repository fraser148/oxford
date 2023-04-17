import numpy as np

g = 9.81

# T = np.array((3,30))

# lambda_1 = g/2/np.pi*T**2
# print(lambda_1)

# cp = lambda_1/T
# print(cp)

T = 15
lambda_1 = g/2/np.pi*T**2
print(lambda_1)

w = np.sqrt(2*np.pi*g/lambda_1)
print(w)

print(w**2/g)

print(2*np.tanh(0.052*31)/0.052)

a = 280
d = 10

print(np.sqrt(np.pi/a*g*np.tanh(np.pi/a*d)))