// [AUTHOR] hi-malik
// [DESCRIPTION] [Java/C++] Easiest Explanations
// [LINK] https://leetcode.com/problems/container-with-most-water/discuss/1915172/JavaC%2B%2B-Easiest-Explanations

/*

Java

class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max = 0;
        while(left < right){
            int w = right - left;
            int h = Math.min(height[left], height[right]);
            int area = h * w;
            max = Math.max(max, area);
            if(height[left] < height[right]) left++;
            else if(height[left] > height[right]) right--;
            else {
                left++;
                right--;
            }
        }
        return max;
    }
}


C++

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxi = 0;
        while(left < right){
            int w = right - left;
            int h = min(height[left], height[right]);
            int area = h * w;
            maxi = max(maxi, area);
            if(height[left] < height[right]) left++;
            else if(height[left] > height[right]) right--;
            else {
                left++;
                right--;
            }
        }
        return maxi;
    }
};

*/

// ==========================================================================


// [AUTHOR] StefanPochmann
// [DESCRIPTION] Simple and fast C++/C with explanation
// [LINK] https://leetcode.com/problems/container-with-most-water/discuss/6090/Simple-and-fast-C%2B%2BC-with-explanation    

/*

C++

int maxArea(vector<int>& height) {
    int water = 0;
    int i = 0, j = height.size() - 1;
    while (i < j) {
        int h = min(height[i], height[j]);
        water = max(water, (j - i) * h);
        while (height[i] <= h && i < j) i++;
        while (height[j] <= h && i < j) j--;
    }
    return water;
}

C

A bit shorter and perhaps faster because I can use raw int pointers, but a bit longer because I don't have min and max.

int maxArea(int* heights, int n) {
    int water = 0, *i = heights, *j = i + n - 1;
    while (i < j) {
        int h = *i < *j ? *i : *j;
        int w = (j - i) * h;
        if (w > water) water = w;
        while (*i <= h && i < j) i++;
        while (*j <= h && i < j) j--;
    }
    return water;
}

*/



// ==========================================================================

// [AUTHOR] StefanPochmann
// [DESCRIPTION] Simple and clear proof/explanation
// [LINK] https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation


/*

I've seen some "proofs" for the common O(n) solution, but I found them very confusing and lacking. Some even didn't explain anything but just used lots of variables and equations and were like "Tada! See?". I think mine makes more sense:

Idea / Proof:

    1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
    2. All other containers are less wide and thus would need a higher water level in order to hold more water.
    3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

Implementation: (Python)

class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water


Further explanation:

Variables i and j define the container under consideration. We initialize them to first and last line, meaning the widest container. Variable water will keep track of the highest amount of water we managed so far. We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. Multiply them to get how much water this container can hold, and update water accordingly. Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.

*.


// ==========================================================================

// My NOT working solution very first implementation
// We need also to take into consideration the 
// difference between indecies. Stopped, because was
// out of time.
function maxArea(height: number[]): number {
  let leftIdx = 0,
      rightIdx = height.length - 1,
      maxVolume = Number.NEGATIVE_INFINITY,
      currVolume = 0;
  
  while (leftIdx < rightIdx) {    
    let currentMinHeight = Math.min(height[leftIdx], height[rightIdx])
    let volumeBucket = currentMinHeight * currentMinHeight
    
    console.log(height[leftIdx], height[rightIdx], volumeBucket, maxVolume)
    
    if (maxVolume < volumeBucket) {
      maxVolume = volumeBucket
    }
    
    if (height[leftIdx] < height[rightIdx]) {
      leftIdx++;
    } else {
      rightIdx--;
    }

  }
  
  return maxVolume;

};