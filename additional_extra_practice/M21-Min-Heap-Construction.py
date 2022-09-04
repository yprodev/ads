class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)


	# O(n) time | O(1) space
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2

		for currIdx in reversed(range(firstParentIdx)):
			self.siftDown(currIdx, len(array) - 1, array)

		return array


	# O(log n) time | O(1) space
	def siftDown(self, currIdx, endIdx, heap):
		childLeftIdx = currIdx * 2 + 1
		childRightIdx = currIdx * 2 + 2

		while childLeftIdx <= endIdx:
			childRightIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
			if childRightIdx != -1 and heap[childRightIdx] < heap[childLeftIdx]:
				idxToSwap = childRightIdx
			else:
				idxToSwap = childLeftIdx

			if heap[idxToSwap] < heap[currIdx]:
				self.swap(currIdx, idxToSwap, heap)
				currIdx = idxToSwap
				childLeftIdx = currIdx * 2 + 1
			else:
				break


	# O(log n) time | O(1) space
	def siftUp(self, currIdx, heap):
		parentIdx = (currIdx - 1) // 2

		while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
			self.swap(currIdx, parentIdx, self.heap)
			currIdx = parentIdx
			parentIdx = (currIdx - 1) // 2


	def peek(self):
		return self.heap[0]


	def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)

		return valueToRemove


	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(heap) - 1, self.heap)


	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]

