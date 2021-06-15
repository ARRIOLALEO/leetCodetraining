class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        if(nums[0] == 0):
            zeroes += 1
        for num in range(1,len(nums)):
            if(nums[num] != 0):
                [nums[num - zeroes],nums[num]] = [nums[num],nums[num - zeroes]]
            else:
                zeroes += 1
