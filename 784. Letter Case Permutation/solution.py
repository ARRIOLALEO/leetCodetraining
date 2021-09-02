class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        size = len(s)
        result = [s.lower()]
        for i in range((size - 1), -1 , -1):
            if s[i].isalpha():
                temp =[]
                for e in result:
                    temp.append(e)
                    left = list(e)
                    left[i] = left[i].upper()
                    temp.append("".join(left))
                result = temp
        return result
