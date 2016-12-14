
import sys

N,a,b,c = [int(x) for x in sys.stdin.readline().strip().split()]
a,b,c = sorted([a,b,c])

def slowest(a,b,c,N):
  #print "a,b,c,N", a,b,c,N
  S = 0
  S0 = 0
  for x in xrange(N/a,-1,-1):
    #print "x", x
    for z in xrange((N-x*a)/c+1,-1,-1):
      #print "y", y
      y = (N-x*a-z*c)/b
      if x*a+y*b+z*c == N:
        #print "x,y,z", x,y,z
        #print "a,b,c", a,b,c
        S0 = x+y+z
        #return S0
        if S0 > S:
          S = S0
  return S


if __name__ == "__main__":
  print slowest(a,b,c,N)
