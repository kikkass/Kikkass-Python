
def distribute(balls,players):

	balls.sort()

	start = 0

	for i in range(1, len(balls) - players +1):
		if balls[i + players - 1] - balls[i] < balls[start + players - 1] - balls[start]:
			start = i

	return balls[start:start+players]

num_bags = 10
balls = [2,5,7,9,12,13,21,4,6,4]
players = 4

distrubuted = distribute(balls,players)
print(distrubuted)

