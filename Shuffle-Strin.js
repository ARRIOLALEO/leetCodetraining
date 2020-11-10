/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
   // create an array to hold the solution
 let solution =[]
    // create an array with both array in order to pair the elements
 for (let i = 0; i < indices.length ; i ++){
     solution.push([indices[i],s[i]])
 }
     //sort the elements on the array base on the first element that it is numeric
  solution =solution.sort((a,b) => a[0]-b[0])
     //create the solution with the join of the second element 
  solution = solution.map(s=> s[1]).join("")
  //retur the solution 
  return solution
};
restoreString("codeleet",[4,5,6,7,0,2,1,3])
