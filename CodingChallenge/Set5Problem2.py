'''
This is the Python implementation for:
Set 5: Tame of Thrones - Problem2: Breaker Of Chains
'''

'''
Imports:
    collections.Counter - Count occurance of each letter
    random.shuffle - to shuffle the messages in ballot box
    random.randint - random integer to select the message from list of messages
'''
from collections import Counter
from random import shuffle,  randint

'''
Global Variables:
    kingdom_details - This dictionary stores kingdom name and corresponding emblem and it's king as a key value pair. (Assumption : Every kindom as a king)
    random_messages - list of messages to randomly chose from
'''
kingdom_details = {'space': ('gorilla', 'Shan'), 'land': ('panda', 'Lungfu'), 'water': ('octopus', 'Sopoctus'), 'air': ('owl', 'Lowl'), 'ice': ('mammoth', 'Mohammat'), 'fire': ('dragon', 'Ondra')}
random_messages = ["Summer is coming", "a1d22n333a4444p", "oaaawaala", "zmzmzmzaztzozh", "Go,  risk it all", "Let's swing the sword together", "Die or play the tame of thrones", "Ahoy! Fight for me with men and money", "Drag on Martin!", "When you play the tame of thrones,  you win or you die.", "What could we say to the Lord of Death? Game on?", "Turn us away,  and we will burn ou first", "Death is so terribly final,  while life is full of possibilities.", "You Win or You Die", "His watch is Ended", "Sphinx of black quartz,  judge my dozen vows", "Fear cuts eeper than swords,  My Lord.", "Different roads sometimes lead to the same castle.", "A DRAGON IS NOT A SLAVE.", "Do not waste paper", "Go ring all the bells", "Crazy Fredrick bought any very exquisite pearl,  emerald and diamond jewels.", "The quick brown fox jumps over a lazy dog multiple times.", "We promptly judged antique ivory buckles for the next prize.", "alar Morghulis: All men must die."]


class Kingdom:
    '''
    This class creates kingdom objects
    This helps us to scale the number of kindoms in future
    '''
    def __init__(self, name, emblem, king):
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
        return "{0:<15}| {1:<15}| {2:<15}".format(self.name, self.king, self.emblem)


class Universe:
    '''
    This class is used to create an object of univese which then inturn creates object of Kingdom
    '''
    def __init__(self, name, ruler=None, allies=None):
        self.kingdoms = []        # We are starting with epty list. This list will be appended with object of kingdom class as it's ceated
        self.name = name
        self.ruler = ruler
        self.allies = allies
        for kingdom, details in kingdom_details.items():
            self.kingdoms.append(Kingdom(kingdom, details[0], details[1]))

    def show_universe(self):
        '''
        This method displays the current snapshot of the universe
        '''
        print('\nWho is the ruler of {}?'.format(self.name))
        if self.ruler:
            print('--> {}'.format(self.ruler.name))
        else:
            print('--> {}'.format(None))
        print('Allies of ruler?')
        if self.allies:
            for kingdom in self.allies:
                print(kingdom.name,  end=' ')
        else:
            print(None)

    def show_kingdoms(self):
        '''
        This method displays Kingdom name,  King and emblem of all the kingdom in the universe
        '''
        print("\n{0:<15}| {1:<15}| {2:<15}".format('Kingdom', 'King', 'Emblem'))
        print('-'*50, end='')
        print('', *self.kingdoms, sep='\n')


class Allie:
    '''
    This class keeps track of the allies
    '''
    def __init__(self, leader):
        self.members = [leader]        # Every allie will have it's creator as starting member
        self.leader = leader

    def __len__(self):
        '''
        method to return length of an allie object
        '''
        return len(self.members)

    def add_member(self, member):
        '''
        method to add new members to an allie
        '''
        self.members.append(member)


class Message:
    '''
    This class defins message object
    '''
    def __init__(self, sender, to, message):
        self.sender = sender
        self.to = to
        self.text = message

    def __str__(self):
        '''
        This method will return the message in string format.
        Note: This was created for testing, not used in the code anymore.
        '''
        return 'From: {}\nTo: {}\n"{}"\n{}'.format(self.sender.name, self.to.name, self.text, '-'*50)


class Ballot:
    '''
    This class defines a ballot box which holds messages from all the contenders in the race to become the ruler
    Each ballot will have a name (round name).
    Creating an instance of Ballot class will create required instance of message class for each contender by picking a random message from random_messages global list
    '''
    def __init__(self, round_name, contenders, universe):
        self.messages = []
        self.round = round_name
        for contender in contenders:
            '''
            Below loop can be avoided with a single for - if statement but I have expanded for readability
            self.messages = [Message(contender,kingdom,random_messages[randint(0, len(random_messages)-1)]) for kingdom in universe.kingdoms if kingdom != contender]
            '''
            for kingdom in universe.kingdoms:
                if kingdom != contender:
                    self.messages.append(Message(contender, kingdom, random_messages[randint(0, len(random_messages)-1)]))

    def __str__(self):
        '''
        This method displays all the messages in the ballot by calling __str__ of Message class
        PS: This was created for testing. This can be removed if not required
        '''
        ballot = ''
        for msg in self.messages:
            ballot += msg.__str__()+'\n'
        return ballot

    def shuffle(self):
        '''
        This method uses shuffle function of random module to shuffle the list of messages.
        This is required to pick random message from the ballot
        '''
        shuffle(self.messages)

def validate_allie(sender, to, allies):
    '''
    Function to validate if the receiver can join the Allie of sender
    This checks if the reciever (to) is part of any alliance already
    '''
    accept = True
    for allie in allies:
        if to in allie.members:
            accept = False
            break
    if accept:
        for allie in allies:
            if allie.leader == sender:
                allie.add_member(to)


def validate_message(to, message):
    '''
    Function to validate if the message contains each characters required number of times
    '''
    for letter, count in to.get_letters().items():
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

def retain_largest(allies):
    '''
    This is custome algorithm to to retain only those allies in the list of allies which has highest number of members
    '''
    i = 0
    while i < len(allies) - 1:
        if len(allies[i]) < len(allies[i+1]):
            del allies[0:i+1]
            i = 0
        elif len(allies[i]) > len(allies[i+1]):
            allies.remove(allies[i+1])
        else:
            i += 1
    return allies

'''
Create an instance of Universe,  this creates all the required instances of kingdoms
'''
southeros = Universe('Southeros')
southeros.show_universe()
southeros.show_kingdoms()

'''
Accept user input for kingdoms competing to be the ruler
'''
contest = []
while not len(contest):
    # This loop will continue to run until users input atleast one correct kingdom name
    contest = input("\nEnter the kingdoms competing to be the ruler\nUpto 5 kingdoms can participate (seperated by space)\n: ").lower().split()
    contest = list(filter(lambda kingdom: (kingdom in kingdom_details.keys()),contest))

'''
If the user inputs all the six kingdoms, this will lead to an infinite loop.
Inorder to avoid this below two steps are applied:
    1. Remove any duplicate kingdoms
    2. Consider only first 5 unique valid kingdoms
'''
contest = list(set(contest))
contest = contest[0:len(southeros.kingdoms) - 1]

# Now we will convert the kingdom name in string to corresponding kingdom object
contest = list(filter(lambda kingdom: (kingdom.name in contest), southeros.kingdoms))

# Set up the counter to track number of rounds
round_count = 1

while True:
    # Continue the competition untill there is only one allie left

    # Create an allie object for each of the participating kingdoms
    allies = []
    for kingdom in contest:
        allies.append(Allie(kingdom))

    # Create a ballot object for the current round and suffle the messages in the ballot
    ballot = Ballot('Round {}'.format(round_count), contest, southeros)
    ballot.shuffle()

    # Read each message from the shuffled ballot and validate the message
    for message in ballot.messages:
        if validate_message(message.to, message.text):
            # Alliance will be validated only if the message is validated
            validate_allie(message.sender, message.to, allies)

    # Show the result after each round
    print('\nResult after {}:'.format(ballot.round))
    for allie in allies:
        print("Allies for {} : {}".format(allie.leader.name, len(allie)-1))

    # Retain allies with highest number of members
    allies = retain_largest(allies)

    # Check for number of winners. Exit from loop if there is only a single winner
    if len(allies) > 1:
        contest = []
        for allie in allies:
            # Recreate the contest with kingdoms with most number of allies Only these kingdoms will take part in next round
            contest.append(allie.leader)
        round_count += 1
    else:
        southeros.ruler = allies[0].leader
        ruler_allies = list(filter(lambda kingdom: (kingdom != southeros.ruler),  allies[0].members))
        southeros.allies = ruler_allies
        break

# Display the snapshot of Universe after the election
southeros.show_universe()
