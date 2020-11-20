/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
// we have two arrays one has the values and the other the index
var createTargetArray = function(nums, index) {
    // we create an array for the solution 
    const solution = []
    // walk the array 
    for (let i = 0; i < nums.length; i++) {
        //replace the element with its index good thing about
        //splice it is move the desplaced element to the next space
        solution.splice(index[i], 0, nums[i])
    }
    return solution
};
