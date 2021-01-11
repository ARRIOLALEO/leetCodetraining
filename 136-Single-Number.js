/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let solution = []
    nums.forEach(number =>{
        let exists = nums.filter(element => element === number)
      if( exists.length  < 2  ) return number
    })
 
};
