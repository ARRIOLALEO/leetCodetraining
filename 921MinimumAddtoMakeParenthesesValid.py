class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []  
        for p in s:
            if p == "(":
                stack.append(p)
            else:
                tail = stack[-1] if len(stack) > 0 else ""
                if tail == "(":
                    stack.pop(-1)
                else:
                    stack.append(p)
        return len(stack)
        
