# [AUTHOR]: Olsh
# [DESCRIPTION]: THE EASIEST but UNUSUAL snowball JAVA solution BEATS 100% (O(n)) + clear explanation

# READ: https://leetcode.com/problems/move-zeroes/discuss/172432/THE-EASIEST-but-UNUSUAL-snowball-JAVA-solution-BEATS-100-(O(n))-%2B-clear-explanation

"""

class Solution {
     public void moveZeroes(int[] nums) {
        int snowBallSize = 0; 
        for (int i=0;i<nums.length;i++){
	        if (nums[i]==0){
                snowBallSize++; 
            }
            else if (snowBallSize > 0) {
	            int t = nums[i];
	            nums[i]=0;
	            nums[i-snowBallSize]=t;
            }
        }
    }
}

"""



# ===================================================

# [AUTHOR]: dxmpu
# [DESCRIPTION]: Simple Python Solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        count = 0
        for i in range(len(nums)):
                if nums[i] != 0:
                    nums[count], nums[i] = nums[i], nums[count]
                    count += 1

# ===================================================

# [AUTHOR]: Raj25226
# [DESCRIPTION]: C-simplest

"""
int n=0;
for(int i=0;i<numsSize;i++)
{
    if(nums[i]!=0){ 
        nums[n]=nums[i];
        n++;
    }
}

"""

# ===================================================

# [AUTHOR]: pvivek4
# [DESCRIPTION]: Easily readable fastest solution

"""

var moveZeroes = function(nums) {
    let count = 0;
for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
        let temp = nums[count];
        nums[count] = nums[i];
        nums[i] = temp;
        count++;
    }
}
return nums   
};
"""

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

