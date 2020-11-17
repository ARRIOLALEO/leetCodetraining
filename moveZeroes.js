/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var moveZeroes = function(nums) {
// variable to count the 0's
 let counter = 0
 // we walk the array
    for (let i = 0 ; i < nums.length ; i++){
    // if the element of the array is 0
        if (nums[i] === 0){
        // we remove the element
            nums.splice(i,1)
            // we go one back in order to check again if the first element is an 0
            i --
            // we count the 0
            counter ++
        }        
    }
    
    //we add the  amount of 0's at the end
    for(let i = 0 ; i < counter ; i ++){
        nums.push(0)
    }
};
