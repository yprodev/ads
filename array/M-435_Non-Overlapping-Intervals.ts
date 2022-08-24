// [AUTHOR] algorithm_cat
// [DESCRIPTION] Python sorting O(nlogn) solution w/ explanation, beats 94%
// [LINK] https://leetcode.com/problems/non-overlapping-intervals/discuss/792805/Python-sorting-O(nlogn)-solution-w-explanation-beats-94

/*

Thought process:
This problem asks us to find the minimum # of intervals to remove to maintain zero overlap, in other words, we want to find the maximum # of intervals to keep while having no overlap.

So how do we check overlaps? We could compare every pair of intervals, but that alone would be O(n^2); so is it really necessary to check every pair of intervals? And we realize that if the array was sorted, the problem is simplified a lot because the potential overlapping intervals would be adjacent to one another.

For example consider the sorted array:
[[1,2],[1,3],[2,3],[3,4]]
Start from the beginning,

    1. [[1,2], [1,3]]-> it's obvious these two overlap; would there be any reason to keep [1,3] instead of [1,2]? No. Because it will only decrease the number of intervals we can fit without causing overlaps. So we keep [1,2], aka the interval with the smaller ending.
    2. [[1,2], [2,3]]-> No overlap here, we can keep both. now the "most recent interval" is [2,3]
    3. [[2,3],[3,4]] -> No overlap here, we can keep both. now the "most recent interval" is [3,4]
    4. We can fit 3 intervals without overlap, so we return len(s)-3=4-3=1

Generalized algorithm:

sort the array and keep track of the last interval's ending point as end
if end > next interval's beginning, keep the interval that ends earlier
if end <= next interval's beginning or we reach the end, increment the interval count

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        lastIntervalEnd = intervals[0][0] #edit: removed -1 per @jca88's comment
        maxNonoverlapIntervals = 0
        for interval in intervals:
            if lastIntervalEnd > interval[0]:
                lastIntervalEnd = min(lastIntervalEnd, interval[1])
            else:
                maxNonoverlapIntervals += 1
                lastIntervalEnd = interval[1]        
        return len(intervals) - maxNonoverlapIntervals

*/


// ==========================================================================

// [AUTHOR] execute_order66
// [DESCRIPTION] [Python] Greedy
// [LINK] https://leetcode.com/problems/non-overlapping-intervals/discuss/2014306/Python-Greedy

/*

Credits to neetcode for the excellent explanation here: https://www.youtube.com/watch?v=nONCGxWoUfM

Intuition:

What's the most straightforward way we can think of to minimize the number of removals of overlapping intervals? By removing the overlapping interval with the longer end.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        last_end = intervals[0][1]
        remove = 0
        
        for i in range(1, len(intervals)):
            # found overlap
            if intervals[i][0] < last_end:
                remove += 1
                # remove the interval with the longer end
                last_end = min(intervals[i][1], last_end)
            else:
                last_end = intervals[i][1]
            
        return remove

*/


// ==========================================================================

// [AUTHOR] control_the_narrative
// [DESCRIPTION] JavaScript Clean 5-Liner, Greedy Approach
// [LINK] https://leetcode.com/problems/non-overlapping-intervals/discuss/736509/JavaScript-Clean-5-Liner-Greedy-Approach

/*

Time Complexity: O(N LogN);
Space Complexity: O(1);

*/

var eraseOverlapIntervals = function(intervals) {
    // sort by earliest finish time
    intervals.sort((a, b) => a[1] - b[1]);
    let prev = intervals[0], remove = 0;
    
    for(let i = 1; i < intervals.length; i++) {
        if(intervals[i][0] < prev[1]) remove++;
        else prev = intervals[i];
    }
    return remove;
};

// ==========================================================================

// [AUTHOR] StefanPochmann
// [DESCRIPTION] Short Ruby and Python
// [LINK] https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python

/*

Which interval would be the best first (leftmost) interval to keep? One that ends first, as it leaves the most room for the rest. So take one with smallest end, remove all the bad ones overlapping it, and repeat (taking the one with smallest end of the remaining ones). For the overlap test, just keep track of the current end, initialized with negative infinity.

def eraseOverlapIntervals(self, intervals):
    end = float('-inf')
    erased = 0
    for i in sorted(intervals, key=lambda i: i.end):
        if i.start >= end:
            end = i.end
        else:
            erased += 1
    return erased

*/

// ==========================================================================

// [AUTHOR] DBabichev
// [DESCRIPTION] [Python] O(n log n) sort ends with proof, explained
// [LINK] https://leetcode.com/problems/non-overlapping-intervals/discuss/793070/Python-O(n-log-n)-sort-ends-with-proof-explained

/*

How you can handle this problem if you see it first time? If number of segments is small, we can try to check all possible options. However in this problem number of segments can be quite big and it is not going to work. Next options are dp or greedy approaches, that we need to check, and let us try to use greedy approach. Let us try to build the longest set of non-overlapping intevals. There are different options how we can try to choose greedy strategy:

    1. The first one strategy, which is not going to work is to sort segments by its starts, but we have counterexample here: [1,100], [2,3], [3,4]: we will choose only first segment, however we can choose two of them.
    2. Another strategy is to sort segments by its ends? Why it is going to work? Let us prove it by mathematical induction: we have segments s_1, ... , s_n with sorted ends and we can choose k out of these n segments, such that they not overlap. We add s_{n+1} segment, such that its end is greater or equal than the end of s_n. How many segments we can choose out of our new n+1 segments? It can not be more that k+1, because we can choose at most k out of first n. Also, we can choose k+1 only in the case, when we take the last segment. When we can take the last segment? Only if it is not intersecting with segment number n! Because if it is intersection with some previous segment, it must intersect with segment number n: intersection of s_{n+1} with s_i means that start of s_{n+1} is more that end of s_i. and the bigger i, the bigger the end of s_i. So we always can use greedy strategy.

Complexity: time complexity is O(n log n), for sort all segments and space complexity is O(n) if we count that we use space for sorted intervals.

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]
        
        for i in range(n):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]
                
        return n - count   

*/


