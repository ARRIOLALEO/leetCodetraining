class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dc ={}
        for index, i in enumerate(numbers):
            missing = target - i
            if missing in dc:
                return [dc[missing],index+1]
            dc[i] = index + 1
        
                
            
