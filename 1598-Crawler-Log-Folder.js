/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    let operations = 0
   for(let operation of logs) {
       if(operation !== "../"  && operation !== "./"  ){
           operations++
       }else if ( operation === "../"){
           operations--
           if(operations < 0){
               operations = 0
           }
       }
   }
    if (operations < 0 ){
        return 0
    }else{
        return  operations 
    }
};
