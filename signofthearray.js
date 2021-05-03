/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    var solution = nums.reduce((a,b)=> a * b)
    if( solution > 0 ) return 1
    if( solution < 0 ) return -1
    return 0
    
};
