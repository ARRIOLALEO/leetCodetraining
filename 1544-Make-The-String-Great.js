/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    if(s.length === 1) return s
    let myStack= ['']
    for(let i =0 ; i < s.length ; i++){
        if (Math.abs(s.charCodeAt(i) - s.charCodeAt(i+1)) === 32){
          i++;  
        }else if(Math.abs(myStack[myStack.length-1].charCodeAt()- s.charCodeAt(i) ) === 32){
            myStack.pop();
        }else{
            myStack.push(s[i]);
        }
    }
    return myStack.join("")
};
