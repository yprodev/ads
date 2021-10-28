// [AUTHOR]: uzzwal
// [DESCRIPTION]: One Pass - Two Pointer Solution

/*

Consider two pointers, one oddIx, pointing to odd position and the other evenIx, pointing to even position.
Begining with oddIx at 1 and evenIx at 0, we will increment these until one exceeds the length of the array.
If we have odd number at even position or even number at odd position, we will like to change this, so we will swap only when both, oddIx and evenIx, holds number of opposite category(even/odd).
Else, we would simply skip the position for oddIx and evenIx if they hold number belonging to their category.


class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int oddIx = 1, evenIx = 0;
        while(oddIx < nums.length && evenIx < nums.length){
            if (nums[oddIx] % 2 < nums[evenIx] % 2){
                int temp = nums[oddIx];
                nums[oddIx] = nums[evenIx];
                nums[evenIx] = temp;
            }
            if (nums[oddIx] % 2 == 1)
                oddIx = oddIx + 2;
            if (nums[evenIx] % 2 == 0)
                evenIx = evenIx + 2;
        }
        return nums;
    }
}

*/





// ===================================================

// [AUTHOR]: Saura_v
// [DESCRIPTION]: Python 2 pointer solution

/*

# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx = 0
        odd_idx = len(nums)-1
        n = len(nums)
        
        while even_idx < n and odd_idx > 0:
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            
            elif nums[odd_idx] % 2 != 0:
                odd_idx -= 2
                
            else:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                even_idx += 2
                odd_idx -= 2
                
        return nums

*/

// ===================================================

// [AUTHOR]: Edgar__Li
// [DESCRIPTION]: 3 lines JavaScript solution.

let evenArray = A.filter(x => x % 2 === 0);
let oddArray = A.filter(x => x % 2 === 1);
return A.map((x, index) => index % 2 === 0 ? evenArray.pop() : oddArray.pop());


// ===================================================

// [AUTHOR]: jamiehsmith
// [DESCRIPTION]: Javascript - Simple using filter

var sortArrayByParityII = function(A) {
    let evenNums = A.filter((i) => i % 2 === 0);
    let oddNums = A.filter((i) => i % 2 !== 0);
    
    let res = [];
    for (let i = 0; i < A.length / 2; i++) {
        res.push(evenNums[i], oddNums[i]);
    }
    
    return res;
};



// ===================================================


// [AUTHOR] ME
// [DESCRIPTION] The solutions was inspired by uzzwal example
var sortArrayByParityII = function(nums) {
  let oddIdx = 1,
      evenIdx = 0,
      n = nums.length;
  
    
  while (oddIdx < n && evenIdx < n) {
    if (nums[oddIdx] % 2 < nums[evenIdx] % 2) {
      [nums[oddIdx], nums[evenIdx]] = [nums[evenIdx], nums[oddIdx]];
    }
    
    if (isOdd(nums[oddIdx])) {
      oddIdx += 2;
    }
    
    if (isEven(nums[evenIdx])) {
      evenIdx += 2;
    }
  }
    

  
  return nums;
    
};

function isEven(num) {
  return num % 2 === 0;
};

function isOdd(num) {
  return num % 2 !== 0;
};

