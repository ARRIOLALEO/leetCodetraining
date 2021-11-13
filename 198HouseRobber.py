class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        if len(nums) < 4:
            if (nums[0] + nums[2]) > nums[1]:
                return(nums[0] + nums[2])
            else:
                return nums[1]
        max_robery = [0] * len(nums)
        max_robery[0] = nums[0]
        max_robery[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            max_robery[i] = max(max_robery[i-1], nums[i] + max_robery[i-2])
        return max_robery[-1]
            

#cleaner solution

    def rob(self, nums: List[int]) -> int:
        number_of_houses = len(nums)
        if number_of_houses == 1:
            return nums[0]
        if number_of_houses == 2:
            return max(nums[0],nums[1])
        
        max_robbery = [nums[0],max(nums[0],nums[1])]
        
        for house in range(2,number_of_houses):
            max_robbery.append(max(max_robbery[house-2]+nums[house],max_robbery[-1]))
                              
        return max(max_robbery[-1],max_robbery[-2])

