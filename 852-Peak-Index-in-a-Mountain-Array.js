/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    if(arr.length < 3) return false
    for (let i = 0 ; i < arr.length - 1 ; i++){
        if(arr[i] > arr[i+1] ) return i 
    }
};
