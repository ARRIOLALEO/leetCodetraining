/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function(firstWord, secondWord, targetWord) {
    let number1 = toNumber(firstWord)
    let number2 = toNumber(secondWord)
    let targetNumber = toNumber(targetWord)
    console.log(number1, number2, targetNumber)
    if ((number1 + number2) === targetNumber) return true
    return false

};

function toNumber(string) {
    let solution = string.split("").map(element =>
        element.charCodeAt(0) - 97).join("")
    return (parseInt(solution, 10))
}
