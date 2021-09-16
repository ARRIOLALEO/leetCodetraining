class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dc = {}
        for n in nums:
            if n in dc:
                dc[n] += 1
            else:
                dc[n] = 1
        dc = sorted(dc.items())
        solution = []
        dc.sort(key=lambda tup:tup[1])
        for i in range(k):
            x = dc.pop(-1)
            solution.append(x[0])
     
        return solution
  
