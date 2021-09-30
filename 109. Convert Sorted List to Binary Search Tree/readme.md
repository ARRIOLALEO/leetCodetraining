# 109. Convert Sorted List to Binary Search Tree

<pre>Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.</pre>

 

### Example 1:


<pre>Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.</pre>

### Example 2:

<pre>Input: head = []
Output: []</pre>

### Example 3:

<pre>Input: head = [0]
Output: [0]
</pre>

### Example 4:
<pre>
Input: head = [1,3]
Output: [3,1]
 </pre>

### Constraints:
<pre>
The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105</pre>
