# [AUTHOR] tanvi284
# [DESCRIPTION] Python simple solution 
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        maps={}
        for num in A:
            if num not in maps:
                maps[num] = 1
            else:
                return num

# ===================================================================================
# [AUTHOR] user6049O
# [DESCRIPTION] Python Randomness O(1) and O(1)
"""
Pick two indices, i and j, in the range [0,len(A)-1] at random. If they are different and A[i] is equal to A[j], then A[i] is the answer.

Space is O(1). Each iteration of the while loop is O(1) in time. What is the expected number of iterations? The probability that we succeed at a given iteration is approximately 1/4 (I don't count the probability of getting first == second which is small if A is large). Hence the expected number of iterations is 4. Just like the average number of dice rolls needed to get a 6. (See here, for example.) The total time complexity is O(1). In practice, it does not perform as great though :)
"""

def repeatedNTimes(self, A: List[int]) -> int:
    while True:
        first = random.randint(0, len(A)-1)
        second = random.randint(0, len(A)-1)
        if first != second and A[first] == A[second]:
            return A[first]

# ===================================================================================
# [AUTHOR] msampathkumar
# [DESCRIPTION] Python using dict with O(N)
"""
Keypoints to note

N+1 unique items like [1, 2, 3]
1 item repeates N times like [1, 2, 2, 3]
so, other than 1 item no other item is going to repeat itself. We will use a dict to record the items we have seen already. We will find the this item by the time we reach N+1th item
"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        mem = {}
        for each in A:
            if each in mem:
                return each
            else:
                mem[each] = None
        return 0

# ===================================================================================
# [AUTHOR] majinlion
# [DESCRIPTION] O(1) Space and O(n) time solution
# [NOTE from ME]:
"""
Almost the same as from user: user6049O
"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a,b = A[0], A[1]
        for i in range(2,len(A)):
            if A[i]==a or A[i]==b:
                return A[i]
            else:
                a = b
                b = A[i]
        return b


# ===================================================================================
# [AUTHOR] lee215
# [DESCRIPTION] [Java/C++/Python] O(1) Solution
"""
This is a solution just for fun, not for interview.
Instead of compare from left to right,
we can compare in random order.

Random pick two numbers.
Return if same.

50% to get the right number.
Each turn, 25% to get two right numbers.
Return the result in average 4 turns.
Time complexity amortized O(4), space O(1)
"""
def repeatedNTimes(self, A):
    while 1:
        s = random.sample(A, 2)
        if s[0] == s[1]:
            return s[0]




# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	1. Looks like brute-force solution
#	2. After looking into example found out that if you store the same element every time,
#	at some point, you will have only this element in the storage (hash table). You may
#	use a principle "the last survivor".
#	3. The solution with randomnes from user6049O is awesome!

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        listLen = len(A)
        n = listLen / 2
        storage = {}
        
        for item in A:
            if item in storage:
                storage[item] = storage[item] + 1
                if storage[item] == n:
                    return item
            else:
                storage[item] = 1
