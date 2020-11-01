/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const allIntegers = candies.map(x => parseInt(x, 10))
    const sorted = [...allIntegers].sort(function(a, b){return a-b}).slice(-1)
    let response =[]
    allIntegers.forEach(kid=>{
    if ((kid + extraCandies)>= sorted){
        response.push(true)
    }
        else{
          response.push(false)  
        }
    })
    return response
};
