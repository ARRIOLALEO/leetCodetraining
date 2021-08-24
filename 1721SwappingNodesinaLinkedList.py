# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        newHead = head
        nHead = head

        while newHead:
            size = 1
            newHead = newHead.next
        if size == 1:
            return head
        nodeKinit = k - 1
        nodeKend = size - k
        if nodeKinit == nodeKend:
            return head

        counter,n1 ,n2 ,value1 ,value2 = 0, 0, None, None
        
        while nHead:
            if counter == nodeKinit:
                n1 = nHead.val
                value1 = nHead
                counter = 1
                nHead = nHead.next
            elif counter == nodeKend:
                n2 = nHead.val
                value2 = nHead
                counter = 1
                nHead = nHead.next
            else:
                counter = 1
                nHead = nHead.next

        value1.val = n2
        value2.val = n1

        return head


// Photo by Djim Loic on Unsplash
