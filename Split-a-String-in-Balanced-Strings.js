/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    //  create 2 variables 
    const r = [],
        l = [],
        solution = []

    //     solution

    s.split("").forEach(x => {
        if (x === "R") {
            r.push("R")
        } else {
            l.push("L")
        }
        if (r.length === l.length) {
            solution.push(1)
        }
    })

    return solution.length
};
