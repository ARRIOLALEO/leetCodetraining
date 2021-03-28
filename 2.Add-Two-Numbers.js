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
    let firstSume = sumeList(l1);
    let secondSume = sumeList(l2);
    let sume = firstSume + secondSume;
    sume = String(sume);
    sume = [...sume];
    let head = null;
    sume.forEach(x => {
        let n = new ListNode(x);
        n.next = head;
        head = n;
    })
    return head
};

function sumeList(l) {
    let response = "";
    while (l) {
        response += String(l.val);
        l = l.next;
    }
    response = [...response].reverse().join("");
    return parseInt(response);
}
