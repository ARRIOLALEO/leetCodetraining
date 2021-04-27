/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
    
//  we need to pointers the start of the insertion and the end
    let start = list1, end = list1
//     both are pointing at list1 and we need to walk the list to found those points
//      we need to check the start of the insertion that it is a and the end that it is b
//     we will do it with a loop
//     it is also neccesary to check if there is a next in the end and stat 
for(let i = 0;i<=b && start.next && end.next ; i++){
//      here we are walking our list to find our start insertion point
    if(i < a -1 ) start = start.next
//     here we need to find our end insertion point we continue walking our list
//     we need to include our b
    if(i <= b ) end = end.next
}
//      we need our tail that it is the end our list2
 let tail = list2
//   we need to walk our tail to find the last node
 while(tail.next){
     tail = tail.next
 }
//      now we need to joing our lists
    
//     joining the start with the head of the list2
    start.next = list2
//      joining out tail with the end of inins
    tail.next = end
    return list1
};
