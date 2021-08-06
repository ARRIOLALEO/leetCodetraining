
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_gate = ListNode(-1)
        after = after_gate = ListNode(-1)

        while head :
            if head.val < x:
                before_gate.next = head
                before_gate = before_gate.next
            else:
                after_gate.next = head
                after_gate = after_gate.next
            
            head = head.next
            
        after_gate.next = None
        before_gate.next = after.next
        
        return before.next
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_gate = ListNode(-1)
        before = before_gate
        
        after_gate = ListNode(-1)
        after = after_gate
        
        while head:
            if head.val >= x:
                after_gate.next = head
                after_gate = after_gate.next
                
            else:
                before_gate.next = head
                before_gate = before_gate.next
            
            head = head.next
        after_gate.next = None
        
        before_gate.next = after.next
        return before.next
