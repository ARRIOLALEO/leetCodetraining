# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def createlist(nodes):
            if not nodes:
                return
            self.arr.append(nodes.val)
            createlist(nodes.left)
            createlist(nodes.right)
        createlist(root)
        self.arr.sort()
        def addnode(l,r,arr):
            if l > r:
                return
            else:
                mid = (l + r )//2
                node = TreeNode(arr[mid])
                node.left= addnode(l,mid-1,arr)
                node.right= addnode(mid+1,r,arr)
                return node
        
        return addnode(0,len(self.arr) -1,self.arr)
