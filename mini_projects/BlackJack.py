'''
Imports
'''
from random import shuffle
from os import system

suits = ('Spade','Club','Heart','Diamond')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class InsufficientBalanceError(Exception):
	'''
	Custome exception when user enters bet amount higher than available balanve
	'''
	pass

class Card:
	'''
	This class is used to create a Card object which will have Suite and Rank as it's attributes
	'''
	def __init__(self,suit,rank):
		'''
		Initialize the Card object
		'''
		self.suit = suit
		self.rank = rank

	def __str__(self):
		'''
		This method returns the string in 'Rank of Suit' formt when called as print(acrd_object)
		'''
		return self.rank+" of "+self.suit

class Deck:
	'''
	This class creates an object of deck which will inturn creates an object of class for all the 52 cards in the deck
	'''
	def __init__(self):
		'''
		Initialize the deck
		'''
		self.deck = []		#This list will store the card objects. 
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		'''
		This method will print the Deck in string format
		'''
		deck_string = 'Content of the deck:'
		for card in self.deck:
			deck_string += '\n'+card.__str__()
		return deck_string

	def shuffle(self):
		'''
		This method shuffles the current deck
		'''
		shuffle(self.deck)

	def deal(self):
		'''
		This method will take the returns the last card in the deck
		'''
		return self.deck.pop()

class Hand:
	'''
	This class represents a player and also computer dealer
	'''
	def __init__(self):
		'''
		Initialize method for Hand class
		'''
		self.cards = []
		self.value = 0
		self.aces = 0		#This is to keep track and manage aces which are special cards holding dual values

	def add_card(self,card):
		'''
		This method will add a new card to a player. This will be used to assign two cards in the beginning and whenever a player calls Hit
		'''
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		'''
		This method adjust the value of aces if the user has when the total value crosses 21
		'''
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1

class Chips:
	'''
	This class is used to manage players Chips (money)
	'''
	def __init__(self,total=100):
		'''
		Initialize method for Chip class
		'''
		self.total = total
		self.bet = 0

	def win_bet(self):
		'''
		This method will be called when a player wins the bet
		'''
		self.total += self.bet

	def lose_bet(self):
		'''
		This method will be called when a player loses bet
		'''
		self.total -= self.bet

def take_bet(chips):
	'''
	This function is used to take the bet from player
	'''
	while True:
		try:
			chips.bet = int(input('Whats your bet for this round? '))
			if chips.bet > chips.total:
				raise InsufficientBalanceError
			elif chips.bet < 1:
				raise ValueError		# Custom exception
		except ValueError:
			print('\nPlease enter a right bet amount')
		except InsufficientBalanceError:
			print('\nInsufficient Fund')
		else:
			break

def hit(deck,hand):
	'''
	Function to take hit untill they bust. They are called anytime in the game play when the user request for 'Hit'
	Input: Objects of Deck and Hand class
	'''
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	'''
	This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
	If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a while loop later on in our code.
	'''
	global playing

	while True:
		x = input("\nWould you like to Hit or Stand? Enter 'h' or 's' ")

		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print('Player stands. Dealer is playing.')
			playing = False
		else:
			print('Sorry, please try again')
			continue
		break

def show_some(player,dealer):
	'''
	When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible.
	'''
	print("\nDealer's Hand:\n--------------")
	print(" <card hidden>")
	print('',dealer.cards[1])
	print("\nPlayers Hand:\n--------------", *player.cards, sep='\n')

def show_all(player,dealer):
	'''
	At the end of the hand all cards are shown
	'''
	print("\nDealer's Hand:\n--------------", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:\n--------------", *player.cards, sep='\n ')
	print("Player's Hand =",player.value)

def player_busts(chips):
	'''
	Scenario: when user's value cros 21
	'''
	print('\n<< Player bust! >>')
	chips.lose_bet()

def player_wins(chips):
	'''
	Scenario: when user's value is close to 21 than dealer's
	'''
	print('\n<< Player wins! >>')
	chips.win_bet()

def dealer_busts(chips):
	'''
	Scenario: when dealer's value cros 21
	'''
	print('\n<< Dealer bust >>!')
	chips.win_bet()

def dealer_wins(chips):
	'''
	Scenario: when dealer's value is closer to 21 than user's
	'''
	print('\n<< Dealer wins! >>')
	chips.lose_bet()

def push():
	'''
	Scenario: When dealer and player tie
	'''
	print("Dealer and Player tie! It's a Push !")


'''
Game play starts here
'''

system('cls')

# Print an opening statement
print('Welcome to BlackJack! Get close to 21 as you can without going over!\n\
	Dealer hits until she reaches 17.\n\
	Aces count as 1 or 11.')

# Setup a players chip - deafault value is 100
player_chips = Chips()

while player_chips.total > 0:

	# Create a Deck and shuffle
	deck = Deck()
	deck.shuffle()

	# Create a hand object for player and deal two cards to player
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	# Create a hand object for dealer and deal two cards to dealer
	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Take player bet
	take_bet(player_chips)

	# Show the original cards. Hide first card of dealer
	show_some(player_hand,dealer_hand)

	while playing:

		# Prompt the user for hit or stand
		hit_or_stand(deck,player_hand)

		# Show all of players cards after each round. Hide dealers first card
		show_some(player_hand,dealer_hand)

		# If player's hand exceeds 21, run scenarion player_busts()
		if player_hand.value > 21:
			player_busts(player_chips)
			break

	# If player didn't bust, play dealers hand until dealer reaches 17
	if player_hand.value <= 21:

		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		# Show all the cards
		show_all(player_hand,dealer_hand)

		# test for different scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_chips)

		else:
			push()

	# Show players chips after this round
	print("\nPlayers total chips stands at: ",player_chips.total)

	# Ask to play again
	new_game = input("\nWould you like to play another game? Enter 'y' or 'n' ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print('Thanks for playing!')
		break
