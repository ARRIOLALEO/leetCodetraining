var numberOfSteps  = function(num) {
//set a counter
  let response = 0
  const step =(num)=>{
  //we check if is 0
       if(num > 0){
       // we count the step
        response++
        we review if the number if teh divicion by 2 is 0 if not we remove substract 1 and again call the function usin a ternary
       num % 2 === 0?step(num/2):step(num - 1)
       }
  }
  step(num)
  return response
};
