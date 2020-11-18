/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
//     we create a counter
    let movements = 0
//     create a comparative array ordened
     let cheker = [... heights].sort((a,b)=> a-b)
//      we walk the array 
     for(i=0; i < heights.length ; i++){
//          we compair the position if they are not the same e need to move the student
         if(heights[i] != cheker[i]){
//              update our movements
             movements = movements + 1
         }
     }
//     return the number of movements
    return movements
};
