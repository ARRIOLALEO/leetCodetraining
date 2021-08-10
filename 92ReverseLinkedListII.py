# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if left == right :
            return head
        
        dummy= ListNode(-1)
        dummy.next = head
        
        counter = 0
        cur = dummy
        rev = None
        prev = None
        while counter < right:
            if counter == left:
                while counter <= right:
                    temp = rev
                    rev = cur
                    cur = cur.next
                    rev.next = temp
                    counter += 1
                tail = cur
                break
            counter +=1
            prev = cur
            cur = cur.next
            
        prev.next = rev
        while rev and rev.next:
            rev = rev.next
        
        rev.next = tail
        if left == 1:
            return prev.next
        else:
            return head
        
        
