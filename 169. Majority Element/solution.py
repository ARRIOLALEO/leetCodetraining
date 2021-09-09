class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dc ={}
        for num in nums:
            if num in dc:
                dc[num] +=1
            else:
                dc[num] = 1
        
        max_element =  0
        solution = 0
        
        for n in dc:
            r = dc[n]
            if r > max_element:
                max_element = dc[n]
                solution = n
        return solution
