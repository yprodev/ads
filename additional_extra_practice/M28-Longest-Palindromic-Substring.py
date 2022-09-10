# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
	currentLongest = [0, 1]

	for i in range(1, len(string)):
		odd = getLongestPalindromFrom(string, i - 1, i + 1)
		even = getLongestPalindromFrom(string, i - 1, i)
		longest = max(odd, even, key = lambda x: x[1] - x[2])
		currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[2])

	return string[currentLongest[0] : currentLongest[1]]


def getLongestPalindromFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break

		leftIdx -= 1
		rightIdx += 1

	return [leftIdx + 1, rightIdx]
