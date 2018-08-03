''' Implementing bubble sort in python
'''

def bubble_sort(arr):
	for i in range(len(arr) - 1):
		# Keep track of total swaps
		swap_count = 0
		for j in range (len(arr) - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap_count += 1
		print(arr)
		# If there is no swap then the array is already sorted
		if swap_count == 0:
			break
	return arr

input_list = [3,9,8,5,2,4,1,2,9,6,5,7]
print(input_list)
print("************************************")
output_list = bubble_sort(input_list)
print("************************************")
print(output_list)
