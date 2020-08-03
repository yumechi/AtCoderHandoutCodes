package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	_ = sc.Scan()
	i, _ := strconv.ParseInt(sc.Text(), 10, 64)
	if i >= 30 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
