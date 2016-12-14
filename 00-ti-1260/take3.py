
import sys

NN, = [int(i) for i in sys.stdin.readline().strip().split()]

D0 = [0, 1, 1, 2, 4, 6, 9, 14]

D = [None] * 100
for i in xrange(len(D0)):
  D[i] = D0[i]

M = len(D0)

for i in xrange(M, 100):
  D[i] = D[i-1] + D[i-3] + 1

print D[NN]

