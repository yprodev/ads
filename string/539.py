# [AUTHOR]: strawberrykiwi
# [DESCRIPTION]: Python3 O(nlogn) time with detailed explanation :)

"""
This problem is actually quite a brain teaser if you haven't worked much with circular algorithms. It's actually a really fun problem!

Let's consider the distances of all the points here. The distance from p1 to p3 is equal to abs(24:00 - 22:04 + 1:30). The distance from p1 to p2 is equal to abs(1:30 - 10:46). The distance from p2 to p3 is abs(10:46 - 22:04). In general, if we consider two points that are within (including) 12 hours of eachother and there's no crossing over the 0th hour, the calculation is straight forward and just abs (a-b). It gets complicated though in the other events. So how do we account for a distance greater than 12? Well, it means from the point which is larger, we need to do 24:00 - max(a,b) + min(a,b). The 24:00 - max(a,b) part offsets the max point back to 0, and then the min(a,b) part will get you to the destination. Therefore, we can conclude the general formula, dist(a,b) = min(abs(a - b), abs(24 - max(a,b) + min(a,b)). We can just now, for each point compare it to every other point and calculate the distance, getting the max. This would be a operation performed (n-1) + (n-2) + (n-3) + ... + 1 times, and thus, total time compelxity is O(n^2)

As you probably guessed, we can do better! There's a serious flaw with what what we're doing. For each point, we are barbarically looking at every single point and calculating the distance, but there's a good fact we can take advantage of. Consider the diagram. Suppose we wanted to find the minimum distance between p1, p2, and p3. For each given point, we can find the closest point for each by looking both left and right and selecting the first element we see. To better illustrate this, consider this instead.

The closest point, is always, no matter what, is either the first elment looking clockwise or counter clockwise. Looking at any other point is redundant, because they cannot possibly be the closest. Furthermore, we can reduce this to just have every element look clockwise, because the element behind it will calculate the distance in it's ccw direction when it looks cw.

However, we can only guarantee this will work if we have our points sorted, and this is where the O(nlogn) complexity comes from. So, our new algorithm is:

1. Convert each time to minutes. O(n).
2. Sort the list of minutes. O(nlogn).
3. Calculate the distance from p[i] to p[i+1] for all i except p[n-1] where n is the length of the times array. O(n).
4. Calculate the distance of the final point to it's first CW element, which will cross 0. This is the point in which there would be a revolution loop. O(1).

At each step between 3 and 4, minDist = min(current, new).

"""

def toMin(time):
    time = time.split(':')
    res = (60*int(time[0])) + int(time[1])
    return res
    
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            timePoints[i] = toSec(time)
        
        res = sys.maxsize
        timePoints.sort()
        for i in range(0, len(timePoints) - 1): #calculate the closest CW distance of each element except last
            res = min(res, (timePoints[i+1] - timePoints[i]))
        
        res = min(res, 60* 24 - timePoints[-1] + timePoints[0]) #calc final point
        
        return res

# ===================================================

# [AUTHOR]: awice
# [DESCRIPTION]: Python, Straightforward with Explanation

"""
Convert each timestamp to it's integer number of minutes past midnight, and sort the array of minutes.
The required minimum difference must be a difference between two adjacent elements in the circular array (so the last element is "adjacent" to the first.) We take the minimum value of all of them.
"""

def findMinDifference(self, A):
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:])
    minutes = map(convert, A)
    minutes.sort()
    
    return min( (y - x) % (24 * 60) 
                for x, y in zip(minutes, minutes[1:] + minutes[:1]) )

# [COMMENT] from lee215

def findMinDifference(self, timePoints):
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))

# ===================================================

# [AUTHOR]: patrick-replogle
# [DESCRIPTION]: Fast Javascript Solution

"""
var findMinDifference = function(timePoints) {
    let minDifference = Infinity;
    let arr = timePoints
                    .map(el => (Number(el.slice(0, 2)) * 60) + Number(el.slice(3, 5)))
                    .sort((a, b) => a - b);

    for (let i = 1; i < arr.length; i++) {
        minDifference = Math.min(minDifference, Math.abs(arr[i] - arr[i-1]));
    }
    return Math.min(minDifference, 1440 + arr[0] - arr[arr.length - 1])
};
"""

# ===================================================

# [AUTHOR]: Liew-Li
# [DESCRIPTION]: Clean JavaScript Solution

"""
/**
 * @param {string[]} timePoints
 * @return {number}
 */
var findMinDifference = function(timePoints) {
  const _ = t => {
    const [h, m] = t.split(":").map(p => +p);
    return h * 60 + m;
  };
  const time = timePoints.map(t => _(t));
  time.sort((a, b) => a - b);

  let m = Number.MAX_SAFE_INTEGER;
  for (let i = 1; i < time.length; ++i) {
    m = Math.min(m, time[i] - time[i - 1]);
  }
  m = Math.min(m, 24 * 60 - time[time.length - 1] + time[0]);

  return m;
}
"""


# ===================================================


# [AUTHOR] strawberrykiwi
# [DESCRIPTION] Re-typed solution for memorization


"""

1. Convert each time to minutes. O(n).
2. Sort the list of minutes. O(nlogn).
3. Calculate the distance from p[i] to p[i+1] for all i except p[n-1] where n is the length of the times array. O(n).
4. Calculate the distance of the final point to it's first CW element, which will cross 0. This is the point in which there would be a revolution loop. O(1).

At each step between 3 and 4, minDist = min(current, new).

"""

def toSec(time):
    time = time.split(':')
    res = (60 * int(time[0]) + int(time[1]))

    return res


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            timePoints[i] = toSec(time)

        timePoints.sort()

        res = sys.maxsize

        # Calculate the closest CW distance of each element except last
        for i in range(0, len(timePoints) - 1):
            res = min(res, (timePoints[i + 1] - timePoints[i]))

        # Calculate the final point
        return min(res, 60 * 24 - timePoints[-1] + timePoints[0])


