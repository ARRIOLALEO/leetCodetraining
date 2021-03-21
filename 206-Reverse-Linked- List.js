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
var reverseList = function(head) {
      let prevNode = null;
     let currNode = head;
      while (currNode) [currNode.next, prevNode, currNode] = [prevNode, currNode, currNode.next];
     return prevNode;
    
};
