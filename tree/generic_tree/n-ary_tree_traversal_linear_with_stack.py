# 589: N-ary Tree Preorder Traversal

def preorder(self, root):
	if root is None: # Work with only current incomming node
		return

	result = []
	stack = []
	stack.append(root) # Add to stack right away

	while stack: # While we have stack
		node = stack.pop() # Remove and return the last item
		result.append(node.val) # Add to result list
		for i in node.children[::-1]: # Get this nodes' children and reverse it, removing the root (-1)
			stack.append(i) # Append each item of the reversed order

	return result


def preorder(self, root):

	order = list()
	if root is None:return order
	stack1 = []
	stack2 = []
	stack1.append(root)
	while stack1:
		curr = stack1.pop()
		order.append(curr.val)
		for child in curr.children:
			stack2.append(child)
		while stack2:
			stack1.append(stack2.pop())

	return order