'''Implementing merge sort in Python
'''

def merge(arr_left, arr_right, arr):
	'''This function merges two sorted arrays into oe single sorted array
	'''
	i, j, k = 0, 0, 0

	while i < len(arr_left) and j < len(arr_right):
		if arr_left[i] < arr_right[j]:
			arr[k] = arr_left[i]
			i += 1
			k += 1
		else:
			arr[k] = arr_right[j]
			j += 1
			k += 1

	while i < len(arr_left):
		arr[k] = arr_left[i]
		i += 1
		k += 1

	while j < len(arr_right):
		arr[k] = arr_right[j]
		j += 1
		k += 1

	return arr


def merge_sort(arr):

	if len(arr) > 1:

		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		merge_sort(left)
		merge_sort(right)

		merge(left, right, arr)

		return arr


input_list = [3,6,9,8,4,2,1,7,5]
print(input_list)
print("************************************")
output_list = merge_sort(input_list)
print("************************************")
print(output_list)
