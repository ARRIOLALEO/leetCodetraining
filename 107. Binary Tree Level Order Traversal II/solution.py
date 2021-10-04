# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dc ={}
        def helper(root,level):
            if not root:
                return
            
            if root.left is not None:
                helper(root.left, level+1)
                
            if level in dc:
                dc[level] +=[root.val]
            else:
                dc[level] = [root.val]
                
            if root.right:
                helper(root.right,level+1)
        
        helper(root,0)# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dc ={}
        def helper(root,level):
            if not root:
                return
            
            if root.left is not None:
                helper(root.left, level+1)
                
            if level in dc:
                dc[level] +=[root.val]
            else:
                dc[level] = [root.val]
                
            if root.right:
                helper(root.right,level+1)
        
        helper(root,0)
        
        solution = []
        
        while dc:
            last_item = dc.keys()[-1]
            solution.append(dc[last_item])
            del dc[last_item]
            
        return solution
        
        solution = []
        
        while dc:
            last_item = dc.keys()[-1]
            solution.append(dc[last_item])
            del dc[last_item]
            
        return solution
