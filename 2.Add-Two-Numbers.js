/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let first = sume(l1);
    let second = sume(l2);
    let sume1 = first + second;
    sume1 = String(sume1);
    sume1 = [...sume1];
    console.log(sume1);
    let head = null;
    sume1.forEach(x => {
        let n = new ListNode(x);
        n.next = head;
        head = n;
    })
    return head
};

function sume(l) {
    let response = "";
    while (l) {
        response += String(l.val);
        l = l.next;
    }
    response = [...response].reverse().join("");
    return parseInt(response);
}
