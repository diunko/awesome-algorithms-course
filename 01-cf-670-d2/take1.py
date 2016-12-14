
import sys
import random
from itertools import izip

DO = 0
RO = 1
IO = 2

def bake(N,aa,bb):
  result = [None] * N
  i = 0
  for a,b in izip(aa,bb):
    d = b/a
    r = b%a
    result[i] = (d,r,i)
    i+=1
  result.sort(key=lambda x: x[0])
  return result
 
def genR(m,M,N):
  for i in xrange(N):
    yield random.randrange(m,M)

def genN(n, N):
  for i in xrange(N):
    yield n


def checkMagic(aa,bb,rr,M,N):
  "check if we can bake N cookies given M magic"

  i=0
  while i < len(rr):
    #check if we have enough of i-th ingridient
    if N <= rr[i][DO]:
      # enough of current one
      # and enough for all remaining also
      return True 
    needed_magic = (N-rr[i][DO])*aa[rr[i][IO]] - rr[i][RO] #.remainder
    if M < needed_magic:
      return False
    M -= needed_magic  
    i+=1
  return True

def search(aa,bb,rr,M):
  x0, x1 = 1, 2000000000
  if not checkMagic(aa, bb, rr, M, x0):
    return 0
  if checkMagic(aa, bb, rr, M, x1):
    return x1
  
  while True:
    xm = (x0+x1)/2
    #print x0,x1,xm
    t = checkMagic(aa, bb, rr, M, xm)
    if t:
      x0 = xm
    else:
      x1 = xm
    if x1-x0 == 1:
      return x0

def main_gen():
  N = 100000
  M = 10000000000000
  aa = [i for i in genR(1,11,N)]
  bb = [i for i in genR(30,101,N)]
  #aa = genN(10,100)
  #bb = genN(20,100)
  rr = bake(N,aa,bb)
  print rr[-10:]
  n = search(aa,bb,rr,M)
  return n

def main():
  N,M = map(int, sys.stdin.readline().strip().split())
  aa = map(int, sys.stdin.readline().strip().split())
  bb = map(int, sys.stdin.readline().strip().split())
  rr = bake(N,aa,bb)
  n = search(aa,bb,rr,M)
  return n


print main()

