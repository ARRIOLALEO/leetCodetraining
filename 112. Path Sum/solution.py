# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.solution = False
        
        def bfs(node, sume):
            if not node:
                return
            if not node.left and not node.right:
                sume += node.val
                if sume == targetSum:
                    self.solution = True
            bfs(node.left,sume+node.val)
            bfs(node.right,sume+node.val)
        bfs(root, 0)
        return self.solution
