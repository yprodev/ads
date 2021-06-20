# O(nm) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
	# n - is the target value. So this value should
	# be an index. So, we need to do n + 1 later
	# withing the loops.
	ways = [0 for amount in range(n + 1)]
	ways[0] = 1 # The first value is 1 - base case

	for denom in denoms:
		for amount in range(1, n + 1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]

	return way[n]


