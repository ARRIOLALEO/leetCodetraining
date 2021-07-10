class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 120
                counter -=1
        nums.sort()
        for j in range(len(nums)):
            if nums[j] == 120:
                nums[j] = "_"
        return counter 
