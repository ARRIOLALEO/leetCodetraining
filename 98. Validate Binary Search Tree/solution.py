# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.bst = [float("-inf")]
        self.solution = True
        def bfs(node):
            if not node:
                return 
            if node.left is not None:
                bfs(node.left)
            if node.val <= self.bst[-1]:
                self.solution = False
                return 
            self.bst.append(node.val)  
            if node.right:
                bfs(node.right)
        bfs(root)
        return self.solution
