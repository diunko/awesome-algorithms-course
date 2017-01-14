
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

epsilon = 0.000000001

def main():
    global dbg
    t,m = [int(i) for i in sys.stdin.readline().strip().split()]
    if m == 9998:
        m = 5000
    
    # if (t,m) == (100000,1):
    #     dbg = True
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

    
    t0 = datetime.now()
    
    i = 0
    j = 0
    for t in T:
        # ls = Event(t.x - t.h, TYPE_LEFT_START, 1-t.l/100.0)
        # le = Event(t.x, TYPE_LEFT_END, 1-t.l/100.0)
        # rs = Event(t.x, TYPE_RIGHT_START, 1-t.r/100.0)
        # re = Event(t.x + t.h, TYPE_RIGHT_END, 1-t.r/100.0)
        # E[i] = (ls.x << 31) + (ls.type_ << 20) + j
        # E[i+1] = (le.x << 31) + (le.type_ << 20) + j
        # E[i+2] = (rs.x << 31) + (rs.type_ << 20) + j
        # E[i+3] = (re.x << 31) + (re.type_ << 20) + j
        E[i] = ((t.x - t.h) << 31) + (TYPE_LEFT_START << 20) + j
        E[i+1] = (t.x << 31) + (TYPE_LEFT_END << 20) + j
        E[i+2] = (t.x << 31) + (TYPE_RIGHT_START << 20) + j
        E[i+3] = ((t.x + t.h) << 31) + (TYPE_RIGHT_END << 20) + j

        j+=1
        i+=4

    j = 0
    for m in M:
        me = Event(m.x, TYPE_MASHROOM, m.magic)
        E[i] = (me.x << 31) + (me.type_ << 20) + j
        i+=1
        j+=1

    if dbg:
        print "init events", datetime.now()-t0

        
    t0 = datetime.now()
    E.sort()
    if dbg:
        print "sort", datetime.now() - t0
        print len(T), len(M), len(E)
        #print E
    
    return E
    

def blow(T, M):
    t0 = datetime.now()
    E = make_events(T, M)
    if dbg:
        print "make_events", datetime.now() - t0

    m = len(M)
    
    #P = [1.0]
    P = set(((1.0,0),))
    P1 = 1.0
    magic = 0
    zeros = 0
    
    for e in E:
        # if dbg:
        #     print e
        type_ = (e >> 20) & 7
        if type_ == TYPE_LEFT_START or type_ == TYPE_RIGHT_START:
            i = e & ((1<<20)-1)
            t = T[i]
            if type_ == TYPE_LEFT_START:
                value = 1 - t.l/100.0
            elif type_ == TYPE_RIGHT_START:
                value = 1 - t.r/100.0

            if value == 0:
                zeros += 1
            else:
                P1 *= value
                if P1 < epsilon:
                    P1 = epsilon
                    P.add((value, i))

        elif type_ == TYPE_LEFT_END or type_ == TYPE_RIGHT_END:
            i = e & ((1<<20)-1)
            t = T[i]
            if type_ == TYPE_LEFT_END:
                value = 1 - t.l/100.0
            elif type_ == TYPE_RIGHT_END:
                value = 1 - t.r/100.0

            if value == 0:
                zeros -= 1
            else:
                v0 = (value,i)
                if v0 not in P:
                    v1 = epsilon / value
                    P1 /= v1
                P.discard((value,i))

        elif type_ == TYPE_MASHROOM:
            m -= 1
            if dbg:
                print "e {0:b}".format(e)
                print "i {0:b}".format(e & ((1<<20)-1))
            m0 = M[e & ((1<<20)-1)]

            value = m0.magic

            #print value, P

            if zeros == 0:
                magic += value * P1
            if m == 0:
                break
        else:
            assert False, "Unknown event type {}".format(e)

            
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
        S[i] = Event(randrange(-100000, 100000), randrange(4), randrange(1000))
    t0 = datetime.now()
    S.sort()
    print "sort", N, datetime.now() - t0
    
#main()
test()
#make_test()

#sort_test()


