

# ===================================================================================

# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3] 2 similar O(m + n) codes w/ brief explanation and analysis.

"""
Please refer to the perspicacious elaboration from @ikeabord as follows:
This solution uses the fact that the negative regions of the matrix will form a "staircase" shape, e.g.:

++++++
++++--
++++--
+++---
+-----
+-----

What this solution then does is to "trace" the outline of the staircase.

Start from bottom-left corner of the matrix, count in the negative numbers in each row.

"""

def countNegatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    r, c, cnt = m - 1, 0, 0
    while r >= 0 and c < n:
        if grid[r][c] < 0:
            cnt += n - c
            r -= 1
        else:
            c += 1
    return cnt

"""
Simlarly, you can also start from top-right corner, whichever you feel comfortable with, count in the negative numers in each column.
"""

def countNegatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    r, c, cnt = 0, n - 1, 0
    while r < m and c >= 0:
        if grid[r][c] < 0:
            cnt += m - r
            c -= 1
        else:
            r += 1
    return cnt

"""
Analysis:

At most move m + n steps.
Time: O(m + n), space: O(1).

For more practice of similar problem, please refer to:

https://leetcode.com/problems/search-a-2d-matrix-ii/
https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

"""


# ===================================================================================

# [AUTHOR]: nuclearoreo
# [DESCRIPTION]: Python - Simple Solution

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for r in grid:
            for e in r[::-1]:
                if e < 0: count += 1
                else: break
        return count

# ===================================================================================

# [AUTHOR]: Mrmagician
# [DESCRIPTION]: Easy to understand | Binary Search | Faster | Python Solution

"""
Time complexity: O(nlogm), n = no. of rows, m = no. of cols
Space complexity: O(n), But it can be constant easily by taking a variable and adding to it after every iteration

"""

def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([self.binary_search(arr) for arr in grid])
        
    def binary_search(self, arr):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < 0:
                end = mid - 1
            else: 
                start = mid + 1
        return len(arr) - start


# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Python] Different 1-line


# Python, O(N^2)
def countNegatives(self, A):
    return sum(a < 0 for r in A for a in r)

# Python, binary search, O(NlogN)
# by @ManuelP
def countNegatives(self, A):
    return sum(bisect_left(type('', (), {'__getitem__': lambda _, i: r[~i]})(), 0, 0, len(r)) for r in A)

# Python, numpy, O(N^2)
# by @MrDelhi
def countNegatives(self, grid):
    return (np.array(grid) < 0).sum()

# Python, str(), O(N^2)
# by @nikog8
def countNegatives(self, grid):
    return str(grid).count('-')


# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	This is Brute-Force solution. While the columns sub-arrays are sorted,
#	just find the very first negative number position (index) and substruct
#	it from the length of the sub-array. You will get the number of negative
#	items left. No need to go through all the array and use nested loop.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    res += 1
                
                
        return res
