/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let solution = 0
    nums.forEach(number =>{
        let parcial =nums.filter(x=> x === number)
        if(parcial.length === 1) solution += number
    })
    return solution
};
