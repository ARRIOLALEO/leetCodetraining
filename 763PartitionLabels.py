class Solution:
    def printVertically(self, s: str) -> List[str]:
        solution = []
        s = s.split(" ")
        lena= [str(l) for l in s]
        lena = sorted(lena , key=len)
        max_len = len(lena[-1])
        for chrt in range(max_len):
            parcial = ""
            for i in range(len(s)):
                try:
                    s[i][chrt]
                    parcial += s[i][chrt]
                except:
                    parcial += " "
            solution.append(parcial.rstrip())
        return solution
