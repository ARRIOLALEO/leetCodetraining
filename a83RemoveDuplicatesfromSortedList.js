var deleteDuplicates = function(head) {
    let slow = head
    while(slow){
        while(slow && slow.next && slow.val == slow.next.val){
            let temp = slow.next
            slow.next = temp.next
        }
        slow = slow.next
    }
    return head
};
