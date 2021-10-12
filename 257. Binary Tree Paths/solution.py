# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.solution = []
        
        def bfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                self.solution.append(path + str(node.val))
            bfs(node.left,(path)+str(node.val)+"->")
            bfs(node.right,(path)+str(node.val)+"->")
                
        bfs(root,"")
        
        return self.solution
        
