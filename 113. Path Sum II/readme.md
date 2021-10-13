# 113. Path Sum II

<pre>Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 </pre>

### Example 1:

<pre>
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22</pre>

### Example 2:

<pre>
Input: root = [1,2,3], targetSum = 5
Output: []</pre>

### Example 3:
<pre>
Input: root = [1,2], targetSum = 0
Output: []
 </pre>

### Constraints:
<pre>
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000</pre>
