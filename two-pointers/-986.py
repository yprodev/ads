# [AUTHOR]: votrubac
# [DESCRIPTION]: C++ O(n), "merge sort"

"""
Like in the "merge" phase of the merge sort, we use two pointers to combine sorted sequences. Nothing tricky here - just check all conditions carefully.

vector<Interval> intervalIntersection(vector<Interval>& A, vector<Interval>& B) {
  vector<Interval> res;
  for (auto i = 0, j = 0; i < A.size() && j < B.size(); ) {
    if (A[i].end < B[j].start) ++i;
    else if (B[j].end < A[i].start) ++j;
    else {
      res.push_back({ max(A[i].start, B[j].start), min(A[i].end, B[j].end) });
      if (A[i].end < B[j].end) ++i;
      else ++j;
    }
  }
  return res;
}

A slightly different version (with the updated method signature), inspired by MiloLu. Could be easier to understand for some folks.

vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
    vector<vector<int>> res;
    for (auto i = 0, j = 0; i < A.size() && j < B.size(); A[i][1] < B[j][1] ? ++i : ++j) {
        auto start = max(A[i][0], B[j][0]);
        auto end = min(A[i][1], B[j][1]);
        if (start <= end) 
            res.push_back({start, end});
    }
    return res;
}


"""

# ===================================================

# [AUTHOR]: arkaung
# [DESCRIPTION]: [Python] Two Pointer Approach + Thinking Process Diagrams

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        
        result = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            if a_start <= b_end and b_start <= a_end:                       # Criss-cross lock
                result.append([max(a_start, b_start), min(a_end, b_end)])   # Squeezing
                
            if a_end <= b_end:         # Exhausted this range in A
                i += 1               # Point to next range in A
            else:                      # Exhausted this range in B
                j += 1               # Point to next range in B
        return result


# ===================================================

# [AUTHOR]: localhostghost
# [DESCRIPTION]: [Python3] Really easy concept: Overlapping

"""
The solution is pretty simple. There is guaranteed to be an overlap interval if:

A[i].start <= B[j].end and B[j].start <= A[i].end

The above covers all cases for overlaps. Just think it as the right interval moving left.

[(4, 10), (7, 11)]
[(4, 10), (5, 9)]
[(4, 10), (-1, 3)]

"""

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i].start <= B[j].end and B[j].start <= A[i].end:
                res.append([max(A[i].start, B[j].start), min(A[i].end, B[j].end)])
            if A[i].end < B[j].end:
                i+=1
            else:
                j+=1
        return res 

"""
This is the latest version since Leetcode changed the method signature:
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B)
        i = j = 0
        res = []

        while i < m and j < n:
            if A[i][-1] >= B[j][0] and A[i][0] <= B[j][-1]:
                res.append([max(A[i][0], B[j][0]), min(A[i][-1], B[j][-1])])
            if A[i][-1] < B[j][-1]:
                i += 1
            else:
                j += 1

        return res

"""
Note: Got this in one of Uber's interview almost a year ago. The funny thing is, the interviewer wanted me to go with this approach which I think he was basing off of my solution. It was pretty hilarious.
"""



# ===================================================

# [AUTHOR]: AminiCK
# [DESCRIPTION]: JavaScript Solution


"""

The idea
Between two intervals, get the latest start time as maxStart and the earliest end time as minEnd. If maxStart <= minEnd, this means there is an overlap.

/**
 * @param {number[][]} A
 * @param {number[][]} B
 * @return {number[][]}
 */
var intervalIntersection = function(A, B) {
    let Ai = 0, Bi = 0;
    let res = [];
    
    while (Ai < A.length && Bi < B.length) {
        let maxStart = Math.max(A[Ai][0], B[Bi][0]);
        let minEnd = Math.min(A[Ai][1], B[Bi][1]);
        
        if (maxStart <= minEnd) res.push([maxStart, minEnd]) // overlap found
        
        if (A[Ai][1] < B[Bi][1]) Ai++;
        else Bi++;
    }
    
    return res;
};


"""

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First NOT working solution


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        edges = (0, None)
        
        # Mistake #2: Length of the lists provided could
        # different. The solution was done for the same
        # length of both arrays. Dead End! Start
        # doing some research.
        
        # Mistake #1: Check edge case with an empty array
        if not firstList or not secondList:
            return []

        # Confusion #1: Outer edges memorization for checking
        # in the current iteration.
        for idx in range(len(firstList)):
            firstStart, firstEnd = firstList[idx]
            secondStart, secondEnd = secondList[idx]
            
            if firstStart == edges[1]:
                res.append([firstStart, edges[1]])
                
            if edges[0] == secondStart:
                res.append([edges[0], secondStart])
            
            res.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])
            
            edges = (firstEnd, secondEnd)


        return res

