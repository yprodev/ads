// [AUTHOR] gtshepard
// [DESCRIPTION] Backtracking Template | Explanation + Visual | [Python]
// [LINK] https://leetcode.com/problems/subsets/discuss/973667/Backtracking-Template-or-Explanation-%2B-Visual-or-Python

/*

def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        self.dfs(0, res, path, nums)
        return res
        
 def dfs(self, index, res, path, nums):
        res.append(list(path)) 
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(i+1, res, path, nums)
            path.pop()

*/

// ==========================================================================


// [AUTHOR] JorgeGonzalez
// [DESCRIPTION] Recursive JavaScript solution
// [LINK] https://leetcode.com/problems/subsets/discuss/299665/Recursive-JavaScript-solution

function subsets(nums) {
    const powerset = [];
    generatePowerset([], 0);

    function generatePowerset(path, index) {
        powerset.push(path);
        for (let i = index; i < nums.length; i++) {
            generatePowerset([...path, nums[i]], i + 1);
        }
    }

    return powerset;
}



// ==========================================================================


// [AUTHOR] DBabichev
// [DESCRIPTION] [Python] 3 Solutions: Backtracking + 2 oneliners, explained
// [LINK] https://leetcode.com/problems/subsets/discuss/729842/Python-3-Solutions%3A-Backtracking-%2B-2-oneliners-explained

/*

In this problem we need to return all posible subsets of given set, and there are a big number of them: 2^n. It usually means, that we need to use some backtracking approach to do it.
Let us have function dfs(self, current, nums), with parameters:

    1. current is set of indexes choosen number: we always choose indexes in increasing order.
    2. nums are our original numbers (we can make it global varialbe as well).

Also I start with dummy variable index -1, and when we add subset to final answer, we remove this element. Then we recursively run dfs with new added number i.

Complexity: both time ans space is O(2^n*n), because we have 2^n subsets with n/2 elements in average.

class Solution:
    def subsets(self, nums):
        self.out = []
        self.dfs([-1],nums)
        return self.out

    def dfs(self, current, nums):
        self.out.append([nums[s] for s in current][1:])
        for i in range(current[-1] + 1, len(nums)):
            self.dfs(current + [i], nums)

Oneliners
First one is to use combinations library from python, and we itarate over all possible number of elements. Second one uses binary masks.

return chain.from_iterable(combinations(nums, i) for i in range(len(nums)+1))

return [[nums[j] for j in range(len(nums)) if (i&(1<<j))] for i in range(1<<len(nums))]

*/


// ==========================================================================


// [AUTHOR] gany
// [DESCRIPTION] javascript
// [LINK] https://leetcode.com/problems/subsets/discuss/1148900/javascript

var subsets = function(nums) {
    const ret = [], path = [];

    const backtrack = (index, nums) =>{
        ret.push([...path]);
        
        for(let i = index; i < nums.length; ++i){
            path.push(nums[i]);
            backtrack(i+1, nums);
            path.pop();
        }
    };

    backtrack(0, nums);
    return ret;
};


// ==========================================================================


// [AUTHOR] jianchao-li
// [DESCRIPTION] C++ Recursive/Iterative/Bit-Manipulation
// [LINK] https://leetcode.com/problems/subsets/discuss/27278/C%2B%2B-RecursiveIterativeBit-Manipulation

/*

Recursive (Backtracking)

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> subs;
        vector<int> sub;
        subsets(nums, 0, sub, subs);
        return subs;
    }
private:
    void subsets(vector<int>& nums, int i, vector<int>& sub, vector<vector<int>>& subs) {
        subs.push_back(sub);
        for (int j = i; j < nums.size(); j++) {
            sub.push_back(nums[j]);
            subsets(nums, j + 1, sub, subs);
            sub.pop_back();
        }
    }
};

Iterative

Using [1, 2, 3] as an example, the iterative process is like:

    1. Initially, one empty subset [[]]
    2. Adding 1 to []: [[], [1]];
    3. Adding 2 to [] and [1]: [[], [1], [2], [1, 2]];
    4. Adding 3 to [], [1], [2] and [1, 2]: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> subs = {{}};
        for (int num : nums) {
            int n = subs.size();
            for (int i = 0; i < n; i++) {
                subs.push_back(subs[i]); 
                subs.back().push_back(num);
            }
        }
        return subs;
    }
}; 




Bit Manipulation

To give all the possible subsets, we just need to exhaust all the possible combinations of the numbers. And each number has only two possibilities: either in or not in a subset. And this can be represented using a bit.

Using [1, 2, 3] as an example, 1 appears once in every two consecutive subsets, 2 appears twice in every four consecutive subsets, and 3 appears four times in every eight subsets (initially all subsets are empty):

[], [ ], [ ], [    ], [ ], [    ], [    ], [       ]
[], [1], [ ], [1   ], [ ], [1   ], [    ], [1      ]
[], [1], [2], [1, 2], [ ], [1   ], [2   ], [1, 2   ]
[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]


class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size(), p = 1 << n;
        vector<vector<int>> subs(p);
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) {
                    subs[i].push_back(nums[j]);
                }
            }
        }
        return subs;
    }
};




*/