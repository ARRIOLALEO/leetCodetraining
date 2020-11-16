/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
// array is 0 or emty return false
    if(arr.length > 0){
//         we walk the array 
          for(let i =0; i < arr.length ; i ++){ 
//               we walk the array again in order to find if there are 
// Double Exist              
            for(let j = 0; j < arr.length; j++){
                const cheker = arr[j] * 2
                if (j != i && arr[i] === cheker ){
//   if exist a number that is the double return true 
                 return true
                }
            }
        }
    }
  return false
};
