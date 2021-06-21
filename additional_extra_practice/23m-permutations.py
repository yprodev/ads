# O (n! * n ^ 2) time | O(n! * n) space
def getPermutations1(array):
	permutations = []
	permutationsHelper1(array, [], permutations)

	return permutations


def permutationsHelper1(array,  currentPermutation, permutations):

	# Input array is empty and currentPermutations should have values in it
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[ : i] + array[i + 1 : ]
			newPermutation = currentPermutation + [array[i]]
			permutationsHelper1(newArray, newPermutation, permutations)

# ===========================================================================
# O(n! * n) time | O(n! * n) space

def getPermutations2(array):
	permutations = []
	permutationsHelper2(0, array, permutations)

	return permutations


def permutationsHelper2(i,  array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(array, i, j)
			permutationsHelper2(i + 1, array, permutations)
			swap(array, i, j)


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]


