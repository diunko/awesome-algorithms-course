
total = 0
stuck = 0
N = 8 

def genN(c, used):
  global total
  global stuck
  #print "gen", c, used
  if len(used) == N:
    total += 1
    return
  found = 0
  for i in [c-2, c-1, c+1, c+2]:
    if (0 < i) and (i < N+1) and (not (i in used)):
      found += 1
      used.append(i)
      genN(i, used)
      used.pop() 
  if found == 0:
    stuck += 1
    #print stuck, "stuck at", c, used

def gen():
  global N, total, stuck
  for i in xrange(1,20):
    total = 0
    stuck = 0
    N = i
    genN(1, [1])
    print i, total

gen()

