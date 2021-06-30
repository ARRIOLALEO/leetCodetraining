class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) -1
        if target > nums[r]:
            return r + 1
        if target < nums[l]:
            return l
        
        while l <= r:
            middle = round( (l + r )/ 2)
            if nums[middle ] == target:
                return middle
            if nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
                
        return l
