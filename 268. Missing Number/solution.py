class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        parcial = []
        max_len = len(nums)
        for i in range(max_len+1):
            parcial.append(i)
        return (sum(parcial) - sum(nums))
        
