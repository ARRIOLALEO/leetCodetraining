var removeElement = function(nums, val) {
// we walk our array every element
      for (let i = 0; i < nums.length ; i ++){
 // we check if the element is iqual to our vall to remove 
          if(nums[i] === val){
 //  we removed the element thet is === vall
              nums.splice(i,1)
 // we go one step back because we need to check again our element
              i--
          }
      }
};

// another solution
var removeElement = function(nums, val) {
      for (let i = nums.length -1 ; i >= 0 ; i --){
          if(nums[i] === val){
              nums.splice(i,1)
          }
      }
};
