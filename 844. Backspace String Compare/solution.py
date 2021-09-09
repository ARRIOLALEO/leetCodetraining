class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def helper(l):
            stk =[]
            for i in l:
                if i != "#":
                    stk.append(i)
                else:
                    if len(stk) > 0:
                        stk.pop()
            return "".join(stk)
        e1 = helper(s)
        e2 = helper(t)
        
        return e1 == e2
        
