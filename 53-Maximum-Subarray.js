/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    if(nums.length == 1){
        return nums[0]
    }
    
     let maximunSume = Number.MIN_SAFE_INTEGER
     nums.forEach(number =>{
         let sumeSubArray = 0
         for(let i = nums.indexOf(number); i < nums.length ; i++){
              sumeSubArray =  sumeSubArray + nums[i]
              maximunSume = Math.max(maximunSume , sumeSubArray )
              sumeSubArray = sumeSubArray < 0 ? 0 :sumeSubArray;
         }
     })
    return maximunSume
    
};
