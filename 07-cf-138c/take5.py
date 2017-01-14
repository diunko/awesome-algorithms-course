
import sys
from collections import namedtuple as ntuple
from random import randrange
from datetime import datetime
from math import exp,log

dbg = False
stealth_dbg = False

Tree = ntuple("Tree", ["x","h","l","r"])

Mashroom = ntuple("Mashroom", ["x","magic"])
Event = ntuple("Event", ["x", "type_", "value"])

TYPE_LEFT_START  = 0
TYPE_LEFT_END    = 1
TYPE_MUSHROOM    = 2
TYPE_RIGHT_START = 3
TYPE_RIGHT_END   = 4

TYPES = ["ls","le","m","rs","re"]

def event_fmt(e):
    x = e >> 32
    type_ = (e >> 24) & 7
    i = e & M_IDX
    return "[x: {}, type: {}, i: {}]".format(x, TYPES[type_], i)

def main():
    global dbg, stealth_dbg
    t,m = [int(i) for i in sys.stdin.readline().strip().split()]

    t0 = datetime.now()
    T = [None]*(t*4)
    M = [None]*(m*2)
    E = [None]*((t*4)+m)
    for i in xrange(t):
        x,h,l,r = [int(s) for s in sys.stdin.readline().strip().split()]
        if dbg:
            print "x,h,l,r", x,h,l,r
        T[i*4+0], T[i*4+1], T[i*4+2], T[i*4+3] = x, h, l, r
        E[i*4+0] = ((x - h) << 32) + (TYPE_LEFT_START << 24) + i
        E[i*4+1] = (x << 32) + (TYPE_LEFT_END << 24) + i
        E[i*4+2] = (x << 32) + (TYPE_RIGHT_START << 24) + i
        E[i*4+3] = ((x + h) << 32) + (TYPE_RIGHT_END << 24) + i
    t1 = datetime.now()
        
    for i in xrange(m):
        x, m = [int(s) for s in sys.stdin.readline().strip().split()]
        M[i*2 + 0] = (x<<32)
        M[i*2 + 1] = m
        E[t*4+i] = (x << 32) + (TYPE_MUSHROOM << 24) + i
    t2 = datetime.now()

    E.sort()
    t3 = datetime.now()
    
    if dbg:
        print map(event_fmt, E)
        print "init trees", t1-t0
        print "init mushrooms", t2-t1
        print "sort events", t3-t2

    t0 = datetime.now()
    p = blow(T, M, E)
    t1 = datetime.now()
    if dbg:
        print "blow", t1-t0
    print p

M_IDX = (1<<20)-1
    
def blow(T, M, E):
    t0 = datetime.now()

    t, m = len(T), len(M)
    
    P = 0.0
    magic = 0.0
    zeros = 0
    
    for e in E:
        x = e >> 32
        type_ = (e >> 24) & 7
        i = e & M_IDX

        if dbg:
            print event_fmt(e),
        
        if type_ == TYPE_MUSHROOM:
            m -= 1
            x, value = M[i*2], M[i*2+1]
            if zeros == 0:
                magic += value * exp(P)

            if dbg:
                print "value {}, exp(P) {}, magic {}".format(value, exp(P), magic)
            if m == 0:
                break
        else:
            x, h, l, r = T[i*4+0], T[i*4+1], T[i*4+2], T[i*4+3]
            if type_ == TYPE_LEFT_START or type_ == TYPE_RIGHT_START:
                if type_ == TYPE_LEFT_START:
                    value = 1 - l/100.0
                elif type_ == TYPE_RIGHT_START:
                    value = 1 - r/100.0

                if value == 0:
                    zeros += 1
                else:
                    P += log(value)
            elif type_ == TYPE_LEFT_END or type_ == TYPE_RIGHT_END:
                if type_ == TYPE_LEFT_END:
                    value = 1 - l/100.0
                elif type_ == TYPE_RIGHT_END:
                    value = 1 - r/100.0

                if value == 0:
                    zeros -= 1
                else:
                    P -= log(value)
            else:
                assert False, "Unknown event type {}".format(e)
            if dbg:
                print "value {}, exp(P) {}".format(value, exp(P))
            
    return magic
    
def test():
    N,m = 100000,10000
    T = [None]*N
    for i in xrange(N):
        p = randrange(100)
        q = randrange(p+1)
        T[i] = Tree(0, randrange(10000), p, q)
    #M = [Mashroom(randrange(-100000,100000), 10000)]
    M = [None]*m
    for i in xrange(m):
        M[i] = Mashroom(randrange(-100000,100000), 10000)
    t0 = datetime.now()
    print blow(T, M)
    print "blow", datetime.now() - t0

def make_test():
    N,m = 100000, 10
    T = [None]*N
    for i in xrange(N):
        p = randrange(100)
        q = randrange(p+1)
        T[i] = Tree(0, randrange(10000), p, q)
    for i in xrange(m):
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
        e = Event(randrange(-100000, 100000), randrange(4), randrange(1000))
        S[i] = (e.x<<31)+(e.type_<<20)+i
    t0 = datetime.now()

    S.sort()
    print "sort", N, datetime.now() - t0
    

main()
#test()
#make_test()

#sort_test()


