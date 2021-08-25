class Solution:
    def sortColors(self, nums: List[int],position = 0) -> None:
        if len(nums) < 2:
            return nums
        
        ds= [0] * 3
        
        for i in nums:
            ds[i] += 1
            
        pointer = 0
        for i in range(len(ds)):
            for j in range(ds[i]):
                nums[pointer] =  i
                pointer +=1
