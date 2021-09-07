class Solution:
    def __init__(self):
        self.solution = []
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtracking(index = 1 ,arr =[]):
            tsume = sum(arr)
            if(tsume >= n):
                if tsume == n and len(arr) == k:
                    self.solution.append(arr.copy())
                return
            else:
                for i in range(index , 10):
                    arr.append(i)
                    backtracking(i+1,arr)
                    arr.pop()
        backtracking()
        return self.solution
