# QuickSort - Introduction to Algorithm version

def partition(arr, low, high):
	# select the last element of slice as pivot
	pivot = arr[high]
	i = low-1
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def quickSort(arr, low, high):
	if(low < high):
		mid = partition(arr, low, high)
		quickSort(arr, low, mid-1)
		quickSort(arr, mid+1, high)

def qSort(arr):
	toSort = arr
	quickSort(toSort, 0, len(toSort)-1)
	return toSort

# -------------------------------------- #

# Quicksort - another common version

def partition2(arr, low, high):
	pivot = arr[high]
	i, j = low, high
	while(i<j):
		while i<j and arr[i] <= pivot:
			i += 1
		arr[j] = arr[i]
		while i<j and arr[j] >= pivot:
			j -= 1
		arr[i] = arr[j]
	
	arr[i] = high
	return i


def quickSort2(arr, low, high):
	if low<high:
		mid = partition2(arr,low,high)
		quickSort2(arr, low, mid-1)
		quickSort2(arr, mid+1, high)


def qSort2(arr):
	toSort = arr
	quickSort2(toSort, 0, len(toSort)-1)
	return toSort
# -------------------------------------- #


# Unit test
if __name__ == "__main__":
	# case 1
	case_1 = [9,8,7,6,5,4,3,2,1,0]
	sorted = qSort(case_1)
	case_1.sort()
	assert(cmp(case_1, sorted)==0)

	# case 2
	case_2 = [5,2,5,7,4,5,9,5,2,5,7]
	sorted = qSort(case_2)
	case_2.sort()
	assert(cmp(case_2, sorted)==0)

	# case 3
	case_3 = [9,8,7,6,5,4,3,2,1,0]
	sorted = qSort2(case_3)
	case_3.sort()
	assert(cmp(case_3, sorted)==0)

	# case 4
	case_4 = [5,2,5,7,4,5,9,5,2,5,7]
	sorted = qSort2(case_4)
	case_4.sort()
	assert(cmp(case_4, sorted)==0)