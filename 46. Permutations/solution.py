class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        
        if len(nums) == 1:
            return [nums]
        else:
            for index , value in enumerate(nums):
                for rest in self.permute(nums[:index] + nums[index+1:]):
                    x = [value] + rest
                    solution.append(x)
        return solution
            
