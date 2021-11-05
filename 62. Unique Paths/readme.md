A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# 62. Unique Paths

<pre>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?</pre>

 

### Example 1:

<pre>
Input: m = 3, n = 7
Output: 28</pre>

### Example 2:
<pre>
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down</pre>

### Example 3:
<pre>
Input: m = 7, n = 3
Output: 28</pre>

### Example 4:
<pre>
Input: m = 3, n = 3
Output: 6
 </pre>

### Constraints:
<pre>
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.</pre>
