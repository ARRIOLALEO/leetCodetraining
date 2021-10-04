# 501. Find Mode in Binary Search Tree

<pre>Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.</pre>
 

### Example 1:


<pre>Input: root = [1,null,2,2]
Output: [2]</pre>

### Example 2:

<pre> Input: root = [0]
Output: [0]</pre>
 

<pre>Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
</pre>