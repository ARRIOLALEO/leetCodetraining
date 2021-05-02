var replaceDigits = function(s) {
    let myArray = s.slice("")
    let solution = []
    for (let i = 0, n = myArray.length; i < n; i++) {
        if (parseInt(myArray[i])) {
            let element = myArray[i - 1].charCodeAt() + parseInt(myArray[i])
            solution.push(String.fromCharCode(String(element)))

        } else {
            if (myArray[i] == "0") {
                solution.push(myArray[i - 1])
            } else {
                solution.push(myArray[i])
            }

        }
    }
    return solution.join("")
};
