''' Implementing an undirected graph in python
using Adjecensy matrix'''

class Graph:
	''' This class represents the graph
	a graph size is the number of nodes
	'''
	def __init__(self, size):
		''' Initialize the graph
		'''
		self.adj = []
		for i in range(size):
			self.adj.append([0 for j in range(size)])
		self.size = size

	def add_edge(self, org, dest):
		''' Add an edge between an origin and the destination
		As it's an undirected graph, it will also add the edge between dest and origin
		'''
		if (org > 0 and org <= self.size) and (dest > 0 and dest <= self.size):
			self.adj[org-1][dest-1] = 1
			self.adj[dest-1][org-1] = 1
		else:
			print("Trying to add an invalid edge!!")

	def delete_edge(self, org, dest):
		''' Delete an existing edge between an origin and the destination
		As it's an undirected graph, it will also delete the edge between dest and origin
		'''
		if (org > 0 and org <= self.size) and (dest > 0 and dest <= self.size):
			self.adj[org-1][dest-1] = 0
			self.adj[dest-1][org-1] = 0
		else:
			print("Trying to add an invalid edge!!")

	def __str__(self):
		''' Function to print the Graph
		'''
		print_graph = ''
		for i in range(self.size):
			print_graph += '\n' + str(self.adj[i])
		return print_graph

graph = Graph(7)

graph.add_edge(5,7)
graph.add_edge(7,2)
graph.add_edge(2,5)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(4,5)
graph.add_edge(6,4)

print(graph)
