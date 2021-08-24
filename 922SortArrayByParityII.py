class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd =[]
        even =[]
        
        for n in nums:
            if n % 2 == 1:
                odd.append(n)
            else:
                even.append(n)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop(0)
            else:
                nums[i] = odd.pop(0)
        return nums922. Sort Array By Parity II
