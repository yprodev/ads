// [AUTHOR] DBabichev
// [DESCRIPTION] [Python] Math oneliner O(n), using Catalan number, explained
// [LINK] https://leetcode.com/problems/unique-binary-search-trees/discuss/703049/Python-Math-oneliner-O(n)-using-Catalan-number-explained

/*

In this problem we are asked to get number of trees and not necceseraly to return all trees, only number. Here we can use the idea of dynamic programming, let dp[n] be the number of unique Binary Search Trees with n nodes. How can we evaluate them: we need to choose number of nodes in the left subtree and number of nodes in the right subtree, for example n=5, then we have options:

	1. left subtree has 0 nodes, root = 1, and right subtree has 4 nodes, number of options f[0]*f[4]
	2. left subtree has 1 nodes, root = 2, and right subtree has 3 nodes, number of options f[1]*f[3]
	3. left subtree has 2 nodes, root = 3, and right subtree has 2 nodes, number of options f[2]*f[2]
	4. left subtree has 3 nodes, root = 4, and right subtree has 1 nodes, number of options f[3]*f[1]
	5. left subtree has 4 nodes, root = 5, and right subtree has 0 nodes, number of options f[4]*f[0]

So, in total f[5] = f[0]*f[4] + f[1]*f[3] + f[2]*f[2] + f[3]*f[1] + f[4]*f[0], and in general:
f[n] = f[0]*f[n-1] + f[1]*f[n-2] + ... + f[n-2]*f[1] + f[n-1]*f[0].

We can solve this in classical dynamic programming way with O(n^2) complexity. However we can recognize in this formula Catalan Numbers: https://en.wikipedia.org/wiki/Catalan_number and there is direct formula to evaluate them:
f[n] = (2n)!/(n! * n! * (n+1)).

Complexity: time complexity is O(n) to evaluate all factorials, space complexity is O(1).

class Solution:
    def numTrees(self, n):
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)

*/



// ==========================================================================

// [AUTHOR] OldCodingFarmer
// [DESCRIPTION] Python solutions (DP + Catalan number)
// [LINK] https://leetcode.com/problems/unique-binary-search-trees/discuss/31826/Python-solutions-(DP-%2B-Catalan-number)

/*

# DP
def numTrees1(self, n):
    res = [0] * (n+1)
    res[0] = 1
    for i in xrange(1, n+1):
        for j in xrange(i):
            res[i] += res[j] * res[i-1-j]
    return res[n]

# Catalan Number  (2n)!/((n+1)!*n!)  
def numTrees(self, n):
    return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))

*/

// ==========================================================================

// [AUTHOR] archit91
// [DESCRIPTION] [C++/Python] 5 Easy Solutions w/ Explanation | Optimization from Brute-Force to DP to Catalan O(N)
// [LINK] https://leetcode.com/problems/unique-binary-search-trees/discuss/1565543/C%2B%2BPython-5-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Catalan-O(N)


// BETTER TO SEE AUTHOR's SOLUTIONS



// ==========================================================================


// [AUTHOR] aysusayin
// [DESCRIPTION] [Python]Easy DP Solution Explained By Someone Who Used To Struggle To Understand DP
// [LINK] https://leetcode.com/problems/unique-binary-search-trees/discuss/703644/PythonEasy-DP-Solution-Explained-By-Someone-Who-Used-To-Struggle-To-Understand-DP



// ==========================================================================


// [AUTHOR] mad185
// [DESCRIPTION] [Javascript] SIMPLEST - Just math, no loops. Faster than 97%.
// [LINK] https://leetcode.com/problems/unique-binary-search-trees/discuss/276140/Javascript-SIMPLEST-Just-math-no-loops.-Faster-than-97.


/*
I've seen a lot of solutions that are very programmatic using for loops and such to do node traversal. But node combinations can be calculated with a simple Catalan number factorial equation: 2n!/(n+1)!n!
*/

var numTrees = function(n) {
    return factorial( 2 * n ) / ( factorial( n + 1 ) * factorial( n ) );
};

function factorial( num ){
    if( num <= 0 )
        return 1;
    else
        return num * factorial( num - 1 );
}


// ==========================================================================


// [AUTHOR] AminiCK
// [DESCRIPTION] JavaScript Solution DP w/ Explanation
// [LINK] https://leetcode.com/problems/unique-binary-search-trees/discuss/488024/JavaScript-Solution-DP-w-Explanation

/*

The idea
A few key facts we have to understand:

	1. The question is simply asking the sum of different combinations of BST if every number between 1 - n is used as a root node
	2. If number i is the root node, then the total combinations for i will equal to the combination of BST to its left [1... i-1] times the combination of BST to its right [i+1]...n.
	3. Think of BST are just combination of nodes instead of actual numbers, this means, the BST combinations for [1,2,3,4] equals to the BST combinations for [7,8,9,10] because they all have 4 elements.
	4. When we calculate the product of left & right, we are mix and match different combinations of BST. And we don't really care what are the actual numbers are, but instead, the length of the elements we are dealing with.

*/

var numTrees = function(n) {
    let G = new Array(n+1).fill(0);
    G[0] = 1;
    G[1] = 1;
    for (let i=2;i<=n;i++) {
        for (let j=1;j<=i;j++) {
            G[i]+=G[j-1] * G[i - j];
        }
    }
    return G[n];
};


// ==========================================================================