# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] Sort and traverse, explained

"""
Let us sort our intervals by its starts and then iterate them one by one: we can have two options:

The current ending point in our ans is less than beg of new interval:
    1. it means that we have a gap and we need to add new interval to our answer.
    2. In the opposite case our intervals are overlapping, so we need to update the end for last interval we created.

Complexity: time complexity is O(n log n) to sort intervals and space complexity is O(n) to keep sorted intervals and answer.
"""

class Solution:
    def merge(self, intervals):
        ans = []
        
        for beg, end in sorted(intervals):
            if not ans or ans[-1][1] < beg:
                ans += [[beg, end]]
            else:
                ans[-1][1] = max(ans[-1][1], end)

        return ans

# ===================================================

# [AUTHOR]: lchen77
# [DESCRIPTION]: C++ 10 line solution. easing understanding

"""
vector<Interval> merge(vector<Interval>& ins) {
    if (ins.empty()) return vector<Interval>{};
    vector<Interval> res;
    sort(ins.begin(), ins.end(), [](Interval a, Interval b){return a.start < b.start;});
    res.push_back(ins[0]);
    for (int i = 1; i < ins.size(); i++) {
        if (res.back().end < ins[i].start) res.push_back(ins[i]);
        else
            res.back().end = max(res.back().end, ins[i].end);
    }
    return res;
}
"""

# ===================================================

# [AUTHOR]: zhanweiting
# [DESCRIPTION]: [Python3] Sort O(Nlog(N))

"""
intervals [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort [[1, 3], [2, 6], [8, 10], [15, 18]]

interval = [1,3]
merged =[]
not merged:
	merged =[ [1,3] ]

interval =[2,6]
merged = [ [1,3] ]
merged[-1][-1] = 3 > interval[0] = 2:
	merged[-1][-1] = max(merged[-1][-1] = 3 ,interval[-1] = 6) =6
merged = [[1,6]]

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        merged =[]
        for i in intervals:
			# if the list of merged intervals is empty 
			# or if the current interval does not overlap with the previous,
			# simply append it.
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
			# otherwise, there is overlap,
			#so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged

"""
Time complexity:
In python, use sort method to a list costs O(nlogn), where n is the length of the list.
The for-loop used to merge intervals, costs O(n).
O(nlogn)+O(n) = O(nlogn)
So the total time complexity is O(nlogn).
Space complexity
The algorithm used a merged list and a variable i.
In the worst case, the merged list is equal to the length of the input intervals list. So the space complexity is O(n), where n is the length of the input list.

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if previous_end >= current_start: # overlap
                    merged[-1][1] = max(previous_end,current_end)
                else:
                    merged.append(intervals[i])
        return merged


# ===================================================

# [AUTHOR]: StefanPochmann
# [DESCRIPTION]: 7 lines, easy, Python

def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First NOT working solution


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newArr = list()
        itemsLength = len(intervals)

        if itemsLength <= 1:
            return intervals
        
        for curr in range(itemsLength):
            if curr + 1 < itemsLength:
                currPair = intervals[curr]
                nextPair = intervals[curr + 1]
                
        
                if currPair[1] >= nextPair[0]:
                    newArr.append([currPair[0], nextPair[1]])
                elif itemsLength == 2 and currPair[1] <= nextPair[0]:
                    return intervals
                else:
                    newArr.append(intervals[curr + 1])
                
        print(newArr)
        
        return newArr


# [AUTHOR] ME
# [DESCRIPTION] First working solution (used DBabichev's variant as an example)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        for beg, end in sorted(intervals):
            if not res or res[-1][1] < beg:
                res.append([beg, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res


#[RECAP]
# 1. Think in terms of cases
# 2. Find edge cases:
#   2.1 Only one interval
#   2.2 Two intervals with the gap
#   2.3 Two overlapping intervals
# 3. Find the "key factor"





# Test cases
# [[1,3],[2,6],[8,10],[15,18]]
# [[1,3]]
# [[1,4],[5,6]]
# [[1,4],[4,5]]
# [[1,4],[0,4]]