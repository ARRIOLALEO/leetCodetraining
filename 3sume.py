class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        dictionary = set()
        
        for i in range(len(nums) -1 , -1 , -1):
            lastElement = nums[i]
            first = 0
            last = i -1
            while first < last:
                sume = lastElement + nums[first] + nums[last]
                if sume == 0:
                    if(lastElement, nums[first], nums[last]) not in dictionary:
                        solution.append([lastElement, nums[first], nums[last]])
                    else:
                        pass
                    dictionary.add((lastElement,nums[first],nums[last]))
                    first +=1
                elif sume > 0:
                    last -=1
                else:
                    first += 1
        return solution
