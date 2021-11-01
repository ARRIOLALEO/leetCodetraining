class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(nums,left,right,turn):
            if left == right:
                return turn * nums[left]
            a = turn * nums[left] + winner(nums,left+1,right, -turn )
            b = turn * nums[right] + winner(nums,left,right-1, -turn )
            return turn * max(turn * a , turn * b)
        
        return winner (nums, 0 ,len(nums)-1,1) >=0
    
