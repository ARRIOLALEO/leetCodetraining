class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # this is the matrix creattion
        paths= [[1] * n] *  m
        cols = len(paths) 
        rows = len(paths[0])
        for col in range(1,cols):
            for row in range(1,rows): 
                paths[col][row] = paths[col-1][row] + paths[col][row-1]
        return paths[cols-1][rows-1]
        
