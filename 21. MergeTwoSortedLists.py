# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        new_head = dummy = ListNode(-1)
        
        while l1  or l2 :
            
            if l1 is not None and l2 is not None and (l1.val <= l2.val):
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
                dummy.next = None
            elif l2 is not None and l1 is not None and (l2.val < l1.val):
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
                dummy.next = None
            elif l1 is not None:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
                dummy.next = None
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
                dummy.next = None
                
        return new_head.next
      
      
#       clean Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        new_head = dummy = ListNode(-1)
        
        while l1 is not None  and l2 is not None:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
                dummy.next = None
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
                dummy.next = None
                
        if l1 is not None:
            dummy.next = l1
        if l2 is not None:
            dummy.next = l2
                
                
        return new_head.next
            
            
        
        
