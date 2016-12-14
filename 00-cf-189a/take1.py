import sys

a,b,c,N = [int(x) for x in sys.stdin.readline().strip().split(",")]

def maximum_cut(a,b,c,N):
  results = []
  for x in xrange(0,N/a):
    for y in xrange(0,N/b):
      for z in xrange(0,N/c):
        if a*x+b*y+c*z == N:
          results.append(x+y+z)
  results = sorted(results)
  return results[len(results)-1]

def slowest(a,b,c,N):
  S = 0
  for x in xrange(4000):
    for y in xrange(4000):
      for z in xrange(4000):
        S += (x*a+y*b+z*c) % N
  return S
        

if __name__ == "__main__":
  print slowest(4,5,6,3987)
