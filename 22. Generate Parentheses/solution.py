class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        response = []
        def backtrack(s=[],left =0 , right = 0):
            if len(s) == 2 * n:
                response.append("".join(s))
                return
            if left < n:
                s.append("(")
                backtrack(s,left+1,right)
                s.pop()
            if right < left:
                s.append(")")
                backtrack(s,left, right + 1)
                s.pop()
        backtrack()
        return response
