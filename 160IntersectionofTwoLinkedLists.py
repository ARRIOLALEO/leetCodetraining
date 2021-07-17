class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        size_a = self.get_size(headA)
        size_b = self.get_size(headB)
        diference = abs(size_a - size_b)
        print(diference)
        
        if size_a > size_b:
            for i in range(diference):
                headA = headA.next
            while headB and headA:
                if headB == headA:
                    return headB
                headB = headB.next
                headA = headA.next
            return None
        elif size_a == size_b:
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None
        else:
            for i in range(diference):
                headB= headB.next                
            while headB and headA:
                if headB == headA:
                    return headB
                headB = headB.next
                headA = headA.next
            return None
                       
    def get_size(self,listhead):
        size = 0
        while listhead is not None:
            size += 1
            listhead = listhead.next
        return size
        
        
        second solution:
        
        
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        solution = set()
        
        while headA:
            solution.add(headA)
            headA = headA.next
            
        while headB:
            if headB in solution:
                return headB
            headB = headB.next
            
        return None
        
