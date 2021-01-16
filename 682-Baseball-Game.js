/**
 * @param {string[]} ops
 * @return {number}
 */
var calPoints = function(ops) {
    let myStackBaseGa = []

    for (let i = 0; i < ops.length; i++) {
        let score = ops[i]
        if (score === "+") {
            myStackBaseGa.push(myStackBaseGa[myStackBaseGa.length - 1] + myStackBaseGa[myStackBaseGa.length - 2])
        } else if (score === "D") {
            myStackBaseGa.push(myStackBaseGa[myStackBaseGa.length - 1] * 2)
        } else if (score === "C") {
            myStackBaseGa.pop()
        } else {
            myStackBaseGa.push(parseInt(score, 10))
        }
    }
    return (myStackBaseGa.reduce((a, b) => a + b))
};
