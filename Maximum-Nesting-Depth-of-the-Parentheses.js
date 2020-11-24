/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    s = [...s]
    let open = 0
    let solution = 0
    s.forEach(x => {
        if (x === "(") {
            open = open + 1
        } else if (x === ")") {
            open = open - 1
        }
        solution = Math.max(solution, open)
    })
    return solution
};
  maxDepth("(1+(2*3)+((8)/4))+1")//solution3
// Photo by Alex on Unsplash
