class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        myArray = []
        for i in range(len(nums)):
            sum += nums[i]
            myArray.append(sum)
        return myArray
