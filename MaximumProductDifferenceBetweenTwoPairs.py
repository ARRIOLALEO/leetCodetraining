class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        end_list = len(nums) - 1
        min_price_pair = nums[0] * nums[1]
        max_price_pair = nums[end_list] * nums[end_list -1]
        return max_price_pair - min_price_pair
