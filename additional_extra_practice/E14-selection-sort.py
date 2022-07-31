# O(n^2) time | O(1) space
def selectionSort(array):
	startIdx = 0

	while startIdx < len(array) - 1:
		smallestIdx = startIdx

		for i in range(startIdx + 1, len(array)):
			if array[smallestIdx] > array[i]:
				smallestIdx = i

		swap(startIdx, smallestIdx, array)
		startIdx += 1

	return array


def swap(startIdx, smallestIdx, array):
	array[smallestIdx], array[startIdx] = array[startIdx], array[smallestIdx]

