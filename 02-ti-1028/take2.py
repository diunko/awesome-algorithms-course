
import sys

dbg = False

indent = 0

result = []

def merge_levels(P, L, U):
    # merge levels of L and U, sorted by X, where all Us are higher than Ls

    global result
    
    ll, lr = L
    ul, ur = U

    li, ui = ll, ul

    ci = 0

    last_level = 0
    
    while ui < ur and li < lr:
        lp = P[li]
        up = P[ui]

        if lp[0] <= up[0]:
            #last_level = lp[2] + 1
            last_level += 1

            # pop lp
            result[ci] = lp
            ci+=1
            li+=1
            
        else:
            up[2] += last_level

            # pop up
            result[ci] = up
            ci+=1
            ui+=1

    if ui == ur:
        for i in xrange(li, lr):
            result[ci] = P[i]
            ci+=1
    elif li == lr:
        for i in xrange(ui, ur):
            up = P[i]
            up[2] += last_level
            result[ci] = up
            ci+=1
    else:
        assert False, "unreachable"
            
    for i in xrange(0, ur-ll):
        P[ll+i] = result[i]


def find_levels(P,l,r):
    global indent
    
    if r-l <= 1:
        return
    
    m = l+(r-l)/2
    indent += 1
    find_levels(P,l,m)
    find_levels(P,m,r)

    merge_levels(P, (l, m), (m,r))
    indent -= 1


def find_levels_nn(P):
    for i in xrange(len(P)):
        for j in xrange(len(P)):
            if P[j][0] <= P[i][0] and P[j][1] <= P[i][1] and i != j:
                P[i][2] += 1

def get_distr(P):
    distr = {}
    for p in P:
        if p[2] in distr:
            distr[p[2]] += 1
        else:
            distr[p[2]] = 1
    return distr
    

def levels_distribution(P):
    find_levels(P, 0, len(P))
    return get_distr(P)
    

def main():
    global result
    N, = [int(i) for i in sys.stdin.readline().strip().split()]
    P = [None]*N
    result = [None]*N
    for j in xrange(N):
        x,y = (int(i) for i in sys.stdin.readline().strip().split())
        P[j] = [x,y,0]

    d = levels_distribution(P)
    for i in xrange(len(P)):
        print d.get(i, 0)

def gen_map(X,Y,N):
    M = {}
    for i in xrange(N):
        while True:
            x,y = randrange(0,X), randrange(0,Y)
            if (x,y) not in M:
                M[(x,y)] = 1
                break

    return sorted(M.keys(), key=lambda x: (x[1], x[0]))
    
main()

