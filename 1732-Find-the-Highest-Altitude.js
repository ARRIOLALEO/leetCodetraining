/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
let previus = 0
let solution = [ 0 , ...gain.map(x =>{
    previus = previus + x
    return parseInt(previus)
}).sort((a,b)=> a - b)]
solution[solution.length -1 ] > 0?solution[solution.length -1 ] :
  }else{
      return solution[0]
  } 
};
