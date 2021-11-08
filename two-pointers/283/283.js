// [AUTHOR]: VicV13
// [DESCRIPTION]: Simple Python Solution

/*

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

*/

// ===================================================

// [AUTHOR]: kishorK1
// [DESCRIPTION]: Simplest two pointer C++ solution in O(n) time

/*

Here is the easiest way to understanding and writing the code

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int len = nums.size(), left=0, right=0;
        while(right<len){
            if (nums[right]==0){
                right++;
            }
            else {
                swap(nums[left++],nums[right++]);
            }
        }
    }
};

*/


// ===================================================

// [AUTHOR]: guyariely
// [DESCRIPTION]: javascript solution 96.99%

const moveZeroes = nums => {
  let i = 0,  j = 0;
  while (i < nums.length) {
    if (nums[i] != 0) {
      let temp = nums[i];
      nums[i] = 0;
      nums[j] = temp;
      j++;
    }
    i++;
  }
  return;
};

// ===================================================

// [AUTHOR]: ehdwn1212
// [DESCRIPTION]: JavaScript Solution


var moveZeroes = function(nums) {
    let emptyIndex = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            swap(nums, i, emptyIndex++);
        }
    }
};

var swap = function(arr, i, j) {
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}


// ===================================================

// [AUTHOR]: Me (inspired by VicV13 solution on Python)
// [DESCRIPTION]: Python 2 pointer solution
var moveZeroes = function(nums) {
    let i = 0;
    
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] !== 0) {
            [nums[i], nums[j]] = [nums[j], nums[i]];
            i++;
        }
    }
};

