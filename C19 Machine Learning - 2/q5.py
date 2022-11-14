import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform

class mixed_gaussian():
  def __init__(self, pi, mu, s):
    self.pi = pi
    self.mu = mu
    self.s = s

  def eval(self, x):
    p = 0
    for i in range(0, len(self.s)):
      p += self.pi[i] * norm.pdf(x, self.mu[i], self.s[i])

    return p

  def plot(self, x):
    p = np.zeros(len(x))
    for i in range(0, len(self.s)):
      p += self.pi[i]*norm.pdf(x, self.mu[i], self.s[i])

    return p
    

def fp(pi, mu, s, x):
  p = 0
  for i in range(0, len(s)):
    p += pi[i] * norm.pdf(x, mu[i], s[i])
  
  return p

def q5a(gaus: mixed_gaussian, n, k):
  samples = []
  # Very Slow!

  # for _ in range(0, n):
  #   x0 = np.random.uniform(-20, 60)
  #   q = 1/150
  #   p = 0.5 * norm.pdf(x0,mu_1,s_1) + 0.5*norm.pdf(x0, mu_2, s_2)
  #   z0 = np.random.uniform(0, k*q)
  #   if z0 < p:
  #     samples.append(x0)

  # Much faster
  a = -0
  b = 80
  x0 = np.random.uniform(a, b, n)
  q = 1/(b-a)
  z0 = np.random.uniform(0, k*q, n)
  samples += x0[z0 < gaus.eval(x0)].tolist()

  return samples

def q5b(gaus: mixed_gaussian, n):
  x = [0]
  
  def criteria(x_can, x_n, p : mixed_gaussian, sigma):
    return p.eval(x_can)/p.eval(x_n)*norm.pdf(x_n, x_can, sigma)/norm.pdf(x_can, x_n, sigma)

  def step(x0, sigma):
    x_candidate = np.random.normal(x0, sigma)
    accept = min(1, criteria(x_candidate, x0, gaus, sigma))

    if np.random.uniform() <= accept:
      x1 = x_candidate
      a = 1
    else:
      x1 = x0
    return x1
  
  x_burn = 0
  for _ in range(0, 100):
    x_burn = step(x_burn, 20)
  x[-1] = x_burn

  # I don't think this can be done using vectors to make it faster
  # since the samples aren't independent
  for _ in range(0, n):
    x0 = step(x[-1], 20)
    x.append(x0)

  return x

def main():
  pi = [0.5, 0.5]
  mu = [20, 40]
  s = [3, 10]

  k = 6
  n = 10_000

  gaus = mixed_gaussian(pi, mu, s)
  x_g  = q5a(gaus, n, k)
  x_MH = q5b(gaus, n)

  num_points = 10000
  x_series = np.linspace(-50,110, num_points)

  fig, axs = plt.subplots(2)
  fig.suptitle('MCMC methods')
  axs[0].plot(x_series, gaus.plot(x_series))
  axs[1].plot(x_series, gaus.plot(x_series))

  axs[0].hist(x_g, density=True, bins=200)
  axs[1].hist(x_MH, density=True, bins=200)

  axs[0].set_title("Gibbs")
  axs[1].set_title("Metropolis-Hastings Algorithm")

  plt.show()


if __name__ == "__main__":
  main()