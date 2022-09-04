# O(d) time | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendantDepth(descendantOne, topAncestor)
	depthTwo = getDescendantDepth(descendantTwo, topAncestor)

	if depthOne > depthTwo:
		return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, ancestor):
	depth = 0

	while descendant != ancestor:
		depth += 1
		descendant = descendant.ancestor

	return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1

	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor

	return lowerDescendant


