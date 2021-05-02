# [AUTHOR]: mokar2001
# [DESCRIPTION]: Clear Python Solution

class Solution:
    #Number of cells which are arround of g[i][j] and are inside of island
    def one_surround(self, g, i, j): 
        ans = 0
        n = len(g)
        m = len(g[0])

        if j > 0 and g[i][j-1] == 1:ans += 1
        if i > 0 and g[i-1][j] == 1:ans += 1
        if j < m-1 and g[i][j+1] == 1:ans += 1
        if i < n-1 and g[i+1][j] == 1:ans += 1

        return ans

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 4-self.one_surround(grid, i, j)

        return ans

# ===================================================

# [AUTHOR]: jdjdjd
# [DESCRIPTION]: Mine is pretty similar

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            u = 1 if i>0 and grid[i-1][j]==1 else 0
            d = 1 if i<m-1 and grid[i+1][j]==1 else 0
            l = 1 if j>0 and grid[i][j-1]==1 else 0
            r = 1 if j<n-1 and grid[i][j+1]==1 else 0
            return 4-u-d-l-r
            
        p = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    p += dfs(i,j)
        return p

# ===================================================

# [AUTHOR]: Xyzzy123
# [DESCRIPTION]: Xyzzy123

def islandPerimeter(self, grid: List[List[int]]) -> int:
    perim = 0
    h, w = len(grid), len(grid[0])

    # Iterate through each cell
    for row in range(0, h):
        for col in range(0, w):

            # Is this a land cell?
            if grid[row][col] == 1:

                # Top edge
                if row == 0 or grid[row - 1][col] == 0:
                    perim += 1

                # Bottom edge
                if row == h - 1 or grid[row + 1][col] == 0:
                    perim += 1

                # Left edge
                if col == 0 or grid[row][col - 1] == 0:
                    perim += 1

                # Right edge
                if col == w - 1 or grid[row][col + 1] == 0:
                    perim += 1

    return perim

# ===================================================

# [AUTHOR]: StefanPochmann
# [DESCRIPTION]: Short Python

def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid))) # *grid - spread operator



# Comment area (from ysonglc):

class Solution(object):
    def islandPerimeter(self, grid):
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]
        return sum(row.count('01') + row.count('10') for row in grid_ext)

# ===================================================

# [AUTHOR]: holyghost
# [DESCRIPTION]: clear and easy java solution

"""

public class Solution {
    public int islandPerimeter(int[][] grid) {
        int islands = 0, neighbours = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++; // count islands
                    if (i < grid.length - 1 && grid[i + 1][j] == 1) neighbours++; // count down neighbours
                    if (j < grid[i].length - 1 && grid[i][j + 1] == 1) neighbours++; // count right neighbours
                }
            }
        }

        return islands * 4 - neighbours * 2;
    }
}


loop over the matrix and count the number of islands;
if the current dot is an island, count if it has any right neighbour or down neighbour;
the result is islands * 4 - neighbours * 2
"""

# ===================================================

# [AUTHOR]: StefanPochmann
# [DESCRIPTION]: Python via Strings

def totalHammingDistance(self, nums):
    return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

# ===================================================

# [AUTHOR]: 
# [DESCRIPTION]: 

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] Copied solution from mokar2001 and jdjdjd
# Issues:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        def neighbors(grid, rowLen, colLen, row, col):
            res = 0
            
            # Lower band - not negative iterator
            # Last col has neighbor before it
            if j > 0 and grid[i][j - 1] == 1: 
                res += 1
            
            # Lower band - not negative iterator
            # The same col, but top row has neighbor at the same position
            if i > 0 and grid[i - 1][j] == 1:
                res += 1
            
            # Upper band - not above the row size
            # Last col next value (neighbor) present
            if j < n - 1 and grid[i][j + 1] == 1:
                res += 1
                
            # Upper band - not above the col size
            # Next row neighbor at the same position present
            if i < m - 1 and grid[i + 1][j] == 1:
                res += 1
                
            return res
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4 - neighbors(grid, m, n, i, j)
                    
        return res


# [LEARN] what is zip function is in python?
# [LEARN] *numbers - spread operator in python?
# [LEARN] What is Hamming distance?
# [LEARN] What is this --> '{:032b}'.format? Looks like formating to binary callback function