/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    let subArr = []
    for(let i = 0 ; i < s.length ; i++){
        let aux = s[i]
        if(s[i+2] === "#" ) {
            aux = aux+ s[i+1] + s[i+2]
            subArr.push(aux)
            i = i +2
        }
        else{
            subArr.push(aux)
        }
    }
    let solution = subArr.map(x=>{
      if(x.includes('#')) x.slice(0, -1)
       return String.fromCharCode(parseInt(x,10) + 96)
    }).join("")
    return solution
};
