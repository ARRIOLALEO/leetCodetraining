/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let a = "" , b = ""
    let newHead = head
    while(newHead){
        a = newHead.val.toString() + a
        b = b + newHead.val.toString()
        newHead = newHead.next
    }
    if(a === b )return true
    return false
};
