Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

 

### Example 1:
![Image of matrix1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

<pre>Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]</pre>

### Example 2:

![image of matrix2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
<pre> Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]</pre>
 

### Constraints:

<pre> m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1</pre>
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
