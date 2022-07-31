# O(n^2) time | O(1) space
def bubbleSort(array):
	isSorted = False
	counter = 0 # Slight optimization

	while not isSorted:
		isSorted = True

		for i in range(len(array) - 1 - counter):
			if array[i] > array[i + 1]:
				swap(i, i + 1, array)
				isSorted = False

		counter += 1

	return array


def swap(curr, nxt, array):
	array[nxt], array[curr] = array[curr], array[nxt]