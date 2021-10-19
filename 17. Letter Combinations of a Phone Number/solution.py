class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dc = {"2":"abc",
              "3":"def",
              "4":"ghi",
              "5":"jkl",
              "6":"mno",
              "7":"pqrs",
              "8":"tuv",
              "9":"wxyz"
             }
        
        if len(digits) == 0:
            return []
        solution = []
        strlen = len(digits)
        def backtracking(current, start):
            if len(current) == strlen:
                solution.append("".join(current))
                return
            phoneLeter = dc[digits[start]]
            for n in range(len(phoneLeter)):
                current.append(phoneLeter[n])
                backtracking(current,start+1)
                current.pop()
        backtracking([],0)
        return solution
        
