# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.levels = {}
        
    def deepestLeavesSum(self, root,level = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(node,level):
            if not node:
                return
            if level in self.levels:
                self.levels[level] += [node.val]
            else:
                self.levels[level] = [node.val]
            
            preorder(node.left,level+1)
            preorder(node.right,level+1)
            
        preorder(root,level)
        
        level_max =0 
        
        for n in self.levels:
            level_max = n
        
        return sum(self.levels[level_max])
