/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let myArray = s.split(" "),
        solution = new Array(myArray.length).fill(0)
    for (let word in myArray) {

        let position = [...myArray[word].split("")].pop()
        let newWord = [...myArray[word]]
        newWord.pop()
        solution[position - 1] = newWord.join("")
    }
    return solution.join(" ")
};
