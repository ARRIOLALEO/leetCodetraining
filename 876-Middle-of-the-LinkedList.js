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
var middleNode = function(head) {
    let cur = head;
    let final = head ;
    let counter = 0;
    while(cur){
        counter++
        cur = cur.next;
    }
    for(let i = 0 , n = (counter -1) / 2 ; i < n; i++){
        final = final.next;
    }
    return final ;
};
