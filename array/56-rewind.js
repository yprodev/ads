// Transformed Python3 solution into a JS
var merge = function(intervals) {
    const result = [];

    const intervalsSorted = intervals.sort((a, b) => a[0] - b[0]);
    
    for (let i = 0; i < intervalsSorted.length; i++) {
        let begin = intervalsSorted[i][0];
        let end = intervalsSorted[i][1];
        
        if (result.length === 0 || result[result.length - 1][1] < begin) {
            result.push(intervalsSorted[i]);
        } else {
            result[result.length - 1][1] = Math.max(result[result.length - 1][1], end);
        }
            
    }
    
    return result;
    
};

/*
    Issues:

    - Forgot to sort the intervals.
    - Forgot to compare the second item of the last interval in the result arr with the end interval.

*/

