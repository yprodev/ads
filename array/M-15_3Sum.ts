// [AUTHOR] DBabichev
// [DESCRIPTION] [Python] 2 Pointers O(n^2) solution, explained
// [LINK] https://leetcode.com/problems/3sum/discuss/725581/Python-2-Pointers-O(n2)-solution-explained

/*

This problem is similar to 2Sum problem, but here we need to find sums of three elements. We can use similar idea with hash-tables, but the problem here is that we can have duplicates, and it is a bit painful to deal with them, using hash-tables, we need to count frequencies, make sure, we did not use the same elements and so on.

Another approach is to use 2 Pointers approach. Let us sort our data first and choose element number i. What we need to find now is some elements with indexes beg and end, such that i < beg < end and nums[beg] + nums[end] = target = -nums[i]. Here times come to use our 2 Pointers approach: we start from beg, end = i + 1, n - 1, and move beg to the right and end to the left, comparing nums[beg] + nums[end] with our target. If it is equal to target, we add it to our result, and move two pointers. However, because we can have equal numbers in nums, we still need to check, that we return unique triples, so we apply set in the end.

Complexity: time complexity is O(n log n + n^2) = O(n^2), because we sorted our data, and then we have loop with n iterations, inside each of them we use 2 pointers approach with O(n) complexity (inside while beg < end: each time distance between our pointers reduced by at least 1). Space complexity is potentially O(n^2), because there can be potentially O(n^2) solutions:

let nums = [-n,-n+1,..., n-1, n] with 2n+1 = O(n) numbers, then there will be solutions:
1 2 -3, 1 3 -4, ... , 1 n-1 -n
2 3 -5, 2 4 -6, ... , 2 n-2 -n

in first group there will be n-2 solutions, in second n-4 and so on.
Sum of arithmetic progression n-2 + n-4 + ... is approximately equalt to n^2/4.
We also have more solutions, but we already showed that there is O(n^2).

class Solution:
    def threeSum(self, nums):
        nums.sort()
        n, result = len(nums), []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue

            target = -nums[i]
            beg, end = i + 1, n - 1

            while beg < end:
                if nums[beg] + nums[end] < target:
                    beg += 1
                elif nums[beg] + nums[end] > target:
                    end -= 1
                else:
                    result.append((nums[i], nums[beg], nums[end]))
                    beg += 1
                    end -= 1

        return set(result)

*/


// ==========================================================================

/*
    My first NOT working solution. In my solution, I have duplicates
    and it is not okay. So, the tests are failing.
*/
function threeSum(nums: number[]): number[][] {
  nums.sort();

  let triplets = [];

  for (let curr = 0; curr < nums.length - 2; curr++) {
    let leftIdx = curr + 1,
        rightIdx = nums.length - 1;

    while (leftIdx < rightIdx) {
      let currentSum = nums[curr] + nums[leftIdx] + nums[rightIdx];

      if (currentSum === 0) {
        triplets.push([nums[curr], nums[leftIdx], nums[rightIdx]]);
        leftIdx++;
        rightIdx--;
      }

      if (currentSum < 0) {
        leftIdx++;
      }

      if (currentSum > 0) {
        rightIdx--;
      }

    }
  }

  return triplets;
};


