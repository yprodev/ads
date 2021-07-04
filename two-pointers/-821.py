# [AUTHOR]: brianchiang_tw
# [DESCRIPTION]: Python O(n) by propagation 85%+ [w/ Diagram]

# Diagram explanation
# https://leetcode.com/problems/shortest-distance-to-a-character/discuss/527161/Python-O(n)-by-propagation-85%2B-w-Diagram

"""
Hint:

Imagine parameter C as a flag on the line.

Think of propagation technique:
1st-pass iteration propagates distance from C on the left hand side
2nd-pass iteration propagates distance from C on the right hand side with min( 1st-pass result, 2nd-pass propagation distance ) in order to update with shortest path.

"""

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        shortest_dist = []
        size = len(S)
        
        if size == 1:
            # Quick response for single character test case
            # Description guarantee that character C must exist in string S
            return [0]
        
        
        # Propagate distance from left to right
        for idx, char in enumerate(S):
            
            if char == C:
                shortest_dist.append(0)
            else:
                if idx == 0:
                    shortest_dist.append( size )
                else:
                    # Propagate distance from C on left hand side
                    shortest_dist.append( shortest_dist[-1] + 1)
                
        # Propagate distance from right to left               
        for idx in range(2, size+1):
            
            # Propagate distance from C on right hand side
            shortest_dist[-idx] = min(shortest_dist[-idx], shortest_dist[-idx+1]+1 )

                
        return shortest_dist

# ===================================================

# [AUTHOR]: slkuo230
# [DESCRIPTION]: JavaScript - 2 passes

"""
var shortestToChar = function(S, C) {
    const dp = new Array(S.length).fill(Infinity);
    
    dp[0] = S[0] === C ? 0 : Infinity
    
    for(let i = 1; i < S.length; i++) {
        if(S[i] === C) {
            dp[i] = 0;
        } else {
            dp[i] = dp[i-1] === Infinity ? Infinity : dp[i-1] + 1;
        }
    }

    let dist = Infinity;
    
    for(let i = S.length-1; i >= 0; i--) {
        if(S[i] === C) {
            dist = 0;
        }
        dp[i] = Math.min(dist, dp[i]);
        dist += 1;
    }
    
    return dp;
    
};
"""

# ===================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [C++/Java/Python] 2-Pass with Explanation

"""

Solution 1: Record the Position
Initial result array.
Loop twice on the string S.
First forward pass to find shortest distant to character on left.
Second backward pass to find shortest distant to character on right.


In python solution, I merged these two for statement.
We can do the same in C++/Java by:

for (int i = 0; i >= 0; res[n-1] == n ? ++i : --i)

But it will become less readable.


Time complexity O(N)
Space complexity O(N) for output

C++

vector<int> shortestToChar(string S, char C) {
    int n = S.size(), pos = -n;
    vector<int> res(n, n);
    for (int i = 0; i < n; ++i) {
        if (S[i] == C) pos = i;
        res[i] = i - pos;
    }
    for (int i = pos - 1; i >= 0; --i) {
        if (S[i] == C)  pos = i;
        res[i] = min(res[i], pos - i);
    }
    return res;
}


Java

public int[] shortestToChar(String S, char C) {
    int n = S.length(), pos = -n, res[] = new int[n];
    for (int i = 0; i < n; ++i) {
        if (S.charAt(i) == C) pos = i;
        res[i] = i - pos;
    }
    for (int i = pos - 1; i >= 0; --i) {
        if (S.charAt(i) == C)  pos = i;
        res[i] = Math.min(res[i], pos - i);
    }
    return res;
}

Python
"""
def shortestToChar(self, S, C):
    n, pos = len(S), -float('inf')
    res = [n] * n
    for i in range(n) + range(n)[::-1]:
        if S[i] == C:
            pos = i
        res[i] = min(res[i], abs(i - pos))
    return res

"""
Solution 2: DP
Another idea is quite similar and has a sense of DP.

C++:

vector<int> shortestToChar2(string S, char C) {
    int n = S.size();
    vector<int> res(n);
    for (int i = 0; i < n; ++i)
        res[i] = S[i] == C ? 0 : n;
    for (int i = 1; i < n; ++i)
        res[i] = min(res[i], res[i - 1] + 1);
    for (int i = n - 2; i >= 0; --i)
        res[i] = min(res[i], res[i + 1] + 1);
    return res;
}


Java:

public int[] shortestToChar(String S, char C) {
    int n = S.length();
    int[] res = new int[n];
    for (int i = 0; i < n; ++i)
        res[i] = S.charAt(i) == C ? 0 : n;
    for (int i = 1; i < n; ++i)
        res[i] = Math.min(res[i], res[i - 1] + 1);
    for (int i = n - 2; i >= 0; --i)
        res[i] = Math.min(res[i], res[i + 1] + 1);
    return res;
}


Python:

"""


def shortestToChar(self, S, C):
    n = len(S)
    res = [0 if c == C else n for c in S]
    for i in range(1, n):
        res[i] = min(res[i], res[i - 1] + 1)
    for i in range(n - 2, -1, -1):
        res[i] = min(res[i], res[i + 1] + 1)
    return res



# ===================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] O(n) solution, explained

"""

What we need to do in this problem is to iterate our data two times: one time from left to right and second time from right to left. Let us use auxilary function letter_get(letter, dr), where dr is direction: +1 for left->right traversal and -1 for right -> left traversal.

How this function will work? We initialize it with zeroes first and we keep cur value, which represents the last place where we meet symbol letter. We traverse string, check each symbol and if it is equal to letter, we update cur place. We put abs(i - cur) to result: this is distance between current place and last place where we meet symbol letter.

Finally, we apply our function twice for two directions and choose the smallest distance. Note also that we initialized curr = -n, because in this case we will have distances >=n for symbols for places, where we do not have elements equal to letter before, and this value is bigger than all possible values in answer, so it works as infinity here.

Complexity: time complexity is O(n), space complexity is O(n) as well.

"""

class Solution:
    def shortestToChar(self, S, C):
        def letter_get(letter, dr):
            n = len(S)
            res, cur = [0]*n, -n
            for i in range(n)[::dr]:
                if S[i] == letter: cur = i
                res[i] = abs(i - cur)
            return res

        return [min(x,y) for x,y in zip(letter_get(C, 1), letter_get(C, -1))]


# ===================================================


# [AUTHOR] akash2099
# [DESCRIPTION] C++ | Two Pass | O(n), 0ms, Beats 100% | Easy Explanation


"""
EXPLANATION

	1. First, iterate the string 's' and store the indexes of 'c' present in 's' into an array or vector ( here vector<int>ioc ) .
	2. Make a left variable for storing the index of left nearest 'c' in ioc and a right variable for storing the index of right nearest 'c' in ioc. Initially, left=0 and right=0, that is keeping the first index of ioc.
	3. Then, iterate string 's' again and at each iteration check if current index crosses ioc[right] ( that is index of 'c' present in ioc pointed by right ) then we need to make left = right and right=right+1.
	4. Also, at each iteration find the minimum value between the following two and store it in ans[i].
		4.1. absolute value of (right nearest 'c' - current index) represented by abs(ioc[right]-i)
		4.2. absolute value of (left nearest 'c' - current index) represented by abs(ioc[left]-i)
	5. Return ans.

CODE IMPLEMENTATION

class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> ioc; // vector for storing the indexed of c present in s
        int n=s.length();
        
        vector<int>ans(n); // answer vector
        
        for(int i=0;i<n;++i){
            if(s[i]==c) 
                ioc.push_back(i);
        }
        
        int m=ioc.size(); // size of ioc vector
        int left=0,right=0;
        
        for(int i=0;i<n;++i){
            
            // if current index has crossed ioc[right] then,
            // we need to make the current left to right and 
            // increment current right for pointing to next index of ioc vector ( if exists )
            if(i>ioc[right]){
                left=right;
                if(right<m-1)
                    ++right;
            }
                        
            // difference = min(abs(right nearest 'c' - curr index),abs(left nearest 'c' - curr index))
            ans[i]=min(abs(ioc[right]-i),abs(ioc[left]-i)); 

        }
        
        return ans;
    }
};


Considering 'n' to be the size of the maximum size of the string 's'.

TIME COMPLEXITY
O(n+n)=O(n) [ For iterating the string two times ]

SPACE COMPLEXITY
O(n) [ In worst case, all characters of 's' is 'c', at that time ( number of 'c' in 's' = size of 's' ) ]
"""

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

