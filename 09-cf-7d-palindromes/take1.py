
import sys

dbg = False

def quick_pow_mod(b, e, m):
    p = b
    r = 1
    while 0<e:
        if e & 1:
            r = (r*p)%m
        p = (p*p)%m
        e = e>>1
    return r

A = 2**32-1
B = 982451653
A_ = quick_pow_mod(A, B-2, B)

def hash_prepend(hna, s):
    h0, n, A_n = hna

    c = ord(s)
    h = (h0*A+c*A)%B
    
    r = h, n+1, (A_n*A)%B

    if dbg:
        print "hash_prepend(", h0,n,A_n,") -> ", r
    return r

def hash_shift(hna, s):
    h0, n, A_n = hna
    c = ord(s)
    h = (h0 - c*A_n)%B
    
    r = h, n-1, (A_n*A_)%B
    if dbg:
        print "hash_shift(", h0,n,A_n,"), ", c, ") -> ", r
    return r

def init_prefix_hashes_lr(s):
    HH = [None]*len(s)
    h = 0,0,1
    for i in xrange(len(s)):
        h = hash_prepend(h, s[i])
        HH[i] = h
    return HH
    
def init_prefix_hashes_rl(s):
    HH = [None]*len(s)
    l = len(s)
    h = 0,0,1
    for i in xrange(l):
        h = hash_prepend(h, s[l-i-1])

    for i in xrange(l):
        HH[l-i-1] = h
        h = hash_shift(h, s[l-i-1])

    return HH

def palindromize(s):
    HH_lr = init_prefix_hashes_lr(s)
    HH_rl = init_prefix_hashes_rl(s)

    return HH_lr, HH_rl

def get_prefix_hashes(HH, e):
    lr, rl = HH
    return lr[e-1], rl[e-1]


def palindrom_sum_degree(s, HH):

    if dbg:
        print s
    
    S = 0
    for i in xrange(len(s)):
        P = 0
        end = i+1
        if dbg:
            print "================"
        while 0<end:
            if dbg:
                print self[0:end]
            lr, rl = get_prefix_hashes(HH, end)
            if lr != rl:
                break
            P += 1
            end = end // 2
        S += P
            
    return S

def palindrom_sum_degree2(s, HH):

    if dbg:
        print s
    
    P = 0

    end = len(s)
    if dbg:
        print "================"
    while 0<end:
        if dbg:
            print self[0:end]
        lr, rl = get_prefix_hashes(HH, end)
        if lr != rl:
            break
        P += 1
        end = end // 2
    if lr == rl:
        return P*(P+1)/2
    else:
        return P

def main():
    s = sys.stdin.readline().strip()
    #s = "abacabadabacaba"
    HH = palindromize(s)
    if dbg:
        print "HH", HH
    print palindrom_sum_degree(s, HH)

def test():

    h = 0,0,1
    for i in xrange(10):
        h = hash_prepend(h, chr(i))
    for i in xrange(10):
        h = hash_shift(h, chr(i))
        
main()
#test()
