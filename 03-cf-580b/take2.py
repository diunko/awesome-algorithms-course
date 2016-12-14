
import sys

dbg = True

def party(F, D):
    F.sort()

    if dbg:
        print F
    
    li, ui = 0,0
    max_party = 0
    
    party = 0
    
    end_reached = False
    
    while not end_reached:

        f0 = F[li]
        if li == ui:
            party += f0[1]
        if dbg:
            print "f0", f0

        while True:
            ui += 1

            if len(F) <= ui:
                end_reached = True
                break
            
            f1 = F[ui]
            if dbg:
                print "f1", f1

            if f1[0] - f0[0] < D:
                #take one more to party
                party += f1[1]
            else:
                break

        if dbg:
            print "party", party
            
        if max_party < party:
            max_party = party
        
        if li < len(F)-1:
            end_reached = False
        if dbg:
            print "# leave out f0", f0[1]
        party -= f0[1]
        if dbg:
            print "party", party
        li += 1

        
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

