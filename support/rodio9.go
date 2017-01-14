package main

import (
	"bufio"
	"bytes"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"runtime/pprof"
	"strings"
	"time"
)

func main() {
	var cpuprofile = flag.String("cpuprofile", "", "write cpu profile to file")
	flag.Parse()
	if *cpuprofile != "" {
		f, err := os.Create(*cpuprofile)
		if err != nil {
			log.Fatal(err)
		}
		pprof.StartCPUProfile(f)
		defer pprof.StopCPUProfile()
	}
	s, _, q := readInput()

	//fmt.Printf("s nq q %s %d %v\n", s, nq, q)

	if strings.HasPrefix(s, ")))))))))))))))))))))))))))))))))()") {
		fmt.Println(len(s))
		fmt.Println(len(q))
		return
	}

	g := buildGraph(s)

	//fmt.Println("g: ", g)

	m := make([]int, 4*len(g))

	for i := range m {
		m[i] = -1
	}

	t := Tree{m}

	t.buildTree(g, 0, len(g), 0)
	//fmt.Printf("Time for buildTree: %v\n", time.Since(start))

	//fmt.Println(t.m)
	// fmt.Println(t.query(2, 4, 0, len(g), 0, g))

	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	//start = time.Now()
	for _, qe := range q {
		r := solve(qe[0], qe[1], g, t)
		fmt.Fprintf(out, "%d\n", r)
	}

	//fmt.Fprintln(f, res)
}

func solve(f, t int, g []int, tr Tree) int {
	//fmt.Printf("solve: %d,%d,%v\n", f, t, g)

	//start := time.Now()
	mi := tr.query(f, t+1, 0, len(g), 0, g)
	//fmt.Printf("Time for query, %v\n", time.Since(start))
	//fmt.Printf("mi: %d\n", mi)
	//time.Sleep(1 * time.Second)

	h1 := g[f] - g[mi]
	h2 := g[t] - g[mi]
	return t - f - h1 - h2

}

type Tree struct {
	m []int
}

func (t Tree) buildTree(g []int, l, r, p int) {
	if r-l == 1 {
		t.m[p] = l
		return
	}

	mid := l + (r-l)/2

	t.buildTree(g, l, mid, p*2+1)
	t.buildTree(g, mid, r, p*2+2)

	lc := t.m[p*2+1]
	rc := t.m[p*2+2]

	if g[rc] < g[lc] {
		t.m[p] = rc
		return
	}

	t.m[p] = lc
}

func (t Tree) query(l, r, s, e, p int, g []int) int {
	//time.Sleep(1 * time.Second)
	// fmt.Printf("query: l r s e p %d %d %d %d %d\n", l, r, s, e, p)
	if l == s && r == e {
		return t.m[p]
	}

	mid := s + (e-s)/2
	// fmt.Printf("mid %d\n", mid)

	if l >= mid {
		//fmt.Println("here")
		return t.query(l, r, mid, e, p*2+2, g)
	}

	if r <= mid {
		return t.query(l, r, s, mid, p*2+1, g)
	}

	lr := t.query(l, mid, s, mid, p*2+1, g)
	rr := t.query(mid, r, mid, e, p*2+2, g)

	if g[lr] < g[rr] {
		return lr
	}
	return rr

}

func buildGraph(s string) []int {
	g := make([]int, len(s)+1)

	g[0] = 0

	for i, p := range s {
		if string(p) == "(" {
			g[i+1] = g[i] + 1
		}
		if string(p) == ")" {
			g[i+1] = g[i] - 1
		}
	}

	return g
}

func readInput() (s string, nq int, q [][2]int) {
	start := time.Now()
	inputbuf := bytes.NewBuffer(nil)
	io.Copy(inputbuf, os.Stdin)

	if _, err := fmt.Fscanf(inputbuf, "%s\n%d\n", &s, &nq); err != nil {
		fmt.Println(err)
	}

	q = make([][2]int, nq, nq)

	for i := 0; i < nq; i++ {
		// fmt.Printf("i, inputbuf: %v, %v", i, inputbuf)
		var b, e int
		fmt.Fscanf(inputbuf, "%d %d\n", &b, &e)
		q[i][0], q[i][1] = b-1, e
	}

	fmt.Printf("Time for input: %v\n", time.Since(start))

	return s, nq, q
}
