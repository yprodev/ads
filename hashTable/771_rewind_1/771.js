var numJewelsInStones = function(jewels, stones) {
    let counter = 0;
    
    for (let i = 0, len = stones.length; i < len; i++) {
        if (jewels.includes(stones[i])) {
            counter += 1;
        }
    }
    
    return counter;
};