
import sys
import threading

def walk():
    global G, M, U, X, Y
    while 0 < len(U):
        x,y = U.pop()
        c = G[y][x]
        if _walk(c, -1, -1, x, y):
            return True

def neighbors(x,y):
    for x1,y1 in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0 <= x1 and x1 < X and 0<= y1 and y1 < Y:
            yield (x1,y1)
        
def _walk(c,x0,y0,x,y):
    global G, M, U, X, Y

    if M[y][x] == 1:
        return True

    #me.mark()
    M[y][x] = 1
    U.discard((x,y))

    for x1,y1 in neighbors(x,y):
        if (x1,y1) != (x0,y0) and G[y1][x1] == c:
            if _walk(c, x, y, x1, y1):
                return True
                 
    return False

X, Y, G, M, U = (None,)*5

def main():
    global G, M, U, X, Y
    Y,X = [int(i) for i in sys.stdin.readline().strip().split()]
    G = []
    M = [None]*Y
    U = set()
    for y in xrange(Y):
        G.append(sys.stdin.readline().strip())
        assert X == len(G[y])
        M[y] = [0]*X
        for x in xrange(X):
            U.add((x,y))
    if walk():
        print "Yes"
    else:
        print "No"

sys.setrecursionlimit(1000000)
threading.stack_size(10240000)
thread = threading.Thread(target=main)
thread.start()
