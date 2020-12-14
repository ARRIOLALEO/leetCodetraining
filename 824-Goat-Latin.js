/**
 * @param {string} S
 * @return {string}
 */
var toGoatLatin = function(S) {
    //     first make and array withe the words
    const words = S.split(" ")
    const vowels = ["a", "e", "i", "o", "u"]
    const solution = []
    //     one add counter starts 1
    let addas = "a"
    // for each word check if word[0] = vowel add ma
    words.forEach(word => {
        if (!vowels.includes(word[0].toLowerCase())) {
            let arrayWord = word.split("")
            let aux = arrayWord.shift()
            arrayWord.push(aux) -
                solution.push(arrayWord.join("") + "ma" + addas)

        } else {
            solution.push(word + "ma" + addas)
        }
        addas = addas + "a"
    })
    return solution.join(" ")

};
