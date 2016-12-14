
import sys

def search(ii, l):
  #print "search", ii
  x0,x1 = 0, len(ii)-1
  if l <= ii[x0]:
    return x0
  if not (l <= ii[x1]):
    return x1

  # ii[x0] < l
  # l < ii[x1]
  while True:
    xm = (x0+x1)/2
    if ii[xm] < l:
      x0 = xm
    else:
      x1 = xm
    if x1 - x0 == 1:
      return x1
    

def query(D, q):
  #print "q", q
  l,r,x = q
  if x not in D:
    return False
  ii = D[x]
  i = search(ii, l)
  #print "search result", i
  #print "l,r", (l, r)
  if l <= ii[i] and ii[i] <= r:
    return True
  return False

def main():
  N = map(int, sys.stdin.readline().strip().split())[0]
  dd = map(int, sys.stdin.readline().strip().split())
  QN = map(int, sys.stdin.readline().strip().split())[0]
  qq = [None] * QN
  result = bytearray(QN)
  D = {}

  for i in xrange(len(dd)):
    if dd[i] in D:
      D[dd[i]].append(i)
    else:
      D[dd[i]] = [i]

  #print D
  
  for i in xrange(QN):
    l,r,x = map(int, sys.stdin.readline().strip().split())
    l,r,x = l-1, r-1, x
    qq[i] = (l,r,x)
  
  for i in xrange(QN):
    r = query(D, qq[i])
    if r:
      result[i]="1"
    else:
      result[i]="0"
  print result


main()
