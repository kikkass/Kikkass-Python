'''Implementing merge sort in Python
'''

def merge_sort(arr):

	if len(arr) > 1:

		mid = len(arr) // 2
		left = merge_sort(arr[:mid])
		right = merge_sort(arr[mid:])

		i, j, k = 0, 0, 0

		while i < len(left) and j < len(right):

			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
				k += 1
			else:
				arr[k] = right[j]
				j += 1
				k += 1

		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

		return arr

input_list = [3,9,8,5,2,4,1,2,9,6,5,7]
print(input_list)
print("************************************")
output_list = merge_sort(input_list)
print("************************************")
print(output_list)


