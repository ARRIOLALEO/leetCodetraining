/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var findDiagonalOrder = function(matrix) {
    if (matrix.length === 0) {
        return []
    }
    //this is our staring poin 
    let row = 0,
        col = 0
    //  calculate the max of colums and rows
    const rowMax = matrix.length - 1,
        columsMax = matrix[0].length - 1
    //    we will stroew the solution in this array
    let solution = []
    //     we creare the squeleton of our array
    // we walk our array to fill it 
    for (let i = 0; i < (rowMax + 1) * (columsMax + 1); i++) {
        //   we add our value to the array
        solution.push(matrix[row][col])
        if ((col + row) % 2 === 0) {
            if (col == columsMax) {
                row++
            } else if (row == 0) {
                col++
            } else {
                col++
                row--
            }
        } else {
            if (row == rowMax) {
                col++
            } else if (col == 0) {
                row++
            } else {
                col--
                row++
            }
        }
    }
    return solution
};
