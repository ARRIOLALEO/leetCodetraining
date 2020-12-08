/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    let solution = 0
    nums.sort((a,b)=> a -b)
    for(let i = 0 ; i < nums.length ; i = i + 2){
        solution = solution + nums[i] 
    }
    return solution
};

arrayPairSum([1,4,3,2])//

// Photo by Francesco Castiglione on Unsplash
