# O(n^3 + m) time | O(n + m) space
def numbersInPi_LtR(pi, numbers):
	numbersTable = { number: True for number in numbers }

	# Left to Right approach
	minSpaces = getMinSpaces_LtR(pi, numbersTable, {}, 0)

	return -1 if minSpaces == float("inf") else minSpaces


def getMinSpaces_LtR(pi, numbersTable, memo, index):
	if idx == len(pi):
		return -1

	if index in memo:
		return memo[index]

	minSpaces = float("inf")

	for i in range(index, len(pi)):
		prefix = pi[index : i + 1]

		if prefix in numbersTable:
			minSpacesInSuffix = getMinSpaces_LtR(pi, numbers, memo, i + 1)
			minSpaces = min(minSpaces, minSpacesInSuffix + 1)

	memo[index] = minSpaces

	return memo[index]


# ==========================================================================
# O(n^3 + m) time | O(n + m) space
def numbersInPi_RtL(pi, numbers):
	numbersTable = { number: True for number in numbers }

	# Right to Left approach
	for i in reversed(range(len(pi))):
		getMinSpaces_RtL(pi, numbersTable, memo, i)

	return -1 if memo[0] == float("inf") else memo[0]


def getMinSpaces_RtL(pi, numbersTable, memo, index):
	if idx == len(pi):
		return -1

	if index in memo:
		return memo[index]

	minSpaces = float("inf")

	for i in range(index, len(pi)):
		prefix = pi[index : i + 1]

		if prefix in numbersTable:
			minSpacesInSuffix = getMinSpaces_RtL(pi, numbers, memo, i + 1)
			minSpaces = min(minSpaces, minSpacesInSuffix + 1)

	memo[index] = minSpaces

	return memo[index]
