var subtractProductAndSum = function(n) {
    const numbers= n.toString().split("")
    let mult=1;
    let sume = 0; 
    for(i=0 ; i < numbers.length ; i ++){
       mult = mult * parseInt(numbers[i]);
      sume = sume + parseInt(numbers[i])  
    }
  return mult - sume
};
