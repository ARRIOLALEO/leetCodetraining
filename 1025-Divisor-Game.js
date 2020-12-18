/**
 * @param {number} N
 * @return {boolean}
 */
var divisorGame = function(N) {
    if(N < 2){
        return false
    }
//   there is not winner yet
let theWinerIs = false

for(let i = 1; i < N ; i++){
//     first time Alice took a card Alsice is the winner
  theWinerIs = !theWinerIs
//     lets remove one card 
  i = i++
//     there are card for bob  not there are not than alice is the winner
    if(i == N){
        break
    }
//     if not there are cards for bob we check it again 
}  
//     here we now that alice goes first if is true alice wins if is false 
   return theWinerIs
};
