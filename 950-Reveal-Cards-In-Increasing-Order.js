/**
 * @param {number[]} deck
 * @return {number[]}
 */
var deckRevealedIncreasing = function(deck) {
    let myArray = deck.sort((a,b)=> a -b)
     let  response = []
     while(deck.length){
         response.unshift(deck.pop())
         response.unshift(response.pop())
     }
    response.push(response.shift())
    return response
};
