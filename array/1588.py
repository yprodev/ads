

# ===================================================================================

# [AUTHOR]: lokeshsenthilkumar
# [DESCRIPTION]: Python Simple Solution

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s+=sum(arr[i:j+1])
        return s

# ===================================================================================

# [AUTHOR]: Philno
# [DESCRIPTION]: python 3 99.78% faster and 100% less space

"""

he idea is to count the frequency of each element in arr appearing in the sub array, then sum up arr[i]*freq[i]. The key is how to count the freq[i] of each element arr[i]. Actually, freq[i] = freq[i-1]-(i+1)//2+(n-i+1)//2. n is the arr length.

for example arr = [1,4,2,5,3], element arr[0] = 1. The appearing freq of head element arr[0] should be how many odd-length sub arrays it can generate. The answer is (len(arr)+1)//2. Therefore, the freq of element arr[0] = 1 is (5+1)//2=3.

Now let's take element arr[1] = 4 for example, if we take element arr[0] = 1 out, then arr[1] = 4 becomes the new head element, thus the freq of arr[1] = 4 in the new subarray could be calculated as the same way of arr[0] = 1. It seems that all we need to do is add the freq of previous element arr[0] up then we get the freq of arr[1].

No, we also need to minus the subarrays of previous element arr[0] = 1 when they do not include arr[1]=4. In this case, it is [1]. This is why freq[i] = freq[i-1]-(i+1)//2+(n-i+1)//2.

To sum up, the core idea is to find the relationship between freq_current_element and freq_previous_element.

TAKE A LOOK AT 1588.png IMAGE in ARRAY FOLDER.

"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # corner case
        
        res = 0; freq = 0; n = len(arr)
        for i in range(n):
            freq = freq - (i + 1) // 2 + (n - i + 1) // 2
            res += freq * arr[i]
        return res


# ===================================================================================

# [AUTHOR]: geordgez
# [DESCRIPTION]: O(n) time, O(1) space step-by-step explanation [Python]

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
		
        for i in range(n):
            even_away = ((i // 2) + 1) * ((n - i - 1) // 2 + 1)
            odd_away = ((i + 1) // 2) * ((n - i) // 2)
            res += arr[i] * (even_away + odd_away)
            
        return res

"""
Approach
Summary: we can quickly count the number of times that each element in the array will be added to the final sum. That way, the answer is just the sum of [each element times its frequency]. And we know the number of times it will be added to the sum is the number of unique valid odd intervals which contain it

Even distance away from current index i
Consider all indices 0 to n - 1 which are an even distance away from index i

	all possible starting indices for odd-length intervals which include i are {i, i - 2, i - 4, ...}
		the number of starting indices is (i // 2) + 1
	all possible ending indices for odd-length intervals which include i are {i, i + 2, i + 4, ...}
		the number of ending indices is (n - 1 - i) // 2 + 1

Final number of occurrences of the element at index i is just the number of possible starting indices multiplied by the number of possible ending indices.

Apply the same logic for all candidate points an odd distance away from current index i.

	all possible starting indices for intervals which include i are {i - 1, i - 3, i - 5, ...}
		the number of starting indices is (i + 1) // 2
	all possible ending indices for intervals which include i are {i + 1, i + 3, i + ,5 ...}
		the number of ending indices is (n - i) // 2

Illustrated

Example for i = 3, n = 10

Even        [        [ ]        ]         ]         ]
Index  0 -- 1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 7 -- 8 -- 9
Odd    [         [         ]         ]         ]

[ = potential start
] = potential end

Element at index 3 arr[3] is added |"["| * |"]"| = 2 * 4 = 8 times by intervals which start from an even index distance away.

Even starts: {1, 3}
Even ends: {3, 5, 7, 9}
All even intervals [i, j] where the sum arr[i:j + 1] contributes arr[3] to the final answer: [1, 3], [3, 3], [1,5], [3, 5], [1, 7], [3, 7], [1, 9], [3, 9]
arr[3] is also added 2 * 3 = 6 times by intervals which start from an odd index distance away.

Intuition for counting number of starting and ending indices for a given index i

	From 0 to i there are i // 2 + 1 even distance indices because this is equivalent to the number of even numbers from 0 to i & 0 (i.e. i if i is even, otherwise i - 1 if i is odd) inclusive. To see this, map all indices i => i // 2. Then this is the equivalent of counting the numbers from 0 to (i & 0) / 2 = i // 2 inclusive, which is (i // 2 - 0) + 1 = i // 2 + 1

	From 0 to i there are (i + 1) // 2 odd distance indices because we are counting the number of even numbers from 0 to i + 1. Why i + 1? Because every time i becomesa add, it adds an extra start candidate. i = 0 has no odd start candidates. i = 1 and i = 2 both have one odd start candidate j, although j = 0 for i = 1 and j = 1 for i = 2. i = 3 and i = 4 both have two start candidates.

	Apply the same analysis to count the number of ending candidate indices from i to n - 1 for even and odd index distances

(Writing this up so I can reinforce the idea to myself since this kind of thinking isn't intuitive for me and other linear explanations don't try to explain how to get the counts / frequencies of each element. I imagine it will be helpful for other people who see linear explanations which don't completely explain the intuition.)


"""


# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Java/C++/Python] O(N) Time, O(1) Space

"""
Intuition
Hmmm, totally not an easy problem.
That where it's misleading:
It lets brute force get accepted,
and mark it as easy.


Solution 1: Brute Force
Enumerate all possible odd length of subarray.
Time O(n^3)
Space O(1)

"""

# Python
def sumOddLengthSubarrays(self, A):
        n = len(A)
        res = 0
        for l in xrange(1, n + 1, 2):
            for i in xrange(n - l + 1):
                res += sum(A[i:i + l])
        return res

# Python 1 line

def sumOddLengthSubarrays(self, A):
        return sum(sum(A[i:i + l]) for l in xrange(1, 100, 2) for i in xrange(len(A) - l + 1))


"""
Also suggested by @mayank12559 and @simtully.

Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left,
from A[0] to A[i],
we have i + 1 choices.

we can take 0,1,2..,n-1-i elements on the right,
from A[i] to A[n-1],
we have n - i choices.

In total, there are k = (i + 1) * (n - i) subarrays, that contains A[i].
And there are (k + 1) / 2 subarrays with odd length, that contains A[i].
And there are k / 2 subarrays with even length, that contains A[i].

A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times for our question.


Example of array [1,2,3,4,5]
1 2 3 4 5 subarray length 1
1 2 X X X subarray length 2
X 2 3 X X subarray length 2
X X 3 4 X subarray length 2
X X X 4 5 subarray length 2
1 2 3 X X subarray length 3
X 2 3 4 X subarray length 3
X X 3 4 5 subarray length 3
1 2 3 4 X subarray length 4
X 2 3 4 5 subarray length 4
1 2 3 4 5 subarray length 5

5 8 9 8 5 total times each index was added, k = (i + 1) * (n - i)
3 4 5 4 3 total times in odd length array with (k + 1) / 2
2 4 4 4 2 total times in even length array with k / 2s


Complexity
Time O(N)
Space O(1)


"""

"""
C++

int sumOddLengthSubarrays(vector<int>& A) {
    int res = 0, n = A.size();
    for (int i = 0; i < n; ++i) {
        res += ((i + 1) * (n - i) + 1) / 2 * A[i];
    }
    return res;
}
"""


# Python
def sumOddLengthSubarrays(self, A):
    res, n = 0, len(A)
    for i, a in enumerate(A):
        res += ((i + 1) * (n - i) + 1) / 2 * a
    return res

def sumOddLengthSubarrays(self, A):
    return sum(((i + 1) * (len(A) - i) + 1) / 2 * a for i, a in enumerate(A))


# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] NOT working solution
# Issues:
#	Looks like this should be done with the dynamic programming. Not confident 
#	enough in this area

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int], nxt: int, memo: any = {}) -> int:
               
        # Negative base case
        if arr is None:
            return 0
        
        newArr = arr[nxt]
        
        # Base case
        if len(arr) <= 2:
            return arr[nxt] + arr[nxt + 1]
        
        memo[nxt + "," + nxt + 1]

