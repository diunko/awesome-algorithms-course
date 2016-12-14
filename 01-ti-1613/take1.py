
import sys

def search(di, y):
  i0, i1 = 0, len(di)-1
  if not(di[i0][1] < y):
    return i0
  if not(y <= di[i1][1]):
    return i1

  while True:
    im = (i0+i1)/2
    if di[im][1] < y:
      i0 = im
    elif y <= di[im][1]:
      i1 = im
    else:
      sys.exit(1)
    if i1-i0 == 1:
      return i1

def query(di, q):
  l,r,x = q
  i = search(di, x)
  while di[i][1] == x:
    if l <= di[i][0] and di[i][0] <= r:
      return True
  return False

def main():
  N = map(int, sys.stdin.readline().strip().split())[0]
  dd = map(int, sys.stdin.readline().strip().split())
  QN = map(int, sys.stdin.readline().strip().split())[0]
  qq = [None] * QN
  di = [None] * len(dd)
  result = bytearray(QN)

  for i in xrange(len(dd)):
    di[i] = (i,dd[i])
  di.sort(key=lambda x: x[1])
  
  for i in xrange(QN):
    l,r,x = map(int, sys.stdin.readline().strip().split())
    l,r,x = l-1, r-1, x
    qq[i] = (l,r,x)
  
  for i in xrange(QN):
    r = query(di, qq[i])
    if r:
      result[i]="1"
    else:
      result[i]="0"
  print result


main()
