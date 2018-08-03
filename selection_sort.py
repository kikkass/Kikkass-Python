''' Implementing selection sort in Python
'''

def selection_sort(arr):

	for i in range(0, len(arr)-1):
		print(arr)
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				arr[j], arr[i] = arr[i], arr[j]
	return arr

input_list = [3,9,8,5,2,4,1,2,9,6,5,7]
print(input_list)
print("************************************")
output_list = selection_sort(input_list)
print("************************************")
print(output_list)