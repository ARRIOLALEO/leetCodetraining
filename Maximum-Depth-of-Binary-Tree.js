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
 * @return {number}
 */
var maxDepth = function(root) {
    
    function deep(root){
        if(root == null){
            return 0
        }
           let solutionLeft = deep(root.left) + 1
            let solutionRight = deep(root.right) + 1
        return Math.max(solutionRight,solutionLeft)
    }
    
    return deep(root)
};
