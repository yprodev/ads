# O(nc) time | O(nc) space | n - the number of items we have, c - capacity
def knapsackProblem(items, capacity):
	# DP table - Tabulation
	knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
	for i in range(1, len(items) + 1):
		currentWeight = items[i - 1][1]
		currentValue = items[i - 1][0]

		for cap in range(0, capacity + 1):
			if currentWeight > cap:
				knapsackValues[i][cap] = knapsackValues[i - 1][cap]
			else:
				maxValueInPreviousRow = knapsackValues[i - 1][cap - currentWeight] + currentValue
				knapsackValues[i][cap] = max(knapsackValues[i - 1][cap], maxValueInPreviousRow)

	return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


# Create backtracking helper function to find
# which items we put into a knapsack
def getKnapsackItems(knapsackValues, items):
	sequence = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) - 1

	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i - 1][c]:
			i -= 1
		else:
			# We have additional empty row, so we need to remove shift
			sequence.append(i - 1)
			c -= items[i - 1][1]
			i -= 1

		if c == 0:
			break

	return list(reversed(sequence))
