class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) -1
        if nums[right] > nums[0]:
            return nums[0]
        
        while left < right:
            center = left + (right- left) /2
            
            if nums[center] > nums[center+1]:
                return nums[center +1]
            if nums[center-1] > nums[center]:
                return nums[center]
            
            if nums[center] > nums[0]:
                left = center +1
            else:
                right = center -1
                
            
                
                
                
        
