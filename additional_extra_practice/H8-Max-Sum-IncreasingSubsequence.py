# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
	sequences = [None for x in array]
	sums = array[ : ]
	maxSumIdx = 0

	for i in range(len(array)):
		currentNum = array[i]

		for j in range(0, i):
			otherNum = array[j]

			# Strictly increasing subsequence
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]
				sums[i] = sums[j] + currentNum
				sequences[i] = j

		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i

	return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(arrayo, sequences, currentIdx):
	seq = []

	while currentIdx is not None:
		seq.append(array[currentIdx])
		currentIdx = sequences[currentIdx]

	return list(reversed(seq))
