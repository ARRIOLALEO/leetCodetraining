# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dc = {}
        
        def dfs(node,level):
            if not node:
                return
            if node.left is not None:
                dfs(node.left,level + 1)
            if level in dc:
                if level % 2 == 0:
                    dc[level] += [node.val]
                else:
                    dc[level] = [node.val] + dc[level]
            else:
                dc[level] = [node.val]
            if node.right:
                dfs(node.right, level +1)
        dfs(root,0)
        solution = []
        
        for n in dc:
            solution.append(dc[n])

        return solution
