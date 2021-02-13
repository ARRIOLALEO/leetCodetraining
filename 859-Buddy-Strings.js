var buddyStrings = function(A, B) {
    if(A === B && [...new Set(A)].length === A.length) return false
    if (A === B && [...new Set(A)].length !== A.length) return true
    if(A.length === 0 || B.length ===  0) return false
    let sentinel = 0
    A = [...A]
   for(let i = 0; i < A.length ; i++){
       if ( A[i] !== B[i]){
           sentinel++
            let support = B[i]
            for(let j = i ; j < B.length ; j++){
                if(support  === A[j]){
                let secondHelper =A[i]
                  A[i] = A[j]
                  A[j] = secondHelper
                  if (A.join("") !== B) {return false}
                  return true
                }
            }
            
       }
   }
    return false
};
