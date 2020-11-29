/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    const solution = []
    bth(root)

    function bth(root) {
        if (root == null) {
            return
        }
        if (root.left) {
            bth(root.left)
        }
        if (root.right) {
            bth(root.right)
        }
        solution.push(root.val)

    }
    return solution
};
