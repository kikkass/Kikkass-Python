''' Program to check if two srings are anagram
'''

def partition(arr, low, high):
	''' Partition function for quick sort
	'''
	pivot = arr[high]
	partition_index = low

	for i in range(low, high):
		if arr[i] <= pivot:
			arr[partition_index], arr[i] = arr[i], arr[partition_index]
			partition_index += 1
	arr[partition_index], arr[high] = pivot, arr[partition_index]
	return partition_index



def quick_sort(arr, low, high):
	''' Quick sort function
	'''
	if low < high:
		p_index = partition(arr, low, high)
		quick_sort(arr, low, p_index - 1)
		quick_sort(arr, p_index + 1, high)
		return arr



def is_anagram(str1, str2):

	if len(str1) != len(str2):
		return False

	str1 = quick_sort(list(str1), 0, len(str1)-1)
	str2 = quick_sort(list(str2), 0, len(str2)-1)

	for i in range(len(str1)):
		if str1[i] != str2[i]:
			return False

	return True

# get input from user
string1 = input('String 1: ')
string2 = input('String 2: ')

if is_anagram(string1, string2):
	print("Anagram")
else:
	print("Not Anagram")