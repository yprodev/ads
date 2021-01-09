# [AUTHOR] lei8c8yahoo
# [DESCRIPTION] Clean Python
# [DEBUGGING]
#	We need to sort. Sorting position will automatically give you an answer
#	of the smallest values in comparison to current value.In case you have
#	duplications - you will find the first index, which means the same
#	number of smaller values.
"""
Solution 1: slow but clean
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]

"""
Solution 2: faster, but need more space (additional hash map)
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lookup = {}
        for i, v in enumerate(sorted(nums)):
            if v in lookup:
                continue
            lookup[v] = i
        return [lookup[num] for num in nums]

# ===================================================================================
# [NO NEED TO SHOW OTHER EXAMPLES]
# ===================================================================================

# [AUTHOR] Me
# [DESCRIPTION] First Working Solution
# Issues:
#	Basic knowledge of Python3
#	Hard to understand how to do it without nested loop
#	Hard to understand where we need to apply Hash Table (we need array only)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        storage = [0] * numsLen
        
        for i in range(numsLen):   
            for j in range(numsLen):
                if nums[i] > nums[j]:
                    storage[i] += 1
                
        
        return storage