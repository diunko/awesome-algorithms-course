package main

import "fmt"

import "os"
import "bytes"
import "io"

type Node struct {
	L     int
	R     int
	M     int
	C     int
	O     int
	Left  *Node
	Right *Node
}

var dbg = false

type Query struct {
	l, r int
}

func build_tree(s string, l int, r int) (n *Node) {
	var m, c, o int
	if r-l == 1 {
		m, c, o = 0, 0, 0
		if s[l] == '(' {
			o = 1
		} else {
			c = 1
		}

		n = &Node{M: m, C: c, O: o, L: l, R: r}
		return
	}

	mid := (r-l)/2 + l
	n1 := build_tree(s, l, mid)
	n2 := build_tree(s, mid, r)

	m, c, o = merge(n1.M, n1.C, n1.O, n2.M, n2.C, n2.O)

	n = &Node{M: m, C: c, O: o, L: l, R: r, Left: n1, Right: n2}
	return
}

func merge(m1, c1, o1, m2, c2, o2 int) (m, c, o int) {
	t := c2
	if o1 < c2 {
		t = o1
	}

	m = m1 + m2 + 2*t
	c = c1 + c2 - t
	o = o2 + o1 - t
	return
}

func query(t *Node, l, r int) (m, c, o int) {

	if dbg {
		fmt.Println(l, r, t)
	}

	if l == r {
		return 0, 0, 0
	}

	if t.L == l && t.R == r {
		return t.M, t.C, t.O
	}

	mid := t.L + (t.R-t.L)/2

	if r <= mid {
		return query(t.Left, l, r)
	} else if mid <= l {
		return query(t.Right, l, r)
	} else {
		m1, c1, o1 := query(t.Left, l, mid)
		m2, c2, o2 := query(t.Right, mid, r)
		return merge(m1, c1, o1, m2, c2, o2)
	}
}

func equate(s string, qq []Query) {

	t := build_tree(s, 0, len(s))

	var m0 int
	var buf bytes.Buffer

	for _, q := range qq {
		m, _, _ := query(t, q.l, q.r)
		m0 += m
		if !dbg {
			fmt.Fprintf(&buf, "%d\n", m)
			//fmt.Println(m)
		}
	}
	buf.WriteTo(os.Stdout)
}

func main() {

	var input bytes.Buffer

	io.Copy(&input, os.Stdin)

	var s string
	fmt.Fscanf(&input, "%s\n", &s)

	var qn int
	fmt.Fscanf(&input, "%d\n", &qn)

	qq := []Query{}

	for i := 0; i < qn; i++ {
		var l, r int
		fmt.Fscanf(&input, "%d %d\n", &l, &r)
		qq = append(qq, Query{l - 1, r})
	}

	equate(s, qq)
}
