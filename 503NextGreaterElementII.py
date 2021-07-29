class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        solution = []
        for i in range(len(nums)):
            greater = nums[i]
            for j in range(i , len(nums)):
                if nums[j] > greater:
                    greater = nums[j]
                    break
            if greater == nums[i]:
                for j in range(0,i,1):
                    if nums[j] > greater:
                        greater = nums[j]
                        break
            if greater != nums[i]:
                solution.append(greater)
            else:
                solution.append(-1)
        return solution
        
