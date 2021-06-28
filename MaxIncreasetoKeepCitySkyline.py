class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        solution = []
        for row in range(len(grid)):
            for col in range(len(grid)):
                building = grid[col][row]
                max_col = 0
                max_row = 0
                for n in range(len(grid)):
                    if max_row < grid[n][row]:
                        max_row = grid[n][row]
                    if max_col < grid[col][n]:
                        max_col = grid[col][n]
                max_build = max_col if max_col < max_row else max_row
                to_add = max_build - building if building < max_build else 0
                solution.append(to_add)
        return (sum(solution))

        
            
        
