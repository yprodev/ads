# ==================== Variant 1 ====================
# Iterative
# O(n) time | O(n) space
def spiralTraverse(array):
	result = []
	startRow, endRow = 0, len(array) - 1
	startCol, endCol = 0, len(array[0]) - 1

	# Use <= for the flat array where startRow can
	# be equal to the endRow. The same for columns.
	while startRow <= endRow and startCol <= endCol:
		# endCol + 1 - means inclusive
		for col in range(startCol, endCol + 1):
			result.append(array[startRow][col])

		# startRow + 1 - avoid double count
		# endRow + 1 - include the last row
		for row in range(startRow + 1, endRow + 1):
			result.append(array[row][endCol])

		for col in reversed(range(startCol, endCol)):
			result.append(array[endRow][col])

		for row in reversed(range(startRow + 1, endRow)):
			result.append(array[row][startCol])

		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1

	return result


# ==================== Variant 1 ====================
# Recursive
# O(n) time | O(n) space
def spiralTraverseRec(array):
	result = []

	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)

	return result

def spiralFill(array, startRow, endRow, startCol, endCol, results):
	if startRow > endRow or startCol > endCol:
		return

	for col in range(startCol, endCol + 1):
		result.append(array[startRow][col])

	# startRow + 1 - avoid double count
	# endRow + 1 - include the last row
	for row in range(startRow + 1, endRow + 1):
		result.append(array[row][endCol])

	for col in reversed(range(startCol, endCol)):
		result.append(array[endRow][col])

	for row in reversed(range(startRow + 1, endRow)):
		result.append(array[row][startCol])

	spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, results)














