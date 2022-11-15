import numpy as np

def get_k(w, d):
  g = 9.81
  k = np.linspace(0, 0.1, 10000)
  solid = np.full(len(k), w)
  w = np.sqrt(k*g*np.tanh(k*d))

  best_index = 0
  best_diff = 1000

  for i in range(0, len(k)):
    diff = np.abs(solid[i] - w[i])
    if diff < best_diff and w[i] != 0:
      best_index = i
      best_diff = diff

  return k[best_index]

H2 = 2.8
g = 9.81
lambda_2 = 71
d = 10


c_g = np.sqrt(g*d)

k2 = np.pi*2/lambda_2
w = np.sqrt(k2*g*np.tanh(k2*d))
c_p2 = np.sqrt(g/k2*np.tanh(k2*d))
c_g2 = c_p2*0.5*(1+(2*k2*d)/(np.sinh(2*k2*d)))
c_g1 = 1/2*g/w
H1 = H2*np.sqrt(c_g2/c_g1)

lambda_1 = 2*np.pi*g/w**2
T = 2*np.pi/w
u_max = H2/2*g*k2/w*np.cosh(0)/np.cosh(k2*d)

print("Q2. a) i)")
print("H1 is {}".format(H1))
print("Lambda 1 is {}".format(lambda_1))
print("Q2. a) ii)")
print("T is {}".format(T))
print("Q2. a) iii)")
print("cg @ 10m is {:.5f}m/s".format(c_g2))
print("cp @ 10m is {:.5f}m/s".format(w/k2))
print("u_max @ 10m is {:.5f}m".format(u_max))

print("Q2. b)")
print("k @ fair is {}".format(w**2/g))
print("k @ 12m is {}".format(get_k(w, 12)))

k12 = get_k(w, 12)
d12 = 12

c_g12 = 1/2/k12*w*(1+2*k12*d12/np.sinh(2*k12*d12))
print("c_g @ 12m is {:.5f}m/s".format(c_g12))

k1 = w**2/g
print(k1)
theta1 = np.pi/4
theta2 = np.arcsin(k1*np.sin(theta1)/k12)
print("Theta @ far is {:.5f}deg".format(theta2/(2*np.pi)*360))

H12 = H1*np.sqrt(c_g1*np.cos(theta1)/c_g12/np.cos(theta2))
print("H @ 12m is {:.5f}".format(H12))

rho = 1030
E = 1/8*rho*g*H12**2
print("Energy per unit length {:.5f}".format(E))

u_max_12 = H12/2*g*k12/w/np.cosh(k12*12)
print("U_max @ 12m {:.5f}".format(u_max_12))