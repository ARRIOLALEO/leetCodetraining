class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        self.backtracking(candidates,[],solution,target)
        return solution
    def backtracking(self,candidates,currNow,solution,target):
        if target <= 0:
            if target == 0:
                currNow.sort()
                if currNow not in solution:
                    solution.append(currNow)
            return
        for i in range(len(candidates)):
            self.backtracking(candidates[:i] + candidates[i:],currNow + [candidates[i]],solution,target - candidates[i])
