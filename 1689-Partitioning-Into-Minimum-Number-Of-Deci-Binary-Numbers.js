/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
 let solution = -Infinity;
    for(let i = 0 ; i < n.length ; i ++){
        if(n[i]=== 9){
            return 9
            break
        }
        solution  = Math.max(solution , n[i])
    }
   return solution
};
