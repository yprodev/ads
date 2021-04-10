// First solution with additionaly defined array of 
// exact size:

var sortArrayByParity = function(A) {
    const arrLen = A.length;
    const resultArr = new Array(arrLen);
    let start = 0;
    let end = arrLen - 1;
    
    for (let i = 0; i < arrLen; i++) {
        if (A[i] % 2 === 1) {
            resultArr[end] = A[i];
            end -= 1;
        } else {
            resultArr[start] = A[i];
            start += 1;
        }
    }
    
    return resultArr;
    
};

// ============================================

// Second solution uses in-place swap (with additional variable).
// You may simplify with destructuring and remove the temp variable.
var sortArrayByParity = function(A) {
    let s = 0,
        e = A.length - 1;
    
    while (s < e) {
        if (A[s] % 2 === 0) {
            s += 1;
        } else {
            let temp = A[s];
            A[s] = A[e];
            A[e] = temp;
            e -= 1;
        }
    }
    
    return A;
    
};


// ============================================

// The third example is almost the same as the second one, but
// here we use bitwise operators to compare numbers (values).
var sortArrayByParity = function(A) {
    let s = 0,
        e = A.length - 1;
    
    while (s < e) {
        if (A[s] & 1) {
            let temp = A[s];
            A[s] = A[e];
            A[e] = temp;
        }
        
        s += !(A[s] & 1);
        e -= A[e] & 1;
    }
    
    return A;
    
};

