a = [8,3,2,5,6,1,5,8,9,6,4,2,3]
k = 10
pairs = []
for i in range(len(a)-1):
	for j in range(i+1, len(a)):
		if a[i] + a[j] == k:
			pairs.append((a[i],a.pop(a[j])))
			j -= 1