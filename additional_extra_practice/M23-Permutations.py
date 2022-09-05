# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations1(array):
	permutations = []

	permutationsHelper1(array, [], permutations)

	return permutations

def permutationsHelper1(array, currPermutation, permutations):
	if not len(array) and len(currentPermutation):
		permutations.append(currPermutation)
	else:
		for i in range(len(array)):
			newArray = array[ : i] + array[i + 1 : ] # O(n)
			newPermutation = currentPermutation + [array[i]] # O(n)
			permutationsHelper1(newArray, newPermutation, permutations) # O(n!)

# =======================================================================

# O(n*n!) time | O(n*n!) space
def getPermutations2(array):
	permutations = []

	permutationsHelper2(0, array, permutations)

	return permutations


def permutationsHelper2(index, array, permutations):
	isFinalPosition = index == len(array) - 1

	if isFinalPosition:
		# Create a snapshot
		permutations.append(array[ : ])
	else:
		for j in range(index, len(array)):
			swap(array, i, j)
			permutationsHelper2(i + 1, array, permutations)
			swap(array, i, j)


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
