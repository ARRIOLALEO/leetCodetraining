# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(li):
            result = None
            while li:
                temp = result
                result = li
                li = li.next
                result.next = temp
            return result
        
        solution = None
        carry = 0
        l1 = reverse(l1)
        l2 = reverse(l2)
        while l1 or l2 or carry > 0:
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            sume = n1 + n2 + carry
            if sume > 9:
                carry = 1
                sume -= 10
            else:
                carry = 0
            temp = solution
            solution = ListNode(sume)
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            solution.next = temp
        return solution
            
            
        
