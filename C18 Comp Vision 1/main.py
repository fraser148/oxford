import torch

class Model():
  def forward(self, x):
    # Of form (C, H, W)
    y = torch.rand(x.size())

    for i in range(len(x)):
      av = torch.mean(x[i])
      y[i] = x[i] - av
    
    return y

model = Model()
x = torch.rand(256, 16, 16)
y = model.forward(x)

p = torch.rand(1, 256*16*16)


def forward(x: torch.Tensor) -> torch.Tensor:
  y = torch.zeros_like(x)

  for i, c in enumerate(x):
    m = torch.mean(c)
    y[i] = c - m

  return y

def fbp(p, x):
  # fbp = p . dvec(f)/dvec(x)
  temp_f = forward(x)

  g = torch.inner(p, temp_f)
  C, W, H = x.size()
  gdt = torch.ones(C*H*W, 1) * 1-(1/(H*W))
  p_prime = p * gdt
  return p_prime