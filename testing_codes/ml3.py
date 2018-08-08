import numpy as np

input = np.array([[1,2,2,3,4,4,5,6,7,7,8,8,9]])
output = np.array([[3,2,4,4,3,5,4,4,4,5,5,6,5]])

theta0 = 0
theta1 = 0
error = 999
alpha = 0.01

def calc_cost(t0,t1):
    matrix1 = np.r_[[np.ones(input.size)],input]
    theta = np.array([[t0],[t1]])
    hp = matrix1.T.dot(theta)
    diff = hp - output.T
    difr0 = diff.sum()
    difr1 = (diff * input.T).sum()
    cost =  diff.T.dot(diff) / (input.size * 2)
    t0 = t0 - (alpha / input.size) * difr0
    t1 = t1 - (alpha / input.size) * difr1
    return (cost.sum(),t0,t1)

def think(num):
    return (theta0 + theta1 * num)

while True:
    cost,t0,t1 = calc_cost(theta0,theta1)
    if error < cost:
        print("********************************")
        print("Minimum error: {}".format(error))
        print("Theta 0 : {}\nTheta 1: {}".format(theta0,theta1))
        break
    else:
        error,theta0,theta1 = cost,t0,t1

for i in range(11):
    print(think(i))
