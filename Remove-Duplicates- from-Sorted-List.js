/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {

    function header(cur, prev) {
        if (cur == null) {
            return
        }
        if (prev && prev.val === cur.val) {
            prev.next = cur.next
            header(cur.next, prev)
        } else {
            header(cur.next, cur);
        }
    }
    header(head, null)
    return head
};
