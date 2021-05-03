// First solution
var largestAltitude = function(gain) {
    const altitude = [0];

    for (let i = 0; i < gain.length; i++) {
        altitude.push(altitude[i] + gain[i]); // Find the difference on each step
    } 

    return Math.max(...altitude);
};

// Second solution
var largestAltitude = function(gain) {
    let max = 0,
        curr = 0;

    for (let i = 0; i < gain.length; i++) {
        curr = curr + gain[i];

        if (curr > max) {
            max = curr;
        }
    }

    return max;
};

