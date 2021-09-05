# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        entrance = head
        while entrance:
            size += 1
            entrance = entrance.next
        newhead = head  
        if size == 1 and n == 1:
            return None
        if (size - n) == 0:
            head = head.next
            return head
        for i in range(size - n -1):
            newhead = newhead.next
        
        temp = newhead.next.next
        newhead.next = temp
        
        return head
