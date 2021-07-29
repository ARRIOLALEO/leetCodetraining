class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        solution = []
        dictionary = {}
        for i in range(len(nums2)):
            greater = nums2[i]
            for j in range(i , len(nums2)):
                if greater < nums2[j]:
                    greater = nums2[j]
                    break
            if greater == nums2[i]:
                dictionary[nums2[i]] = -1
            else:
                dictionary[nums2[i]] = greater
        print(dictionary)
        for element in nums1:
            solution.append(dictionary[element])
            
        return solution
