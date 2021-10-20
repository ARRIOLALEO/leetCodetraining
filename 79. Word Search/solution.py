class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len_matrix = len(board)
        col_len_matrix = len(board[0])
        len_word = len(word)
        #using to not repeat the path
        path = set()
        
        def backtracking(col,row,position_word):
            if position_word == len_word:
                return True
            # i need to check is im out the matrix col or row are or less then 0
            # or they are same or bigger than the real matrix size
            # also is i alredy visited the path 
            # and is my actual position is dosent match with the word position
            elif(
                row < 0 or col < 0
                or row >= row_len_matrix or col >= col_len_matrix
                or word[position_word] != board[row][col]
                or (row,col) in path
            ):
                return False
            path.add((row))
            # here i will check my 4 options up dow left and right if one is true i will continue
            # here im repeting this option till i my function find true or false all the options
            #also is needed to move one more in my search of the word
            response = (backtracking(row,col + 1, position_word + 1) or
                       backtracking(row, col - 1, position_word + 1) or
                       backtracking(row - 1, col, position_word + 1) or 
                       backtracking(row + 1, col, position_word + 1))
            # i remove the position of search that it was my pivot to start a new search
            path.remove((col,row))
            
            return response
        for row in range(row_len_matrix):
            for col in range(col_len_matrix):
                if backtracking(row,col,0):
                    return True
        return False
                        
