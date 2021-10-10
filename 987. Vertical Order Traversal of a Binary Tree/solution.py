# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary  = {}
        row = col =  0
        def bfs(node, row, col):
            if not node:
                return
            if col in dictionary:
                dictionary[col].append((row,node.val))
            else:
                dictionary[col] = [(row,node.val)]            
            if node.left is not None:
                bfs(node.left,row+1,col -1)
            if node.right:
                bfs(node.right,row+1,col+1)
        bfs(root,0,0)
        keys  = []
        for key in dictionary:
            keys.append(key)
        keys.sort()
        solution = []
        for key in keys:
            parcial = []
            dictionary[key].sort()
            for element in dictionary[key]:
                parcial.append(element[1])
            solution.append(parcial)
            
        return solution
                                       
