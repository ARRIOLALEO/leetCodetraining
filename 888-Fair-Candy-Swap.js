/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var fairCandySwap = function(A, B) {
    let qCandiesAlice = A.reduce((a, b) => a + b)
    let qCandiesBob = B.reduce((a, b) => a + b)
    for (let i = 0; i < A.length; i++) {
        let restOfCandies = qCandiesAlice - A[i]
        for (let j = 0; j < B.length; j++) {
            if ((restOfCandies + B[j]) == (qCandiesBob + A[i] - B[j])) {
                return ([A[i], B[j]])
                break
            }
        }
    }
};
