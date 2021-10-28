# [AUTHOR]: Peregrin
# [DESCRIPTION]: Python one-pass, O(1) memory, simple code, beats 90%

class Solution:
    def sortArrayByParityII(self, a):
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(a)
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                a[i],a[j] = a[j],a[i]
                i += 2
                j += 2

        return a

# ===================================================

# [AUTHOR]: votrubac
# [DESCRIPTION]: C++ 5 lines, two pointers + 2-liner bonus

"""

Use two pointers to search for missplaced odd and even elements, and swap them.

vector<int> sortArrayByParityII(vector<int>& A) {
    for (int i = 0, j = 1; i < A.size(); i += 2, j += 2) {
        while (i < A.size() && A[i] % 2 == 0) i += 2;
        while (j < A.size() && A[j] % 2 == 1) j += 2;
        if (i < A.size()) swap(A[i], A[j]);
    }
    return A;
}

Now, some fun for for my minimalistic functional friends. It's techically a two-liner, though I split swap into 3 lines for readability :) It actually may even look a bit cleaner, as you do not have to do "plus 2".

vector<int> sortArrayByParityII(vector<int>& A) {
  for (int i = 0, j = 0; i < A.size() && j < A.size(); ) swap(
      *find_if(begin(A) + i, end(A), [&] (int v) { return (i++ % 2 == 0 && v % 2 != 0) || i == A.size(); }),
      *find_if(begin(A) + j, end(A), [&] (int v) { return (j++ % 2 != 0 && v % 2 == 0) || j == A.size(); }));
  return A;
}

"""

# ===================================================

# [AUTHOR]: haleyysz
# [DESCRIPTION]: [javascript] O(n)

"""

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParityII = function(A) {
    let result = new Array(A.length);
    
    for(let i = 0, even = 0, odd = 1; i < A.length; i ++) {
        if(A[i] % 2 === 0) {
            result[even] = A[i];
            even += 2;
        } else {
            result[odd] = A[i];
            odd += 2;
        }
    }
    return result;
};

"""

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] I created a shame :) 

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        leftPtr = 0
        rightPtr = len(nums) - 1
        
        while leftPtr < rightPtr:
            if self.canMove(nums, leftPtr):
                leftPtr += 1
        
            if self.canMove(nums, rightPtr):
                rightPtr -= 1
                
            if (self.isEven(nums[leftPtr]) and not self.isEven(rightPtr)) and (self.isEven(nums[rightPtr]) and not self.isEven(leftPtr)):
                self.swap(nums, leftPtr, rightPtr)

                leftPtr += 1
                rightPtr -= 1

            
        return nums
            
            
            
    def isEven(self, num):
        return num % 2 == 0
    
    def canMove(self, arr, ptr):
        return self.isEven(ptr) and self.isEven(arr[ptr])
    
    def swap(self, arr, ptr1, ptr2):
        print('> ', arr[ptr1], ptr1, '\n', '>', arr[ptr2], ptr2)

