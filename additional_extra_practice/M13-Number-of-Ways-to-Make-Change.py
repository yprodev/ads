"""
Dynamic Programming - Tabulation

$10 [1, 5, 10, 25] 4

Right answer: 4

10 is target
denominations: [1, 5, 10, 25]

25 is bigger than target 10
so, the max index will be 10

# 10                      4
# 5            2 2 2 2 2  3
# 1    1 1 1 1 1 1 1 1 1  1
ways = 1 0 0 0 0 0 0 0 0  0
       1 2 3 4 5 6 7 8 9 10

"""

# O(nd) time | O(n) space (n - number of positions to target, d - denominations)
def numberOfWaysToMakeChange(target, denoms):
	# Create ways array
	ways = [0 for amount in range(target + 1)]
	# Create minimum base case
	ways[0] = 1;

	for denom in denoms:
		for amount in range(1, target + 1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]

	return ways[target]
