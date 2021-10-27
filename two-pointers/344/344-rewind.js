// [AUTHOR]: jamiehsmith
// [DESCRIPTION]: Javascript - Simple with comments


var reverseString = function(s) {
    // Loop through 1/2 of s
    for (let i = 0; i < s.length / 2; i++) {
        // Save current val
        let temp = s[i];
        
        // Replace with end of array char
        s[i] = s[s.length - 1 - i];
        
        // Replace end of array letter with current val
        s[s.length - 1 - i] = temp;
    }
};


// ===================================================

// [AUTHOR]: jesseokeya
// [DESCRIPTION]: Javascript Solution. Beats 87.72%

var reverseString = function(s) {
    for (let i = 0; i < s.length / 2; i++) {
        [s[i], s[(s.length - i) - 1]] = [s[(s.length - i) - 1], s[i]] 
    }
};


// ===================================================

// [AUTHOR] ME
// [DESCRIPTION] Second working solution

var reverseString = function(s) {
    let temp = null,
        left = 0,
        right = s.length - 1;

    while (left < right) {
        temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
};
