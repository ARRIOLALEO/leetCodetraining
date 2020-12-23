/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let numberInBinary = n.toString(2)
    let response = (numberInBinary.split("")).filter(binary => binary == 1 )
    return response.length
};
