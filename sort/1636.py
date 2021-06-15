# [AUTHOR]: denisrasulev
# [DESCRIPTION]: Python 3 solution - with process of thinking and improvement

"""
Part 1
Sunday morning, Spotify, coffee, console... Task from the list of tasks to solve later.
Let's go!

~ ❯ python3                                                                                                                     at 10:38:03
Python 3.9.1 (default, Feb  3 2021, 07:38:02)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> nums = [1,1,2,2,2,6,6,4,4,5,5,3]

Ok, so I need to count frequency of each of the unique values... First idea - use Counter. This returns collection type of object:

>>> d = Counter(nums)
>>> d
Counter({2: 3, 1: 2, 6: 2, 4: 2, 5: 2, 3: 1})
>>> type(d)
<class 'collections.Counter'>


Now I need to sort those values following the requirements in the description. 'Counter' object has no attribute 'sort', and 'sorted' will only sort values, not frequencies. Googling options, found this StackOverflow question with lots of useful answers. Reading... Let's try easier object:

>>> r = Counter(nums).most_common()

This returns a list of tuples, where first number is value and second - its' frequency. Can I sort it in the same command? Jumping to the official documentation. Nope, not sortable in the command itself, moreover: "Elements with equal counts are ordered in the order first encountered". Ok, let's sort it directly, first by values in the decreasing order, then by frequencies in the increasing.

>>> r.sort(key = lambda x: x[0], reverse=True)
>>> r.sort(key = lambda x: x[1])
>>> r
[(3, 1), (6, 2), (5, 2), (4, 2), (1, 2), (2, 3)]


Looks promising. Now I want to expand those tuples into a single list... Still browsing answers to the same question. Remembering that I can expand tuple and get every number from it by using this:

>>> a, b = (3, 2)
>>> a
3
>>> b
2

so then I can repeat every value by the number of its' frequency like so:

>>> [3]*2
[3, 3]


Aha. Now I need an empty list to combine all those tuples into a single list:


t = []
for i in r:
    a, b = i
    t.extend([a] * b)

>>> t
[3, 6, 6, 5, 5, 4, 4, 1, 1, 2, 2, 2]


Woo-hoo! That's what I need. So the complete solution now looks like this:


"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        r = Counter(nums).most_common()
        r.sort(key = lambda x: x[0], reverse=True)
        r.sort(key = lambda x: x[1])
        
        t = []
        for i in r:
            a, b = i
            t.extend([a]*b)
            
        return t


"""

Result:
Runtime: 52 ms, faster than 63.30% of Python3 online submissions for Sort Array by Increasing Frequency.
Memory Usage: 14.2 MB, less than 58.20% of Python3 online submissions for Sort Array by Increasing Frequency.

Not the best, but the task is solved.

Part 2
Now it's time for another fun - can I make it one-liner or optimize the solution in any other way?

Looking at sorting lines... Can I sort it in one go? Yes! So, first we sort by values in the reverse order (-x[0]) and then by their frequencies (x[1]) in direct order.


>>> r.sort(key = lambda x: (x[1], -x[0]))

Basically, it's the same operation as the above but now coded in one line. Love Python :) Same logic applies to the tuple expansion part and it allows to save another line:

t = []
for i in r:
	t += ([i[0]] * i[1])

And then I thought - if I can sort by value and its' frequency why do I need intermediate list? Can I sort the original list the same way?! Let's see...

>>> nums
[1, 1, 2, 2, 2, 6, 6, 4, 4, 5, 5, 3]
>>> r = Counter(nums)
>>> r
Counter({2: 3, 1: 2, 6: 2, 4: 2, 5: 2, 3: 1})
>>> nums.sort(key=lambda x: (r[x], -x))
>>> nums
[3, 6, 6, 5, 5, 4, 4, 1, 1, 2, 2, 2]


Voila! That feels sooo good. But x.sort makes it in-place and I need to return an object... So, I need to change it to sorted then:

>>> result = sorted(nums, key=lambda x: (r[x], -x))
>>> result
[3, 6, 6, 5, 5, 4, 4, 1, 1, 2, 2, 2]


Perfect. So the final variant would be:

"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        r = Counter(nums)
        return sorted(nums, key=lambda x: (r[x], -x))

"""

And it's even faster!

Runtime: 44 ms, faster than 95.07% of Python3 online submissions for Sort Array by Increasing Frequency.
Memory Usage: 14.3 MB, less than 58.20% of Python3 online submissions for Sort Array by Increasing Frequency.

NOTE

If you want to downvote this post, please, be brave and comment why. This will help me and others to learn from it.
If you think that others can learn something from this post, then please, upvote it. Thanks.

"""



# ===================================================

# [AUTHOR]: shadow_sm36
# [DESCRIPTION]: Easy Python Solution with Explanation

from collections import Counter
class Solution:
	def frequencySort(self, nums: List[int]) -> List[int]:
		d = Counter(nums)
		def check(x):
			return d[x]

		nums.sort(reverse=True)
		nums.sort(key=check)
		return nums


"""
o the basic idea is we use the Python's inbuilt sort function with a custom method which returns the frequency of that element in the array to sort. So, first we create a frequency array using the Python's Counter function (This returns a dictionary, the same could have been manually using a blank dictionary but since we can utilise the capabilities of Python, that is what we do here.)

and we create a new function which returns the frequency of that element in our array (The same could have been done easier with a lambda function as well, but this was my first instinct so I went with this)

Now, we reversed sorted the list first normally so that when sorting the second time using our custom sort, our answer comes out to be what we want, (decreasing order for elements with the same frequency)

Next we use our custom sort function which generates a frequency wise + decreasing order for same frequency elements. Our inbuilt custom sort is stable, meaning it won't change the relative order among elements.

Example:
In Stable Frequency Wise Sort:
[1,3,3,2,4] --> [1,2,4,3,3] (relative order of 1,2,4 is maintained)
In Unstable Frequency Wise Sort:
[1,3,3,2,4] --> [4,1,2,3,3] (relative order of 1,2,4 is not maintained)

Note: We can achieve this in one sort also by instead of returning a single key in our check function, we return a tuple of keys.

So that would make our check function something like:

"""

def check(x):
	return (d[x], -x)

"""

The purpose of -x is because in case of elements with the same frequency, we want them sorted in reverse sorted order.

Example: nums = [1,2,3,4]

So, for this list, the element:

1 --> (1, -1)
2 --> (1, -2)
3 --> (1, -3)
4 --> (1, -4)
element --> (frequency of element, -element)
So, first our list is sorted based on the first element, so since all are 1. Nothing happens. Next, we sort all the 1s based on the second element. So, -4 is the smallest so, that comes first, then -3 then -2 and lastly -1.

So the order becomes: (1, -4) , (1, -3), (1, -2), (1, -1) which means [4,3,2,1]. Which is what we wanted.

Please feel free to ask anything here, I will be happy to help/respond.

"""

# ===================================================

# [AUTHOR]: votrubac
# [DESCRIPTION]: C++/Python3 Sort by Count

"""
C++
Since the range of numbers is limited, and I am using array to collect count for the performance.

vector<int> frequencySort(vector<int>& nums) {
    int cnt[201] = {};
    for (auto n : nums)
        ++cnt[n + 100];
    sort(begin(nums), end(nums), [&](int a, int b) {
       return cnt[a + 100] == cnt[b + 100] ? a > b : cnt[a + 100] < cnt[b + 100];
    });
    return nums;
}
"""


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return sorted(nums, key = lambda n: (cnt[n], -n))

# ===================================================

# [AUTHOR]: rock
# [DESCRIPTION]: [java/Python 3] Sort frequency followed by value.

"""
public int[] frequencySort(int[] nums) {
    var freq = new HashMap<Integer, Integer>();
    for (int n : nums) {
        freq.put(n, 1 + freq.getOrDefault(n, 0));
    }
    var pq = new PriorityQueue<Integer>(Comparator.<Integer, Integer>comparing(i -> freq.get(i)).thenComparing(i -> -i));
    for (int n : nums) {
        pq.offer(n);
    }
    int[] ans = new int[nums.length];
    for (int i = 0; !pq.isEmpty(); ++i) {
        ans[i]= pq.poll();
    }
    return ans;
}
"""

def frequencySort(self, nums: List[int]) -> List[int]:
    freq = Counter(nums)
    return sorted(nums, key=lambda x : (freq[x], -x))


# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First NOT working solution

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mem = {}
        newArr = []
        maxFreq = 0
        maxInt = nums[0]
        
        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1
                
        for k, freq in mem.items():
            if freq > 1 and freq > maxFreq:
                newArr += [k] * freq
                maxFreq = freq
            
            if freq == 1 and k > maxInt:
                newArr = [k] + newArr
                maxInt = k
                
                
        return newArr

# [WORKING ON THE CODE]:
# To get a map of element frequency withing the array use Counter
from collections import Counter

# ... and instead of this code ...
def createFreqHashTable(nums):
	mem = {}
        
    for num in nums:
        if num in mem:
            mem[num] += 1
        else:
            mem[num] = 1

# ... start useing this ...
def createFreqHashTableWithCounter(nums):
	mem = Counter(nums)

# ===================================================

# [AUTHOR] Re-typed from author: denisrasulev
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mem = Counter(nums)
        return sorted(nums, key = lambda x: (mem[x], -x))

