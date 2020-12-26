/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(n, m, indices) {
    //  we initial our matrix with 0
    const myInitialMatrix = new Array(n).fill(0).map(element => new Array(m).fill(0))
    let Solution = []
    indices.forEach(indice => {
        const rowToIncrise = indice[0]
        const colummToIncrise = indice[1]
        myInitialMatrix[rowIncrise] = myInitialMatrix[rowIncrise].map(element => element + 1)
        myInitialMatrix.map(element => {
            for (j = colummToIncrise; j < colummToIncrise + 1; j++) {
                element[j] = element[j] + 1
            }
        })
        Solution = myInitialMatrix.flat(Infinity)
        Solution = Solution.filter(element => element % 2 === 1)

    })

    return (Solution.length)
};
