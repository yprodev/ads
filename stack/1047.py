# Input: String with duplicates ---> "abbaca"
# Output: String without duplicates ---> "ca"

# ===================================================================================

# [AUTHOR]: cs_abhi
# [DESCRIPTION]: python | No stack | Using slow and fast pointer | TC: O(n) SC: O(1)
class Solution:
    def removeDuplicates(self, a: str) -> str:
        slow=0
        a=list(a)
        for fast in range(len(a)):
            if slow==0 or a[slow-1]!=a[fast]:
                a[slow]=a[fast]
                slow+=1
            else:
                slow-=1
        return ''.join(a[:slow])

# ===================================================================================

# [AUTHOR]: waxwingSlain
# [DESCRIPTION]: Python Recursion Solution
class Solution:
    def removeDuplicates(self, S: str) -> str:
        originalS = S
        for i in range(len(S) - 1):
            if S[i] == S[i+1]:
                S = S.replace(S[i]+S[i+1], '', 1)
                break

        if originalS == S:
            return S
        else:
            return self.removeDuplicates(S)

# ===================================================================================

# [AUTHOR]: abhyasa
# [DESCRIPTION]: Python3 | Stack Solution | O(n)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp = []
        temp.append(S[0])

        for i in range(1, len(S)):
            element = S[i]
            if temp and temp[-1] == element:
                temp.pop()
            else:
                temp.append(S[i])

        return ''.join(temp)

# ===================================================================================

# [AUTHOR]: priyabhatia
# [DESCRIPTION]: Python Solution Using Stack
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	Basic knowledge of Python3
#	Really slow algorithm (probably because of copying the list after
#	the else statement)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for i in range(0, len(S)):
            if not stack or S[i] != stack[-1]:
                stack.append(S[i])
            else:
                stack = stack[:-1]

        return "".join(stack)

# [AUTHOR] ME
# [DESCRIPTION] Second working solution (optimized)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        
        for i in range(0, len(S)):
            if not stack or S[i] != stack[-1]:
                stack.append(S[i])
            else:
                stack.pop()
                
        return "".join(stack)


# NOTES:
# list(str) - creates a list of characters
