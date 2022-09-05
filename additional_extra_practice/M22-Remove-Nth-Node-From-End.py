"""
	F 					S
	0 -> 1 -> 2 -> 3 -> 4
"""

# O(n) time | O(1) space
def removeNthNodeFromEnd(head, n):
	counter = 1
	first = head
	second = head

	while counter <= n:
		second = second.next
		counter += 1

	# Edge case with offset is a head node
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return

	# SECOND.NEXT please, note it is not SECOND POINTER
	while second.next is not None:
		second = second.next
		first = first.next

	first.next = first.next.next
