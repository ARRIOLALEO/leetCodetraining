class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        temp  = []
        solution =[]
        for j in s:
            if j ==" ":
                if len(temp) > 0:
                    solution.append("".join(temp))
                    temp = []
            else:
                temp.append(j)
        if len(temp) >0:
            solution.append("".join(temp))
        solution  = reversed(solution)
        
        return (" ".join(solution))
