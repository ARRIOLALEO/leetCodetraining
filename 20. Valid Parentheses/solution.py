class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dc = {"}":"{",")":"(","]":"["}
        
        for p in s:
            if p in dc:
                if stack and stack[-1] == dc[p]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(p)
                
        return not stack
                    

                
