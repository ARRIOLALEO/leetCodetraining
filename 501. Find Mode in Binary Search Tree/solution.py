# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hash_map = {}
        
        def helper(node):
            if not node:
                return
            if node.left:
                helper(node.left)
            if node.val in hash_map:
                hash_map[node.val] += 1
            else:
                hash_map[node.val] = 1
            if node.right:
                helper(node.right)
        helper(root)
        max_r = float("-inf")
        
        for n in hash_map:
            max_r = max(max_r,hash_map[n])
            
        result = []
        for n in hash_map:
            if hash_map[n] == max_r:
                result.append(n)
                
        return result
