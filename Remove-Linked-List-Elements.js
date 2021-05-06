/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    while (head && head.val === val) head = head.next
    let entrance = head
    while (entrance && entrance.next) {
        if (entrance.next.val === val) {
            entrance.next = entrance.next.next
        } else {
            entrance = entrance.next
        }
    }
    return head
};
