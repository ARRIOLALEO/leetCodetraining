# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow =  fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        revers = None
        while slow:
            temp = revers
            revers = slow
            slow = slow.next
            revers.next = temp
        
        while revers and revers.next :
            if head.val != revers.val:
                return False
            head = head.next
            revers = revers.next
            
        return True
            
