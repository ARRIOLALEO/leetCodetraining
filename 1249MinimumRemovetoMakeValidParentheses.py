class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        solution  =[]
        counter = 0
        closed = 0
        for char in s:
            if char == ")" and counter > 0:
                counter -= 1
                solution.append(char)
            elif char == ")":
                continue
            elif char == "(":
                counter +=1
                solution.append(char)
            else:
                solution.append(char)
        rever = ""
        iv = 0
    
        for i in range(len(solution) -1 , -1 , -1):
            temp = solution[i]
            if solution[i] == "(" and iv > 0:
                iv -=1
                rever = temp + rever
            elif solution[i] == "(":
                continue
            elif solution[i] == ")":
                rever = temp + rever
                iv += 1
            else:
                rever = temp + rever
                
        return rever
            
        
