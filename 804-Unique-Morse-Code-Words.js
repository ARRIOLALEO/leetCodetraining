/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    let morese = {
        a: ".-",
        b: "-...",
        c: "-.-.",
        d: "-..",
        e: ".",
        f: "..-.",
        g: "--.",
        h: "....",
        i: "..",
        j: ".---",
        k: "-.-",
        l: ".-..",
        m: "--",
        n: "-.",
        o: "---",
        p: ".--.",
        q: "--.-",
        r: ".-.",
        s: "...",
        t: "-",
        u: "..-",
        v: "...-",
        w: ".--",
        x: "-..-",
        y: "-.--",
        z: "--.."
    }
    let solution = []
    words.forEach(x => {
        let toupload = [...x].map(j => morese[j]).join("")
        solution.push(toupload)
    })
    solution = new Set(solution)
    return solution.size
};
