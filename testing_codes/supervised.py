def costFunc(n):
	x = [1,2,3,3,4,4,5,5,6,6]
	y = [2,2,2.5,3.5,2.5,4,3,3.5,3.5,4.5]
	sqr_sum = 0
	for i in range(10):
		sqr_sum += pow(n * x[i] - y[i], 2)
	cost = sqr_sum/20
	return cost

min_cost = 999
j_theta = 0
for theta in [round(x * 0.01,2) for x in range(1, 100)]:
	cost = costFunc(theta)
	if cost < min_cost:
		min_cost = cost
		j_theta = theta

print(j_theta,min_cost)