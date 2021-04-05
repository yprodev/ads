

# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Java/C++/Python] Stack, One Pass

"""
Intuition
Similar to the problem 503. Next Greater Element II


Complexity
Time O(N)
Space O(N)


Java:

public int[] finalPrices(int[] A) {
    Stack<Integer> stack = new Stack<>();
    for (int i = 0; i < A.length; i++) {
        while (!stack.isEmpty() && A[stack.peek()] >= A[i])
            A[stack.pop()] -= A[i];
        stack.push(i);
    }
    return A;
}

C++:

vector<int> finalPrices(vector<int>& A) {
    vector<int> stack;
    for (int i = 0; i < A.size(); ++i) {
        while (stack.size() && A[stack.back()] >= A[i]) {
            A[stack.back()] -= A[i];
            stack.pop_back();
        }
        stack.push_back(i);
    }
    return A;
}

Python:


"""
def finalPrices(self, A):
    stack = []
    for i, a in enumerate(A):
        while stack and A[stack[-1]] >= a:
            A[stack.pop()] -= a
        stack.append(i)
    return A


"""
More Good Stack Problems
Here are some problems that impressed me.
Good luck and have fun.

1673. Find the Most Competitive Subsequence
1671. Minimum Number of Removals to Make Mountain Array
1475. Final Prices With a Special Discount in a Shop
1425. Constrained Subsequence Sum
1130. Minimum Cost Tree From Leaf Values
 907. Sum of Subarray Minimums
 901. Online Stock Span
 856. Score of Parentheses
 503. Next Greater Element II
 496. Next Greater Element I
  84. Largest Rectangle in Histogram
  42. Trapping Rain Water

"""

# ===================================================================================

# [AUTHOR]: rock
# [DESCRIPTION]: 

"""
In short, use a stack to maintain the indices of strickly increasing prices.

1. Clone the prices array as original price before discount;
2. Use a stack to hold the indices of the previous prices that are less than current price;
3. Keep poping out the prices that are NO less than current price, deduct current price as discount from previous prices.

"""
def finalPrices(self, prices: List[int]) -> List[int]:
        res, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)
        return res

# ===================================================================================

# [AUTHOR]: anshul1pathak
# [DESCRIPTION]: Easiest C++ Solution !!

"""
class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        
        for(int i=0; i<prices.size()-1; i++)
        {
            for(int j=i+1; j<prices.size(); j++)
            {
                if(prices[j]>prices[i])
                {
                    continue;
                }
                else
                {
                  prices[i]-=prices[j];
                    break;
                }
            }
        }
        return prices;
        
    }
};
"""

# ===================================================================================


# [AUTHOR] ME
# [DESCRIPTION] NOT WORKING SOLUTION
# Issues:
#	


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pLength = len(prices)
        res = []
        point = 0
        
        for i in range(pLength):
            for j in range(i, pLength):
                if prices[j] < prices[i]:
                    res.append(prices[i] - prices[j])
                    break

