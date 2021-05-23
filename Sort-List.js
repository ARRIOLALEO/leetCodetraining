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
var sortList = function(head) {
    let entrance = head
    let values = []
    while (entrance) {
        values.push(entrance.val)
        entrance = entrance.next
    }
    values = values.sort((a, b) => b - a)
    let newList = null
    for (let i = 0, n = values.length; i < n; i++) {
        let temp = newList
        newList = new ListNode(values[i])
        newList.next = temp
    }
    return newList
};
