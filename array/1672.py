# ===================================================================================
# [AUTHOR] [Python] Two Solutions: For Loop and Map
# [DESCRIPTION] leihua

"""
Solution 1: For loop
It's a pretty standard for loop and also inefficient.
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        new = []
        for i in accounts:
            row_sum = sum(i)
            new.append(row_sum)
        return max(new)


"""
Solution 2: Map
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return(max(map(sum,accounts)))

# ===================================================================================
# [AUTHOR] splorgdar
# [DESCRIPTION] Python one-liner...
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(a) for a in accounts])

# ===================================================================================
# [AUTHOR] zywscq
# [DESCRIPTION] 3 One-Line Python solutions
"""
use higher order function map
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts))
"""
https://medium.com/techtofreedom/higher-order-functions-in-python-e78daaeb37ae
"""

"""
Use list comprehension
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(a) for a in accounts])
"""
https://medium.com/techtofreedom/8-levels-of-using-list-comprehension-in-python-efc3c339a1f0
"""

"""
3. use tuple comprehension
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(a) for a in accounts)

"""
https://medium.com/techtofreedom/the-4-types-of-comprehensions-in-python-2cf1096fffc0
"""

# ===================================================================================
# [AUTHOR] atrevisan21
# [DESCRIPTION] Python low memory usage
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts.sort(key=lambda x: sum(x))
        return  sum(accounts[-1])


# ===================================================================================

# [AUTHOR] Me
# [DESCRIPTION] First working solution

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        biggestSum = 0

        for customer in accounts:
            tempSum = sum(customer)
            if tempSum > biggestSum:
                biggestSum = tempSum

        return biggestSum