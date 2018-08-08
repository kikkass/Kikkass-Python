def find_break(arr):

	if len(arr) > 2:
		mid = len(arr)//2

		if (arr[mid-1] - arr[mid] > 0) and (arr[mid] - arr[mid+1] > 0):
			return find_break(arr[mid+1:])
		elif (arr[mid-1] - arr[mid] < 0) and (arr[mid] - arr[mid+1] < 0):
			return find_break(arr[:mid-1])
		else:
			return arr[mid]
	else:
		return arr[0]

a = [19,13,12,8,7,2,3,4,5,6]
bp = find_break(a)
print(bp)