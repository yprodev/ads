// [AUTHOR] FujiwaranoSai
// [DESCRIPTION] DP solution & some thoughts
// [LINK] https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

/*
public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
        dp[0] = A[0];
        int max = dp[0];
        
        for(int i = 1; i < n; i++){
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(max, dp[i]);
        }
        
        return max;
}

*/

// ==========================================================================


// [AUTHOR] Chaitanya1706
// [DESCRIPTION] JAVA | Kadane's Algorithm | Explanation Using Image
// [LINK] 


/*

Intution: Start traversing your array keep each element in the sum and every time keep the max of currSum and prevSum.
But the catch here is that if at any point sum becomes negative then no point keeping it because 0 is obviously greater than negative, so just make your sum 0.

Now here in this question you can see that you can also be asked some more things like :

    1. Length of the max subarray
    2. Elements of the max subarray
    3. Start and End index of max subarray

This is very important concept from interview point so try to get the ans of above mentioned point and have confidence on this algorithm.

P.S. : I see a lots of comments saying this algorithm will not work if all the elements are negative....plz analyze it carefully...this is working for every case.

if(sum<0) sum = 0; -> this line is doing some magic. Dry run the algorithm carefully and u will get the answer.

class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int max = Integer.MIN_VALUE, sum = 0;
        
        for(int i=0;i<n;i++){
            sum += nums[i];
            max = Math.max(sum,max);
            
            if(sum<0) sum = 0;
        }
        
        return max;
    }
}

*/

// ==========================================================================


// [AUTHOR] linfongi
// [DESCRIPTION] JavaScript solution
// [LINK] https://leetcode.com/problems/maximum-subarray/discuss/20471/JavaScript-solution

function maxSubArray(A) {
  var prev = 0;
  var max = -Number.MAX_VALUE;

  for (var i = 0; i < A.length; i++) {
    prev = Math.max(prev + A[i], A[i]);
    max = Math.max(max, prev);
  }
  return max;
}

// ==========================================================================

// [AUTHOR] EziO-
// [DESCRIPTION] Kadane's Algorithm Javascript
// [LINK] https://leetcode.com/problems/maximum-subarray/discuss/1152811/Kadane's-Algorithm-Javascript

var maxSubArray = function(nums) {
    let sum = 0;
    let maxSum = -Infinity;
    
    if(nums.length === 0) return 0;
    if(nums.length === 1) return nums[0]
    
    for(let i = 0;i<nums.length;i++){
        sum+=nums[i];
        maxSum = Math.max(maxSum,sum);
        if(sum < 0) sum = 0;
    }
    return maxSum;
};

// ==========================================================================

// [AUTHOR] archit91
// [DESCRIPTION] [C++/Python] 7 Simple Solutions w/ Explanation | Brute-Force + DP + Kadane + Divide & Conquer
// [LINK] https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer

// BETTER TO SEE IT WITH YOUR OWN EYES

// ==========================================================================

