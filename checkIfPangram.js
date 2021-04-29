/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    let myArray= sentence.split("")
    let mySet = new Set(myArray)
    if (mySet.size !== 26) return false
    return true
};
