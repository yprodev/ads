/*
===================================================================================
[SOURCE] YouTube: https://www.youtube.com/watch?v=J5IIH35EBVE
[AUTHOR]: Nate Santti
# [DESCRIPTION]: Sum of All Odd Length Subarrays | LeetCode 1588 | Explained and Java Code

class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int result = 0;
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int end = i + 1;
            int start = n - 1;
            int total = start * end;
            int odd = total / 2;
            if (total % 2 == 1) {
                odd++;
            }
            result += odd * arr[i];
        }

        return result;
    }
}

*/

var sumOddLengthSubarrays = function(arr) {
    let result = 0; // The actual number we need to get
    let n = arr.length // The size of an array

    for (let i = 0; i < n; i++) {
        let end = i + 1; // end - just the ending position of a sub-array
        let start = n - i; // start - starting point of each sub-array found
        let total = start * end;
        let odd = parseInt(total / 2); // Find the number of odd sub-arrays

        if (total % 2 === 1) {
            odd++; // Specify the exact number of odd sub-arrays
        }

        result += parseInt(odd * arr[i])
    }

    return result;
};


// The same solution in less lines of code
var sumOddLengthSubarrays = function(arr) {
    let result = 0,
        n = arr.length;

    for (let i = 0; i < n; i++) {
        result += parseInt(((i + 1) * (n - i) + 1) / 2) * arr[i];
    }

    return result;
};
