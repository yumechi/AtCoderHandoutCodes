package main
import "fmt"

func main() {
	var i int
	fmt.Scan(&i)
	fmt.Println(i)
	for cnt := 0; cnt < i; cnt++ {
		fmt.Println(1)	
	}
}