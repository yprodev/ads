'''
[
	[ 1,  2,  3, 4],
	[12, 13, 14, 5],
	[11, 16, 15, 6],
	[10,  9,  8, 7],
]

	to become

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

'''

# O(n) time | O(n) space
def spiralTraverseInc(array):
	result = []

	startRow, endRow = 0, len(array) - 1
	startCol, endCol = 0, len(array[0]) - 1

	# we use <= because the final step of the traversal might be
	# a flat line.
	while startRow <= endRow or startCol <= endCol:
		# Perimeter # 1
		# We want for the endCol to be inclusive
		# that is why we do encCol + 1
		for col in range(startCol, endCol + 1):
			result.append(array[startRow][col])

		# Perimeter # 2
		# We increase startRow by 1, because we already have
		# value 4 after the first traversal, and we want
		# to start from value 5
		for row in range(startRow + 1, endRow + 1):
			result.append(array[row][endCol])

		# Perimeter # 3
		# When we traverse the perimeter #3 we need
		# not to iclude value 7 twice. So, we need to
		# not increment endCol. Also we need to do this 
		# traversal in the reversed order to go spiral
		for col in reversed(range(startCol, endCol)):
			result.append(array[endRow][col])

		# Perimeter # 4
		# We need to skip the very first value when we
		# started a traversal. So, we need to start
		# from startRow + 1
		for row in reversed(range(startRow + 1, endRow)):
			result.append(array[row][startCol])

		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1

	return result


# O(n) time | O(n) space
def spiralTraversalRec(array):
	result = []

	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)

	return result


def spiralFill(array, startRow, endRow, startCol, endCol, results):
	if startRow > endRow or startCol > endCol:
		return

	for col in range(startCol, endCol + 1):
		result.append(array[startRow][col])

	for row in range(startRow + 1, endRow + 1):
		result.append(array[row][endCol])

	for col in reversed(range(startCol, endCol)):
		result.append(array[endRow][col])

	for row in reversed(range(startRow + 1, endRow)):
		result.append(array[row][startCol])

	spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, results)
