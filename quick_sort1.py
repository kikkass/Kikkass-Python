'''Implementing quick sort v1.0 - Last item as pivotin Python
'''

def partition(arr, start, end):
	'''This is the core logic of quick sort
	It finds the right place of the pivot element
	'''
	pivot = arr[end]
	partition_index = start

	for i in range(start,end):
		if arr[i] <= pivot:
			# Swap the elements
			arr[i], arr[partition_index] = arr[partition_index], arr[i]
			partition_index += 1
	arr[partition_index], arr[end] = pivot, arr[partition_index]
	return partition_index

def quick_sort(arr, start, end):
	''' This functions finds the partition index
	And it recursively calls qick sort while tehre are more than one element in the segment
	'''
	if start < end:
		p_index = partition(arr, start, end)
		print(p_index)
		print(arr)
		quick_sort(arr, start, p_index - 1)
		quick_sort(arr, p_index + 1, end)


input_list = [3,6,9,8,4,2,1,7,5]
print(input_list)
print("************************************")
quick_sort(input_list, 0, len(input_list)-1)
print("************************************")
print(input_list)
