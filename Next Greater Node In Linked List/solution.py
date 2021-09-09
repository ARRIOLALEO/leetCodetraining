# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        stk=[arr[-1]]
        arr[-1]=0
        for i in range(len(arr)-2,-1,-1):
            while stk and arr[i]>=stk[-1]:
                stk.pop()
            if not stk:
                stk.append(arr[i])
                arr[i]=0
            else:
                stk.append(arr[i])
                arr[i]=stk[-2]
        return arr
        
