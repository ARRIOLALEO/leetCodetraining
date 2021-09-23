class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack =[]
        
        next_greater = {}
        
        for index, n in enumerate(nums1):
            ind = nums2.index(n)
            temp = nums2[ind:]
            for b in temp:
                if b > n:
                    next_greater[n] = b
                    break
            if not n in next_greater:
                next_greater[n]= -1
            
        for n in nums1:
            stack.append(next_greater[n])
            
        return stack
