var removeElements = function(head, val) {
    while(head && head.val == val){
        head = head.next  
    }
    let entrance = head
    
    while(entrance && entrance.next){
        if(entrance.next.val == val){
            let temp = entrance.next.next
            entrance.next = temp
        }else{
        entrance = entrance.next
        }
    }
    return head
};
