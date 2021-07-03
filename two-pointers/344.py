# [AUTHOR]: xz2210
# [DESCRIPTION]: Simple C++ solution

"""
class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size() - 1;
        while(i < j){
            swap(s[i++], s[j--]); 
        }
        
        return s;
    }
};
"""


# ===================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] Oneliner, two pointers explained

"""
It is very tempting in Python just to use reverse() function, but I think it is not fully honest solution.
Instead, we go from the start and the end of the string and swap pair of elements. One thing, that we need to do is to stop at the middle of our string. We can see this as simplified version of two points approach, because each step we increase one of them and decrease another.

Complexity: Time complexity is O(n) and additional space is O(1).
"""

class Solution:
    def reverseString(self, s):
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]

# [COMMENT]: https://www.youtube.com/watch?v=5keS487q67M

# ===================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution

class Solution:
    def reverseString(self, s: List[str]) -> None:

        if len(s) < 2:
            return s

        leftPtr = 0
        rightPtr = len(s) - 1

        while leftPtr < rightPtr:
            s[leftPtr], s[rightPtr] = s[rightPtr], s[leftPtr]
            leftPtr += 1
            rightPtr -= 1

        return s


