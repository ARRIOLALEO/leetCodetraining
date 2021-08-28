class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        
        remotions = 0
        for  i , num in enumerate(nums):
            if num in dic:
                dic[num] += 1
                if dic[num] > 2:
                    nums[i] = float("inf")
                    remotions +=1
            else:
                dic[num] = 1
        nums.sort()
        return (len(nums) - remotions)
