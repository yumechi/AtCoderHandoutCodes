package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	sc.Split(bufio.ScanWords)

	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	sc.Scan()
	d, _ := strconv.Atoi(sc.Text())

	var ans int
	for i := 0; i < n; i++ {
		sc.Scan()
		f, _ := strconv.Atoi(sc.Text())
		sc.Scan()
		s, _ := strconv.Atoi(sc.Text())
		if d >= int(math.Ceil(math.Sqrt(float64((f*f)+(s*s))))) {
			ans++
		}

	}
	fmt.Println(ans)
}
