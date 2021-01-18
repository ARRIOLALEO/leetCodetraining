var minAddToMakeValid = function(S) {
    let paren = [...S],
        needed = []
    for (let i = 0; i < paren.length; i++) {
        if (S[i] === "(") {
            needed.push(S[i])
        } else if (needed[needed.length - 1] === "(") {
            needed.pop()
        } else {
            needed.push(S[i])
        }
    }
    return needed.length
};
