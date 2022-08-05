# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
	# Ask interview if it's okay to sort an array in place
	# (without writing additional function to sort them)
	# or to create a copies of the arrays to sort.
	arrayOne.sort()
	arrayTwo.sort()

	idxOne = 0
	idxTwo = 0
	smallest = float('inf')
	current = float('inf')
	smallestPair = []

	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]

		# current = abs(firstNum - secondNum)
		if firstNum < secondNum:
			currentSum = secondNum - firstNum
			idxOne += 1
		elif firstNum > secondNum:
			currentSum = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum, secondNum]

		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]

	return smallestPair








