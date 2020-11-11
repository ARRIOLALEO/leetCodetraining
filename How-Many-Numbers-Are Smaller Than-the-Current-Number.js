var smallerNumbersThanCurrent = function(nums) {
  //  create the array that will get the answer
  const response =[]
//   iterate the array
  nums.forEach(num=>{
//     create a counter that will check how many small number we get
    let counter = 0;
//    we iterate the array to compair
    for(let i= 0 ; i < nums.length; i ++){
//       if our number is number than the compared in the array we add one to our array
      if(num > nums[i]){
        counter++
      }
    }
//   adding how many number are smaller then the compared number to our array
     response.push(counter)
  })
// returning the answer
  return response
};
smallerNumbersThanCurrent([8,1,2,2,3]) // [0,0,0,0]
smallerNumbersThanCurrent([7,7,7,7]) // [4,0,1,1,3]


// another solution with sore we save 4 ms
var smallerNumbersThanCurrent = function(nums) {
  const response =[]
  const compared =[...nums].sort()
  nums.forEach(num=>{
    let counter = 0;
    for(let i= 0 ; i < compared.length; i ++){
      if(num > compared[i]){
        counter++
      }
    }
     response.push(counter)
  })
  return response   
};
