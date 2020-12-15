/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let theRichest = 0
    accounts.forEach(customer=>{
      let rich=  customer.reduce((acc,wealth)=>{
            return acc = acc + wealth
        },0)
      theRichest = Math.max(theRichest , rich)
    })
    return theRichest
};
