# [AUTHOR] lee215
# [DESCRIPTION] [Java/C++/Python] Count

"""
JAVA

    public int numIdenticalPairs(int[] A) {
        int res = 0, count[] = new int[101];
        for (int a: A) {
            res += count[a]++;
        }
        return res;
    }
"""

"""
C++

    int numIdenticalPairs(vector<int>& A) {
        int res = 0;
        unordered_map<int, int> count;
        for (int a: A) {
            res += count[a]++;
        }
        return res;
    }
"""

"""
C++

int numIdenticalPairs(vector<int>& A) {
    return accumulate(A.begin(), A.end(), 0, [count = unordered_map<int, int> {}] (auto a, auto b) mutable {
        return a + count[b]++;
    });
}
"""


"""
python
"""
def numIdenticalPairs(self, A):
    return sum(k * (k - 1) / 2 for k in collections.Counter(A).values())

# ===================================================================================

# [AUTHOR] hbjORbj
# [DESCRIPTION] Easy Python Solution

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        diction = dict()
        pairs = 0
        for num in nums:
            if num in diction:
                pairs += diction[num]
                diction[num] += 1
            else:
                diction[num] = 1
        return pairs
# ===================================================================================

# [AUTHOR] random_bits101
# [DESCRIPTION] Python - Counting, O(N)
# [NOTES]
"""
The key observation is that, if there are n number of same numbers, you can create pairs by choosing two points from n. This is combinations (nCr) where r is always 2. So, the formula becomes n * (n - 1) / 2.
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return sum(val * (val - 1) // 2 for key, val in count.items())

# ===================================================================================

# [AUTHOR] akaghosting
# [DESCRIPTION] python solution

class Solution:
	def numIdenticalPairs(self, nums: List[int]) -> int:
		d = collections.defaultdict(int)
		res = 0
		for i in range(len(nums)):
			d[nums[i]] += 1
		for v in d.values():
			if v > 1:
				res += sum([i for i in range(1, v)])
		return res

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	Looks like very obvious solution

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        length = len(nums)
        r = range(length)
        count = 0
        
        for i in r:
            for j in r:
                if nums[i] == nums[j] and i < j:
                    count += 1
                    
                    
        return count

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] Second working solution
# Issues:
#	Basic knowledge of Python3
#	Tried to speed up the process, however just won -10ms
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        slowPtr = 0
        fastPtr = 0
        length = len(nums)
        lastIndex = length - 1

        while slowPtr <= lastIndex and fastPtr <= lastIndex:
            if nums[slowPtr] == nums[fastPtr] and slowPtr < fastPtr:
                count += 1

            if fastPtr == lastIndex:
                slowPtr += 1
                fastPtr = slowPtr

            fastPtr += 1

        return count
