# [AUTHOR]: lee215
# [DESCRIPTION]: [Java/C++/Python] O(N) Solution, Life needs 996 and 669

"""

Intuition
If working hour > 8 hours, yes it's tiring day.
But I doubt if 996 is a well-performing interval.
Life needs not only 996 but also 669.


Explanation
We starts with a score = 0,
If the working hour > 8, we plus 1 point.
Otherwise we minus 1 point.
We want find the maximum interval that have strict positive score.

After one day of work, if we find the total score > 0,
the whole interval has positive score,
so we set res = i + 1.

If the score is a new lowest score, we record the day by seen[cur] = i.
seen[score] means the first time we see the score is seen[score]th day.

We want a positive score, so we want to know the first occurrence of score - 1.
score - x also works, but it comes later than score - 1.
So the maximum interval is i - seen[score - 1]


Java

Complexity
Time O(N) for one pass.
Space O(N) in worst case if no tiring day.

public int longestWPI(int[] hours) {
    int res = 0, score = 0, n = hours.length;
    Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < n; ++i) {
        score += hours[i] > 8 ? 1 : -1;
        if (score > 0) {
            res = i + 1;
        } else {
            seen.putIfAbsent(score, i);
            if (seen.containsKey(score - 1))
                res = Math.max(res, i - seen.get(score - 1));
        }
    }
    return res;
}


C++

int longestWPI(vector<int>& hours) {
    int res = 0, score = 0, n = hours.size();
    unordered_map<int, int> seen;
    for (int i = 0; i < n; ++i) {
        score += hours[i] > 8 ? 1 : -1;
        if (score > 0) {
            res = i + 1;
        } else {
            if (seen.find(score) == seen.end())
                seen[score] = i;
            if (seen.find(score - 1) != seen.end())
                res = max(res, i - seen[score - 1]);
        }
    }
    return res;
}


"""

def longestWPI(self, hours):
    res = score = 0
    seen = {}
    for i, h in enumerate(hours):
        score = score + 1 if h > 8 else score - 1
        if score > 0:
            res = i + 1
        seen.setdefault(score, i)
        if score - 1 in seen:
            res = max(res, i - seen[score - 1])
    return res


# ===================================================

# [AUTHOR]: md_faisal
# [DESCRIPTION]: Detailed Explanation with example| O(N) time | one pass |

"""
approach: traverse linearly through the array, tracking total number of days with hours >8:
(say for instance a variable score=0 do the same)
and for each val>8 in hours score=score+1 else score -1

if socre >0 then ans=i+1 (simply means if take all elements uptil now then it would be a well-performing interval)
elsecache the score with its index,,,,, if score is not present in the cache:
Reason of doing so is simple ,for next time whenever we find score values to be score+1
then we can assert that all the day in between cache[score] and cache[score+1] constitue a well-performing interval and would update our ans if needed.
examples:

ans=0,score=0,cache={}

arr:    4,5,10,9,9,3,8
for i=0:
4<=8:
score=-1 ; cache{-1:0};  ans=0
for i=1:
5<=8:
score=-2 ; cache{-1:0,-2:1};  ans=0
for i=2:
10>8:
score=-1 ; cache{-1:0,-2:1};  ans=max(ans,i-cache[-2])=1
i=3:
9>8:
score=0 ; cache{-1:0,-2:1};  ans=max(ans,i-cache[-1])=3
for i=4:
9>8:
score=1 ; cache{-1:0,-2:1};  ans=i+1     (since score is +ve) =5
for i=5:
3<=8:
score=0 ; cache{-1:0,-2:1};  =max(ans,i-cache[-1])=5
8<=8:
for i=6
3<=8:
score=-1 ; cache{-1:0,-2:1};  =max(ans,i-cache[-2])=5


here goes the code for the same:

"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res=score=0
        cache={}
        for i,h in enumerate(hours):
            
            score=score+1 if h>8 else score-1
            if score>0:
                res=i+1
            else:
                if score not in cache:
                    cache[score]=i
                if score-1 in cache:
                    res=max(res,i-cache[score-1])
        return res

# ===================================================

# [AUTHOR]: jiah
# [DESCRIPTION]: O(N) Without Hashmap. Generalized Problem&Solution: Find Longest Subarray With Sum >= K.

"""

You may have noticed that almost all O(n) hashmap solution posts are based on the +1, -1 property. And these solutions try to find a longest subarrary with sum > 0.

Here I propose a more generalized problem and a solution to it.

Problem:

	1. input: arrary arr in which elements are arbitrary integers.
	2. output: length of a longest subarray arr[i, j) with sum(arr[i], ... , arr[j-1]) >= K.

Solution:

	1. Compute prefix sum of arr as prefixSum where prefixSum[i] = sum(arr[0], ... arr[i-1]) for i > 0 and prefixSum[0] = 0.
	2. Iterate through prefixSum from begin to end and build a strictly monotone decreasing stack smdStack. (smdStack.top() is the smallest)
	3. Iterate through prefixSum from end to begin. For each prefixSum[i], while smdStack.top() is less than prefixSum[i] by at least K, pop smdStackand try to update result by subarray [index of top,i). Until top element is not less than it by K.
	4. Return result.

Time complexity: O(n)

	1. step1, compute prefixSum O(n)
	2. step2, build strictly monotone decreasing stack O(n)
	3. step3, iterate prefixSum O(n). pop top elements in smdStack O(n)

Explanation:
For simplicity, call (i, j) a valid pair if the inequation prefixSum[j] - prefixSum[i] >= K holds. Our goal is to optimize j-i over all valid pair (i, j).

	1. Firstly, fix j and minimize i. Consider any i1 and i2 that i1 < i2 < j and prefixSum[i1] <= prefixSum[i2]. It is obvious that (i2, j) can't be a candidate of optimal subarray because (i1, j) is more promising to be valid and longer than (i2, j). Therefor candidates are monotone decreasing, and we can use a strictly monotonic descresing stack to find all candidates. (Monotone stack are just normal stack with a constraint that the elements in them are monotonically increasing or decreasing. When processing a new element, we either pop top elements then push new elem or discard this new element to guarantee the property of monotonicity. If you are not familiar with this data structure, you'd better solve some similar leetcode problems before this one).

	2.Secondly, fix i and maximize j. Consider any j1 and j2 that i < j1 < j2 and prefixSum[j2] - prefix[i] >= K. We can find that (i, j1) can't be a candidate of optimal subarrary because (i, j2) is better. This discovery tells us that we should iterate j from end to begin and if we find a valid (i, j), we don't need to keep i in smdStack any longer.

CPP solution for problem 1124 using monotone stack. (20ms, 11.2MB, faster than 100%)

Similar problems that can be solved by monotone increasing or decreasing stack/queue/list:

683. K Empty Slots
862. Shortest Subarray with Sum at Least K
962. Maximum Width Ramp


class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int len = hours.size();
        vector<int> prefixSum(len+1, 0);
        for (int i = 1; i <= len; ++i) {
            prefixSum[i] = prefixSum[i-1] + (hours[i-1] > 8 ? 1 : -1);
        }
        stack<int> smdStack;
        for (int i = 0; i <= len; ++i) {
            if (smdStack.empty() || prefixSum[smdStack.top()] > prefixSum[i]) {
				// Trick, store index than value.
                smdStack.push(i);
            }
        }
        int res = 0;
        for (int j = len; j >= 0; --j) {
		    // For generalized problem:
		    // while (!smdStack.empty() && prefixSum[smdStack.top()]+K <= prefixSum[j]) {
            
			// For this problem:
			while (!smdStack.empty() && prefixSum[smdStack.top()] < prefixSum[j]) {
                res = max(res, j - smdStack.top());
                smdStack.pop();
            }
        }
        return res;
    }
};

"""


# ===================================================

# [AUTHOR]: jryzkns
# [DESCRIPTION]: Trying to be the simplest O(n) explanation in Python

"""
Preamble / Initial setup
Given our input array, lets start with identifying which days are the tiring ones and which aren't. If it is tiring, then we will have it be +1. If it isn't tiring, then it's a -1:


>>> hours = [9,9,6,0,6,6,9] 
>>> tired = [1 if hour > 8 else -1 for hour in hours]
>>> tired
[1, 1, -1, -1, -1, -1, 1]

The idea in doing this is if you add all the numbers in a sub-array, you get a net tiredness value (we will call this ntv from here on forth):

>>> tired[1:5]
[1, -1, -1, -1]
>>> sum(tired[1:5])
-2


A well performing interval (WPI) in this setup now means an interval [a, b] such that the ntv of this interval is positive (sum(tired[a:b+1]) > 0). Ideally we want to get ntv = 1, meaning we have maximized our tired days, and took enough non-tiring days to balance it out.

A first stab to start the conversation (Brute Forcing)

The brute force solution would be to find every possible subinterval [a, b] and compute their sum, maximize the sum then get the length of the interval. However, the number of subintervals are in order of O(n^2) and each sum for that interval is O(n) for a total of O(n^3) time complexity. We can do much better than that. There are two optimizations that we can apply on top of this solution, and we will talk about these separately.

Optimization 1: Prefix Sum

A prefix sum is basically an "integral" of the array that you are working with. Every element in a prefix sum is a sum of itself and the sum of everything that came before it (prefix_sum_tired[i] = sum(tired[:i+1])). You can compute a prefix sum in a single passthrough in O(n) time.
The reason why using a prefix sum is desirable is that a prefix sum allows you to sum over an interval in O(1) time:

"""
# doesn't this look like the fundamental theorem of calculus II?
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus#Second_part
sum(tired[a:b+1]) == prefix_sum_tired[b] - prefix_sum_tired[a]

"""

Using this method, you would apply prefix sum on the input first, before checking every interval: O(n) + O(n^2) = O(n^2). We have went from O(n^3) down to O(n^2). We can still do better!

Optimization 2: Caching values in the Prefix Sum

Now that we have an understanding of the prefix sum, we can look at some properties that we can exploit. Suppose our prefix sum looks like this:

"""

prefix_sum_tired = [1,2,3,2,3,2,3,4]

"""
We know that prefix_sum_tired[7] - prefix_sum_tired[6] = 1. However, we also know that prefix_sum_tired[7] - prefix_sum_tired[4] = 1 and prefix_sum_tired[7] - prefix_sum_tired[2] = 1. This means that the ntv of [7,6], [7,4], and [7,2] are all the same. However, we definitely prefer [7,2] because that's the longest interval among the three. With the setup as is, we would need to scan backwards to find the earliest possible value of 3 in our prefix_sum, and that takes some work to do and scales O(n). This is where caching comes in.

We can cache the values in the prefix sum by setting up a map prefix_sum_first_preimage that maps ntv to the index of a day. Whenever we see an ntv for the first time, we want to add it to the map. If the ntv exists in the map already, then we don't touch it:

"""

prefix_sum_first_preimage = {}
# some other stuff that's not as relevant at the moment
if ntv not in prefix_sum_first_preimage:
	prefix_sum_first_preimage[ntv] = day_idx # suppose day_idx is the index of the current day in question

"""
When we have this set up, then we can have something that looks like this:
"""

day_idx = 6
ntv = 5
if ntv - 1 in prefix_sum_first_preimage:
	print(f"{day_idx - prefix_sum_first_preimage[ntv - 1]} is the longest WPI ending on {day_idx} with net 1")

"""
We can now find the longest WPI given an end day in O(1) time as well.

Piecing everything together

With all of the above knowledge, you probably noticed that we can construct the prefix sum on the fly and check for the longest WPI as we are going through the array instead of having to brute force everything. The final solution would look something like this:

"""

def longestWPI(hours):

    max_wpi, ntv, first_preimage = 0, 0, {}

    for day_idx, hrs_today in enumerate(hours):

        # check if today was a tiring day or not
        ntv += 1 if hrs_today > 8 else -1

        # if our net is positive (the net here is starting from first 
        # day), we just set the longest wpi to days that has passed
        if ntv > 0: max_wpi = day_idx + 1

        # if we haven't seen this ntv before, we store it
        if not ntv in first_preimage: first_preimage[ntv] = day_idx

        # if the ntv that is 1 less is seen before (for a net 1 ntv)
        # we compute the wpi from that and see if that's longer than
        # the longest we've seen so far
        if ntv - 1 in first_preimage:
            max_wpi = max(max_wpi, day_idx - first_preimage[ntv - 1])

    return max_wpi




# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        largest = max(hours)
        largestIdx = hours.index(largest)

        daysTiring = 0
        daysRegular = 0
        
        resTiring = []
        resRegular = []
        
        for i in range(largestIdx, len(hours)):
            
            print('tiring: ', resTiring)
            print('regular: ', resRegular)
            
            if hours[i] > 16:
                continue
                
            if i != 0 and len(resTiring) == len(resRegular):
                return len(resTiring) + len(resRegular) - 1
            
            if hours[i] > 8:
                resTiring.append(hours[i])
                daysTiring += 1
            
            else:
                resRegular.append(hours[i])
                daysRegular += 1

"""
[TESTCASES]
[6,6,6] - Didn't pass this test case

"""