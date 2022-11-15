import numpy as np

C = [0.5, 0.5]

# I.e. for R=F | C=T it would be CR[1][0] amd CR[C][R]
CR = [[0.8, 0.2], [0.2, 0.8]]

# I.e. for S=T | C=F it would be CS[0][1] and CS[C][S]
CS = [[0.5, 0,5], [0.9, 0.1]]

# I.e. for S=T, R=F, W=F it would be SRW[1][0][0]
# This is p(W=F|S=T, R=F)
# SRW[S][R][W]
SRW = [[[1, 0], [0.1, 0.9]], [[0.1, 0.9], [0.01, 0.99]]]

def q6a():
  
  # Want conditional of p(C=T|W=T)
  top = 0
  bottom = 0

  for i in range(0,2):
    for j in range(0,2):
      top += C[1] * CS[1][i] * CR[1][j] * SRW[i][j][1]

  for i in range(0,2):
    for j in range(0,2):
      for k in range(0,2):
        bottom += C[i] * CS[i][j] * CR[i][k] * SRW[j][k][1]

  return top/bottom

# Bruh idk
def q6b():
  # Define state x [Sprinkler, Rain]
  x = [[1, 1]]

  for _ in range(0,10000):
    m = np.random.uniform()

    # Select either sprinkler or rain to update since we set cloudy and wetgrass to 1
    if m < 0.5:
      # Rainy
      z = np.random.uniform()
      p = CR[x[-1][0]][1]
      if z < p:
        x.append(x)


def main():
  print(q6a())

if __name__ == "__main__":
  main()