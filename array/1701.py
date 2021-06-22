# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3] Track the chef's available time, w/ analysis.

"""
Analysis:
Time: O(n), space: O(1), where n = customers.length.

public double averageWaitingTime(int[][] customers) {
    double wait = 0, nextAvailableTime = 0;
    for (int[] c : customers) {
        nextAvailableTime = c[1] + Math.max(c[0], nextAvailableTime);
        wait += nextAvailableTime - c[0];
    }
    return wait / customers.length;
}

"""

def averageWaitingTime(self, customers: List[List[int]]) -> float:
    wait = next_available_time = 0
    for arrival, time in customers:
        next_available_time = time + max(next_available_time, arrival)
        wait += next_available_time - arrival
    return wait / len(customers)


# ===================================================

# [AUTHOR]: pratham1807
# [DESCRIPTION]: [JAVA] Easy Solution, Time O(n) Space O(1)

"""
Approach

1. Keep a track of the current time time and total wait time waitingTime.
2. If the time of arrival of the next customer is greater than the current time, fast forward to that time time = Math.max(cust[0],time)
3. Increament the time with the time required to prepare the dish time = time + cust[1]
4. Calculate the total time customer[i] had to wait and add it to total time.
5. Divide by the total no. of customers to get average.

class Solution {
    public double averageWaitingTime(int[][] customers) {
        double time = 0;
        double waitingTime = 0;
        
        for(int[] cust : customers){
            time = Math.max(cust[0],time);            
            time = time + cust[1];
            waitingTime += (time - cust[0]);
        }
                
        return waitingTime/customers.length;
    }
}

"""



# ===================================================

# [AUTHOR]: felixthe8
# [DESCRIPTION]: Javascript Solution


"""
/**
 * @param {number[][]} customers
 * @return {number}
 */
var averageWaitingTime = function(customers) {
    let waitingTimes = 0;
    let time = customers[0][0];

    customers.forEach((c) => {
		// Handle the case where the customer arrives and 
	   // after the last order was completed
        if(c[0] > time) {
            time = c[0];
        } 
		
		// Advance time to when the order is completed
        time+=c[1];
		
		// Keep running total of the waiting times
        waitingTimes+=(time-c[0]);
    })

    return waitingTimes / customers.length;
};


// Runtime: 156 ms (Beats 83.23 % of Javascript submissions )
// Memory Usage: 63.9 MB ( Beats 37.89 % of javascript submissions )

"""

# ===================================================

# [AUTHOR]: vatsalbhuva11
# [DESCRIPTION]: [Python 3] Simple Solution with Explanation


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait = customers[0][1]
        wait_temp = sum(customers[0])
        for i in customers[1:]:
            if i[0] >= wait_temp:
                wait_temp = sum(customers[customers.index(i)])
                total_wait += i[1]
            else:
                wait_temp += i[1]
                total_wait += wait_temp - i[0]
        return total_wait/len(customers)

"""
	* total_wait is the total wait time of all customers.
	* wait_temp is the wait time after each customer's order gets ready.

The approach is to subtract each customer's arrival time from the wait_temp in that iteration to find how long the customer waited altogether till his order arrived.


Two situations are possible:

	1. A customer B arrives during the time when the previous customer A's order is being made:
		* Here, we have to add the 'extra time' that B has to wait until A's order is ready, and then add his own time to total_wait
	2. A customer B arrives after the previous customer A's order is ready:
		* Now, the customer B does not have to wait any extra time, because when he arrives at the restaurant, no other orders are being made.
		* Hence, I'm setting the wait_temp to be the time taken for B's order only (because now, we can treat the situation as a sub-problem wherein customer B is the first customer of the restaurant), and then the process of calculation is the same as we had started off with.

"""

# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
# 	Started to do the solution within the editor
# 	Started with reduce function in JavaScript


"""
var averageWaitingTime = function(customers) {
    customers.reduce((acc, curr, idx) => {
        
        if (acc.finishTime === 0) {
            acc.finishTime = acc.finishTime + curr[0] + curr[1];
            acc.waitTime = acc.finishTime - curr[0];
        }
        
        
        console.log(acc, curr, acc.finishTime, curr[1])
        
        return {
            ...acc,
            finishTime: acc.finishTime + curr[1],
            waitTime: acc.waitTime,
            avg: acc.avg + acc.waitTime / (idx + 1)
        }
    }, { finishTime: 0, waitTime: 0, avg: 0 });
    
};
"""

# ===================================================

# [AUTHOR] Copied from rock author
# [DESCRIPTION] Re-typed solution for memorizing

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        timeNext = timeWait = 0

        for arrival, time in customers:
            timeNext = time + max(timeNext, arrival)
            timeWait += timeNext - arrival

        return timeWait / len(customers)


# [AUTHOR] Copied from rock author
# [DESCRIPTION] Re-typed solution for memorization


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        timeNxt = timeWait = 0

        for arrival, timePrep in customers:
            timeNxt = max(timeNxt, arrival) + timePrep
            timeWait += timeNxt - arrival

        return timeWait / len(customers)

