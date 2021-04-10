# [AUTHOR] brianchiang_tw
# [DESCRIPTION] Several Python solution. [w/ Explanation]
"""
Explanation:

This is a classical question about occurrence counting and element-set relationship.

It can be solved by two kinds of viewpoints.

Method_#1:
Iterate on stones, check if current stone is also a jewel, and accumulate the counter if it is.

Method_#2:
Iterate on jewels, accumulate the occurrence of corresponding jewel in stone.
"""
# Implementation_1-a: Traditional loop, like what we do in other high-level languages, such as C++/Java/Go/Scala
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewels = set(J)
        count_of_jewel = 0
        
        for item in S:
            if item in jewels:
                count_of_jewel += 1

        return count_of_jewel

# Implementation_1-b: With the same concept, rewrite in generator expression in Python
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel = set(J)
        return sum( 1 for item in S if item in jewel )

# Implementation_1-c: With the same concept, rewrite in list comprehension in Python
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel = set(J)
        return sum( [1 for item in S if item in jewel ] )

# Implementation_2-a: Traditional loop, like what we do in other high-level languages, such as C++/Java/Go/Scala
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count_of_jewels = 0

        for j in J:
            count_of_jewels += S.count(j)

        return count_of_jewels

# Implementation_2-b: With the same concept, rewrite in generator expression in Python
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        return sum( S.count(jewel) for jewel in J )


# Implementation_2-c: With the same concept, rewrite in list comprehension in Python
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        return sum( [ S.count(jewel) for jewel in J ] )


# ===================================================================================

# [AUTHOR] ZitaoWang
# [DESCRIPTION] Python solution
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(J)
        return len(list(filter(lambda x: x in jewels, list(S))))

# ===================================================================================
# [AUTHOR] RogerFederer
# [DESCRIPTION] Python solution
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = collections.Counter(S)
        count = 0
        for ch in J:
            count += counter[ch]
        return count
# ===================================================================================
# [AUTHOR] Sidzy
# [DESCRIPTION] Python Beats 99.82%
class Solution(object):
    
    def _1_numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        uses hashmap internally
        
        20 ms, faster than 99.82% of Python online submission
        11.7 MB, less than 5.25% of Python online submissions 
        """
        num_jewels = 0
        for stone in S:
            if stone in J:
                num_jewels += 1
        
        return num_jewels
        
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        does not use hash map
        Runtime: 36 ms, faster than 7.51% of Python online submissions for Jewels and Stones.
        Memory Usage: 11.8 MB, less than 5.25% of Python online submissions for Jewels and Stones.
        """
        
        sorted_j = sorted(J)
        sorted_s = sorted(S)
        num_jewels = 0
        index_j, index_s = 0, 0
        while index_j < len(sorted_j) and index_s < len(sorted_s):
            if sorted_j[index_j] == sorted_s[index_s]:
                num_jewels += 1
            
            if ord(sorted_j[index_j]) < ord(sorted_s[index_s]):
                index_j += 1
            else:
                index_s += 1
            
            if index_s >= len(sorted_s):
                break    
        return num_jewels

# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
"""
	1. Basic knowledge of Python3
	2. Issue with understading how to use stored information. Looks like we don't need
	the hash table.
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        journal = dict()
        
        for stone in stones:
            if stone in jewels:
                if stone in journal:
                    journal[stone] = journal[stone] + 1
                else:
                    journal[stone] = 1
               
                    
        return sum(journal.values())


# [AUTHOR] ME
# [DESCRIPTION] Second working solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        for stone in stones:
            if stone in jewels:
               counter += 1 
               
        return counter