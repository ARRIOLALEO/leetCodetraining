# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.node_values = []
        self.size = 0
        new_head = head
        
        while new_head:
            self.node_values.append(new_head.val)
            self.size += 1
            new_head = new_head.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        
        return self.node_values[int(random.random() *  self.size)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
