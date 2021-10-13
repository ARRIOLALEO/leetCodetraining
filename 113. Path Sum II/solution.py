# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.solution= []
        
        def bfs(node,path,targetSum):
            if not node:
                return
            
            path.append(node.val)
            
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    deep_copy = [x for x in path]
                    self.solution.append(deep_copy)
                    
            bfs(node.left,path,targetSum)
            bfs(node.right,path,targetSum)
            
            del path[-1]
        
        bfs(root,[],targetSum)
        
        return self.solution
        
        
            
        
