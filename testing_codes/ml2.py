x = [1,2,2,3,4,4,5,6,7,7,8,8,9]
y = [3,2,4,4,3,5,4,4,4,5,5,6,5]

alpha = 0.01

theta0 = 0
theta1 = 0

error = 999999


def cost_func(t0,t1):

	sqr_sum = 0;
	for i in range(len(x)):
		hp = t0 + (t1 * x[i])
		diff = hp - y[i]
		sqr_sum += pow(diff,2)

	cost = sqr_sum / (2 * len(x))
	return cost

def find_theta(t0,t1):
	difr_0 = 0
	difr_1 = 0
	for i in range(len(x)):
		hp = t0 + (t1 * x[i])
		diff = hp - y[i]
		difr_0 += diff
		difr_1 += (diff * x[i])
	new_t0 = t0 - (alpha / len(x)) * difr_0
	new_t1 = t1 - (alpha / len(x)) * difr_1
	return (new_t0,new_t1)

while error > cost_func(theta0,theta1):
	error = cost_func(theta0,theta1)
	print(error)
	theta0,theta1 = find_theta(theta0,theta1)
	print(theta0,theta1)

print('************************************************')
print('Final cost: {}'.format(error))
print(theta0,theta1)




