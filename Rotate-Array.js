/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    for(let i = 0 ; i < k ; i ++){
        let lastOne = nums.pop()
        nums.unshift(lastOne)
    }
    return nums
};

let nums = [1,2,3,4,5,6,7], k = 3

rotate(nums,k) //[5,6,7,1,2,3,4]
