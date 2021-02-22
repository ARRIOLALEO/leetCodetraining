/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
//      we need to destroy the leters to an array
let array1 = [...word1];
let array2 = [...word2];
// need to take the longest
let n = array1.length >= array2.length ?  array1.length  : array2.length ;
let solution = []
 for ( let i = 0 ; i < n ; i++)
   {
       if (array1.length > 0)
       {
           solution.push(array1.shift());
       }
       if (array2.length > 0)
       {
           solution.push(array2.shift());
       }
   }
//      we print the solution joing the strings 
    return (solution.map(x=>x).join(""));
};
