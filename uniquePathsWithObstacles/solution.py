class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        cols = len(obstacleGrid)
        rows =  len(obstacleGrid[0])
        
        #filling firs collumn
        for n in range(1,cols):
            obstacleGrid[n][0]= int(obstacleGrid[n][0] == 0 and obstacleGrid[n-1][0] == 1 )
        
        #filling first row
        for m in range(1,rows):
            obstacleGrid[0][m] = int(obstacleGrid[0][m] == 0 and obstacleGrid[0][m-1] == 1)
            
                    
        for col in range(1,cols):
            for row in range(1,rows):
                if obstacleGrid[col][row] == 0:
                    obstacleGrid[col][row] = obstacleGrid[col -1][row] + obstacleGrid[col][row -1] 
                else:
                    obstacleGrid[col][row] = 0
        return obstacleGrid[cols-1][rows-1]
