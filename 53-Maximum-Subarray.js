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


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_product = nums[0]
        max_product_include_actual = 0
        
        for n in nums:
            if (n + max_product_include_actual ) > n:
                max_product_include_actual += n
            else:
                max_product_include_actual = n
            
            if max_product > max_product_include_actual :
                pass
            else:
                max_product = max_product_include_actual

            
        return max_product
