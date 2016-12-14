
import sys

dbg = False

def pre(*args):
    return "|   "*indent

def walk():
    global N, D, A, M, G, O, U, indent
    if dbg:
        print "N, D, A, M, G, O, U", N, D, A, M, G, O, U
    n = U.pop()
    p = _walk(-1, n)

    print p
    for i in xrange(N):
        print O[i]

def unlink(i,j):
    global N, D, A, M, G, O, U, indent
    assert M[i][j] == M[j][i] and M[j][i] == ord("1"), "link should exist when unlinking"
    M[i][j] = "0"
    M[j][i] = "0"
    O[i][j] = "d"
    O[j][i] = "d"

def link(i,j):
    global N, D, A, M, G, O, U, indent
    if M[i][j] == M[j][i] and M[j][i] != ord("0"):
        if dbg:
            print pre(), "link({}->{}) exists when linking: {}".format(i,j, chr(M[j][i]))
            for k in xrange(len(M)):
                print pre(), M[k]

        assert False, "link should not exist when linking"
    M[i][j] = "1"
    M[j][i] = "1"
    O[i][j] = "a"
    O[j][i] = "a"
        
def _walk(i0, i):
    # explore(from, current)
    if dbg:
        print pre(), "_walk({}, {})".format(i0,i)
    global N, D, A, M, G, O, U, indent
    indent += 1

    w = 0
    
    # mark
    G[i] = 1

    for i1 in xrange(N):
        if i1 == i0: 
            # we just came from it
            continue

        if M[i][i1] == ord("1"):
            # there is a flight to i1

            if G[i1] == 1:
                # we've been to i1
                w += D
                unlink(i,i1)
            else:
                U.discard(i1)
                w += _walk(i,i1)

    if indent == 1:
        while 0 < len(U):
            n = U.pop()
            w += A
            link(i, n)
            w += _walk(i, n)

    indent -= 1
    return w

N, D, A, M, G, O, U, indent = (None,)*8

def main():
    global N, D, A, M, G, O, U, indent
    indent = 0
    N, = [int(i) for i in sys.stdin.readline().strip().split()]
    D,A = [int(i) for i in sys.stdin.readline().strip().split()]
    G = [0]*N
    M = [None]*N
    O = [None]*N
    U = set(xrange(N))
    for i in xrange(N):
        M[i] = bytearray(sys.stdin.readline().strip())
        O[i] = bytearray(N)
        for j in xrange(N):
            O[i][j] = "0"
    walk()
            
    
main()
