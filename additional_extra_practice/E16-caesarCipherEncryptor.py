# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
	newLetters = []
	# Edge case: key should be the same size of english alphabet
	newKey = key % 26

	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))

	return "".join(newLetters)


def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key

	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# ------------------------------------------------------------------------------------------

def caesarCipherEncryptorAlphabet(string, key):
	newLetters = []
	# Edge case: key should be the same size of english alphabet
	newKey = key % 26
	alphabet = ["abcdefghijklmnopqrstuvwxyz"]

	for letter in string:
		newLetters.append(getNewLetterAlphabet(letter, newKey, alphabet))

	return "".join(newLetters)


def getNewLetterAlphabet(letter, key, alphabet):
	newLetterCode = alphabet.index(letter) + key

	return alphabet[newLetterCode] if newLetterCode <= 122 else alphabet[-1 + newLetterCode % 25]
