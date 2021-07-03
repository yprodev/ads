# O(n ^ 2) time | O(1) Space
def twoNumberSum1(array, targetSum):
	for i in range(len(array) - 1):
		firstNum = array[i]

		for j in range(i + 1, len(array)):
			secondNum = array[j]

			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]

	return []


# =============================================

# O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
	nums = {}

	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch, num]
		else:
			nums[num] = True

	return []


# =============================================

# O(n log n) time | O(1) space
def twoNumberSum3(array, targetSum):
	array.sort()

	leftPtr = 0
	rightPtr = len(array) - 1

	while leftPtr < rightPtr:
		currentSum = array[leftPtr] + array[rightPtr]

		if currentSum == targetSum:
			return [array[leftPtr], array[rightPtr]]

		if currentSum < targetSum:
			leftPtr += 1

		if currentSum > targetSum:
			rightPtr -= 1

	return []





