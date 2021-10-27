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

# [AUTHOR]: jamiehsmith
# [DESCRIPTION]: Javascript - Simple with comments

"""
var reverseString = function(s) {
    // Loop through 1/2 of s
    for (let i = 0; i < s.length / 2; i++) {
        // Save current val
        let temp = s[i];
        
        // Replace with end of array char
        s[i] = s[s.length - 1 - i];
        
        // Replace end of array letter with current val
        s[s.length - 1 - i] = temp;
    }
};
"""

# ===================================================

# [AUTHOR]: jesseokeya
# [DESCRIPTION]: Javascript Solution. Beats 87.72%

"""
var reverseString = function(s) {
    for (let i = 0; i < s.length / 2; i++) {
        [s[i], s[(s.length - i) - 1]] = [s[(s.length - i) - 1], s[i]] 
    }
};
"""


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




"""
# [AUTHOR] ME
# [DESCRIPTION] Second working solution

var reverseString = function(s) {
    let temp = null,
        left = 0,
        right = s.length - 1;

    while (left < right) {
        temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }


};

"""
