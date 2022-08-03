// Author: goeyj
// Description: [JavaScript] Easy to follow O(n) - 92ms

function minOperations(boxes) {
  const result = Array(boxes.length).fill(0);
  
  // First we make one pass through the array (left to right).
  // For each index, we calculate the moves needed to get every
  // non-empty box on the left of the current index to the current index.
  
  // At each i in boxes:
  //   - add the running sum to result[i]
  //   - increment the notEmpty box count if the current box is '1'
  //   - add the previously seen notEmpty boxes (including current index) to the runningSum
  
  let notEmpty = 0;
  let runningSum = 0;
  
  for (let i = 0; i < boxes.length; ++i) {
    result[i] += runningSum;
    if (boxes[i] === '1') ++notEmpty;
    runningSum += notEmpty;
  }
  
  // Make one more pass through the array (right to left).
  // The operations are identical to the first loop, except that
  // this pass calculates the moves needed to get every non-empty box
  // on the right of each index to the current index.
  
  notEmpty = 0;
  runningSum = 0;
  
  for (let i = boxes.length - 1; i >= 0; --i) {
    result[i] += runningSum;
    if (boxes[i] === '1') ++notEmpty;
    runningSum += notEmpty;
  }
  
  return result;
}


// =============================================================================

// Author: votrubac
// Description: C++/Java O(n) LTR + RTL

/*

We first "move" balls from left to right, and track how many ops it takes for each box.
For that, we count how many balls we got so far in cnt, and accumulate it in ops.
Then, we do the same from right to left.

C++

vector<int> minOperations(string boxes) {
    vector<int> res(boxes.length()); 
    for (int i = 0, ops = 0, cnt = 0; i < boxes.length(); ++i) {
       res[i] += ops;
       cnt += boxes[i] == '1' ? 1 : 0;
       ops += cnt;
    }
    for (int i = boxes.length() - 1, ops = 0, cnt = 0; i >= 0; --i) {
        res[i] += ops;
        cnt += boxes[i] == '1' ? 1 : 0;
        ops += cnt;
    }
    return res;
}

Java

public int[] minOperations(String boxes) {
    int[] res = new int[boxes.length()];
    for (int i = 0, ops = 0, cnt = 0; i < boxes.length(); ++i) {
       res[i] += ops;
       cnt += boxes.charAt(i) == '1' ? 1 : 0;
       ops += cnt;
    }    
    for (int i = boxes.length() - 1, ops = 0, cnt = 0; i >= 0; --i) {
        res[i] += ops;
        cnt += boxes.charAt(i) == '1' ? 1 : 0;
        ops += cnt;
    }
    return res;
}

*/



