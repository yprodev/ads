# [AUTHOR]: WangQiuc
# [DESCRIPTION]: Python Greedy -- Interval Scheduling

"""

A classic greedy case: interval scheduling problem.

The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.

Time complexity is O(NlogN) as sort overwhelms greedy search.

"""

def eraseOverlapIntervals(intervals):
	end, cnt = float('-inf'), 0
	for s, e in sorted(intervals, key=lambda x: x[1]):
		if s >= end: 
			end = e
		else: 
			cnt += 1
	return cnt

# ===================================================

# [AUTHOR]: ninjaVic
# [DESCRIPTION]: Python greedy solution with explanation

"""
Sort the intervals by their start time. If two intervals overlap, the interval with larger end time will be removed so as to have as little impact on subsequent intervals as possible.
"""

def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    if not intervals: return 0
    intervals.sort(key=lambda x: x.start)  # sort on start time
    currEnd, cnt = intervals[0].end, 0
    for x in intervals[1:]:
        if x.start < currEnd:  # find overlapping interval
            cnt += 1
            currEnd = min(currEnd, x.end)  # erase the one with larger end time
        else:
            currEnd = x.end   # update end time
    return cnt

# ===================================================

# [AUTHOR]: 
# [DESCRIPTION]: 

"""

Which interval would be the best first (leftmost) interval to keep? One that ends first, as it leaves the most room for the rest. So take one with smallest end, remove all the bad ones overlapping it, and repeat (taking the one with smallest end of the remaining ones). For the overlap test, just keep track of the current end, initialized with negative infinity.

Ruby
Take out intervals as described above, so what's left is the bad overlapping ones, so just return their number.


def erase_overlap_intervals(intervals)
  end_ = -1.0 / 0
  intervals.sort_by(&:end).reject { |i|
    end_ = i.end if i.start >= end_
  }.size
end

Alternatively, i.start >= end_ and end_ = i.end works, too.

Python

"""

def eraseOverlapIntervals(self, intervals):
    end = float('-inf')
    erased = 0
    for i in sorted(intervals, key=lambda i: i.end):
        if i.start >= end:
            end = i.end
        else:
            erased += 1
    return erased


# ===================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] O(n log n) sort ends with proof, explained

"""
How you can handle this problem if you see it first time? If number of segments is small, we can try to check all possible options. However in this problem number of segments can be quite big and it is not going to work. Next options are dp or greedy approaches, that we need to check, and let us try to use greedy approach. Let us try to build the longest set of non-overlapping intevals. There are different options how we can try to choose greedy strategy:

	1. The first one strategy, which is not going to work is to sort segments by its starts, but we have counterexample here: [1,100], [2,3], [3,4]: we will choose only first segment, however we can choose two of them.
	
	2. Another strategy is to sort segments by its ends? Why it is going to work? Let us prove it by mathematical induction: we have segments s_1, ... , s_n with sorted ends and we can choose k out of these n segments, such that they not overlap. We add s_{n+1} segment, such that its end is greater or equal than the end of s_n. How many segments we can choose out of our new n+1 segments? It can not be more that k+1, because we can choose at most k out of first n. Also, we can choose k+1 only in the case, when we take the last segment. When we can take the last segment? Only if it is not intersecting with segment number n! Because if it is intersection with some previous segment, it must intersect with segment number n: intersection of s_{n+1} with s_i means that start of s_{n+1} is more that end of s_i. and the bigger i, the bigger the end of s_i. So we always can use greedy strategy.

Complexity: time complexity is O(n log n), for sort all segments and space complexity is O(n) if we count that we use space for sorted intervals.

"""

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

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution


