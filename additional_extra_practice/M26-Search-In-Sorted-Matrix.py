# O(N + M) time | O(1) space
def searchInSortedMatrix(matrix, target):
	row = 0
	col = len(matrix[0]) - 1

	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1

		if matrix[row][col] < target:
			row += 1

		return [row, col]

	return [-1, -1]
