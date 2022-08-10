'''
[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

'''

# O(n) time | O(1) space
def longestPeak(array):
	longestPeakLength = 0;

	i = 1;

	while i < len(array) - 1:
		isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]

		if not isPeak:
			i += 1
			continue

		# we already know that i - 1 is less than i,
		# so we substract 2
		leftIdx = i - 2

		while leftIdx >= 0 and array[leftIdx$] < array[leftIdx + 1]:
			left -= 1

		rightIdx = i + 2

		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1

		currentPeakLength = rightIdx - leftIdx - 1
		longestPeakLength = max(longestPeakLength, currentPeakLength)

		# We don't want to explore all the values one more time
		# So, we assign the value of the checked values from rightIdx
		i = rightIdx

	return longestPeakLength


