/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let seconds = 0
    for (let i = 0; i < points.length; i++) {
        if ((i + 1) == points.length) break
        let difX = Math.abs(points[i][0] - points[i + 1][0])
        let difY = Math.abs(points[i][1] - points[i + 1][1])
        seconds = seconds + Math.max(difX, difY)

    }
    return seconds
};
