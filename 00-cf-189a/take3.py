
import sys

N,a,b,c = [int(x) for x in sys.stdin.readline().strip().split()]
a,b,c = sorted([a,b,c])

def slowest(a,b,c,N):
  S = 0
  S0 = 0
  x = N/a
  while -1 < x:
    #for x in xrange(N/a,-1,-1):
    if x*a == N:
      return x
    z = (N-x*a)/c
    while -1 < z:
      #for z in xrange((N-x*a)/c+1,-1,-1):
      y = (N-x*a-z*c)/b
      if x*a+y*b+z*c == N:
        #print "a,b,c", a,b,c
        #print "x,y.z", x,y,z
        S0 = x+y+z
        if S0 > S:
          S = S0
      z -= 1
    x -= 1
  return S


if __name__ == "__main__":
  print slowest(a,b,c,N)
