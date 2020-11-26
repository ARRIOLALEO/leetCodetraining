/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
// create an array that will be the result 
    let nums =[]
// push the values to the array that are start + i * 2
    for(let i = 0 ; i < n ; i++){
        nums.push( start + (i * 2))
    }
    // reduce the array using Xor 
  nums = nums.reduce((acc,x) => acc = acc ^ parseInt(x)  ,0)
  // returning the answer 
  return nums
};
