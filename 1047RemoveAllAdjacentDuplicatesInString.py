class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[""]
        for char in s:
            if char == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(char)
        stack.pop(0)
        return "".join(stack)
