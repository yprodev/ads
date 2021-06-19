# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] O(n) solution, explained

"""

I am not sure, why this problem is marked as hard, because we do not use any smart ideas to solve it: just do what is asked: traverse our intervals and merge them. Let us consider the case: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] and go through our code:

	1. Interval [1,2] is before [4,8], that is y < I[0], so we just add it to our res.
	2. Interval [3,5] is not before [4,8] but not after also, so it is the third case and we need to update I: I = [3,8] now.
	3. Interval [6,7]: the same logic, update I = [3,8] now (it did not change though)
	4. Interval [8,10]: still condition number 3, so I = [3,10] now.
	5. Interval [12,16]: it is after our I, so this is condition number 2 and we break from our loop: i = 3 now.
	6. Outside loop we combine res = [1,2], I = [3,10] and intervals[4:] = [12,16].

Why we use i -= 1 inside our loop, before break? It can happen, that we did not visit this part and it means, that our suffix intervals[i+1:] should be empty.

Complexity: time complexity is O(n), space complexity is O(n) as well and additional space complexity (if we do not count our output) is O(1).

Note: that intstead of traversing our intervals with linear search, we can use binary search, however it will not reduce the overall complexity of algorithm, our result will have in average O(n) elements.

"""
class Solution:
    def insert(self, intervals, I):
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
                break
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
                
        return res + [I] + intervals[i+1:]


# ===================================================

# [AUTHOR]: StefanPochmann
# [DESCRIPTION]: 7+ lines, 3 easy solutions

# Solution 1: (7 lines, 88 ms)
# Collect the intervals strictly left or right of the new interval, then merge the new one with the middle ones (if any) before inserting it between left and right ones.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]
    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)
    return left + [Interval(s, e)] + right


# Solution 2: (8 lines, 84 ms)
# Same algorithm as solution 1, but different implementation with only one pass and explicitly collecting the to-be-merged intervals.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    parts = merge, left, right = [], [], []
    for i in intervals:
        parts[(i.end < s) - (i.start > e)].append(i)
    if merge:
        s = min(s, merge[0].start)
        e = max(e, merge[-1].end)
    return left + [Interval(s, e)] + right


# Solution 3: (11 lines, 80 ms)
# Same again, but collect and merge while going over the intervals once.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right



# ===================================================

# [AUTHOR]: DebbieAlter
# [DESCRIPTION]: Python Super Short, Simple & Clean Solution 99% faster

"""

the main idea is that when iterating over the intervals there are three cases:

the new interval is in the range of the other interval
the new interval's range is before the other
the new interval is after the range of other interval

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
			# the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval); 
        return result


# ===================================================

# [AUTHOR]: OldCodingFarmer
# [DESCRIPTION]: Python O(n) and O(nlgn) solutions.

# O(nlgn) time, the same as Merge Intervals 
# https://leetcode.com/problems/merge-intervals/
def insert1(self, intervals, newInterval):
    intervals.append(newInterval)
    res = []
    for i in sorted(intervals, key=lambda x:x.start):
        if res and res[-1].end >= i.start:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res
    
# O(n) time, not in-place, make use of the 
# property that the intervals were initially sorted 
# according to their start times
def insert(self, intervals, newInterval):
    res, n = [], newInterval
    for index, i in enumerate(intervals):
        if i.end < n.start:
            res.append(i)
        elif n.end < i.start:
            res.append(n)
            return res+intervals[index:]  # can return earlier
        else:  # overlap case
            n.start = min(n.start, i.start)
            n.end = max(n.end, i.end)
    res.append(n)
    return res

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

