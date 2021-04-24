// Singly-linked lists are already defined with this interface:
// function ListNode(x) {
//   this.value = x;
//   this.next = null;
// }
//
function mergeTwoLinkedLists(l1, l2) {
    //  this is the head of my list
    mergeList = null
    //  now i need to walk my two lists
    myArray = [...toArray(l1),...toArray(l2)]
    myArray = myArray.sort((a,b)=>a-b).reverse()
    //  create my solution
    for(e of myArray){
        temp = mergeList
        newNode = new ListNode(e)
        mergeList = newNode
        mergeList.next = temp
    }
    return mergeList
}

function toArray(list){
    myArray = []
    while(list){
        myArray.push(list.value)
        list = list.next
    }
    return (myArray)
}
