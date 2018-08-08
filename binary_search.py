'''Implementing inay search in Python
'''

def binary_search(arr, num):

	if len(arr) < 2 and arr[0] != num:
		return False
	elif len(arr) < 2 and arr[0] == num:
		return True

	mid = len(arr)//2

	if num < arr[mid]:
		return binary_search(arr[0:mid], num)
	elif num > arr[mid]:
		return binary_search(arr[mid+1:], num)
	else:
		return True

array = [2,4,5,7,5,3,2,3,4,5,67,78,7,8,8,7,6,54,3,2,232,3,4,45,56,66,76,67,64,3,72,2,23,2]
array.sort()
print(binary_search(array,4))