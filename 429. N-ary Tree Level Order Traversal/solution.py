"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue =[root]
        nq = []
        res = []
        while queue:
            level = []
            for node in queue:
                level.append(node.val)
                if node.children:
                    nq += node.children
            res.append(level)
            queue = nq
            nq = []
        return res
        
