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
 * @return {boolean}
 */
var isUnivalTree = function(root) {
     return check(root,root.val)
};
function check(val,value){
    if(!val)return true
    if(val.val != value){ return false}
    return(check(val.left,value) && check(val.right,value))
}
