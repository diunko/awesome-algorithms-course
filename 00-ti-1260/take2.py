
import sys

NN, = [int(i) for i in sys.stdin.readline().strip().split()]

D0 = [0, 1, 1, 2, 4, 6, 9, 14]

D = [None] * 100
for i in xrange(len(D0)):
  D[i] = D0[i]

M = len(D0)

def gen(N):
  global M
  if N < M:
    return D[N]
  else:
    g = gen(N-1) + gen(N-3) + 1
    D[M] = g
    M+=1
    return g

def main(N):
  for i in xrange(1, N):
    gen(i)
  return gen(N)

print main(NN)

