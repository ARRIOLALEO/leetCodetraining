/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
    const myStack = []
    let lengthTarget = 0
    for(let i = 1 ; i <= n;i++){
        myStack.push("Push") 
        lengthTarget++
        if(!target.includes(i)){
            myStack.push("Pop")
            lengthTarget--
        }
        if(lengthTarget === target.length) break
    }   
    return myStack
};
