/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (!head) return head
    let lenghtList = size(head)
    k = k % lenghtList
    if (!k) {
        return head;
    }

    for (let i = 0; i < k; i++) {
        let tail = reverse(head)
        let temp = head
        head = tail
        head.next = temp
        let disconect = head
        for (let j = 0; j < lenghtList - 1; j++) {
            disconect = disconect.next
        }
        disconect.next = null

    }
    return head
};

function reverse(list) {
    while (list && list.next) {
        list = list.next
    }
    return list
}

function size(list) {
    let counter = 0
    while (list) {
        list = list.next
        counter++
    }
    return counter
}
