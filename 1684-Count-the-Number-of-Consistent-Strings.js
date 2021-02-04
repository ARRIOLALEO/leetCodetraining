/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let solution = []
    words.forEach(x=>{
        let uploads = true
        for(let i = 0 ; i < x.length ; i++){
           if(!allowed.includes(x[i])){
              uploads = false
              }
        }
        if(uploads){
            solution.push(x)
        }
    })
    return solution.length
};
