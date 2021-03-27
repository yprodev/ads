

# ===================================================================================

# [AUTHOR]: Aragorn_
# [DESCRIPTION]: Python Solution - 90% Speed - O(n) Time, O(1) Space Complexity

"""
Python Solution - 90% Speed - O(n) Time, O(1) Space Complexity

The code below tracks two variables (a,b) representing the two highest values found in the array. After one linear pass, we can use these values to return the answer.
Cheers,

"""

class Solution:
    def maxProduct(self, nums):
        a, b = float('-inf'), float('-inf')
        for x in nums:
            if x>a:
                a, b = x, a
            elif x>b:
                b = x
        return (a-1)*(b-1)

# ===================================================================================

# [AUTHOR]: Kedaar_Kalyan
# [DESCRIPTION]: simple python solution


def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

# ===================================================================================

# [AUTHOR]: brianchiang_tw
# [DESCRIPTION]: Python O(n) by linear scan. [w/ Comment]
"""
Python O(n) by linear scan.

Hint:

Maintain a record of first largest number as well as second largest

"""
class Solution(object):
    def maxProduct(self, nums):

        first, second = 0, 0
        
        for number in nums:
            
            if number > first:
                # update first largest and second largest
                first, second = number, first
                
            else:
                # update second largest
                second = max( number, second)
        
        return (first - 1) * (second - 1)



# ===================================================================================

# [AUTHOR]: wkdankit
# [DESCRIPTION]: Python | Faster than 93% | Max operation | Easy to understand

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h1 = max(nums)
        nums.remove(h1)
        h2 = max(nums)
        
        return (h1-1) * (h2-1)


# ===================================================================================

# [AUTHOR]: Isnottom
# [DESCRIPTION]: Python solution faster than 80%

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        k=len(nums)
        return (nums[k-1]-1)*(nums[k-2]-1)




# ===================================================================================

# [AUTHOR]: AkalaDream
# [DESCRIPTION]: Python ONE PASS O(N) Solution without sorting

class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		max1, max2 = 0, 0
		for i in range(len(nums)):
			if nums[i] > max1:
				max2 = max(max2, max1)
				max1 = nums[i]
			else:
				max2 = max(max2, nums[i])
		return (max1 - 1) * (max2 - 1)



# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] NOT WORKING SOLUTION
# Issues:
#	Does not work with the bigger ammount of data...

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        
        for i in range(length):
            for j in range(length):
                if i is not j:
                    cur = (nums[i] - 1)  * (nums[j] - 1)
                
                    if cur > res:
                        res = cur
                    
                    
        return res
            
