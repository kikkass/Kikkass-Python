''' Implementing single linked list in Python
'''

class Node:
	''' This class repesents each node
	Each node will have it's data and link to next node
	'''
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node


class LinkedList:
	'''This class represents a lnked list
	Ths holds node elements of this list
	'''
	def __init__(self):
		'''Linkd list initalisation function
		'''
		self.head = None

	def is_empty(self):
		''' Function to check if the node is empty
		'''
		return self.head == None

	def add_at_front(self, data):
		''' Functon to add a node at the begining
		'''
		# Create a new node and assign it to head of the list
		# Pass current head as next item for new node
		self.head = Node(data, self.head)

	def add_at_end(self, data):
		''' Function to add a node at the end of the list
		'''
		# Check if the node is empty
		if self.is_empty():
			self.head = Node(data, self.head)
		else:
			node = self.head
			while node.next_node:
				node = node.next_node
			node.next_node = Node(data, node.next_node)

	def delete(self, key):
		

	def __str__(self):
		''' Function to print list in string format
		'''
		if self.is_empty():
			return "LIST is empty!"
		else:
			node = self.head
			print_list = ''
			while node.next_node:
				print_list += '{} --> '.format(node.data)
				node = node.next_node
			print_list += '{} \\'.format(node.data)
			return print_list

link_list = LinkedList()

print(link_list)

print(link_list.is_empty())

link_list.add_at_end(20)
link_list.add_at_front(10)
link_list.add_at_end(30)

print(link_list.is_empty())

print(link_list)

