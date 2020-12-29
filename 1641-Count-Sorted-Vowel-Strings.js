/**
 * @param {number} n
 * @return {number}
 */
const factorial= ( number)=>{
    let solution = 1
    for(i = 2; i<= number; i++){
        solution *= i
    }
    return solution
}

var countVowelStrings = function(n) {
// (n+r−1)!/ !r!(n−1)!
let numerator = factorial(n + 4)
let nMinusOne = 24
let number = factorial(n)
return (numerator / (number * nMinusOne))
};
