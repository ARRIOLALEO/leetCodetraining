class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictionary = {0:1}
        accumulator = 0
        how_many_sum_k = 0
        
        for element in nums:
            accumulator += element
            if accumulator - k in dictionary:
                how_many_sum_k += dictionary[accumulator - k]
            if accumulator not in dictionary:
                dictionary[accumulator] = 1
            else:
                dictionary[accumulator] += 1
        return how_many_sum_k
