class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        response = sum(nums[:3])
        for l in range(len(nums)):
            c , r = l + 1 , len(nums) - 1
            while c < r :
                parcial = sum((nums[l], nums[c], nums[r]))
                if abs(parcial - target )< abs(response - target):
                    response = parcial
                if parcial < target:
                    c += 1
                elif parcial > target:
                    r -=1
                else:
                    return response
        return response
        

// Photo by Paul Earle on Unsplash
