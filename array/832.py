

# ===================================================================================

# [AUTHOR]: dlima
# [DESCRIPTION]: Python Readable
# [QUESTIONS]
# 1. What is xrange?

for row in xrange(len(A)):
        A[row] = A[row][::-1] # reverse the row
        
        for invert in xrange(len(A[row])): # invert each element
            if A[row][invert] == 0:
                A[row][invert] = 1
            else:
                A[row][invert] = 0
                
    return A



# ===================================================================================

# [AUTHOR]: clfm
# [DESCRIPTION]: Python 3 - Clean & Correct
# [QUESTIONS]:
# 1. Why do we need to find middle? Is there some idea like merge sort?

class Solution:

    def flipAndInvertImage(self, A):
        """
        Time:  O(mn)  [m = len(A), n = len(A[0])]
        Space: O(1)
        """
        if not A or not A[0]:
            return None

        middle = (len(A[0]) + 1) // 2
        for row in A:
            for left in range(middle):
                right = len(row) - 1 - left
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
        return A

# ===================================================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] Oneliner, explained

"""
Let us do exactly what is asked in this problem: for each row: flip the image horizontally, then invert it. Quick way to get 0 from 1 and 1 from 0 is to use 1^q (however tests are so small, so difference is not very big).

Complexity: time complexity is O(mn), where m, n are sizes of image. Space complexity is also O(mn) if we count output and O(1) space if we do not count. Note, that if we allowed to modify original image, than we can have O(1) space.
"""

class Solution:
    def flipAndInvertImage(self, A):
        return [[1^q for q in row[::-1]] for row in A]


"""
[COMMENTS]

You can replace row[::-1] with reversed(row) to reduce the usage of memory and accelerate the program.

1^q will be the same with 1 - q .

"""



# ===================================================================================

# [AUTHOR]: fauzankadri
# [DESCRIPTION]: One-Liner JavaScript Solution
"""
var flipAndInvertImage = function(A) {
    // take each row, reverse it, then map each number in it and invert it. map returns a list
    return A.map(row => row.reverse().map(num => num^1));

};
"""

# ===================================================================================

# [AUTHOR]: kevinhynes
# [DESCRIPTION]: Python3 - Beats 99.78% with explanation

def flipAndInvertImage(self, A):
	for row in A:
		i, j = 0, len(row) - 1
		while i <= j:
			if row[i] == row[j]:
				row[i], row[j] = row[i]^1, row[j]^1
			i += 1
			j -= 1
	return A

"""
After reviewing some examples you will notice the following patterns:
1) Look at first and last value of row. If they are the same (1,1 or 0,0), they will be flipped in the output.
If they are different (1,0 or 0,1), they do not change. Work your way inward to the middle of the list
applying this rule.
2) If the row has an odd number of entries, the middle value always flips. For example if len(row) = 5,
then row[2] must change values.

Bitwise XOR --> 0^1 = 1, 1^1 =0

Let i be the index at the beginning of the row, and j be the index at the end of the row. If the the values at
these indices (row[i] and row[j]) are equal, flip their values using XOR ^. If they values are not equal, do
nothing and move i and j closer to the middle. When i == j , the code still executes as it should.

Edit:
If len(A) = num_words = M and len(A[0]) = word_length = N, we iterate over (word_length / 2) * num_words or (N/2) * M values. Time complexity is O((N/2) * M), but its still just linear with the input so we can generalize as O(N). Space complexity is O(1).


"""

# ===================================================================================

# [AUTHOR]: Nishil
# [DESCRIPTION]: Python 1 line

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return [[1-i for i in row[::-1]] for row in A]

# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [Java/C++/Python] Reverse and Toggle

"""
Explanation:
	1. reverse every row.
	2. toggle every value.

In Java, I did both steps together:
Compare the i th and n - i - 1 th in a row.
The "trick" is that if the values are not the same,
but you swap and flip, nothing will change.
So if they are same, we toggle both, otherwise we do nothing.


Complexity:
Time O(N^2)
Space O(N^2) for output

Java:

    public int[][] flipAndInvertImage(int[][] A) {
        int n = A.length;
        for (int[] row : A)
            for (int i = 0; i * 2 < n; i++)
                if (row[i] == row[n - i - 1])
                    row[i] = row[n - i - 1] ^= 1;
        return A;
    }

C++:
by @guybrush2323

    static const vector<vector<int>>& flipAndInvertImage(vector<vector<int>>& A) {
        for (auto& row : A) {
            reverse(row.begin(), row.end());
            for (auto& v : row) v ^= 1;
        }
        return A;
    }
"""

# 1-line Python:

    def flipAndInvertImage(self, A):
        return [[1 ^ i for i in reversed(row)] for row in A]

# ===================================================================================

# [AUTHOR]: 
# [DESCRIPTION]: 


# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	Mistakes where to put the variable with a new list
#	Mistake with understanding what is index and what is 
#	actual element in Python (for in loop with / without)
#	range() function call.

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            newRow = list()
            
            for row in reversed(image[i]):
                if row == 1:
                    newRow.append(0)
                else:
                    newRow.append(1)
                    
            image[i] = newRow
            
        return image

