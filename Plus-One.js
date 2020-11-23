var plusOne = function(digits) {
    // check the lenght of the array 
    const nDigits = digits.length
    // the array we joing it and we have an
    //string that we parse to Big intenget and we add 1
    digits = BigInt(digits.join("")) + BigInt(1)
    //i create an array called solution tostore the data
    let solution = []
    // after add one i passed the bigInt to string and spread in an array
    digits = [...digits.toString()]
    // in the case that our solution is longer that means our array had 0 at begining
    if (nDigits > digits.length) {
        //we add the 0's at the bigining missing
        for (let j = 0; j < (nDigits - digits.length); j++) {
            solution.push("0")
        }
        return solution = [...solution, ...digits]
    }
    // if the length is the same we just return our array of Digits with one more
    return digits
};
