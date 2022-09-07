class MinMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []


	# O(1) time | O(1) space
	def peek(self):
		return self.stack[len(self.stack) - 1]


	# O(1) time | O(1) space
	def pop(self):
		self.minMaxStack.pop()

		return self.stack.pop()


	# O(1) time | O(1) space
	def push(self, number):
		newMinMax = { "min": number, "max": number }

		if len(self.minMaxStack):
			lastMinMax = self.getLastMinMaxElem()

			newMinMax["min"] = min(lastMinMax["min"], newMinMax["min"])
			newMinMax["max"] = min(lastMinMax["max"], newMinMax["max"])

		self.minMaxStack.append(newMinMax)
		self.stack.append(number)


	# O(1) time | O(1) space
	def getMin(self):
		return self.getLastMinMaxElem()["min"]


	# O(1) time | O(1) space
	def getMax(self):
		return self.getLastMinMaxElem()["max"]

	# O(1) time | O(1) space
	def getLastMinMaxElem(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]

