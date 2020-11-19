var decompressRLElist = function(nums) {
    
 const solution =[]
  for ( let i = 0; i < nums.length ; i = i + 2){
      for(j =0 ; j < nums[i] ;j ++){
          solution.push(nums[i +1])
      }
  }
    return solution
};
