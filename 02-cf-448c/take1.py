

import sys

def merge(A,B,n):
  if A.horizontal and B.horizontal:
    return A+B
  elif A.horizontal:
    B1 = solve(B.cut(n))
    if B1 < B:
      return A+B1
    else:
      return A+B
  elif B.horizonal:
    A1 = solve(A.cut(n))
    if A1 < A:
      return A1+B
    else:
      return A+B
  else:
    # A.vertical and B.vertical
    A1 = solve(A.cut(n))
    B1 = solve(B.cut(n))
    
    d = A+B - (A1+B1)
    R = solve(n-d, m)
    if R < A+B+m:
      return R
    else:
      return R
    

def main():
  pass
