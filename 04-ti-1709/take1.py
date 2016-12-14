


def walk(i0,i,j):
    # what is j? I can't remember!
    
    mark(i)
    
    for x in xrange(N):
        if x != i0:
            if M[x][j]:
                if marked(j):
                    unlink(i,j)
                else:
                    w += walk(x, j)

    while 0 < len(U):
        N = U.pop()
        link(i, N)
        walk(i, N)
    

