package main

import (
    "fmt"
)

func main() {
    num := 10
    var countOfThree, countOfFive int;
    if (num > 0 && num < 300) {
        for i := 1; i < num + 1; i++ {
            countOfFive  += 1
            countOfThree += 1
            if (countOfThree == 3 && countOfFive == 5) {
                fmt.Println("fizzbuzz")
                countOfThree = 0
                countOfFive = 0
            } else if (countOfThree == 3) {
                fmt.Println("fizz")
                countOfThree = 0
            } else if (countOfFive == 5) {
                fmt.Println("buzz")
                countOfFive = 0
            } else {
                fmt.Println(num)
            }
        }
    } else {
        fmt.Println("I dont work with negative and large numbers")
    }
}
