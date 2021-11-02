// [AUTHOR]: Sporkyy
// [DESCRIPTION]: JavaScript Solution with Comments

const shortestToChar = (s, c) => {
  // Create an array to hold the distances the same length as the string
  // And fill it with `Infinity` because `Math.min` gets used below
  // But filling with `s.length` or `104` (from Constraints) would also work.
  const res = new Array(s.length).fill(Infinity);
  for (
    // Create some variables to use while looping through the string
    // - `li` Left Index: Traverse the string from left to right
    // - `ld` Left Distance: Reset to `0` every time `c` is seen in the string
    // - `ri` Right Index: Traverse the string from right to left
    // - `rd` Right Distance: Reset to `0` every time `c` is seen in the string
    let li = 0, ld = Infinity, ri = s.length - 1, rd = Infinity;
    // Stop the loop before the Left Index goes off the right end of the string
    // This also stops the loop before the Right Index goes off the left end
    li < s.length;
    // After every iteration:
    // - The left index moves `1` place to the left
    // - The left distance increases by `1`
    // - The right index moves `1` place to the right
    // - The right distance increases by `1`
    li++, ld++, ri--, rd++
  ) {
    // If the character at the left index is the character we're looking for,
    // reset the left distance to `0`
    if (s[li] === c) ld = 0;
    // As we move left, set the `res` array value to the lesser distance:
    // - `res[li]` The default value, `Infinity` or, passed the halfway point,
    //   the previously set Right Distance to the sought character
    // - `ld` Distance to the sought character looking left
    res[li] = Math.min(res[li], ld);
    // If the character at the right index is the character we're looking for,
    // reset the right distance to `0`
    if (s[ri] === c) rd = 0;
    // As we move right, set the `res` array value to the lesser distance:
    // - `res[ri]` The default value, `Infinity` or, passed the halfway point,
    //   the previously set Left Distance to the sought character
    // - `rd` Distance to the sought character looking right
    res[ri] = Math.min(res[ri], rd);
  }
  return res;
};

// ===================================================

// [AUTHOR]: YehudisK
// [DESCRIPTION]: C++ Simple Solution 0 ms faster than 100%

/*

class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> res;
        int prev_char = -s.size();
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == c)
                prev_char = i;
            res.push_back(i - prev_char);
        }

        for (int i = prev_char; i >= 0; i--) {
            if (s[i] == c)
                prev_char = i;
            res[i] = min(res[i], prev_char - i);
        }
        return res;
    }
};

*/


// ===================================================

// [AUTHOR]: bt4r9
// [DESCRIPTION]: [javascript] 2 pass simple solution with explanation

/*

The problem becomes really simple if we consider the example.

0 1 2 3 4 5 6 7 8 9 10 11
l o v e l e e t c o d  e

What is the shortest distance for index 9 if the character is e?
The closest e from the left side has the index 6.

9 - 6 = 3

The closest e from the right side has the index 11.

11 - 9 = 2

The minimum distance between them is 2, so the answer is 2. Can we do it for any index?
Yes we can, all we need to do is to keep track of the previous character index while iterating from the left to the right and vice versa. The only edge case here is that initially we could possibly don't have a previous index, so to mitigate it for such indecies we can put the shortest distance for them as Infinity and once we complete 2 passes at least one non-Infinity value for each index should exist.
Let's consider the example again.

character = "e"

index  | 0 1 2 3 4 5 6 7 8 9 10 11
char   | l o v e l e e t c o d  e
// shortest distance from left to right
l -> r | I I I 0 1 0 0 1 2 3 4  0 // I = Infinity
// shortest distance from right to left
l <- r | 3 2 1 0 1 0 0 4 3 2 1  0
// the minimum between them is the answer
result | 3 2 1 0 1 0 0 1 2 2 1  0

*/

var shortestToChar = function(s, c) {
    let n = s.length;
    let res = [];
        
    let prev = Infinity;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === c) prev = i;
        res[i] = Math.abs(prev - i);
    }

    prev = Infinity;

    for (let i = n - 1; i >= 0; i--) {
      if (s[i] === c) prev = i;
      res[i] = Math.min(res[i], prev - i);
    }

    return res;
}


// ===================================================


// [AUTHOR] ME
// [DESCRIPTION] The solutions was inspired by uzzwal example

