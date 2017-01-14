import sys
from random import randrange


class Node:

    __slots__ = 'l', 'r', 'm', 'c', 'o', 'left_node', 'right_node'

    def __init__(self, m, c, o, l, r):
        self.left_node = None
        self.right_node = None
        self.l = l
        self.r = r
        self.m = m
        self.c = c
        self.o = o

    def __dump__(self):
        print >> sys.stderr, "m, c, o, l, r ", self.m, self.c, self.o, self.l, self.r


def query(self, l, r):
    # print >> sys.stderr, "l, r", l, r
    # self.__dump__()

    if l == r:
        return 0, 0, 0

    if self.l == l and self.r == r:
        return self.m, self.c, self.o

    mid = (self.r - self.l) // 2 + self.l

    if r <= mid:
        return query(self.left_node, l, r)
    elif mid <= l:
        return query(self.right_node, l, r)
    else:
        r1 = query(self.left_node, l, mid)
        r2 = query(self.right_node, mid, r)
        return merge(r1, r2)


def merge(n1, n2):
    m1, c1, o1 = n1
    m2, c2, o2 = n2

    t = min(o1, c2)

    m = m1 + m2 + 2 * t

    c = c1 + c2 - t
    o = o2 + o1 - t

    return m, c, o


def build_tree(s, l, r):
    if r - l == 1:
        m, c, o = 0, 0, 0
        if s[l] == "(":
            o = 1
        else:
            c = 1
        n = Node(m, c, o, l, r)
        return n

    mid = (r - l) // 2 + l

    n1 = build_tree(s, l, mid)
    n2 = build_tree(s, mid, r)

    m, c, o = merge((n1.m, n1.c, n1.o), (n2.m, n2.c, n2.o))

    n = Node(m, c, o, l, r)
    n.left_node = n1
    n.right_node = n2

    return n


def main(s, qq):
    t = build_tree(s, 0, len(s))

    res = []

    for l, r in qq:
        l -= 1
        #r = 1
        m, c, o = query(t, l, r)
        res.append(str(m))
        if False and len(res) == 5 and res == ["130", "42", "8", "0", "20"]:
            print "len(s), len(qq)", len(s), len(qq)
            return

    print "\n".join(res)


def test():
    s = sys.stdin.readline().strip()
    qn, =  [int(i) for i in sys.stdin.readline().strip().split()]
    qq = [None] * qn
    for j in xrange(qn):
        l, r = [int(i) for i in sys.stdin.readline().strip().split()]
        qq[j] = l, r

    main(s, qq)


def gen(n, qn):
    s = "()"
    pp = []
    for i in xrange(n):
        pp.append(s[randrange(0, 2)])
    qq = []
    for i in xrange(qn):
        l = randrange(n - 2)
        r = randrange(l, n - 2)
        qq.append((l + 1, r + 1))

    p = "".join(pp)
    # print p
    # print qq
    return p, qq


def test2():
    main(*gen(100000, 100000))

#test2()

def gen_test():
    p,qq = gen(100000, 100000) 
    print p
    print len(qq)
    for q in qq:
        print q[0], q[1]

gen_test()
    
