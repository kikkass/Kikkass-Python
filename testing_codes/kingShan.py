'''
Imports:
	collections.Counter - Count occurance of each letter
'''
from collections import Counter

'''
Global Variables:
	kingdom_details - This dictionary stores kingdom name and corresponding emblem and it's king as a key value pair. 
	(Assumption : Every kindom as a king)
'''
kingdom_details = {'Space':('gorilla','Shan'),'Land':('panda','Lungfu'),'Water':('octopus','Sopoctus'),'Air':('owl','Lowl'),'Ice':('mammoth','Mohammat'),'Fire':('dragon','Ondra')}

class Kingdom:
	'''
	This class creates kingdom objects
	This helps us to scale the number of kindoms in future
	'''
	def __init__(self,name,emblem,king):
		self.name = name
		self.emblem = emblem
		self.king = king

	def get_letters(self):
		'''
		This method will return a dictionary containing letters that are ocuring and number of occurance in the emblem of called class
		'''
		return dict(Counter(self.emblem))

	def __str__(self):
		'''
		This method will return the called Kingdom object in string format for display
		'''
		return "{0:<15}| {1:<15}| {2:<15}".format(self.name,self.king,self.emblem)

class Universe:
	'''
	This class is used to create an object of univese which then inturn creates object of Kingdom
	'''
	def __init__(self,name,ruler=None):
		self.kingdoms =[]		# We are starting with epty list. This list will be appended with object of kingdom class as it's ceated
		self.name = name
		self.ruler = ruler
		for kingdom,details in kingdom_details.items():
			self.kingdoms.append(Kingdom(kingdom,details[0],details[1]))

	def show_universe(self):
		'''
		This method displays the current snapshot of the universe
		'''
		print('\nWelcome to the Universe of {}'.format(self.name))
		print('{} is currently ruled by {}'.format(self.name,self.ruler))
		print('There are {} kingdoms in this universe:'.format(len(self.kingdoms)))
		print("\n{0:<15}| {1:<15}| {2:<15}".format('Kingdom','King','Emblem'))
		print('-'*50,end='')
		print('',*self.kingdoms,sep='\n')

class Allie:
	'''
	This class keeps track of the alies
	'''

	def __init__(self,creator):
		self.members = [creator]		# Every allie will have it's creator as starting member
		self.creator = creator

	def __len__(self):
		return len(self.members)

	def add_member(self,member):
		self.members.append(member)






def validate_allie(message,kingdom,allie):

	print('Sending your message to King {} of {}'.format(kingdom.king,kingdom.name))

	for letter,count in kingdom.get_letters().items():
		if letter in dict(Counter(message)):
			if count <= dict(Counter(message))[letter]:
				match = True
			else:
				match = False
				break
		else:
			match = False
			break

	if match:
		print('{} accepted your messgae and joing your allie**'.format(kingdom.name))
		allie.add_member(kingdom.name)
	else:
		print('{} declined your messgae!!'.format(kingdom.name))





def send_message(universe,wannabe_ruler,allie):

	for kingdom in universe.kingdoms:
		if kingdom.name != wannabe_ruler:
			msg = input("What's your message to - {}: ".format(kingdom.name))
			validate_allie(msg,kingdom,allie)




'''
Begin game play
'''
my_universe = Universe('Southeros')
my_universe.show_universe()

wannabe_ruler_kingdom = ''

while True:
	wannabe_ruler_kingdom = input('\nKing of which Kingdom wants to be the ruler? ')
	if wannabe_ruler_kingdom in kingdom_details.keys():
		break
	else:
		print('No such kingdom exist. Please try again!!')

allie_1 = Allie(wannabe_ruler_kingdom)

print("\nNow you are - {0}".format(kingdom_details[wannabe_ruler_kingdom][1]))
print('\nYou need the support of atleast 3 more kingdoms to become the ruler of Southeroes.')
print('What are you waiting for, get started with sending secret messages to other Kingdom My Lord.')

send_message(my_universe,wannabe_ruler_kingdom,allie_1)

if len(allie_1) > 3:
	print('Congragulation!! You are the ruler of this universe')
else:
	print('Sorry, you did not get enough support')

