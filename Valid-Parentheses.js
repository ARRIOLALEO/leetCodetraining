/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    s = [...s]
    const stack = []
    let solution = true
    if (s.length <= 1) {
        solution = false
    }
    s.forEach(x => {
        if (x == "(") {
            stack.push(")")
        } else if (x == "[") {
            stack.push("]")
        } else if (x == "{") {
            stack.push("}")
        } else {
            let toCheck = stack.pop()
            if (toCheck != x) {
                solution = false
            }
        }
    })
    if (stack.length > 0) {
        solution = false
    }
    console.log(stack)
    return solution
};
