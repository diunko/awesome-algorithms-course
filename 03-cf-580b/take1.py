
import sys

dbg = False

def party(F, D):
    F.sort()
    if dbg:
        print F

    party = F[0][1]
    max_party = 0

    l,u = 0,1


    while l < len(F):

        f0 = F[l]

        # if l < u:
        #     pass
        # else:
        #     party += f0[1]

        while u < len(F):

            f1 = F[u]
            
            if f1[0] - f0[0] < D:
                party += f1[1]
                u += 1
            else:
                break

        if max_party < party:
            max_party = party

        if u == len(F):
            break
        else:
            l += 1 
            party -= f0[1]

    return max_party
            
        
        
        
    
    
        

def main():
    global result
    N,D = [int(i) for i in sys.stdin.readline().strip().split()]
    F = [None]*N
    for i in xrange(N):
        m,f = (int(i) for i in sys.stdin.readline().strip().split())
        F[i] = (m,f)

    if dbg:
        print "D", D
    print party(F, D)

main()

