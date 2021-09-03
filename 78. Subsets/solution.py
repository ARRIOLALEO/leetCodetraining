class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = [[]]
        WIDTH = len(nums)
        
        for num in nums:
            solution += [cur + [num] for cur in solution]
        return solution
                
                
        
        
