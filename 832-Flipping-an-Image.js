/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function(A) {
    A= A.map(x => x.reverse())
    A = A.map(x=>{
        let helper = []
        for(let i = 0 ; i < x.length ; i ++){
            x[i]=== 1? helper.push(0):helper.push(1)
        }
        return helper
    })
    return A
};
