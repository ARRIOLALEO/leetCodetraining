var mergeKLists = function(lists) {
    let numbers = []
    for(let subList of lists){
        while(subList){
            numbers.push(subList.val)
            subList = subList.next
        }
                    
    }
    
    numbers.sort((a,b)=> a-b)
    
    let solution = null
    
    while(numbers.length > 0){
        const newNode = new ListNode(numbers.pop())
        let temp = solution
        solution = newNode
        solution.next = temp
    }
    
    return solution
    
}; 
