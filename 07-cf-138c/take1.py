
import sys
from collections import namedtuple as ntuple

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
        ls = Event(t.x - t.h, TYPE_LEFT_START, 100-t.l)
        le = Event(t.x, TYPE_LEFT_END, 100-t.l)
        rs = Event(t.x, TYPE_RIGHT_START, 100-t.r)
        re = Event(t.x + t.h, TYPE_RIGHT_END, 100-t.r)
        E[i] = ls
        E[i+1] = le
        E[i+2] = rs
        E[i+3] = re
        i+=4

    for m in M:
        E[i] = Event(m.x, TYPE_MASHROOM, m.magic)
        i+=1

    E.sort()
        
    if dbg:
        print len(T), len(M), len(E)
        print E
    
    return E
    
    
def blow(T, M):
    E = make_events(T, M)
    
    P = 1
    exponent = 0.0
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
                exponent += 2
        elif e.type_ == TYPE_LEFT_END or e.type_ == TYPE_RIGHT_END:
            if e.value == 0:
                zeros -= 1
            else:
                P /= e.value
                exponent -= 2
        elif e.type_ == TYPE_MASHROOM:
            if zeros == 0:
                magic += e.value * (P/10**exponent)
        else:
            assert False, "Unknown event type {}".format(e)
            
    return magic
    
        
main()

