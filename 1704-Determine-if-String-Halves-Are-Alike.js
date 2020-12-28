/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    const lengthOftheString = s.length
    const firstHalf = s.slice(0, (lengthOftheString / 2))
    const secondHalf = s.slice((lengthOftheString / 2))
    let solution = false
    if (checkVowels(firstHalf).length === checkVowels(secondHalf).length) {
        solution = true
    }

    function checkVowels(value) {
        let theVowels = [...value].filter(vowel => 'aeiou'.includes(vowel.toLowerCase()))
        return theVowels
    }
    return solution

};
