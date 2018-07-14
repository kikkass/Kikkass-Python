'''
This is the Python implementation for:
Set 5: Tame of Thrones - Problem1: A Golden Crown
Unlike problem statement where King Shan of Space wants to be the ruler,
this program takes any kingdom as input who aspires to be the ruler.
Assumption: Every Kingdom has a king
'''

'''
Imports:
    collections.Counter - Count occurance of each letter
'''
from collections import Counter

'''
Global Variables:
    kingdom_details - Stores Kingdom name as key and emblem and king as values
'''
kingdom_details = {'space': ('gorilla', 'Shan'), 'land': ('panda', 'Lungfu'), 'water': ('octopus', 'Sopoctus'), 'air': ('owl', 'Lowl'), 'ice': ('mammoth', 'Mohammat'), 'fire': ('dragon', 'Ondra')}


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


def validate_allie(sender, to, allies):
    '''
    Function to validate if the receiver can join the Allie of sender
    Note: This function is created to support even Problem2
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


'''
Create an instance of Universe,  this creates all the required instances of kingdoms
'''
southeros = Universe('Southeros')
southeros.show_universe()
southeros.show_kingdoms()

'''
-------------------------------------------------------------------------------
Beginning of Problem1: Any one kingdom can opt to be the ruler of the universe.
That kingdom will then send secret messages to other kingdom seeking alligance.
-------------------------------------------------------------------------------
'''

while not southeros.ruler:
    # This loop will run untill there is a ruler for the universe
    to_be_ruler = ''
    while True:
        # This loop will continue untill user enters correct kingdom name (Case insensitive)
        to_be_ruler = input('\nWho wants to be the ruler? ').lower()
        if to_be_ruler in kingdom_details.keys():
            break
        else:
            print('No such kingdom exist. Please try again!!')

    '''
    Below condition is used to convert the kingdom name in string to corresponding Kingdom object.
    Note - We can acive the same in single line. I have expanded for readability.
    to_be_ruler = [kingdom for kingdom in southeros.kingdoms if kingdom.name = to_be_ruler][0]
    '''
    for kingdom in southeros.kingdoms:
        if kingdom.name == to_be_ruler:
            to_be_ruler = kingdom

    # Create an instance of Allies for the selected kingdom
    allie = Allie(to_be_ruler)

    # Prompt user to input message for each kingdom
    for kingdom in southeros.kingdoms:
        # below condition disables sending self message
        if kingdom != to_be_ruler:
            msg = input("\nYour message to - {}: ".format(kingdom.name)).lower()
            if validate_message(kingdom, msg):
                # If the message is validated to true, then Allies will be validated
                # Note: We are passing allie as a list because the validate_allie() function is designed to work with array of allies for problem 2
                validate_allie(to_be_ruler, kingdom, [allie])

    # Check if the Kingdom has enough support to be the ruler
    if len(allie) > 3:
        southeros.ruler = to_be_ruler
        southeros.allies = [member for member in allie.members if member != to_be_ruler]

    # Displaying the snapshot of Universe at the end of iteration
    southeros.show_universe()