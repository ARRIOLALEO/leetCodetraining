class Solution(object):
    def __init__(self):
        self.arr = {}
        self.maxperlevel = []
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        def dfs(root,level):
            if not root:
                return 
            if level in self.arr:
                self.arr[level].append(root.val)
            else:
                self.arr[level] = [root.val]
            dfs(root.left,level+1)
            dfs(root.right,level+1)
            
        dfs(root,0)
        for i in self.arr:
            self.maxperlevel.append(max(self.arr[i]))
        return self.maxperlevel
