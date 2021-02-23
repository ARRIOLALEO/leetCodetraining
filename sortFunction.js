/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
      let aux ;
  for(let i = 0, n = nums.length ; i < n-1 ; i++){
     if( nums[i] < nums[i-1]){
       aux = nums[i-1];
       nums[i - 1]= nums[i];
       nums[i] = aux;
     }
    if(nums[i] > nums[i + 1]){
      aux = nums[i];
      nums[i] = nums[i + 1 ];
      nums[i+1] = aux;
      i = i-2;
    } 
  }
  return nums
};
