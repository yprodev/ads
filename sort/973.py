# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3]  6/1 liner using PriorityQueue/heapq

"""
Put the points into a PriorityQueue, and the order is by their distance to origin descendingly;
Whenever the size reaches K + 1, poll the farthest point out.

Analysis:

Time: O(nlogK), space: O(K).

public int[][] kClosest(int[][] points, int K) {
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> -a[0] * a[0] - a[1] * a[1]));
    for (int[] p : points) { 
        pq.offer(p); 
        if (pq.size() > K) { pq.poll(); } // poll out the farthest among the K + 1 points.
    }
    // int[][] ans = new int[K][2];
    // while (K-- > 0) { ans[K] = pq.poll(); }
    // return ans; // the above 3 lines can be replaced by the following line.
    return pq.toArray(new int[K][2]); // credit to @roolerzz, who make the code neat.
}


Analysis:

Time: O(nlogK), space: O(n).
"""

def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    return heapq.nsmallest(K, points, lambda p: p[0] * p[0] + p[1] * p[1])

# ===================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Java/C++/Python] O(N)


"""
Java:
Sort all points and return K first, O(NlogN)

public int[][] kClosest(int[][] points, int K) {
    Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));
    return Arrays.copyOfRange(points, 0, K);
}

C++
O(N) quick select

vector<vector<int>> kClosest(vector<vector<int>>& A, int K) {
    nth_element(A.begin(), A.begin() + K, A.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
    });
    return vector<vector<int>>(A.begin(), A.begin() + K);
}

"""



"""
Python:
Sort using heap of size K, O(NlogK)

"""
def kClosest(self, points, K):
    return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)

# ===================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] Easy, heap O(n log k) solution, explained

"""

When you see in the statement of the problem that you need you find k biggest or k smallest elements, you should immediately think about heaps or sort. Here we need to find the k smallest elements, and hence we need to keep max heap. Why max and not min? We always keep in the root of our heap the k-th smallest element. Let us go through example: points = [[1,2],[2,3],[0,1]], [3,4], k = 2.

	1. First we put points [1,2] and [2,3] into our heap. In the root of the heap we have maximum element [2,3]
	2. Now, we see new element [0,1], what should we do? We compare it with the root, see, that it is smaller than root, so we need to remove it from our heap and put new element instead, now we have elements [1,2] and [0,1] in our heap, root is [1,2]
	3. Next element is [3,4] and it is greater than our root, it means we do not need to do anything.

Complexity:
We process elements one by one, there are n of them and push it into heap and pop root from our heap, both have O(log k) complexity, so finally we have O(n log k) complexity, which is faster than O(n log n) algorighm using sorting.

Code:
First, we create heap (which is by definition min heap in python, so we use negative distances). Then we visit all the rest elements one by one and update our heap if needed.

"""

class Solution:
    def kClosest(self, points, K):
        heap = [[-i*i-j*j, i, j] for i,j in points[:K]]
        rest_elem = [[-i*i-j*j, i, j] for i,j in points[K:]]
        heapq.heapify(heap)
        for s, x, y in rest_elem:
            if s > heap[0][0]:
                heapq.heappush(heap, [s,x,y])
                heapq.heappop(heap)

        return [[x,y] for s,x,y in heap]


# ===================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] oneliner using sort

"""
Even though this algorighm has not optimal algorithmic complexity (it is O(n log n) vs heaps O(n log k), on leetcode it can work faster. Just sort points by distances and choose the smallest K of them
"""

class Solution:
    def kClosest(self, points, K):
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]


# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

class Solution:
    def findEuclidDistance(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        originPoint = [0, 0]
        arr = []
        res = []
        
        
        for pointIdx in range(len(points)):
            arr.append((pointIdx, self.findEuclidDistance(
                originPoint[0],
                points[pointIdx][0],

                originPoint[1],
                points[pointIdx][1]
            )))
        
        newArr = sorted(arr, key=lambda item: item[1])
        
        if k <= 0:
            return
        
        
        for kth in range(k):
            res.append(points[newArr[kth][0]])

        return res
