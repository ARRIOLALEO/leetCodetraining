# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        
        new_list = ListNode(0)
        new_list.next = head
        
        new_head = new_list
        
        for i in range(left -1 ):
            new_head = new_head.next
        
        reverse_list = None
        tail = new_head.next
        
        for i in range(right - left + 1):
            temp = reverse_list
            reverse_list = tail
            tail = tail.next 
            reverse_list.next = temp
        new_head.next.next = tail
        new_head.next = reverse_list
        return new_list.next
