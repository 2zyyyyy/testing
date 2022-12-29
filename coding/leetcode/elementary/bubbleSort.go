package main

import "fmt"

// Bubble Sort(Go)
func bubble_sort(nums []int) []int {
	n := len(nums)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if nums[j] > nums[j+1] {
				// 交换(>用于控制排序规则)
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
	return nums
}

func main() {
	nums := []int{46, 43, 50, 49, 9, 16, 43, 40, 6, 20}
	fmt.Println("原始数据：", nums)
	nums = bubble_sort(nums)
	fmt.Printf("排序后数据：%d\n", nums)
}
