"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node',i = 1) -> int:
        if root:
            if not root.children:
                return i
            maxD = 0
            for j in root.children:
                dpt = self.maxDepth(j, i + 1)
                if maxD < dpt:
                    maxD = dpt
            return maxD
        return 0
        
