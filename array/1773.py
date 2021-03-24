# [AUTHOR]: darkTianTian
# [DESCRIPTION]: Withing comment for this - "[Python3] 1-line"

def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    return sum((ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)) for t, c, n in items)

# ===================================================================================

# [AUTHOR]: idontknoooo
# [DESCRIPTION]: Python 3 | 2-liner | Explanation

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for item in items if item[d[ruleKey]] == ruleValue)

# ===================================================================================

# [AUTHOR]: Chandreshwar
# [DESCRIPTION]: [Python] Easy Solution

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dct = {"type": 0, "color": 1, "name": 2}
        key = dct[ruleKey]
        res = 0
        for item in items:
            if item[key] == ruleValue:
                res += 1
        return res

# ===================================================================================

# [AUTHOR]: diogodutra
# [DESCRIPTION]: Python 100% faster, 2 lines

"""
First get the index ruleIndex of the ruleKey corresponding to the column of items.
Then, extract the list out of this column ([item[ruleIndex] for item in items]), compare each element of it with ruleValue and sum the resulting list of booleans.
"""

ruleIndex = ['type', 'color', 'name'].index(ruleKey)
return sum(map(lambda x: x == ruleValue, [item[ruleIndex] for item in items]))

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        def getRuleNumber (ruleKey: str):
            if ruleKey == "type":
                return 0
            elif ruleKey == "color":
                return 1
            elif ruleKey == "name":
                return 2
            else:
                raise "There is no such key"

        result = 0

        for i, item in enumerate(items):
            rKey = getRuleNumber(ruleKey)

            if item[rKey] == ruleValue:
                result += 1

        return result
