def q6a():
  C = [0.5, 0.5]

  # I.e. for R=F | C=T it would be CR[1][0] amd CR[C][R]
  CR = [[0.8, 0.2], [0.2, 0.8]]

  # I.e. for S=T | C=F it would be CS[1][0] and CS[C][S]
  CS = [[0.1, 0.9], [0.5, 0,5]]

  # I.e. for S=T, R=F, W=F it would be SRW[0][1][1]
  # This is p(W=F|S=T, R=F)
  # SRW[S][R][W]
  SRW = [[[0.99,0.01], [0.9, 0.1]],[[0.9, 0.1], [0, 1]]]

  # Want conditional of p(C=T|W=T)

  top = 0
  bottom = 0

  for i in range(0,2):
    for j in range(0,2):
      top += C[0] * CS[0][i] * CR[0][j] * SRW[i][j][0]

  for i in range(0,2):
    for j in range(0,2):
      for k in range(0,2):
        bottom += C[i] * CS[i][j] * CR[i][k] * SRW[j][k][0]

  return top/bottom


def main():
  print(q6a())

if __name__ == "__main__":
  main()