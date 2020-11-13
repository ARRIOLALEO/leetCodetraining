/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
//     create an array that will contain the response
    const response =[]
//     iterate the array to check all have an  even number of digits.
    nums.forEach(x=>{
//         in order to check the length of a number we transfor 
//         it into String and we check its length
        const number = x.toString().length
//         if the lenght % 2 === 0 it is even
        if(number % 2 === 0){
//             we push to our response array
            response.push(number)
        }
    })
//     returning the length of the response
     return response.length
};
