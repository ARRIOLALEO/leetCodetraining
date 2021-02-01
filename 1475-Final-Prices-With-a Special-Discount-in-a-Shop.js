/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    let solution = []
    for (let i = 0; i < prices.length; i++) {
        let toInsert = -1
        for (let j = i + 1; j < prices.length; j++) {
            if (prices[i] >= prices[j]) {
                toInsert = (prices[i] - prices[j])
                break
            }
        }
        toInsert >= 0 ? solution.push(toInsert) : solution.push(prices[i])
    }
    return solution
};
