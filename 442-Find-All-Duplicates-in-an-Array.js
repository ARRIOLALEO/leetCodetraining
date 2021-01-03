/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    const notDuplicated = [...new Set(nums)]
    let index = 0
    for (let i = 0; i < notDuplicated.length; i++) {
        index = nums.indexOf(notDuplicated[i])
        nums.splice(index, 1)
    }
    return nums
};
