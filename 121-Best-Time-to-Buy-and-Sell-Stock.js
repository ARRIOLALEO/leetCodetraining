/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
 let revennue = 0
 let minPriceToBuy = prices[0]
 for(let i = 0; i< prices.length ; i++){
   revennue= Math.max(revennue , prices[i] - minPriceToBuy)
   minPriceToBuy = Math.min(minPriceToBuy, prices[i])
 }
  return revennue

};
