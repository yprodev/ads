

# ===================================================================================

# [AUTHOR]: shukhrat_1995
# [DESCRIPTION]: Python3 solution with comments

from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        # Time Complexity O(n)
        # Space Complexity O(n)
        
        hash_table = Counter(nums) # create a hash table using Counter function
        res = 0 # initalize a variable res with zero
        for k, v in hash_table.items(): # loop through all keys and values inside hash table
            if v == 1: # if the value of current key is equal to 1
                res += k # then increment the result
        return res # return the final result

# [NOTE] The same I did with additional import to have counter (frequency) of unique vals.


# ===================================================================================

# [AUTHOR]: YashashriShiral
# [DESCRIPTION]: Python Easy Solution

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts=0
        final=0
        for i in range(len(nums)):
            counts = nums.count(nums[i])
            if counts==1:
                final= final+nums[i]
        return(final)


# ===================================================================================

# [AUTHOR]: Levankhaduri
# [DESCRIPTION]: [python3] 85% speed 100% memory

class Solution:
	def sumOfUnique(self, nums: List[int]) -> int:
		setNums = set(nums)
		result = 0

		for i in setNums:
			if nums.count(i) == 1:
				result+=i

		return result


# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Python] 1-line

"""
Explanation
Count the frequency of elements in A using Counter
Sum up the element a if its frequency c == 1


Complexity
Time O(n)
Space O(n)

Python
"""
def sumOfUnique(self, A):
    return sum(a for a, c in collections.Counter(A).items() if c == 1)


# ===================================================================================

# [AUTHOR]: [Java/Python 3] 3/1 liners.
# [DESCRIPTION]: rock
"""
public int sumOfUnique(int[] nums) {
    int[] cnt = new int[101];
    for (int n : nums) {
        ++cnt[n];
    }
    int sum = 0;
    for (int i = 1; i <= 100; ++i) {
        if (cnt[i] == 1) {
            sum += i;
        }
    }
    return sum;
}

public int sumOfUnique(int[] nums) {
    int[] cnt = new int[101];
    IntStream.of(nums).forEach(n -> ++cnt[n]);
    return IntStream.range(1, 101).filter(i -> cnt[i] == 1).sum();
}

"""

def sumOfUnique(self, nums: List[int]) -> int:
    return sum(k for k, v in Counter(nums).items() if v == 1)


# ===================================================================================

# [AUTHOR]: votrubac
# [DESCRIPTION]: C++ 7 Solutions


"""
If our array is very large, but number values are limited (e.g. [1, 100], then two loops solutions will be more efficient.

Also, if number values are sparse, then hashmap solutions are prefferable.

Two hashsets will be more memory efficient than hashmap as we do not need to store the counts. Or we can just track a boolean flag in the hashmap.
"""

"""
1. Array, two loops

int sumOfUnique(vector<int>& nums) {
    int cnt[101] = {}, res = 0;
    for (auto n : nums)
        ++cnt[n];
    for (auto i = 1; i <= 100; ++i)
        if (cnt[i] == 1)
            res += i;
    return res;
}


2. Hashmap, two loops

int sumOfUnique(vector<int>& nums) {
    unordered_map<int, int> m;
    for (auto n : nums)
        ++m[n];
    return accumulate(begin(m), end(m), 0, [](int sum, const auto &p) {
        return sum + (p.second == 1 ? p.first : 0);
    });
}


3. Hashsets, two loops

int sumOfUnique(vector<int>& nums) {
    unordered_set<int> one, many;
    for (auto n : nums)
        if (!many.count(n))
            if(!one.insert(n).second) {
                many.insert(n);
                one.erase(n);
            }
    return accumulate(begin(one), end(one), 0);
}


4. Hashmap of booleans, two loops

int sumOfUnique(vector<int>& nums) {
    unordered_map<int, bool> m;
    for (auto n : nums) {
        auto it = m.find(n);
        if (it != end(m))
            it->second = true;
        else
            m.insert({n, false});
    }
    return accumulate(begin(m), end(m), 0, [](int sum, const auto &p) {
        return sum + (p.second ? 0 : p.first);
    });
}


5. Array, single loop

int sumOfUnique(vector<int>& nums) {
    int cnt[101] = {}, res = 0;
    for (auto n : nums)
        res += ++cnt[n] == 1 ? n : cnt[n] == 2 ? - n : 0;
    return res;
}


6. Hashmap, single loop

int sumOfUnique(vector<int>& nums) {
    unordered_map<int, int> m;
    int res = 0;
    for (auto n : nums) {
        int cnt = ++m[n];
        res += cnt == 1 ? n : cnt == 2 ? -n : 0;
    }
    return res;
}



7. Hashmap of booleans, single loops

int sumOfUnique(vector<int>& nums) {
    unordered_map<int, bool> m;
    int res = 0;
    for (auto n : nums) {
        auto it = m.find(n);
        if (it != end(m)) {
            res -= it->second ? 0 : n;
            it->second = true;
        }
        else {
            m.insert({n, false});
            res += n;
        }
    }
    return res;
}

"""


# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mem = dict()
        res = 0
        
        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1
                
        for item in mem.items():
            if item[1] is 1:
                res += item[0]

        return res

# [KNOWLEDGESHARING]:
# 	1. There is a count method on the list: nums.count(item) which shows
#	how many times the items occurs in the list.
#	2. There is a special hash table implementation with counter we can
#	import: "from collections import Counter"
#	3. We can do the list with the unique values with set: setNums = set(nums)





