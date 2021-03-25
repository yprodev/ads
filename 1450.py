

# ===================================================================================

# [AUTHOR]: user1811
# [DESCRIPTION]: Python - faster tan 97.86% less memory than 94%

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        len_start_time = len(startTime)
        busy_student = 0
        for i in range(0,len_start_time):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                busy_student+=1

        return busy_student

# ===================================================================================

# [AUTHOR]: leetcoder786786
# [DESCRIPTION]: Python Simple Stack Solution

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        stack = []
        
        for s in startTime:
            if s <= queryTime:
                stack.append(s)
        
        for e in endTime:
            if e < queryTime and stack:
                stack.pop()
                
        return len(stack)

# ===================================================================================

# [AUTHOR]: blue_sky5
# [DESCRIPTION]: Comment area of this topic - Python One-Liner

return sum(1 for s, e in zip(startTime, endTime) if s<= queryTime <= e)



# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	Could be more simpler code

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        numStudent = len(startTime)
        student = 0
        res = 0

        while student < numStudent:
            if queryTime >= startTime[student] and queryTime <= endTime[student]:
                res += 1
                
            student += 1
            
        return res

