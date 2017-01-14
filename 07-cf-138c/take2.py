
import sys
from collections import namedtuple as ntuple
from random import randrange
from datetime import datetime

dbg = False

Tree = ntuple("Tree", ["x","h","l","r"])
Mashroom = ntuple("Mashroom", ["x","magic"])
Event = ntuple("Event", ["x", "type_", "value"])

TYPE_LEFT_START  = 0
TYPE_LEFT_END    = 1
TYPE_MASHROOM    = 2
TYPE_RIGHT_START = 3
TYPE_RIGHT_END   = 4


def main():
    t,m = [int(i) for i in sys.stdin.readline().strip().split()]
    T = [None]*t
    M = [None]*m
    for i in xrange(t):
        T[i] = Tree(*[int(s) for s in sys.stdin.readline().strip().split()])

    for i in xrange(m):
        M[i] = Mashroom(*[int(s) for s in sys.stdin.readline().strip().split()])

    p = blow(T,M)
    print p

def make_events(T, M):
    # if coords are equal, order should be as follows:
    # left_start, left_end, mushroom, right_start, right_end

    E = [None]*(len(T)*4+len(M))

    i = 0
    for t in T:
        ls = Event(t.x - t.h, TYPE_LEFT_START, 1-t.l/100.0)
        le = Event(t.x, TYPE_LEFT_END, 1-t.l/100.0)
        rs = Event(t.x, TYPE_RIGHT_START, 1-t.r/100.0)
        re = Event(t.x + t.h, TYPE_RIGHT_END, 1-t.r/100.0)
        E[i] = ls
        E[i+1] = le
        E[i+2] = rs
        E[i+3] = re
        i+=4

    for m in M:
        E[i] = Event(m.x, TYPE_MASHROOM, m.magic)
        i+=1

    t0 = datetime.now()
    E.sort()
    print "sort", datetime.now() - t0
        
    if dbg:
        print len(T), len(M), len(E)
        print E
    
    return E
    

def blow(T, M):
    t0 = datetime.now()
    E = make_events(T, M)
    print "make_events", datetime.now() - t0
    
    m = len(M)
    
    P = 1
    magic = 0
    zeros = 0
    
    for e in E:
        if dbg:
            print e
        if e.type_ == TYPE_LEFT_START or e.type_ == TYPE_RIGHT_START:
            if e.value == 0:
                zeros += 1
            else:
                P *= e.value
        elif e.type_ == TYPE_LEFT_END or e.type_ == TYPE_RIGHT_END:
            if e.value == 0:
                zeros -= 1
            else:
                P /= e.value
        elif e.type_ == TYPE_MASHROOM:
            #m -= 1
            if zeros == 0:
                magic += e.value * P
            if m == 0:
                break
        else:
            assert False, "Unknown event type {}".format(e)
            
    return magic
    
def test():
    N = 100000
    T = [None]*N
    for i in xrange(N):
        p = randrange(100)
        q = randrange(p+1)
        T[i] = Tree(0, randrange(10000), p, q)
    M = [Mashroom(randrange(-100000,100000), 10000)]
    print blow(T, M)

def make_test():
    N = 100000
    T = [None]*N
    for i in xrange(N):
        p = randrange(100)
        q = randrange(p+1)
        T[i] = Tree(0, randrange(10000), p, q)
    M = [Mashroom(randrange(-100000,100000), 10000)]

    print len(T), len(M)
    for t in T:
        print t.x, t.h, t.l, t.r
    print M[0].x, M[0].magic

def sort_test():
    N = 400000
    S = [None]*N
    for i in xrange(N):
        #S[i] = Event(randrange(-100000, 100000), randrange(4), randrange(1000))
        S[i] = randrange(-100000, 100000) << 31 + randrange(4) << 20 + randrange(1000)
        #S[i] = randrange(-100000000, 100000000)
    t0 = datetime.now()
    S.sort()
    print "sort", N, datetime.now() - t0
    
#main()
#test()
#make_test()

sort_test()


