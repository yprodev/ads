# O(n^2) time | O(n) space
def isPalindrome(string):
	reversedString = ""
	for i in reversed(range(len(string))):
		reversedString += string[i] # re-creating a string each time

	return reversedString == string

# --------------------------------------------

# O(n) time | O(n) space
def isPalindromeChars(string):
	reversedChars = []
	for i in reversed(range(len(string))):
		reversedChars.append(string[i])

	return "".join(reversedChars) == string

# --------------------------------------------

# O(n) time | O(n) space
def isPalindromeRec(string, leftIdx = 0):
	rightIdx = len(string) - 1 - leftIdx;

	return True if leftIdx >= rightIdx else string[leftIdx] == string[rightIdx] and isPalindromeRec(string, leftIdx + 1) 


# O(n) time | O(1) space
def isPalindromeRecTail(string, leftIdx = 0):
	rightIdx = len(string) - 1 - leftIdx;

	if leftIdx >= rightIdx:
		return True

	if string[leftIdx] != string[rightIdx]:
		return False

	return isPalindromeRecTail(string, i + 1)

# --------------------------------------------


# O(n) time | O(1) space
def isPalindromePointers(string):
	leftIdx = 0
	rightIdx = len(string) - 1

	# there should NOT be the case with one pointers point to the same char
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False

		leftIdx += 1
		rightIdx -= 1

	return True
