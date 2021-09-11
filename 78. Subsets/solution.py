class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = [[]]
        WIDTH = len(nums)
        
        for num in nums:
            solution += [cur + [num] for cur in solution]
        return solution
                
                
class Solution(object):
    def __init__(self):
        self.solution =[]
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # def of backtracking function it is needed to know is helper arr is
        #size of the required arr
        def backtracking(start=0,helper =[]):
        # eg is needed arr 0 is len(arr) == 0 append it to the solution
            if len(helper) == k:
                self.solution.append(helper[:])
                return
            else:
                for i in range(start,s):
                    #add the number to the helper arr
                    helper.append(nums[i])
                    # move one step fron
                    backtracking(i+1,helper)
                    # no duplicate remove the number used
                    helper.pop()
        s = len(nums)
        ##+1 becuase i need an empty arr
        for k in range(s+1):
            # calling backtrack and k is the leng of the sub array needed
            backtracking()
        #return solution
        return self.solution
                
        
        
