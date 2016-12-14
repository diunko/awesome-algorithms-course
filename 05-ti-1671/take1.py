
import sys

dbg = True


class Graph(object):

    def __init__(self, nodes_count):
        self._nodes = range(nodes_count)
        self._roots_count = nodes_count

    def link(self, edge):
        n0, n1 = edge

        s0 = self._find(n0)
        s1 = self._find(n1)
        
        self._union(s0, s1)

    def _find(self, n):
        N = self._nodes
        i = n
        nn = []
        while N[i] != i:
            nn.append(i)
            i = N[i]
        u = i
        for i in nn:
            N[i] = u
        return u

    def _union(self, u0, u1):
        if u0 != u1:
            self._nodes[u0] = u1
            self._roots_count -= 1

    def get_roots_count(self):
        return self._roots_count
        
def tangle_and_tear(N, E, D):

    E1 = set(E)
    for i in D:
        E1.discard(E[i])

    G = Graph(N)
    R = [None]*len(D)
    for e in E1:
        G.link(e)

    for i in xrange(len(D)):
        R[len(D)-1 - i] = G.get_roots_count()
        G.link(E[D[len(D)-1 - i]])

    return R
    

def main():
    N,M = [int(i) for i in sys.stdin.readline().strip().split()]
    E = [None]*M
    for i in xrange(M):
        n0, n1 = [int(n)-1 for n in sys.stdin.readline().strip().split()]
        E[i] = (n0, n1)
    Q, = [int(i) for i in sys.stdin.readline().strip().split()]
    D = [int(i)-1 for i in sys.stdin.readline().strip().split()]
    assert len(D) == Q, "len(D) == Q"

    R = tangle_and_tear(N, E, D)
    print " ".join((str(i) for i in R))
    
main()

