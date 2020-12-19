/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
//    i need to store the elements to compair  
let firstElement, secondElement
for( let number of nums){
    if(number > secondElement) return true
    if( number > firstElement) secondElement = number
    else firstElement  = number
}
    return false
};
