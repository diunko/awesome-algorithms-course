
import sys
import threading

from math import exp, log, ceil

import heapq

dbg = False


class heapq1(object):
    def __init__(self, N):
        s = int(ceil(log(N,2)))
        S = 1 << s
        self._heap = [0]*S
        self._last = -1

    def push(self, i):
        self._last += 1
        self._heap[self._last] = i
        self._raise(self._last)

    def pop(self):
        if self._last == -1:
            raise RuntimeError("heap is empty")
        x = self._heap[0]
        self._heap[0] = self._heap[self._last]
        self._last -= 1
        if 0 <= self._last:
            self._lower(0)
        return x

    def min(self):
        if self._last == -1:
            raise RuntimeError("heap is empty")
        return self._heap[0]

    def _raise(self, i):
        assert (i <= self._last), "index within heap range"
        pi = (i-1) >> 1
        if dbg:
            print "_raise: i, pi", i, pi
        
        if i == 0:
            return
        
        if self._heap[i] < self._heap[pi]:
            p = self._heap[pi]
            self._heap[pi] = self._heap[i]
            self._heap[i] = p
            self._raise(pi)
        
    def _lower(self, i):
        assert (i <= self._last), "index within heap range"
        ci0, ci1 = (i<<1)+1, (i<<1)+2
        if dbg:
            print "_lower: i, ci0, ci1, _last", i, ci0, ci1, self._last
        H = self._heap
        if self._last < ci0:
            return
        elif self._last < ci1:
            c0 = H[ci0]
            if H[i] < c0:
                H[ci0] = H[i]
                H[i] = c0
        else:
            c0, c1 = H[ci0], H[ci1]
            if c0 <= c1:
                H[ci0] = H[i]
                H[i] = c0
                self._lower(ci0)
            else:
                H[ci1] = H[i]
                H[i] = c1
                self._lower(ci1)
            
    
def main():
    N,K = [int(i) for i in sys.stdin.readline().strip().split()]
    hq = [0]*K

    r = []
    
    for i in xrange(N):
        s, m = [int(i) for i in sys.stdin.readline().strip().split()]

        s0 = hq[0]
        if s0 < s:
            s0 = s
        s0 += m
        r.append(str(s0))
        heapq.heapreplace(hq, s0)
    print "\n".join(r)

sys.setrecursionlimit(1000000)
threading.stack_size(10240000)
thread = threading.Thread(target=main)
thread.start()
