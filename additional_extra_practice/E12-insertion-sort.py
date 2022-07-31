# O(n^2) time | O(1) space
def insertionSort(array):
	for in range(1, len(array)):
		j = i

		while j > 0 and array[j] < array[j - 1]:
			swap(j, j - 1, array)
			j -= 1

	return array


def swap(curr, prev, array):
	array[curr], array[prev] = array[pre], array[curr]
