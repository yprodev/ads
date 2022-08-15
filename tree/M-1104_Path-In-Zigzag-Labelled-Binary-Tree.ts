// [AUTHOR] votrubac
// [DESCRIPTION] Invert Labels
// [LINK] https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323293/Invert-Labels

/*

Intuition
If the tree is numbered left-to-right (not zigzag), the parent's label can be always determined as label / 2. For zigzag, we need to "invert" the parent label.

Simplified Solution
The idea is the same as for the original solution below, but I hope this one is a bit easier to understand. We first build the path from label to the root (by dividing the label by two).

Then, we go thougth the path, and invert odd labels.

C++

vector<int> pathInZigZagTree(int label) {
    vector<int> res;
    for (; label > 0; label /= 2)
        res.push_back(label);
    for (int i = res.size() - 1; i >= 0; --i)
        if (i % 2 == 1)
            res[i] = (1 << (res.size() - i - 1)) * 3 - res[i] - 1;
    return vector<int>(rbegin(res), rend(res));
}


Original Solution
Determine the tree level where our value is located. The maximum label in the level is 1 << level - 1, and minimum is 1 << (level - 1). We will use this fact to "invert" the parent label.

C++

vector<int> pathInZigZagTree(int label, int level = 0) {
  while (1 << level <= label) ++level;
  vector<int> res(level);
  for(; label >= 1; label /= 2, --level) {
    res[level - 1] = label;
    label = (1 << level) - 1 - label + (1 << (level - 1));
  }
  return res;
}


Complexity Analysis
Runtime: O(log n)
Memory: O(1) or O(log n) if we consider the memory required for the result.

*/


// ==========================================================================


// [AUTHOR] laser
// [DESCRIPTION] Python O(logn) time, and space with readable code, and step by step explanation
// [LINK] https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-O(logn)-time-and-space-with-readable-code-and-step-by-step-explanation


/*


Step by Step Explanation
With the thought in mind that in an ordered binary tree that goes from 1 to n:

Normally Ordered Binary Tree:
             1
           /   \
         2       3
       /  \     /  \
     4     5   6     7
   / |    /|   |\    | \
 8   9  10 11 12 13  14  15

Thought 1) You can easily determine the parent by dividing by 2 with a normally ordered (non-zigzag) binary tree
For example the parent of 9 can be calculated via int(9/2) which is 4

Thought 2) So we now how how to trace from the input label to the root node. So lets start with label In our example, we will use 14. To determine the parent of 14, notice that in the same spot in a normally ordered binary tree that it is 9. So you just need to calculate how to get from 14 to 9.

Zig Zag Binary Tree:
             1
           /   \
         3       2  <- 3+2-3 = 2/2 = 1
       /  \     /  \
     4     5   6     7   <- 7+4-4 = 7/2 = 3
   / |    /|   |\    | \
 15 14  13 12 11 10  9  8   <- 15+8-14 = 9/2 = 4
inversion formula: (max number of current level + min number of current level) - current number
For example to find the inversion of 14: 15 + 8 - 14 = 9
From here you just divide 9 by 2 to find the parent 4

Thought 3) You have to run the inversion formula at every level because at every level the row is inverted relative to the previous row

Time Complexity:
O(3 log n). 3 are needed as commented in the code.

Space Complexity:
If including the space required for the return res object counts as space then we need
O(log n) because we need to store the path from the root to the label.

class Solution:
    def pathInZigZagTree(self, label):
        res = [] # O(log n) space
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count*2: # O(log n) time
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0: # O(log n) time
            res.append(label)
            level_max = 2**(level) - 1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label)/2)
            level -= 1
        return res[::-1] # O(n) time

*/


// ==========================================================================


// [AUTHOR] _Dexter
// [DESCRIPTION] easy to understand (faser than 100%) 11 lines
// [LINK] https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/556569/easy-to-understand-(faser-than-100)-11-lines

/*

 vector<int> pathInZigZagTree(int label) {
    int level = log(label) / log(2) + 1;  
    vector<int> path(level);
    while (label) {
        path[level - 1] = label;
        label = pow(2, level) - 1 - label + pow(2, level - 1);
        label >>= 1;
        level--;
    }
    return path;
 }

*/


// ==========================================================================


// [AUTHOR] jelouta
// [DESCRIPTION] [Python] O(log n) level-wise parent calculation
// [LINK] https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/608949/Python-O(log-n)-level-wise-parent-calculation

/*


Intuition
A starting point to solve this problem is to think of the much simpler case. when the labelling is always done from left-to-right.
In that case, you may get the solution by simply dividing the current label by 2 until you reach the top (1).
However, we must make sure we divide the correct number by finding its symmetry in the level, hence, avoiding the fact that the labelling direction keeps switiching up.

Procedure
We first determine the level of the label.
We init the solutions list as a deque to prepend elements in O(1)
We iterate starting from the label's level up to the first level (0).
We append the current label to the deque.
We get the label of the previous level in one operation, it uses:
last_element: the last element in the current level: 2**l - 1
first_element: the first element in the current level: 2**(l-1)
The update operation is: (last_element + first_element - label) // 2
Time: O(log n), Space: O(1)
from math import log
from collections import deque

class Solution:
    def pathInZigZagTree(self, label):
        level = int(log(label, 2))
        solution = deque()
        for l in range(level, -1, -1):
            solution.appendleft(label)
            label = (3*(2**l) - 1 - label) // 2
        return solution

*/




// ==========================================================================


// [AUTHOR] 
// [DESCRIPTION] 
// [LINK] 



// ==========================================================================
