class Solution:
    def __init__(self):
        self.solution =[]
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(index=0,arr=[]):
            parcial  = sum(arr)
            if parcial >= target:
                if parcial == target:
                    self.solution.append(arr.copy())
                return
            else:
                for i in range(index,len(candidates)):
                    arr.append(candidates[i])
                    backtracking(i,arr)
                    arr.pop()
        backtracking()
        return self.solution
