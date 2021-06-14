# [AUTHOR]: votrubac
# [DESCRIPTION]: C++ 3 lines, hash map + map
"""

We use hash map to lookup ordered {timestamp, value} pairs by key in O(1). Then, we use binary search to find the value with a timestamp less or equal than the requested one.

unordered_map<string, map<int, string>> m;

void set(string key, string value, int timestamp) {
  m[key].insert({ timestamp, value });
}

string get(string key, int timestamp) {
  auto it = m[key].upper_bound(timestamp);
  return it == m[key].begin() ? "" : prev(it)->second;
}

Since our timestamps are only increasing, we can use a vector instead of a map, though it's not as concise.

unordered_map<string, vector<pair<int, string>>> m;

void set(string key, string value, int timestamp) {
  m[key].push_back({ timestamp, value });
}

string get(string key, int timestamp) {
  auto it = upper_bound(begin(m[key]), end(m[key]), pair<int, string>(timestamp, ""), [](
    const pair<int, string>& a, const pair<int, string>& b) { return a.first < b.first; });
  return it == m[key].begin() ? "" : prev(it)->second;
}

Complexity analysis
Assuming n is the number of set operations, and m is the number of get operations:

	Time Complexity:
		Set: O(1) single operation, and total O(n).
			Note: assuing timestamps are only increasing. If not, it's O(n log n).
		Get: O(log n) for a single operation, and total O(m log n).

	Space Complexity: O(n) (assuming every { timestamp, value } is unique).

"""


# ===================================================

# [AUTHOR]: yidong_w
# [DESCRIPTION]: [Python] Dict and Binary search Implementation

"""
Most of the solution here doesn't give you the binary search implementation, but you propabaly needs to write it during the interview...

"""
class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
            mid = (left + right) / 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]


# ===================================================

# [AUTHOR]: StayingFoolish
# [DESCRIPTION]: (JS Version) Map + Binary Search


"""
function TimeMap () {
  this.map = new Map()
}

TimeMap.createNew = function () {
  return new TimeMap()
}

TimeMap.prototype.set = function(key, value, timestamp) {
  if (!this.map.has(key)) {
    this.map.set(key, [])
  }
  this.map.get(key).push({
    timestamp,
    value
  })
}

TimeMap.prototype.get = function(key, timestamp) {
  if (!this.map.has(key)) {
    return ''
  }

  let arr = this.map.get(key)

  // Binary search
  let L = 0, R = arr.length - 1, M
  while (L < R) {
    let M = Math.floor((L + R) / 2), center = arr[M]
    if (timestamp === center.timestamp) {
      return center.value
    } else if (timestamp < center.timestamp) {
      R = M - 1
    } else {
      L = M + 1
    }
  }

  // Not exist, then find next smaller [timestamp]
  while (L >= 0 && arr[L].timestamp > timestamp) {
    --L
  }
  
  return L >= 0 ? arr[L].value : ''
}

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = Object.create(TimeMap).createNew()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
"""




# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	1. Out of time
#	2. Forgot how to write binary search
#	3. Forgot how to write hash function
#	4. Forgot what is Map in JS






