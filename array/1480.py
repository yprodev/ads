# [AUTHOR] PYTHON LESS THAN 100% MEMORY USAGE
# [DESCRIPTION] PythonEpicUserBoy
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        num = 1
        while len(lst) != len(nums):
            lst.append(sum((nums[0:num])))
            num += 1
        return lst
"""
Comment
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_nums = []
        for num in nums:
            sum_nums.append(sum(nums[:len(sum_nums)+1]))
        
        return sum_nums

# ===================================================================================

# [AUTHOR] RohanPark
# [DESCRIPTION] switching from cpp to python
# python 
#1st
def runningSum(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
            i+=1
        return nums
        
#2nd
def runningSum(self, nums: List[int]) -> List[int]:          
            for i in range(len(nums)-1):
                nums[i+1] += nums[i]
            return nums

#3rd 
def runningSum(self, nums: List[int]) -> List[int]:
      return functools.reduce(lambda a,b: a + [a[-1] + b], nums[1:], [nums[0]])

# C++
# vector<int> runningSum(vector<int>& nums) {
#         for(int i=1 ; i<nums.size() ; i++)
#             nums[i]+=nums[i-1];
#         return nums;
#     }

# ===================================================================================

# [AUTHOR] brianchiang_tw
# [DESCRIPTION] Python O(n) by itertaion [w/ visualization]
"""
Implementation by iteration with out-of-place update:
"""

class Solution(object):
    def runningSum(self, nums):
        
        # base case:
        prefix_sum = [ nums[0] ]
        
        # general case:
        for idx in range(1, len(nums)):
            
            # compute current running sum
            accumulation = nums[idx] + prefix_sum[-1]
            
            # append to prefix sum array
            prefix_sum.append( accumulation )
            
        return prefix_sum

"""
Implementation by iteration with in-place update:
"""

class Solution(object):
    def runningSum(self, nums):
        
        # in-place update running sum in nums
        for idx in range(1, len(nums)):
            
            nums[idx] += nums[idx-1]
            
        return nums

# ===================================================================================

# [AUTHOR] Me
# [DESCRIPTION] First working solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        mem = 0
        
        for n in nums:
            result.append(mem + n)
            mem += n
        
        return result