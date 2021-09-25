# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.solution = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
      
        def helper(self,node):
            if not node:
                return
            helper(self,node.left)
            self.solution.append(node.val)
            helper(self,node.right)
            
        helper(self,root)
        return self.solution
