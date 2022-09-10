# O(w * n * log(n) + n * w * log(w)) time | O(wn) space
def groupAnagrams(words):
	if len(words) == 0:
		return []

	sortedWords = [ "".join(sorted(w)) for w in words ]
	indicies = [ i for i in range(len(words)) ]

	indicies.sort(key = lambda x: sortedWords[x])

	result = []
	currentAnagramGroup = []
	currentAnagram = sortedWords[indicies[0]]

	for index in indicies:
		word = words[index]
		sortedWord = sortedWords[index]

		if sortedWord == currentAnagram:
			currentAnagramGroup.append(word)
			continue

		result.append(currentAnagramGroup)
		currentAnagramGroup = [word]
		currentAnagram = sortedWord

	result.append(currentAnagramGroup)

	return result

# =========================================================

# O(w * n * log(n)) time | O(wn) space
def groupAnagrams(words):
	anagrams = {}

	for word in words:
		sortedWord = "".join(sorted(word))

		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]

	return list(anagrams.values())

