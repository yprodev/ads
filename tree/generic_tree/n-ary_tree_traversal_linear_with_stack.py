"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = childre
"""

# [DESCRIPTION] N working solution with help
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return []

        values = []
        stack = [root]

        while stack:
            current = stack.pop()
            values.append(current.val)
            if current.children:
                stack = stack + current.children[::-1]

        return values


# [DESCRIPTION] First not working solution.
# Main issues:
# 	The main problem is basic knowledge in Python3.
# 	Lack of understanding the iterative and recursive approaches
# 		Comment: Why do you use stack (initialize it) if you create
#				 some recursive function. There is no goal to just store
#				 stack in memory and use it with recursion.
#	Result of the previous: interlinks emerged.

#         values = []
#         if not root:
#             return values

#         def trace(node):
#             stack = []

#             if not node.children:
#                 values.append(node.val)
#                 stack = stack[:-1]

#             while node.children:
#                 stack = stack + node.children[::-1]
#                 trace(stack[len(stack) - 1])

#         trace(root)

#         return values
