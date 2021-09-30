# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def convertSAB(nums,start,end):
            if start > end:
                return None
            
            newNode = TreeNode()
            
            if start == end:
                newNode.val =nums[start]
                newNode.left = None
                newNode.right = None
                
            else:
                mid = start + (end - start) // 2
                newNode.val =nums[mid]
                newNode.right = convertSAB(nums,mid+1,end)
                newNode.left = convertSAB(nums,start,mid-1)
                
            return newNode
        
        return convertSAB(nums,0,len(nums) - 1)
