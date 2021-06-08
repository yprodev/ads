# [AUTHOR]: Dr_Sean
# [DESCRIPTION]: [Python3] Improving the Leetcode Solution and Avoiding the Use of 'str', 'int' and 'map'

"""
Notes:
Leetcode provided a simple solution, but it is not efficient. K has 5 digits at most, but A can have 10000 elements. This means that the summation might finish after 5 iterations, but the loop will continue for 10000 times! I added a condition to avoid this.
I think the purpose of this question is to provide a summation based on elementary school math, and avoid other functions such as 'str', 'int' and 'map'.
The Leetcode solution does not work for Python3, but slight changes would make it compatible for both Python/ Python3.
Python/ Python3 code:

"""

for i in range(len(A) - 1, -1, -1):
    if not K: break
        K, A[i] = divmod(A[i] + K, 10)
    while K:
        K, a = divmod(K, 10)
        A = [a] + A
    return A

"""LeetCode suggestion


Approach 1: Schoolbook Addition
Intuition

Let's add numbers in a schoolbook way, column by column. For example, to add 123 and 912, we add 3+2, then 2+1, then 1+9. Whenever our addition result is more than 10, we carry the 1 into the next column. The result is 1035.

Algorithm

We can do a variant of the above idea that is easier to implement - we put the entire addend in the first column from the right.

Continuing the example of 123 + 912, we start with [1, 2, 3+912]. Then we perform the addition 3+912, leaving 915. The 5 stays as the digit, while we 'carry' 910 into the next column which becomes 91.

We repeat this process with [1, 2+91, 5]. We have 93, where 3 stays and 90 is carried over as 9. Again, we have [1+9, 3, 5] which transforms into [1, 0, 3, 5].


"""

class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A


# ===================================================

# [AUTHOR]: JLepere2
# [DESCRIPTION]: Simple Python

class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        A[-1] += K
        i = len(A) - 1
        while i > 0 and A[i] > 9:
            A[i-1] += A[i] // 10
            A[i] = A[i] % 10
            i -= 1
        while A[0] > 9:
            A = [A[0] // 10] + A
            A[1] = A[1] % 10
        return A

# ===================================================

# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3] 6 liner w/ comment and analysis

"""
Note:
I read several other java solutions, and found ArrayList.add(0, K % 10) was used, and it is not O(1) but O(n) instead.

LinkedList.add(0, i) or offerFirst(i) is O(1).

Correct me if I am wrong.

public List<Integer> addToArrayForm(int[] A, int K) {
    LinkedList<Integer> ans = new LinkedList<>();
    for (int i = A.length - 1; K > 0 || i >= 0; --i, K /= 10) { // loop through A and K, from right to left.
        K += i >= 0 ? A[i] : 0; // Use K as carry over, and add A[i].
        ans.offerFirst(K % 10); // add the least significant digit of K.
    }
    return ans;
}

Analysis:

Time & space: O(n + logK), where n = A.length.

"""

def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    ans, i = [], len(A) - 1
    while K > 0 or i >= 0:
        K, rmd = divmod(K + (A[i] if i >= 0 else 0), 10)
        ans.append(rmd)
        i -= 1
    return reversed(ans)

# ===================================================

# [AUTHOR]: Just__a__Visitor
# [DESCRIPTION]: C++ Well Commented Solution [With Explanation] [100%]
"""
/* An important observation ---
1) num%10 gives us the last digit of a number
2) num = num/10 cuts off the last digit of the number 
3) numVector.back() gives us the last digit of the number in vector form
4) numVector.pop_back() cuts off the last digit of the number in vector form
5) The extra space required can be reduced by overwriting the first vector. 
*/


class Solution
{
public:
    vector<int> addToArrayForm(vector<int>& a, int k);
};

/* Returns the sum of 2 numbers in vector form */
vector<int> Solution :: addToArrayForm(vector<int>& a, int k)
{
    // Get the length of the first number
    int n = a.size();
    
    // Vector to store the answer
    vector<int> answer;
    
    /* Start adding both the numbers from the end */
    
    int carry = 0;
    // As long as one of the number exists, keep adding them
    while(!a.empty() || k!=0)
    {
        // Get the last digits of both the numbers. If a vector has finished off, the last digit is zero
        int lastDigit_1 = a.empty() ? 0 : a.back();
        int lastDigit_2 = k%10;
        
        // Sum up the digits and add the carry
        int sum = lastDigit_1 + lastDigit_2 + carry;
        answer.push_back(sum%10);
        carry = sum/10;
        
        // Remove the last digits of both the numbers
        if(!a.empty()) a.pop_back();
        k = k/10;
    }
    
    // If the carry is remaining, add it
    if(carry!=0) answer.push_back(carry);
    
    // Reverse the answer, since we were summing up from the end
    reverse(answer.begin(), answer.end());
    
    // Return the answer in vector format
    return answer;
}

"""

# ===================================================


# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3] 6 liner w/ comment and analysis

"""
Note:
I read several other java solutions, and found ArrayList.add(0, K % 10) was used, and it is not O(1) but O(n) instead.

LinkedList.add(0, i) or offerFirst(i) is O(1).

Correct me if I am wrong.

public List<Integer> addToArrayForm(int[] A, int K) {
    LinkedList<Integer> ans = new LinkedList<>();
    for (int i = A.length - 1; K > 0 || i >= 0; --i, K /= 10) { // loop through A and K, from right to left.
        K += i >= 0 ? A[i] : 0; // Use K as carry over, and add A[i].
        ans.offerFirst(K % 10); // add the least significant digit of K.
    }
    return ans;
}

Analysis:

Time & space: O(n + logK), where n = A.length.

"""

def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    ans, i = [], len(A) - 1
    while K > 0 or i >= 0:
        K, rmd = divmod(K + (A[i] if i >= 0 else 0), 10)
        ans.append(rmd)
        i -= 1
    return reversed(ans)


# ===================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        strArr = [str(i) for i in num]
        strInt = ''.join(strArr)
        arrNum = int(strInt)

        res = arrNum + k

        return [int(x) for x in str(res)]

# [QUESTIONS]:
# What is divmod function in Python?
# What does this do: range(len(A) - 1, -1, -1)?
# What is xrange function?



# [AUTHOR] ME (re-typed the solution from rock)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans, i = [], len(num) - 1

        while k > 0 or i >= 0:
            k, rmd = divmod(k + (num[i] if i >= 0 else 0), 10)
            ans.append(rmd)
            i -= 1

        return reversed(ans)

