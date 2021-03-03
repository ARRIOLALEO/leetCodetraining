/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function(A) {
//     we make an array of unique elements
    const unique = [... new Set(A)];
//     we found n
    let n = unique.length - 1;
    for(let i = A.length - 1  ;i >= 0 ; i--){
        let presolution = A.filter(x=> A[i] === x );
        if(presolution.length === n){
            return presolution[0];
        }
    }
    
};
