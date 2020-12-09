/**
 * @param {number} N
 * @return {number}
 */
var fib = function(N) {
 const fibonacci = [0,1,1]
    
    if(N === 0){
        return fibonacci[0]
    }else if( N < 3){
      return fibonacci[1]      
   }else{
      let temp1 = fibonacci[fibonacci.length -2] 
       let temp2 = fibonacci[fibonacci.length -1]
       for(let i = 2; i< N ; i++){
          fibonacci.push(temp1 + temp2) 
            temp1 = fibonacci[fibonacci.length -2] 
            temp2 = fibonacci[fibonacci.length -1]
       }
   }
   return fibonacci[fibonacci.length - 1]
}
