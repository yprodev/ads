class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))

	# O(e + v) time | O(v) space
	def breadthFirstSearch(self, array):
		queue = [self]

		while len(queue) > 0:
			current = queue.pop(0) # FIFO
			array.append(current.name)

			for child in current.children:
				queue.push(child)

		return array
