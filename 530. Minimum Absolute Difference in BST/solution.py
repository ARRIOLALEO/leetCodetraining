# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.stack = []
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def bfs(root):
            if not root:
                return
            self.stack.append(root.val)
            if root.left is not None:
                bfs(root.left)
            
            if root.right:
                bfs(root.right)
                
        bfs(root)
        self.stack.sort()
        minimun = float("inf")
        for i in range(1,len(self.stack)):
            minimun = min(abs(self.stack[i-1] - self.stack[i]),minimun)
            
        return minimun
        
        
