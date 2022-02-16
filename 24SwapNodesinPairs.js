# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        swap = ListNode(-1)
        swap.next = head
        
        cur = swap
        
        while head and head.next:
            first = head
            second = head.next
            
            cur.next = second
            first.next = second.next
            second.next = first
            
            cur = first 
            head = first.next
            
        return swap.next
    
        
