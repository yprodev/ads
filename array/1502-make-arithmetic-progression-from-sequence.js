// [AUTHOR] sambarannnn
// [DESCRIPTION] Intuitive Explained Solutions | O(N) & O(NLOGN) Codes

/*

C++

class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        //O(N) TIME BUT O(N) SPACE TOO!
        // an = a + (n-1) d
        //thus, d = (an - a) / (n - 1)
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int n = arr.length;
        
        HashSet<Integer> set = new HashSet<Integer>();
        
        for(int num : arr) {
            min = Math.min(num, min);
            max = Math.max(num, max);
            set.add(num);
        }
        int d = (max - min) / (n - 1);
        
        int curr = max;
        while(curr > min) {
            if(!set.contains(curr-d)) {
                return false;
            }
            curr = curr - d;
        }
        return true;
        //O(NLOGN) TIME BUT O(1) SPACE
        // Arrays.sort(arr);
        // int diff = arr[1] - arr[0];
        // for(int i = 1; i < arr.length; i++) {
        //     if(arr[i] - arr[i-1] != diff) {
        //         return false;
        //     }
        // }
        // return true;
    }
}

*/




// ===================================================================================

// [AUTHOR] rock
// [DESCRIPTION] [Java/Python 3] O(n) and O(nlogn) codes w/ brief explanation and analysis.

/*

Method 1:

	1. Find the max and min of arr and compute the average difference;
	2. Put all numbers into a HashSet;
	3. Start from the min, add the average difference to make the next number in the arithmetic sequence, check one by one if it is in the HashSet; if any one not in, return false; otherwise, return true.

Note:

	1. There are n - 1 slots between n element of the array;
	2. diff = max = min must be divisible by n - 1 for arr to be an arithmetic sequence;
	3. After sorting arr, the adjacent elements difference must be diff / (n - 1), if it is an arithmetic sequence.

# C++

public boolean canMakeArithmeticProgression(int[] arr) {
    Set<Integer> seen = new HashSet<>();
    int mi = Integer.MAX_VALUE, mx = Integer.MIN_VALUE, n = arr.length;
    for (int a : arr) {
        mi = Math.min(mi, a);
        mx = Math.max(mx, a);
        seen.add(a);
    }
    int diff = mx - mi;
    if (diff % (n - 1) != 0) {
        return false;
    }
    diff /= n - 1;
    while (--n > 0) {
        if (!seen.contains(mi)) {
            return false;
        }
        mi += diff;
    }
    return true;
}

# Python

def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    mi, mx, n, s = min(arr), max(arr), len(arr), set(arr)
    if (mx - mi) % (n - 1) != 0:
        return False    
    diff = (mx - mi) // (n - 1)
    for _ in range(n):
        if mi not in s:
            return False
        mi += diff
    return True



Analysis:

Time & space: O(n).

------------------------------------------------------------------

Q & A

Q1: could you please explain?

1. why do this?
	if (diff % (n - 1) != 0) {
	    return false;
	}

2. how does it become average difference of each element?
	diff /= n - 1;

A1:
If you have 2 elements, there is only 1 difference;
If you have 3 elements, there are 2 differences;
If you have 4 elements, there are 3 differences;
...
If you have n elements, there are n - 1 differences;

	1. if n - 1 can not divide the total difference diff, then at least 1 difference is not same as others;
	2. n elements correspond to n - 1 differences.

End of Q & A

------------------------------------------------------------------

Method 2: Sort

# C++

public boolean canMakeArithmeticProgression(int[] arr) {
    Arrays.sort(arr);
    for (int i = 2; i < arr.length; ++i) {
        if (arr[i - 1] - arr[i] != arr[i - 2] - arr[i - 1]) {
            return false;
        }
    }
    return true;
}

# Python

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i - 2] - arr[i - 1] == arr[i - 1] - arr[i] for i in range(2, len(arr)))


Analysis:

Time: O(nlogn), space: O(1) if excluding space used during sort.
*/



// ===================================================================================

/ * 
  * Test cases

	[3,5,1]
	[1,2,4]

*/

// [AUTHOR] Me
// [DESCRIPTION] NOT working solution
var canMakeArithmeticProgression = function(array) {
  let counter = 0
  let diff = 0;
  
  const isArrayEmpty = !array.length;
  const isArrayHasOneValue = array.length < 2;
  const isLoopRange = (counter + 1) < array.length
  
  if (isArrayEmpty || isArrayHasOneValue) return false;
  
  diff = Math.abs(array[counter] - array[counter + 1]);
  
  while (isLoopRange) {
    let currentDiff = Math.abs(array[counter] - array[counter + 1]);
    
    counter++;
    
    if (currentDiff % diff === 0) continue;
    else return false;
  }
  
  return true;
  
};



