/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let solution = 0
    let second = mat[0].length -1 
    let rightArrow = 0
    let first = 0
    let remove = 0
    for(let i= 0 ; i < mat.length ; i++){
        solution += mat[i][first] + mat[i][second]
        if(first === second){
            remove = mat[i][first]
        }
        first += 1
        second -= 1   
    }
    return (solution - remove)
};
