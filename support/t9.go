package main

import "fmt"

import "os"
import "bytes"
import "io"

var dbg = true

type RMQ struct {
	v []int
	m []int
}

func NewRmq(v []int) (rmq *RMQ) {
	rmq = &RMQ{
		v: v,
		m: make([]int, 4*len(v)),
	}

	rmq.init()
	return
}

func (rmq *RMQ) init() {

	rmq.init_subtree(0, len(rmq.v), 0)
}

func (rmq *RMQ) init_subtree(l, r, p int) (min, idx int) {
	if r-l == 1 {
		rmq.m[p] = l
		min = rmq.v[l]
		idx = l
		return
	}

	mid := (l + r) / 2

	minL, idxL := rmq.init_subtree(l, mid, p*2+1)
	minR, idxR := rmq.init_subtree(mid, r, p*2+2)

	if minL < minR {
		rmq.m[p] = idxL
		return minL, idxL
	} else {
		rmq.m[p] = idxR
		return minR, idxR
	}
}

func (rmq *RMQ) query(l, r int) (min, idx int) {
	min, idx = rmq.query_subtree(l, r, 0, 0, len(rmq.v))
	if dbg {
		fmt.Println("query: l, r, min, idx", l, r, min, idx)
	}
	return
}

func (rmq *RMQ) query_subtree(ql, qr, p, pl, pr int) (min, idx int) {

	if ql == pl && qr == pr {
		idx = rmq.m[p]
		min = rmq.v[idx]
		if dbg {
			fmt.Printf("query_subtree(ql[%d], qr[%d], p[%d], pl[%d], pr[%d]) -> min[%d], idx[%d]\n", ql, qr, p, pl, pr, min, idx)
		}
		return
	}

	if dbg {
		fmt.Println("query_subtree(ql, qr, p, pl, pr)", ql, qr, p, pl, pr)
	}

	mid := (pl + pr) / 2

	if qr <= mid {
		// query left part
		min, idx = rmq.query_subtree(ql, qr, p*2+1, pl, mid)
		return
	}

	if mid <= ql {
		// query right part
		min, idx = rmq.query_subtree(ql, qr, p*2+2, mid, pr)
		return
	}

	minL, idxL := rmq.query_subtree(ql, mid, p*2+1, pl, mid)
	minR, idxR := rmq.query_subtree(mid, qr, p*2+2, mid, pr)

	if minL < minR {
		return minL, idxL
	} else {
		return minR, idxR
	}
}

type Query struct {
	l, r int
}

func solve(s string, qq []Query) {

	v := make([]int, len(s)+1)
	l := 0
	v[0] = 0
	for i, c := range s {
		if c == '(' {
			l += 1
		} else {
			l -= 1
		}
		v[i+1] = l
	}

	if dbg {
		fmt.Println(s)
		fmt.Println(v)
	}
	rmq := NewRmq(v)

	var buf bytes.Buffer

	for _, q := range qq {

		_, idx := rmq.query(q.l, q.r+1)

		h0 := v[q.l] - v[idx]
		h1 := v[q.r] - v[idx]

		l := q.r - q.l - h0 - h1

		if dbg {
			fmt.Println("hl, hm, hr", v[q.l], v[idx], v[q.r])
			fmt.Println("q.l, q.r, h0, h1, l", q.l, q.r, h0, h1, l)
		}

		fmt.Fprintf(&buf, "%d\n", l)
	}
	if dbg {
		fmt.Println("=======================")
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

	solve(s, qq)
}
