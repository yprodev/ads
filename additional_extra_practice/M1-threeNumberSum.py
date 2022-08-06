# O(n^2) time | O(n) space
# No duplicate numbers in an array
def threeNumberSum(array, targetSum):
	array.sort(array)

	triplets = []
	# Use offset 2 because we have currentNumbe pointer
	# with index 0 and we have left pointer with index 1
	offset = 2

	for i in range(len(array - offset)):
		left = i + 1
		right = len(array) - 1

		while left < right:
			currentSum = array[i] + array[left] + array[right]

			if currentSum == targetSum:
				triplets.append(array[i], array[left], array[right])
				right -= 1
				left += 1

			elif currentSum < targetSum:
				left += 1

			elif currentSum > targetSum:
				right -= 1

	return triplets


