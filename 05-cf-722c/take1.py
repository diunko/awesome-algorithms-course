
import sys

dbg = True

def prepare():
    pass

def query():
    pass

def split(i):
    L, R = (0, i), (i+1, N)
    M1 = query(L)
    M2 = query(R)
    
    

def build(l,r):
    if r-l <= 1:
        return ((l,r),A[l], None)

    m = l + (r-l)//2
    L = build(l, m)
    R = build(m, r)
    return ((l, r), L, R)
    
def kill(i):    
    if L:
        ML = kill(L)
        MR = R.M
        self.M = MR if ML < MR else ML
    kill(R)
    

def main():
    N = 1 << 17
    #N, = [int(i) for i in sys.stdin.readline().strip().split()]
    A = [int(i) for i in sys.stdin.readline().strip().split()]
    I = [int(i) for i in sys.stdin.readline().strip().split()]

main()

