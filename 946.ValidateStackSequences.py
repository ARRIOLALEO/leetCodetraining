class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        for element in pushed:
            stack.append(element)
            while len(stack) > 0 and len(popped) > 0 and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
                                
        if len(stack) == 0:
            return True
        
