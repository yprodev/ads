# O(wh) time | O(n) space
def riverSizes(matrix):
	sizes = []
	visited = [[False for value in row] for row in matrix]

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue

			traverseNode(i, j, matrix, visited, sizes)

	return sizes


def traverseNode(row, col, matrix, visited, sizes):
	currentRiverSize = 0;

	# Stack for Depth First Search through the matrix
	nodesToExplore = [[row, col]]

	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]

		if visited[i][j]:
			continue

		visited[i][j] = True

		if matrix[i][j] == 0:
			continue

		currentRiverSize += 1

		unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)

		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)

	if currentRiverSize > 0:
		size.append(currentRiverSize)


def getUnvisitedNeighbors(row, col, matrix, visited):
	unvisitedNeighbors = []

	if row > 0 and not visited[row - 1][col]:
		unvisitedNeighbors.append([row - 1, col])

	if row < len(matrix) -1 and not visited[row - 1][col]:
		unvisitedNeighbors.append([row - 1, col])

	if col > 0 and not visited[row][col - 1]:
		unvisitedNeighbors.append([row, col - 1])

	if col < len(matrix[0]) - 1 and not visited[row][col - 1]:
		unvisitedNeighbors.append([row, col - 1])

	return unvisitedNeighbors















