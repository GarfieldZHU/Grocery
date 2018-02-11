package main

import (
	"fmt"
)

type slice []int

func partition(sls slice, low int, high int) int {
	pivot := sls[high]
	i := low-1
	for j:=low; j<high; j++ {
		if(sls[j] <= pivot){
			i++
			sls[i], sls[j] = sls[j], sls[i]
		}
	}
	sls[i+1], sls[high] = sls[high], sls[i+1]

	return i+1
}

func quickSort(sls slice, low int, high int){
	if(low < high){
		mid := partition(sls[:], low, high)
		quickSort(sls[:], low, mid-1)
		quickSort(sls[:], mid+1, high)
	}
}

func (arr slice) qSort(){
	quickSort(arr[:], 0, len(arr)-1)
}

func main(){
	// test case 1
	case1 := slice{9,8,7,6,5,4,3,2,1,0}
	case1.qSort()
	fmt.Println(case1)

	// test case 2
	case2 := slice{5,2,5,7,4,5,9,5,2,5,7}
	case2.qSort()
	fmt.Println(case2)
}