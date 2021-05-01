# [AUTHOR]: ryancll
# [DESCRIPTION]: Python Solution - Easy to Understand

# [NOTE]: With the improvement from the comment from
# duobaohuabei

def commonChars(self,A):
        check = list(A[0])
        for word in A[1:]: # Improvement from the comment
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check

# ===================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: Python 1 Line

def commonChars(self, A):
    res = collections.Counter(A[0])
    for a in A:
        res &= collections.Counter(a)
    return list(res.elements())

# 1-line version

def commonChars(self, A):
    return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())

# ===================================================

# [AUTHOR]: orang3
# [DESCRIPTION]: [Python3] Simple And Readable Solution

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        arr = []
        for i in set(A[0]):
            ans = [A[0].count(i)]
            for j in A[1:]:
                if(i in j):
                    ans.append(j.count(i))
            if(len(ans) == len(A)):
                arr += ([i] * min(ans))
        return arr


# ===================================================

# [AUTHOR]: sagarbarapatre
# [DESCRIPTION]: C++ simple and sweet

"""
Runtime: 8 ms, faster than 99.08% of C++ online submissions for Find Common Characters.
Memory Usage: 8.9 MB, less than 96.95% of C++ online submissions for Find Common Characters.


class Solution {
public:
	vector<string> commonChars(vector<string>& arr) {
	   vector<int> hash1(26, 0);
		vector<int> hash2(26, 0);

		for(auto ch : arr[0])
		{
			hash1[ch - 'a']++;
		}

		for(int i = 1; i < arr.size() ; i++)
		{
			for(auto ch : arr[i])
			{
				hash2[ch-'a']++;
			}

			for(int i = 0 ; i < 26 ; i++)
			{
				hash1[i] = min(hash1[i], hash2[i]);
				hash2[i] = 0;
			}

		}




		vector<string> ans;
		for(int i = 0 ; i < 26 ; i++)

			if(hash1[i] > 0)
			{
				int count = hash1[i];
				while(count--)
				{
					char x = i+ 'a';
					string s ;
					s = x;
					ans.push_back(s);

				}
			}

		return ans;
	}


"""
# ===================================================

# [AUTHOR]: votrubac
# [DESCRIPTION]: C++ O(n) | O(1), two vectors

"""
For each string, we count characters in cnt1. Then, we track the minimum count for each character in cnt.

vector<string> commonChars(vector<string>& A) {
  vector<int> cnt(26, INT_MAX);
  vector<string> res;
  for (auto s : A) {
    vector<int> cnt1(26, 0);
    for (auto c : s) ++cnt1[c - 'a'];
    for (auto i = 0; i < 26; ++i) cnt[i] = min(cnt[i], cnt1[i]);
  }
  for (auto i = 0; i < 26; ++i)
    for (auto j = 0; j < cnt[i]; ++j) res.push_back(string(1, i + 'a'));
  return res;
}

Complexity Analysis
Runtime: O(n), where n is the total number of characters.
Memory: O(1) (we use two fixed-size vectors).
"""

# ===================================================

# [AUTHOR] ME
# [DESCRIPTION] NOT WORKING solution
# Issues:
"""
The first idea was to split only one word to have the full list of characters as possibles occurences in the all other strings. However, it looked even more complex solution.

The second idea was to split each word by character, save those arrays into a hash map. After cut off the similar sub arrays. In case each record in the hash table has the similar mininum sub-array.

Don't know how to find sub-arrays and compare them in Python.

"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        mem = {}
        sPtr = 0
        
        for word in A:
            mem[word] = sorted(word)
            
            
        for idx, key in enumerate(mem.keys()):
            print(idx, mem[key])



# [AUTHOR] Copied solution from ryancll
# [DESCRIPTION] WORKING solution
# Issues:
#   - Hard to remember how to solve algorithms after some pause

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        firstWordChecker = list(A[0])
        
        for word in A[1:]:
            answers = []
            
            for c in word:
                if c in firstWordChecker:
                    answers.append(c)
                    firstWordChecker.remove(c)
                    
            
            firstWordChecker = answers
            
        return firstWordChecker