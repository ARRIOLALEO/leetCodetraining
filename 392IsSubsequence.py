class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        position = 0
    
        for char in t:
            if s[position] == char:
                position +=1
            if position == len(s):
                break
        
        if position == len(s):
            return True
        
        return False
            
