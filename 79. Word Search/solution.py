class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        WL = len(word)
        path = set()
        def dfs(r,c,pos):
            if pos ==  WL:
                return True
            elif (
            r < 0 or c < 0
            or r >= ROWS or c >= COLS
            or word[pos] != board[r][c]
            or (r,c) in path
            ):
                return False
            path.add((r,c))
            res = (dfs(r+1, c, pos +1) or
                dfs(r-1, c, pos +1) or
                dfs(r, c+1, pos +1) or 
                dfs(r, c-1, pos +1))
            path.remove((r,c))
            return res
        
        
        for r in range(ROWS):
            for i in range(COLS):
                if dfs(r,i,0):
                    return True
        return False
