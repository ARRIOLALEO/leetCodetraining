class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_st(subString):
            subString = subString[::-1]
            return subString
        
        if k < 2:
            return s
        solution = ""
        start, end = 0, len(s)
        while start + k <  end:
            if (end - start) >= ( k * 2 ):
                solution+= reverse_st(s[start : start + k]) + s[start + k : start + k + k]
                start += ( k + k)
            if (end - start ) < (k * 2) and (end - start) > k:
                solution += reverse_st(s[start: start + k])  + s[start + k : len(s) ]
                start += end
            if (end  - start) == k:
                solution += reverse_st(s[start:start + k])
                start = start + k
                
        if solution == "":
           solution = s[::-1]
           return solution
        if start < end:
            solution += reverse_st(s[start:len(s)])
        return solution
