/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let solution = []
    const max_p = n * 2
    const backtracking = (actual=[],left=0,right=0) =>{
        if (actual.length ===  max_p){
            solution.push(actual.join(""))
        }
        if(left < n){
            actual.push("(")
            backtracking(actual,left+1,right)
            actual.pop()
        }
        if(right < left){
            actual.push(")")
            backtracking(actual,left,right+1)
            actual.pop()
        }
    }
    backtracking()
    return solution
};
