/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let initCol = 0;
    let endCols = matrix[0].length ;
    let initRow = 0;
    let endRows = matrix.length ;
    let solution = []
    const total = (endCols) * (endRows);
    while(solution.length < total){
        for(let col = initCol ; col < endCols ; col++){
            solution.push(matrix[initRow][col])
        }
        for(let row = initRow +1; row < endRows ;row++){
            solution.push(matrix[row][endCols-1])
        }
        if(endCols!= initCol){
            for(let col = endCols - 1  ; col > initCol + 1 ; col--){
                solution.push(matrix[endRows -1][col])
            }
         }
        if( endRows != initRow){
            for(let row = endRows - 1 ; row > initRow + 1 ; row--){
                solution.push(matrix[row][initCol +1])
            }
        }
        initCol += 1;
        initRow += 1;
        endCols -=1;
        endRows -= 1;
    }
    return solution
};
