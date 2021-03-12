/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
    let cur = head ;
    let str = '';
    while(cur){
        str +=  cur.val.toString();
        cur = cur.next;
    }
    return parseInt(str,2);
};
