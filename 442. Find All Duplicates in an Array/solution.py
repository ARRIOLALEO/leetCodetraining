class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dc = {}
        
        for n in nums:
            if n in dc:
                dc[n] +=1
            else:
                dc[n] = 1
        ad = []
        for n in dc:
            if dc[n] > 1 :
                ad.append(n)
                
        return ad
