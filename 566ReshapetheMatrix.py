class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0:
            return mat
        
        flat_arr = []
        
        for i in range(len(mat)):
            flat_arr +=mat[i]
            
        if r == 1:
            return [flat_arr]
        solution =[]
        if len(flat_arr) == (r * c):
            for i in range(r):
                solution.append(flat_arr[0: c])
                for j in range(c):
                    flat_arr.pop(0)
        else:
            return mat
        return solution 
        
