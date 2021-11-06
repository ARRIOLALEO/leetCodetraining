class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        solution = []
        for col in range(len(grid)):
            temp = []
            for row in range(len(grid[0])):
                if grid[col][row] == 1:
                    temp.append("0")
                else:
                    temp.append("1")
            if int("".join([str(i) for i in grid[col]])) > int("".join(temp)):
                solution.append(grid[col])
            else:
                solution.append(temp)
                
        for row in range(len(grid[0])):
            temp1 = []
            temp2 = []
            for col in range(len(grid)):
                temp1.append(str(solution[col][row]))
                if int(solution[col][row])== 0:
                    temp2.append("1")
                else:
                    temp2.append("0")
            to_append = []
            t1 = 0
            t2 = 0
            for e in temp1:
                if e == "1":
                    t1 +=1
            for e in temp2:
                if e == "1":
                    t2 +=1
            if t1 > t2:
                to_append = temp1
            else:
                to_append = temp2 
            for n in range(len(solution)):
                solution[n][row] = to_append[n]
        max_solution = 0
        for n in range(len(solution)):
            max_solution += int("".join(solution[n]),2)
        return max_solution
                    
