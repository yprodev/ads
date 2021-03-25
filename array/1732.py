

# ===================================================================================

# [AUTHOR]: Kedaar_Kalyan
# [DESCRIPTION]: Python Simple Solution

def largestAltitude(self, gain: List[int]) -> int:
    ans = [0]

    for i in range(len(gain)):
        ans.append(ans[i] + gain[i])

    return max(ans)


# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Python3] 1-line

# Python3
def largestAltitude(self, A):
    return max([0] + list(accumulate(A)))

# Suggested by @nikamir
def largestAltitude(self, A):
    return max(0, max(accumulate(A)))

# ===================================================================================

# [AUTHOR]: lauvenhelz
# [DESCRIPTION]: python3 explained accumulate solution

from itertools import accumulate 

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial = 0))

"""
If gain = [-5,1,5,0,-7], accumulate by default construct the following:

accumulate([-5,1,5,0,-7]) --> [-5, -4, 1, 1, -6]

(-5) + 1 + 5 + 0 + (-7)

Each element is added to the next, this sum becomes the element of the final list. Could be pictured as a table:

     -5  = -5
-5 +  1  = -4
-4 +  5  =  1
 1 +  0  =  1
 1 + -7  = -6
The second column is the original list [-5,1,5,0,-7], the third column is the final list [-5, -4, 1, 1, -6]. The first column is the result of the previous step.

If the "initial" parameter is not provided, the first element of the result will be the first element of the original iterator. Providing "initial" we set the first element of the result. In case of this problem, the first element should be 0, because a biker always starts from 0:

accumulate([-5,1,5,0,-7], initial=0) --> [0, -5, -4, 1, 1, -6]

In the end just find maximum gain by max()

"""

# ===================================================================================

# [AUTHOR]: akkasayaz
# [DESCRIPTION]: python  faster than 88.13% less memory than 72.00%

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        maximum = 0
        for i in gain:
            high += i
            if high > maximum:
                maximum = high
                
        return maximum

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] NOT working solution
# Issues:
#	

def largestAltitude(self, gain: List[int]) -> int:
    best = 0
    cur = 0
    
    for i in range(len(gain)):
        if gain[i] < 0:
            cur = best + gain[i]

        else:
            cur = abs(gain[i]) + best
            
        if cur >= best:
            best = cur
            
        
        
        print(cur)

# [UPDATE] Use the solution of Kedaar_Kalyan as a reference
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = [0]
        
        for i in range(len(gain)):
            sum.append(sum[i] + gain[i])
            
        return max(sum)
