'''
Imports:
	collections.Counter - Count occurance of each letter
	random.shuffle - to shuffle the messages in ballot box
	random.randint - random integer to select the message from list of messages
'''
from collections import Counter
from random import shuffle, randint

'''
Global Variables:
	kingdom_details - This dictionary stores kingdom name and corresponding emblem and it's king as a key value pair. 
	(Assumption : Every kindom as a king)
	messages - list of messages to randomly chose from
'''
kingdom_details = {'space':('gorilla','Shan'),'land':('panda','Lungfu'),'water':('octopus','Sopoctus'),'air':('owl','Lowl'),'ice':('mammoth','Mohammat'),'fire':('dragon','Ondra')}
random_messages = ["Summer is coming","a1d22n333a4444p","oaaawaala","zmzmzmzaztzozh","Go, risk it all","Let's swing the sword together","Die or play the tame of thrones","Ahoy! Fight for me with men and money","Drag on Martin!","When you play the tame of thrones, you win or you die.","What could we say to the Lord of Death? Game on?","Turn us away, and we will burn ou first","Death is so terribly final, while life is full of possibilities.","You Win or You Die","His watch is Ended","Sphinx of black quartz, judge my dozen vows","Fear cuts eeper than swords, My Lord.","Different roads sometimes lead to the same castle.","A DRAGON IS NOT A SLAVE.","Do not waste paper","Go ring all the bells","Crazy Fredrick bought any very exquisite pearl, emerald and diamond jewels.","The quick brown fox jumps over a lazy dog multiple times.","We promptly judged antique ivory buckles for the next prize.","alar Morghulis: All men must die."]

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
		print('{} is currently ruled by {}'.format(self.name,self.ruler.name))
		print('There are {} kingdoms in this universe:'.format(len(self.kingdoms)))
		print("\n{0:<15}| {1:<15}| {2:<15}".format('Kingdom','King','Emblem'))
		print('-'*50,end='')
		print('',*self.kingdoms,sep='\n')

class Allie:
	'''
	This class keeps track of the alies
	'''

	def __init__(self,leader):
		self.members = [leader]		# Every allie will have it's creator as starting member
		self.leader = leader

	def __len__(self):
		return len(self.members)

	def add_member(self,member):
		self.members.append(member)


class Message:
	'''
	This class defins message object
	'''
	def __init__(self,sender,to,message):
		self.sender = sender
		self.to = to
		self.text = message

	def __str__(self):
		return 'From: {}\nTo: {}\n"{}"\n{}'.format(self.sender.name,self.to.name,self.text,'-'*50)

class Ballot:
	'''
	This class holds the ballot box and this will create the message object
	'''
	def __init__(self,round_name,contenders,universe):
		self.messages = []
		self.round = round_name
		for contender in contenders:
			for kingdom in universe.kingdoms:
				if kingdom != contender:
					self.messages.append(Message(contender,kingdom,random_messages[randint(0,len(random_messages)-1)]))

	def __str__(self):
		ballot = ''
		for msg in self.messages:
			ballot += msg.__str__()+'\n'
		return ballot

	def shuffle(self):
		shuffle(self.messages)


def validate_allie(sender,to,allies):
	accept = True
	for allie in allies:
		if to in allie.members:
			accept = False
			break
	if accept:
		print('*** {} has accepted to join {} ***'.format(to.name,sender.name))
		for allie in allies:
			if allie.leader == sender:
				allie.add_member(to)
	else:
		print('!!! {} has declined to join {} !!!'.format(to.name,sender.name))


def validate_message(to,message):

	for letter,count in to.get_letters().items():
		if letter in dict(Counter(message)):
			if count <= dict(Counter(message))[letter]:
				match = True
			else:
				match = False
				break
		else:
			match = False
			break

	return match


'''
Begin game play
'''
my_universe = Universe('Southeros')
my_universe.show_universe()

while my_universe.ruler == None:
	'''
	Any king can chose to be the Ruler until there is no ruler for the universe
	'''

	wannabe_ruler_kingdom = ''

	while True:
		wannabe_ruler_kingdom = input('\nWhich kingdom wants to be the ruler? ').lower()
		if wannabe_ruler_kingdom in kingdom_details.keys():
			break
		else:
			print('No such kingdom exist. Please try again!!')

	'''
	Below condition is used to convert the kingdom name in string to corresponding Kingdom object
	'''
	for kingdom in my_universe.kingdoms:
		if kingdom.name == wannabe_ruler_kingdom:
			wannabe_ruler_kingdom = kingdom

	allie_1 = Allie(wannabe_ruler_kingdom)

	print("\nNow you are The King {0}".format(wannabe_ruler_kingdom.king))
	print('\nYou need the support of atleast 3 more kingdoms to become the ruler of Southeroes.')
	print('What are you waiting for, get started with sending secret messages to other Kingdom My Lord.')

	#send_message(my_universe,wannabe_ruler_kingdom,allie_1)
	for kingdom in my_universe.kingdoms:
		if kingdom != wannabe_ruler_kingdom:
			msg = input("\nWhat's your message to - {}: ".format(kingdom.name)).lower()
			if validate_message(kingdom,msg):
				validate_allie(wannabe_ruler_kingdom,kingdom,[allie_1])
			else:
				print('!!! {} has declined to join {} !!!'.format(kingdom.name,wannabe_ruler_kingdom.name))

	if len(allie_1) > 3:
		my_universe.ruler = wannabe_ruler_kingdom
		print('\nCongragulation!! You are the ruler of this universe')
	else:
		print('\nSorry, you did not get enough support')

'''
Now some random cribbling from other kings
Remove it if not required
'''


contest = []
while not len(contest):
	contest = input("Enter the kingdoms competing to be the ruler\n(Seperated by space)\n: ").lower().split()

	for kingdom in contest:
		if kingdom not in kingdom_details.keys():
			contest.remove()

contest_obj = []
for contender in contest:
	for kingdom in my_universe.kingdoms:
		if kingdom.name == contender:
			contest_obj.append(kingdom)
			break

del contest

allies = []
for kingdom in contest_obj:
	allies.append(Allie(kingdom))


round1 = Ballot('round1',contest_obj,my_universe)

round1.shuffle()

for message in round1.messages:
	print(message)
	if validate_message(message.to,message.text):
		validate_allie(message.sender,message.to,allies)
	else:
		print('!!! {} has declined to join {} !!!'.format(message.to.name,message.sender.name))

print('\nResult after Round 1:')
for allie in allies:
	print("Allies for {} : {}".format(allie.leader,len(allie)))

i = 0
while i < len(allies) - 1:
	if len(allies[i]) < len(allies[i+1]):
		allies.remove(allies[i])
	elif len(allies[i]) > len(allies[i+1]):
		allies.remove(allies[i+1])
	else:
		i += 1

if len(allies) = 1:
	my_universe.ruler = allies[1].leader