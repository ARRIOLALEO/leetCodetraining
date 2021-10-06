# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dc = {}
        
        def fbs(node,level):
            if not node:
                return
            if node.left is not None:
                fbs(node.left,level+1)
            dc[level] = node.val
            if node.right:
                fbs(node.right,level+1)
        fbs(root,0)
        
        solution = []
        for n in dc:
            solution.append(dc[n])
        return solution
