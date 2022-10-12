"""
Array of disks. Each disk is an array with three disk dimentions:
[2, 3, 5]

2 - width of the disk
3 - depth of the disk
5 - height of the disk

"""
# O(n^2) time | O(n) space
def diskStacking(disks):
	# Sort disks by their height
	disks.sort(key = lambda disk: disk[2])
	heights = [disk[2] for disk in disks]

	sequences = [None for disk in disks]
	maxHeightIdx = 0

	for i in range(1, len(disks)):
		currentDisk = disks[i]

		for j in range(0, i):
			otherDisk = disks[j]

			if areValidDimensions(otherDisk, currentDisk):
				if heights[i] < currentDisk[2] + heights[j]
					heights[i] = currentDisk[2] + heights[j]
					sequences[i] = j

		if heights[i] >= heights[maxHeightIdx]:
			maxHeightIdx = i

	# Backtracking
	return buildSequence(disks, sequences, maxHeightIdx)


def areValidDimensions(otherDisk, currentDisk):
	isLTWidth = otherDisk[0] < currentDisk[0]
	isLTDepth = otherDisk[1] < currentDisk[1]
	isLTHeight = otherDisk[2] < currentDisk[2]

	return isLTWidth and isLTDepth and isLTHeight


def buildSequence(disks, sequences, maxHeightIdx):
	sequence = []

	while currentIdx is not None:
		sequence.append(disks[currentIdx])
		currentIdx = sequences[currentIdx]

	return list(reversed(sequence))




