package main

import (
	"fmt"
)

func main() {
	nums := []int{2,7,11,15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println(result)
}

func twoSum(nums []int, target int) []int {
    seen := map[int]int{}

	for i, num := range nums {
		remain := target - num

        if _, ok := seen[remain]; ok {
			return []int{seen[remain], i}
		}

		seen[num] = i
	}

	return []int{};
}
