
import sys
import threading

dbg = False

ID = 10**6
indent = 0

def loginout(fn):
    def wrap(A, l, r, w):
        global ID, indent
        _id = ID
        ID+=1
        #print "{}=================".format("|   "*indent)
        print "{}{}[{}]({})".format("|   "*indent, fn.__name__, _id, (A, l, r, w))
        print "{}{}({})".format("|   "*indent, "              ", (A[l:r], w))
        indent += 1
        result = fn(A, l, r, w)
        indent -= 1
        print "{}-> {}".format("|   "*indent, result)
        #print "{}{}[{}]({}) -> {}".format("|   "*indent, fn.__name__, _id, (A[l:r], w), result)
        #print "{}{}[{}]({}) -> {}".format("  "*indent, fn.__name__, _id, (A, l, r, w), result)
        return result
    return wrap


def log(*args):
    print "{}{}".format("|   "*indent, args)

def searchLeftMinRange(A,l0,r0,w):
    dbg and log("searchLeftMinRange", A, l0, r0, w)
    m,l,r = A[l0]-w,l0,l0+1
    for i in xrange(l0, r0):
        c = A[i]-w
        if i == r and c == m:
            r = i+1
        elif c < m:
            m = c
            l = i
            r = i+1
    dbg and log("  m,l,r", m,l,r)
    return m,l,r

    


#@loginout
def paint(A, l, r, w):
    
    if l==r:
        return 0
    
    hm, lm, rm = searchLeftMinRange(A,l,r,w)
    
    l0, r0 = l, lm
    l1, r1 = rm, r

    # paint with horizontal hm lines
    a0 = paint(A, l0, r0, w+hm)
    a1 = paint(A, l1, r1, w+hm)
    
    RH = hm + a0 + a1
    dbg and log("RH = hm + a0 + a1",RH, hm, a0, a1) 

    # paint bottom with vertical lines
    RV = r-l
    dbg and log("RV = r-l", RV, r,l)

    return min((RV,RH))
    

def main():
    N, = [int(i) for i in sys.stdin.readline().strip().split()]
    A = [int(i) for i in sys.stdin.readline().strip().split()]
    #A = range(1,5001)
    print paint(A,0,len(A),0)
    

sys.setrecursionlimit(1000000)
threading.stack_size(10240000)
thread = threading.Thread(target=main)
thread.start()
