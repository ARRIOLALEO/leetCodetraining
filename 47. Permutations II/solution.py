class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        solution =[]
        used = {}
        
        if len(nums) == 1:
            return [nums]
        else:
            for index , element in enumerate(nums):
                for rest in self.permuteUnique(nums[:index] + nums[index+1:]):
                    x = [element] + rest
                    hs = [str(s) for s in x]
                    hs = "".join(hs)
                    if hs not in used:
                        used[hs] = 1
                        solution.append(x)
        return solution
        
