class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_arr = len(nums)
        dp = [1] * len_arr
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < (dp[j] + 1):
                        dp[i] = dp[j] + 1
        max_sub_arr = 1
        for sa in range(len(dp)):
            max_sub_arr = max(max_sub_arr,dp[sa])
        return max_sub_arr
            
