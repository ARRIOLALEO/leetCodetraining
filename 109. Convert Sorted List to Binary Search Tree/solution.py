# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        def createBST(arr,start,end):
            if start > end:
                return None
            
            newNode = TreeNode()
            
            if start == end:
                newNode.val = arr[start]
                newNode.left = None
                newNode.right = None
            else:
                mid = start + (end - start) // 2
                newNode.val = arr[mid]
                newNode.left = createBST(arr, start, mid-1)
                newNode.right = createBST(arr,mid+1,end)
                
            return newNode
        return createBST(arr,0,len(arr) -1)
