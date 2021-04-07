

# ===================================================================================

# [AUTHOR]: gokudera17
# [DESCRIPTION]: [Python 3] Using Counter and len

"""
Use Counter to count occurence of numbers.
return length of values and set(values).
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = collections.Counter(arr)
        return len(a.values()) == len(set(a.values()))

# ===================================================================================

# [AUTHOR]: rock
# [DESCRIPTION]: [Java/Python 3] 4 liner and 2 liner Using Map and Set w/ brief explanation and analysis.

"""
Count the occurrences of each char;
Compare if the numbers of distinct chars and distinct counts are equal.

public boolean uniqueOccurrences(int[] arr) {
    Map<Integer, Integer> count = new HashMap<>();
    for (int a : arr)
        count.put(a, 1 + count.getOrDefault(a, 0));
    return count.size() == new HashSet<>(count.values()).size();
}

Analysis:

Time & space: O(n), where n = arr.length
"""

def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))



# ===================================================================================

# [AUTHOR]: votrubac
# [DESCRIPTION]: C++ 2 approaches

"""
Approach 1: Map and set
Count occurences of each number using a hash map. Insert all occurences into a hash set. If, after the insert, the sizes of hash map and set are equal, then all occurences are unique.

bool uniqueOccurrences(vector<int>& arr) {
  unordered_map<int, int> m;
  unordered_set<int> s;
  for (auto n : arr) ++m[n];
  for (auto& p : m) s.insert(p.second);
  return m.size() == s.size();
}

We can improve this for the average case by checking the result of s.insert(), which returns false if an element is already there.

bool uniqueOccurrences(vector<int>& arr) {
  unordered_map<int, int> m;
  unordered_set<int> s;
  for (auto n : arr) ++m[n];
  for (auto& p : m)
      if (!s.insert(p.second).second) return false;
  return true;
}

Complexity Analysis
Time: O(n), where n is the size of input array.
Memory: O(m), where m is the number of unique elements (we store counts in hash map and set).

Approach 2: Counting sort
Since our values are limited to [-1000, 1000], we can use an array instead of hash set to count occurrences. Then, we can sort our array and check that no adjacent numbers are the same.

bool uniqueOccurrences(vector<int>& arr) {
  short m[2001] = {};
  for (auto n : arr) ++m[n + 1000];
  sort(begin(m), end(m));
  for (auto i = 1; i < 2001; ++i)
      if (m[i] && m[i] == m[i - 1]) return false;
  return true;
}

We can also note that the array length is limited to 1000, so no element will repeat more than 1000 times. Therefore we can use another array to do the counting sort over the occurrences.

bool uniqueOccurrences(vector<int>& arr) {
  short m[2001] = {}, s[1001] = {};
  for (auto n : arr) ++m[n + 1000];
  for (auto i = 0; i < 2001; ++i)
      if (m[i] && ++s[m[i]] > 1) return false;
  return true;
}

Complexity Analysis
Time:

First solution: O(n + m log m).
Second solution: O(n).
Memory: O(m).

"""



# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	You may use hash table with counter
#	You may use counter for iterables for this task

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = dict()
        seen = set()
        
        for item in arr:
            if item in mem:
                mem[item] += 1
            else:
                mem[item] = 1
                
        for val in mem.values():
            if val in seen:
                return False
            else:
                seen.add(val)


        return True
