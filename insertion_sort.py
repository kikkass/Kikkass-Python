''' Implementing insertion sort in Python
'''

def insertion_sort(arr):

	for i in range(1, len(arr)):
		print(arr)
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			arr[j-1], arr[j] = arr[j], arr[j-1]
			j -= 1
	return arr

input_list = [3,9,8,5,2,4,1,2,9,6,5,7]
print(input_list)
print("************************************")
output_list = insertion_sort(input_list)
print("************************************")
print(output_list)
