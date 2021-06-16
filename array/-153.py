# [AUTHOR]: StefanPochmann
# [DESCRIPTION]: 1-2 lines Ruby/Python

"""
Use binary search to find the first number that's less than or equal to the last.

Ruby
Direct translation of the above sentence into Ruby.

def find_min(nums)
  nums.bsearch { |num| num <= nums.last }
end


Python
A little hack.
"""

class Solution:
    def findMin(self, nums):
        self.__getitem__ = lambda i: nums[i] <= nums[-1]
        return nums[bisect.bisect(self, False, 0, len(nums))]


# ===================================================

# [AUTHOR]: chuchao333
# [DESCRIPTION]: A concise solution with proof in the comment

"""
class Solution {
public:
    int findMin(vector<int> &num) {
        int low = 0, high = num.size() - 1;
        // loop invariant: 1. low < high
        //                 2. mid != high and thus A[mid] != A[high] (no duplicate exists)
        //                 3. minimum is between [low, high]
        // The proof that the loop will exit: after each iteration either the 'high' decreases
        // or the 'low' increases, so the interval [low, high] will always shrink.
        while (low < high) {
            auto mid = low + (high - low) / 2;
            if (num[mid] < num[high])
                // the mininum is in the left part
                high = mid;
            else if (num[mid] > num[high])
                // the mininum is in the right part
                low = mid + 1;
        }

        return num[low];
    }
};
"""

# [COMMENTS]

"""

Really the BEST solution!! Binary search always bothers me, thanks for sharing. Followings are my understanding from the comments as others reference.

(1) loop is left < right, which means inside the loop, left always < right
(2 ) since we use round up for mid, and left < right from (1), right would never be the same as mid
(3) Therefore, we compare mid with right, since they will never be the same from (2)
(4) if nums[mid] < nums[right], we will know the minimum should be in the left part, so we are moving right.
We can always make right = mid while we don't have to worry the loop will not ends. Since from (2), we know right would never be the same as mid, making right = mid will assure the interval is shrinking.
(5) if nums[mid] > nums[right], minimum should be in the right part, so we are moving left. Since nums[mid] > nums[right],mid can't be the minimum, we can safely move left to mid + 1, which also assure the interval is shrinking

"""

# ===================================================

# [AUTHOR]: water1111
# [DESCRIPTION]: Beat 100%: Very Simple (Python), Very Detailed Explanation

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set left and right bounds
        left, right = 0, len(nums)-1
                
        # left and right both converge to the minimum index;
        # DO NOT use left <= right because that would loop forever
        while left < right:
            # find the middle value between the left and right bounds (their average);
			# can equivalently do: mid = left + (right - left) // 2,
			# if we are concerned left + right would cause overflow (which would occur
			# if we are searching a massive array using a language like Java or C that has
			# fixed size integer types)
            mid = (left + right) // 2
                        
            # the main idea for our checks is to converge the left and right bounds on the start
            # of the pivot, and never disqualify the index for a possible minimum value.

            # in normal binary search, we have a target to match exactly,
            # and would have a specific branch for if nums[mid] == target.
            # we do not have a specific target here, so we just have simple if/else.
                        
            if nums[mid] > nums[right]:
                # we KNOW the pivot must be to the right of the middle:
                # if nums[mid] > nums[right], we KNOW that the
                # pivot/minimum value must have occurred somewhere to the right
                # of mid, which is why the values wrapped around and became smaller.

                # example:  [3,4,5,6,7,8,9,1,2] 
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] > nums[right], we know that at some point to the right of mid,
                # the pivot must have occurred, which is why the values wrapped around
                # so that nums[right] is less then nums[mid]

                # we know that the number at mid is greater than at least
                # one number to the right, so we can use mid + 1 and
                # never consider mid again; we know there is at least
                # one value smaller than it on the right
                left = mid + 1

            else:
                # here, nums[mid] <= nums[right]:
                # we KNOW the pivot must be at mid or to the left of mid:
                # if nums[mid] <= nums[right], we KNOW that the pivot was not encountered
                # to the right of middle, because that means the values would wrap around
                # and become smaller (which is caught in the above if statement).
                # this leaves the possible pivot point to be at index <= mid.
                            
                # example: [8,9,1,2,3,4,5,6,7]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] <= nums[right], we know the numbers continued increasing to
                # the right of mid, so they never reached the pivot and wrapped around.
                # therefore, we know the pivot must be at index <= mid.

                # we know that nums[mid] <= nums[right].
                # therefore, we know it is possible for the mid index to store a smaller
                # value than at least one other index in the list (at right), so we do
                # not discard it by doing right = mid - 1. it still might have the minimum value.
                right = mid
                
        # at this point, left and right converge to a single index (for minimum value) since
        # our if/else forces the bounds of left/right to shrink each iteration:

        # when left bound increases, it does not disqualify a value
        # that could be smaller than something else (we know nums[mid] > nums[right],
        # so nums[right] wins and we ignore mid and everything to the left of mid).

        # when right bound decreases, it also does not disqualify a
        # value that could be smaller than something else (we know nums[mid] <= nums[right],
        # so nums[mid] wins and we keep it for now).

        # so we shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum
        return nums[left]


# ===================================================

# [AUTHOR]: backofhan
# [DESCRIPTION]: My binary-search solution in Python with disscussing

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        first, last = 0, len(num) - 1
        while first < last:
            midpoint = (first + last) // 2
            if num[midpoint] > num[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return num[first]

"""

This solution has a time complexity of O(log(n)) and takes about 50 ms to run.
In python, things are little bit different from the ones in C++ or Java. I am told that each python statement will be translated into one or several c function invocations. So less statements almost always means higher performance. I tried the one line solution "return min(num)" in this subject. It is really a system cheating and has a complexity of O(n). But it yields the identical running time as the binary-search solution. I am not sure about the test inputs. However I think we should have some large ones to make the difference (O(n) VS O(log(n))) visible. I guess we need some inputs which have 100 k or even more numbers.

"""


# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] Failure working solution


class Solution:
    def findMin(self, nums: List[int]) -> int:
        numsLength = len(nums)

        lastItem = nums[numsLength - 1]
        diff = numsLength - lastItem

        # Does not work for number with the step [13, 15, 17, 19]
        return min(nums[diff], nums[diff - 1])

