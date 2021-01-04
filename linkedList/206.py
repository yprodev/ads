
# [AUTHOR] Ravikanth
# [DESCRIPTION] Simple python iterative solution
def reverseList(self, head):
        first = head
        current = None
        previous = None
        while first:
            current = first
            first = first.next
            current.next = previous
            previous = current
        return current

# [COMMENT FROM]: serpol
def reverseList(self, head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

# ===================================================================================

# [AUTHOR] moonlight16
# [DESCRIPTION] Simple in-place Python solution
# [AUTHORS' NOTES]
"""
Your initial instinct might be to iterate through and store values in a stack (list in Python). Then you would have to iterate through again and pop off items off the stack and build a new linked list in reverse order (a stack data structure will naturally help you do that). However, storing the stack structure and building a new linked list data structure would result in O(n) space complexity. So you'll want to think of a way to do this in-place while iterating through the linked list (yielding O(1) space complexity).

You can do this by reversing the links of the existing linked list. As you traverse the linked list you'll want to keep track of the previous node, and modify the next point of the current node to point to the previous node. But what happens if you just modify the next pointer to point to the previous node? You'll lose the pointer to the next node. So you'll also want to keep track of the next node itself.

Here's the Python solution in-place keeping track of the previous and next nodes.
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        return prev


# ===================================================================================

# [AUTHOR] Danny7226
# [DESCRIPTION] Python iteratively and recursively
"""
Iteratively with runtime O(n), extra space O(1).
"""
 # iteratively
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        ptr = head
        while ptr:
            reverse, reverse.next, ptr = ptr, reverse, ptr.next
        return reverse
"""
Recursively with runtime O(n), extra space O(n) as we need stack when doing recursion
"""
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    N = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return N


# ===================================================================================

# [AUTHOR] gabbu
# [DESCRIPTION] Python solution with detailed explanation
"""
Iterative Solution
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
"""
Recursive Solution
"""
class Solution(object):
    def helper(self, root):
        if root is None:
            return None, None
        if root.next is None:
            return root, root
        head, tail = self.helper(root.next)
        tail.next = root
        root.next = None
        return head, root
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head, tail = self.helper(head)
        return head


# ===================================================================================

# [AUTHOR] Me
# [DESCRIPTION] First working iterative solution
# [ISSUES]
#	Basic knowledge in Python 3.
#	Issues with the last node ---> issues with understanding that while loop is stopped
#	on the one item before the last one.
#	Issues with submition because of another edge case.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # [EDGE CASE] Handle first node None case
        if head is None or head.next is None:
            return head

        pointer = head
        nextNode = head.next
        prevNode = None

        while nextNode:
            pointer.next = prevNode
            prevNode = pointer
            pointer = nextNode
            nextNode = nextNode.next

        # [EDGE CASE] Handle last node
        pointer.next = prevNode
        prevNode = pointer

        return prevNode