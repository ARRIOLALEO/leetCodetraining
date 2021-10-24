class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for n in nums:
            if n in dictionary:
                dictionary[n] += 1
            else:
                dictionary[n] =1
                
        for n in dictionary:
            if dictionary[n] < 3:
                return n
            
        
