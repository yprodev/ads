"""
Dynamic Programming - Tabulation

$6 [1, 2, 4] 2

Right answer: 2 (2 + 4)

6 is target, so the max index will be 6
denominations: [1, 2, 4]

"""

# O(nd) time | O(n) space
def minNumberOfCoinsForChange(target, denoms):
	numOfCoins = [float("inf") for amount in range(0, target + 1)]
	# To make $0 we need 0 coins
	numOfCoins[0] = 0

	for denom in denoms:
		for amount in range(len(numOfCoins)):
			if denom <= amount:
				numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])

	return numOfCoins[target] if numOfCoins[target] != float("inf") else -1
