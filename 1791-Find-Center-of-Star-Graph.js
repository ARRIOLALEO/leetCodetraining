/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    [a, b, c, d] = [edges[0][0], edges[0][1], edges[1][0], edges[1][1]]
    return (a === c || a === d ? a : b)
};
