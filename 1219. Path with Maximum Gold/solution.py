class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        path = set()
        self.max_gold = 0
        def backtracking(row,col,temp):
            if (row < 0 or col < 0 or
               row >= len_row or col >= len_col or
               (row,col) in path or
               grid[row][col] == 0):
                self.max_gold = max(self.max_gold, temp)
                return 
            path.add((row,col))
            temp += grid[row][col]
            backtracking(row+1,col,temp)
            backtracking(row-1,col,temp)
            backtracking(row,col+1,temp)
            backtracking(row,col-1,temp)
            path.remove((row,col))
            return
        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] != 0:
                    backtracking(row,col,0)
        return self.max_gold
        
