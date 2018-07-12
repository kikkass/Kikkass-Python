from os import system
from sys import platform

def clear_screen():
	if platform == 'win32':
		system('cls')
		system('MODE 150,30')
	else:
		system('clear')

def select_symbol():
	p1 = ''
	while p1 not in ['X','O'] :
		if p1 == '':
			p1 = input('Player 1: Please select your symbol (X or O) - ')
		else:
			p1 = input('Please select a valid symbol (X or O) - ')
	if p1 == 'X':
		return ('X','O')
	else:
		return ('O','X')

def display(p):

	clear_screen()
	for i in range(2,-1,-1):
		print('\t\t {} | {} | {} '.format(p[(i*3)+1],p[(i*3)+2],p[(i*3)+3]))
		if i != 0:
			print('\t\t-----------')

def take_input(pnum,sym):

	getinput = True
	while getinput:
		num = int(input('Player {}: Please select your marking area:_'.format(pnum)))
		if num < 1 or num > 9 or num in marked:
			print('--> Wrong Seletion!!\n--> Please select a number between 1 and 9 which is not marked.\nMarked : {}'.format(marked))
			getinput = True
		else:
			marked.append(num)
			gamelist[num] = sym
			print('\n')
			display(gamelist)
			getinput = False

def show_result(symbol):

	if symbol == player1:
		win_count['p1'] += 1
		result =1
		winner = 'Player 1'
	elif symbol == player2:
		win_count['p2'] += 1
		result = 1
		winner = 'Player 2'
	else:
		result = 0

	if result == 1:
		print('{0}{1:^150}{0}'.format('-' * 150,winner + ' won!!'))
	else:
		print('{0}{1:^150}{0}'.format('-' * 150,'*Game Levelled*'))

	play = input(">> Press any key to continue. To quit press 'q'")
	return play

clear_screen()

print('\n{1}\n{0:^140}\n{1}'.format('*** Welcome to classic Tick-Tack game ***','-' * 150))
print('{0:^140}'.format('Rules:'))
print('{0:^140}'.format('\t1). 2 players will play against each other on a single system.'))
print('{0:^140}'.format('\t2). One of the player has to chose his symbol (X or O). Other player will be assigned with other symbol.'))
print('{0:^140}'.format('\t3). Each player will mark his choice on the box alternatively untill one of the player wins or there is no place left to mark.'))
print('{0:^140}\n{1}'.format('\t4). A player wins if he/she manage to mark all the 3 cells in a row or in a column or diagonally with their symbol.','-' * 150))

player1,player2 = select_symbol()

win_count = {'p1':0,'p2':0}

print('\n{0:^140}\n'.format('Player 1 - ' + player1 + ' | ' + player2 + ' - Player 2'))

play = input(">> Press any key to continue. To quit press 'q'")

while play != 'q':

	gamelist = ['#','1','2','3','4','5','6','7','8','9']
	marked = []
	win_combi = [(1,2,3),(1,4,7),(1,5,9),(2,5,8),(3,5,7),(3,6,9),(4,5,6),(7,8,9)]

	display(gamelist)

	result_displayed = False

	for i in range (1,10):

		done =0
		if i%2 != 0:
			take_input(1,player1)
		else:
			take_input(2,player2)

		for a,b,c in win_combi:
			if gamelist[a] != ' ' and (gamelist[a] == gamelist[b] == gamelist[c]):
				done = 1
				play = show_result(gamelist[a])
				result_displayed = True
				break

		if done == 1:
			break
	if not result_displayed:
		play = show_result('')

print ('\n{0:^150}'.format('** END OF GAME **'))
print('{0}{1:^150}{2:^150}'.format('-' * 150,'Final scores:','Player 1: ' + str(win_count['p1']) + ' | ' + str(win_count['p2']) + ' :Player2'))
