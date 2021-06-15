# [AUTHOR]: ssaran720
# [DESCRIPTION]: Python Easy Solution, Faster than 100%

costs.sort() #sorting cost array
count = 0  #tracker of candy bars count
for i in costs: #iterating through array
    if(coins-i>=0):  # count is increased only if deduction of cost from coin is more than 0 or 0.
          coins -= i 
          count +=1
return count

# ===================================================

# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3] Sort and apply greedy algorithm.

"""
JAVA

public int maxIceCream(int[] costs, int coins) {
    Arrays.sort(costs);
    for (int i = 0; i < costs.length; ++i) {
        coins -= costs[i];
        if (coins < 0) {
            return i;
        }
    }
    return costs.length;
}

"""

def maxIceCream(self, costs: List[int], coins: int) -> int:
    for i, c in enumerate(sorted(costs)):
        coins -= c
        if coins < 0:
            return i
    return len(costs)


"""
Analysis:

Time: O(nlogn).
"""

# ===================================================

# [AUTHOR]: votrubac
# [DESCRIPTION]: C++/Java Greedy

"""
Buy the cheapest bar, repeat until you cannot buy anymore: not enough coins or you've bought all bars.

C++

int maxIceCream(vector<int>& costs, int coins) {
    sort(begin(costs), end(costs));
    for (int i = 0; i < costs.size(); ++i)
        if (coins >= costs[i])
            coins -= costs[i];
        else
            return i;
    return costs.size();
}

Java

public int maxIceCream(int[] costs, int coins) {
    Arrays.sort(costs);
    for (int i = 0; i < costs.length; ++i)
        if (coins >= costs[i])
            coins -= costs[i];
        else
            return i;
    return costs.length;
}

"""


# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First NOT working solution
# Issues:
#	Count the iteration (bars) is not not the same as indexes
#	There is python sorted() and .sort() functions on the list


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costsOrdered = sorted(costs)
        spendings = 0
        bars = 1
            
            
        if costsOrdered[0] > coins:
            return 0 # should be 0, if don't have money even for the one bar
            
        for priceBar in costsOrdered:

            print('bar price: ', priceBar, ' spendings: ', spendings, ' bars (iter): ', bars)
            
            spendings += priceBar
            bars += 1

            # Not enought money to buy the next bar
            if (coins > spendings) < priceBar:
                print('>>>>bar price: ', priceBar, ' spendings: ', spendings, ' bars (iter): ', bars)
                
                return bars - 1 # instead of getting the price of the next bar
            
            # Enought money to buy them all
            if spendings < coins and len(costsOrdered) == bars:                
                return bars



# [AUTHOR] ME
# [DESCRIPTION] Second re-typed solution (from author: rock)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        for idx, cost in enumerate(sorted(costs)):
            coins -= cost
            
            if coins < 0:
                return idx
            
        return len(costs)

# [TESTCASES]
"""
[1,3,2,4,1]
7
[10,6,8,7,7,8]
5
[1,6,3,1,2,5]
20
[7,3,3,6,6,6,10,5,9,2]
56
"""

