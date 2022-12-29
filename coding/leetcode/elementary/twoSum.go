// 两数之和
package main

import "fmt"

func twoSum(nums []int, target int) []int {
	n := len(nums)
	for i, v := range nums {
		for j := i + 1; j < n; j++ {
			if v+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return nil
}

func main() {
	n := []int{0, 1, 3, 5, 7, 9, 10, 13, 10}
	t := 10
	fmt.Println(twoSum(n, t))
}
