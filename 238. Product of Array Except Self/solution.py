class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        ans = [1] * s
        for n in range(1,s):
            ans[n] = ans[n-1] * nums[n-1]
        aux = 1
        print(ans)
        for i in range(s-2,-1,-1):
            aux =  aux * nums[i + 1] 
            ans[i] = ans[i] * aux
        return ans
        
