# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dc = {}
        
        def dfs(node,level):
            if not node:
                return 
            if node.left is not None:
                dfs(node.left, level +1)
            if level in dc:
                dc[level] += [node.val]
            else:
                dc[level] = [node.val]
            if node.right:
                dfs(node.right,level+1)
                
        
        solution = [-1,float("-inf")]
        dfs(root,1)
        
        for n in dc:
            parcial = sum(dc[n])
            if parcial > solution[1]:
                solution[0] = n
                solution[1] = parcial
                
        return solution[0]
