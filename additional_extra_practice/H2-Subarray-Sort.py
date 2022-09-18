# O(n) time | O(1) space
def subarraySort(array):
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	subarrayLeftIdx = 0
	subarrayRightIdx = len(array) - 1


	for i in range(len(array)):
		num = array[i]

		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)

	if minOutOfOrder == float("inf"):
		return [-1, -1]

	while minOutOfOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1

	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1

	return [subarrayLeftIdx, subarrayRightIdx]


def isOutOfOrder(idx, num, array):
	prevNum, nextNum = array[idx - 1], array[idx + 1]

	if idx == 0:
		return num > nextNum

	if idx == len(array) - 1:
		return num < prevNum

	return num > nextNum or num < prevNum

