def print_spiral(matrix):
	''' Function to print matrix in spiral form
	'''

	# set variables to track firts row, firts column and last row and last column
	fr, fc = 0, 0
	lr, lc = len(matrix) - 1, len(matrix[0]) - 1

	print('fr - {}\nfc - {}\nlr - {}\nlc - {}'.format(fr,fc,lr,lc))

	spiral = []

	while lr > fr and lc > fc:

		for i in range(fc, lc+1):
			spiral.append(matrix[fr][i])
		fr += 1
		print(spiral)

		for i in range(fr, lr+1):
			spiral.append(matrix[i][lc])
		lc -= 1
		print(spiral)

		for i in range(lc, fc - 1, -1):
			spiral.append(matrix[lr][i])
		lr -= 1
		print(spiral)

		for i in range(lr, fr -1, -1):
			spiral.append(matrix[i][fc])
		fc += 1
		print(spiral)

	print(spiral)

matrix1 = [[1,2,3,4],[5,6,7,8]]
print_spiral(matrix1)

# print(' '.join(print_spiral(matrix1)))
