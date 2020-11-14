/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    const response = []
    const size = arr.length
    for (let i = 0 ; i < size; i ++){
        if(arr[i] === 0){
            response.push(arr[i],0)
        }else{
            response.push(arr[i])
     }
    }
    for (let i = 0 ; i < size; i ++){
        arr[i] = response[i]
    }

};
