/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    //     remove the Space
    s = s.trim()
    //     creating an array 
    const arrayOfWords = s.split(" ")
    //     got the last element
    let theLastWord = arrayOfWords.pop()
    //     return the lastWordLenght
    return theLastWord.length
};
