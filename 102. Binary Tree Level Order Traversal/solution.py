# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dc = {}
        def helper(root,level):
            if not root:
                return
            if root.left is not None:
                helper(root.left,level+1)
            
            if level in dc:
                dc[level] += [root.val]
            else:
                dc[level] = [root.val]
            
            if root.right:
                helper(root.right,level +1)
        
        helper(root,0)
        
        solution = []
        
        while dc:
            first_key = dc.keys()[0]
            solution.append(dc[first_key])
            del dc[first_key]
            
        return solution
