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
var oddEvenList = function(head) {
    if (!head) return head
    let odd = null,
        even = null

    while (head) {
        let tempOdd = odd
        odd = head
        head = head.next
        odd.next = tempOdd
        if (head) {
            let tempEven = even
            even = head
            head = head.next
            even.next = tempEven
        }
    }
    odd = reverse(odd)
    even = reverse(even)
    let enter = odd
    while (enter && enter.next) {
        enter = enter.next
    }
    enter.next = even
    return odd
};

function reverse(list) {
    let reversed = null
    while (list) {
        let temp = reversed
        reversed = list
        list = list.next
        reversed.next = temp
    }
    return reversed
}
