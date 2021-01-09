/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let maxMultiplication = 0;
    for(let i = 0 ; i < nums.length ; i++){
        for(let j = i + 1 ;j < nums.length; j ++){
            maxMultiplication = Math.max(maxMultiplication , ((nums[i] -1) * (nums[j]-1)))
        }
    }
    return maxMultiplication
};
