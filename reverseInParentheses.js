function reverseInParentheses(inputString) {
while(inputString.indexOf(')') !== -1){
    // first we detect the firs close parentheses
    let c = inputString.indexOf(')',0);
    //  after that we select the last open parentesis
    let a = inputString.lastIndexOf('(', c);
    //  we slpit the parentesis inside we reverse an join 
    let b = inputString.slice(a +1 , c).split("").reverse().join("");
    //  than we join the information from 0 to the first parentesis 
    inputString = inputString.slice(0,a) + b + inputString.slice(c +1)
}
return inputString
}
