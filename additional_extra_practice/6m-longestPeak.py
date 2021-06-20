# O(n) time | O(1) space
def longestPeak(array):
	longestPeakLength = 0
	i = 1 # Starting from the possible peak

	while i < len(array) - 1: # The peak can not be the last item
		isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]

		if not isPeak:
			i += 1
			continue

		leftPtr = i - 2 # We already checked array[i - 1]
		while leftPtr >= 0 and array[leftPtr] < array[leftPtr + 1]:
			leftPtr -= 1

		rightPtr = i + 2
		while rightPtr < len(array) and array[rightPtr] < array[rightPtr - 1]:
			rightPtr += 1

		currentPeakLength = rightPtr - leftPtr - 1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		i = rightPtr

	return longestPeakLength


