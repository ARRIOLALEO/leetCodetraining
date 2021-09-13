class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        init = 1
        nums = sorted(set(nums))
        for element in nums:
            if element <= 0:
                pass
            elif element > init :
                return init
            else:
                init +=1
        return init
                
        
