class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        solution =[0]
        
        for element in s:
            if element == "(":
                solution.append(0)
            else:
                core = solution.pop()
                base = solution.pop()
                
                solution.append(base + max(core * 2 , 1))
        
        return solution.pop()
        
