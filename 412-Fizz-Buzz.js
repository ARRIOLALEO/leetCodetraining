/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const solution = []        
    for( i = 1 ; i <= n ; i++){
        if(i % 3 !== 0 && i % 5 !== 0){
           solution.push(i.toString()) 
        } else  if(i % 3 === 0 && i % 5 === 0) {
            solution.push("FizzBuzz") 
        }else if(i % 3 === 0) {
           solution.push("Fizz") 
        }else {
            solution.push("Buzz")
        }
    }
    return solution
};
