class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        
        prev = ""
        
        s = [i for i in s]
        if s[0] == "R":
            prev = s.pop(0)
            ls = 0
            rs = 1
        else:
            ls = 1
            rs = 0
            prev = s.pop(0)
            
        
        for i in range(len(s)):
            if s[i] == "R":
                rs +=1
                prev = prev + s[i]
                if rs == ls:
                    stack.insert(0,prev)
                    prev = ""
                    rs = 0
                    ls = 0
            else:
                ls += 1
                prev = prev + s[i]
                if rs == ls:
                    stack.insert(0,prev)
                    prev = ""
        return len(stack)
