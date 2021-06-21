class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        myStack = []
        for p in range(len(s)):
            index = s[p]
            if index == "(":
                myStack.append(index)
            else:
                if myStack and myStack[-1] == "(":
                    myStack.pop(-1)
                else:
                    myStack.append(index)
        return len(myStack)
