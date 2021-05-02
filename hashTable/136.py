# [AUTHOR]: 
# [DESCRIPTION]: 

# ===================================================

# [AUTHOR]: Ivantsang
# [DESCRIPTION]: My O(n) solution using XOR

"""
known that A XOR A = 0 and the XOR operator is commutative, the solution will be very straightforward.

[COMMENT]:

For anyone who didn't understood why this works here is an explanation. This XOR operation works because it's like XORing all the numbers by itself. So if the array is {2,1,4,5,2,4,1} then it will be like we are performing this operation

((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.

Hence picking the odd one out ( 5 in this case).

int singleNumber(int A[], int n) {
    int result = 0;
    for (int i = 0; i<n; i++)
    {
		result ^=A[i];
    }
	return result;
}

"""




# ===================================================

# [AUTHOR]: OldCodingFarmer
# [DESCRIPTION]: Python different solutions.

def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)

# [COMMENT] from hiudawn | Python solution without extra memory

def singleNumber(self, nums):
    for i in range(1,len(nums)):
        nums[0] ^= nums[i]
    return nums[0]

# ===================================================

# [AUTHOR]: ztonege
# [DESCRIPTION]: [Python] Space O(1), XOR+Reduce, Very Simple One Liner (With Explanation)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)

"""
Explanation
I will try to explain this solution by walking through the initial solution that I wrote:

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
		for n in nums:
			result ^= n
		return result

"""
The most crucial trick here is to recognize that if you XOR any same number together, you cancel it out (=0).
For example:
nums = [2,4,5,4,3,5,2]
XORing everything together
= 2 ^ 4 ^ 5 ^ 4 ^ 3 ^ 5 ^ 2
= (2^2) ^ (4^4) ^ (5^5) ^ 3
= 0 ^ 0 ^0 ^ 3
= 3

(If you are unfamiliar with the XOR operation, you can check out this stackoverflow post):

https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do

Now, let's go back to the one liner:
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)

"""
The reduce here just simplifies the previous for loop into one line, it's not doing anything different.
The initializer 0 is put there to prevent the the scenerio where nums is an empty list (I didn't realize that the question statement explicitly mentioned that it would be non-empty).

"""



# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	Didn't know that there is possible to solve it with XOR.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mem = {}
        
        if nums and len(nums) == 1:
            return nums[0]
        
        for i in nums:
            if i not in mem:
                mem[i] = 1
            else:
                del mem[i]
            
        return list(mem.keys())[0]
