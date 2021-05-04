/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    if (nums.length < 2) return 0
    let operations = 0
    let prev = nums[0]
    for(let i = 1, n = nums.length ; i < n ; i++){
        if(prev >= nums[i]){
            let dif = Math.abs( prev - nums[i]) + 1
            operations += dif
            nums[i] += dif
            prev = nums[i]
        }
        else{
            prev = nums[i] 
        }
    }
    return operations
};
