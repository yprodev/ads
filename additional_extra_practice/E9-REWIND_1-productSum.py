# Product Sum task is the task with the special array.
# While iterating through it you need to multiply the
# numbers in it. In case the new array occurs, we sum
# up elements in it and multiply the result by level
# the of depth relative to the main array.


# [ 5, 7, [ 7, -1 ], 3, [ 6, [ -13, 8 ], 4 ] ]
# O(n) time | O(d) space | n - each sub-array + element in it; d - depth
def productSum(array, multiplier = 1):
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier + 1)
		else:
			sum += element

	return sum * multiplier
