class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lo, hig = 0 , len(s)
        solution = []
        for l in s:
            if l == 'I':
                solution.append(lo)
                lo +=1
            else:
                solution.append(hig)
                hig -= 1
        return solution + [lo]
