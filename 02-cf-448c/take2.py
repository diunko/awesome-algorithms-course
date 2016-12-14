
import sys
from itertools import izip, islice
from collections import namedtuple

def paintVertical(A, s=0, e=0):
  return e-s

def paintHorizontal(A, M):
  A = [a - M for a in A]
  return paint(A)

def paint(A, s=0, e=-1, waterline=0):
  if e == -1:
    e = len(A)

  if e-s == 0:
    return 0
  elif e-s == 1:
    return 1

  H = [Plank(v-waterline,i) for i in izip(A[s:e], xrange(s,e))]
  H.sort()

  m = H[0]
  if m.v == 0:
    for i in xrange(1,len(H)):
      if H[i].i == H[i-1].i and H[i].v == m.v:
        continue
      break
    

  for i in xrange(1,len(H)):
    if H[i].i == H[i-1].i and H[i].v == m.v:
      continue
    break
  M = m.v
  N = i

  #A1, A2 = A[:m.i], A[m.i+N:]

  RV = paintVertical(A, s=0, e=m.i) + paintVertical(A, s=m.i+N, e=len(A)) + N
  RH = paint(A, s=0, e=m.i, waterline=M) + paint(A, s=m.i+N, e=len(A), waterline=M) + M
  
  return min(RV, RH)

Plank = namedtuple("Plank", ["v", "i"])

def main():
  N, = [int(i) for i in sys.stdin.readline().strip().split()]
  A = [int(i) for i in sys.stdin.readline().strip().split()]
  paint(A,H)
  
