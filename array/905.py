

# ===================================================================================

# [AUTHOR]: RouRouKerr
# [DESCRIPTION]: Python 2 pointer in place swap, beats 99%

"""
Idea is simple - if odd is on the left and even is on the right, then we swap
"""

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start, end = 0, len(A) - 1
        while start < end:
            m, n = A[start], A[end]
            if m % 2 == 1 and n % 2 == 0:
                A[start], A[end] = n, m
            elif m % 2 == 1:
                end -= 1
            elif n % 2 == 0:
                start += 1
            else:
                start += 1
                end -= 1
        return A


# [COMMENT]: __zzz__
# Same idea and different implementation and I believe is cleaner. O(n) time complexity and O(1) space complexity.

class Solution(object):
    def sortArrayByParity(self, A):
        s, e = 0, len(A) - 1
        while s < e: 
            while A[s] % 2 == 0 and s < e:
                s += 1
            while A[e] % 2 == 1 and s < e: 
                e -= 1
            A[s], A[e] = A[e], A[s]
            
        return A


# [COMMENT]: baby_groot
# Same idea and shorter:

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1:
                A[l], A[r] = A[r], A[l]
            l += not (A[l] & 1)
            r -= A[r] & 1
        return A



# ===================================================================================

# [AUTHOR]: dtorba
# [DESCRIPTION]: One line Python beats 87%

return sorted(A, key=lambda x: x % 2)

# ===================================================================================

# [AUTHOR]: limitless_
# [DESCRIPTION]: Very simple C++/Python/Java O(n) soln (Avoid in-place swapping as the input is passed as reference)


"""
C++

vector<int> sortArrayByParity(vector<int>& A) {
        int size = A.size();
        vector<int> res(size, 0);
        int start = 0, end = size - 1;
        for (int i = 0; i < size; i++) {
            if (A[i] % 2 == 1) {
                res[end--] = A[i];
            } else {
                res[start++] = A[i];
            }
        }
        return res;
    }
"""

# Python
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        size = len(A)
        res = [None] * size
        start = 0
        end = size - 1
        for val in A:
            if val % 2 == 1:
                res[end] = val
                end = end -1
            else:
                res[start] = val
                start = start + 1
        return res


"""
Java

class Solution {
    public int[] sortArrayByParity(int[] A) {
        int size = A.length;
        int start = 0, end = size - 1;
        int[] res = new int[size];
        for (int i = 0; i < size; i++) {
            if (A[i] % 2 == 1) {
                res[end--] = A[i];
            } else {
                res[start++] = A[i];
            }
        }
        return res;
    }
}
"""

# ===================================================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] O(n) In place partition, explained

"""
One way to solve this problem is to just sort data or use additional memory. However, there is better approach without using additional memory, using two pointers. The idea is to have two pointers: beg and end, where beg points just after the group of formed even elements in the beginning and end points just before group of odd elements in the end. Let us consider example: A = [1,10,2,3,7,7,8,2,1,4]. On each step I show current A, beg and end. I denote by bold font numbers which are already on place.


Step 1: A = [4, 10, 2, 3, 7, 7, 8, 2, 1, 1], beg = 0, end = 8
Step 2: A = [4, 10, 2, 3, 7, 7, 8, 2, 1, 1], beg = 1, end = 8
Step 3: A = [4, 10, 2, 3, 7, 7, 8, 2, 1, 1], beg = 2, end = 8
Step 4: A = [4, 10, 2, 3, 7, 7, 8, 2, 1, 1], beg = 3, end = 8
Step 5: A = [4, 10, 2, 1, 7, 7, 8, 2, 3, 1], beg = 3, end = 7
Step 6: A = [4, 10, 2, 2, 7, 7, 8, 1, 3, 1], beg = 3, end = 6
Step 7: A = [4, 10, 2, 2, 7, 7, 8, 1, 3, 1], beg = 4, end = 6
Step 8: A = [4, 10, 2, 2, 8, 7, 7, 1, 3, 1], beg = 4, end = 5
Step 9: A = [4, 10, 2, 2, 8, 7, 7, 1, 3, 1], beg = 5, end = 5
Step 10: A = [4, 10, 2, 2, 8, 7, 7, 1, 3, 1], beg = 5, end = 4

Complexity: Time complexity is O(n), space complexity is O(1), because we do all in place.

Note also, that this problem is special case of problem 75: Sort Colors, where we need to partition in three parts, here we have only two. See my post, explaing this problem.
https://leetcode.com/problems/sort-colors/discuss/681526/Python-O(n)-3-pointers-in-place-approach-explained

"""

class Solution:
    def sortArrayByParity(self, A):
        beg, end = 0, len(A) - 1
        
        while beg <= end:
            if A[beg] % 2 == 0:
                beg += 1
            else:
                A[beg], A[end] = A[end], A[beg]
                end -= 1
        return A




# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
                
        return even + odd
