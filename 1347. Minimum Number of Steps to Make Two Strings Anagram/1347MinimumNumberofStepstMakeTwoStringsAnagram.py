class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 ={}
        for i in s:
            if i in d1:
                d1[i] +=1
            else:
                d1[i] = 1
        for i in t:
            if i in d1:
                d1[i] -= 1
                if not d1[i]:
                    del d1[i]
        missing = 0
        for i in d1:
            missing += d1[i]
        return missing
            
