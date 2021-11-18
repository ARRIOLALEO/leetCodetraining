class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = len(board)
        rows = len(board[0])
        for col in range(cols):
            temp = {}
            for row in range(rows):
                if board[col][row] != ".":
                    if board[col][row]  in temp:
                        temp[board[col][row]] += 1
                        print(temp)
                        return False
                    else:
                        temp[board[col][row]] = 1
                        
                    
        
        for row in range(rows):
            temp = {}
            for col in range(cols):
                if board[col][row] != ".":
                    if board[col][row] not in temp:
                        temp[board[col][row]] = 1
                    else:
                        return False
                    
        for col in range(0,cols,3):
            for row in range(0,cols,3):
                temp = {}
                for tempcol in range(col,col+3):
                    for temprow in range(row,row+3):
                        if board[tempcol][temprow] != ".":
                            if board[tempcol][temprow] not in temp:
                                temp[board[tempcol][temprow]] = 1
                            else:
                                return False
  
        return True
