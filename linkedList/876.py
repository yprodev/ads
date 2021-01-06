# [AUTHOR] lee215
# [DESCRIPTION] [C++/Java/Python] Slow and Fast Pointers

# [NOTES] C++:
"""
ListNode* middleNode(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next)
        slow = slow->next, fast = fast->next->next;
    return slow;
}

"""

# [NOTES] Java:
"""
public ListNode middleNode(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
"""

# [NOTES] Python:

def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ===================================================================================

# [AUTHOR] Huayra
# [DESCRIPTION] Python one pass
# [NOTES]
"""
Fast pointer runs twice as fast than slow pointer, which will land slow to the middle when fast reaches the end.
O(n) Time / O(1) Space
"""
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# ===================================================================================

# [AUTHOR] brianchiang_tw
# [DESCRIPTION] Python O(n) by two-pointers 90%+ [w/ Diagram]
# [NOTES] Python O(n) by two-pointers

"""
Think of two pointers technique with slow runner and fast runner.

Both slow runner and fast runner are initialized to head node.

Each iteration, fast runner moves two steps forward while the slow one moves one steps only.

When fast runner meets the empty node (i.e., NULL) on the tail, the slow one will be right on the node of midpoint.
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow, fast = head, head

        while fast:

            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break

            slow = slow.next

        return slow

# ===================================================================================


# [AUTHOR] Me
# [DESCRIPTION] First working iterative solution
# [ISSUES]
#	Hard to understand fully how to work with re-assigned variables
#	Hard to realize how to work with self-referenced variable
#	Hard to understand iterative flow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        currNode = head
        midNode = head
        size = 1

        if head.next is None:
            return head

        while currNode.next:
            size += 1
            currNode = currNode.next

            if (size % 2) == 0:
                midNode = midNode.next

        return midNode