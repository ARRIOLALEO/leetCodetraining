class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dc = {}
        for l in s:
            if l in dc:
                dc[l] +=1
            else:
                dc[l] =1
                
        for l in t:
            if l not in dc:
                return l
            else:
                dc[l] -=1
                if not dc[l]:
                    del dc[l]
        return False
