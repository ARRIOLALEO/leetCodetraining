/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    const star = [],
        finish = []
    paths.forEach(trip => {
        star.push(trip[0])
        finish.push(trip[1])
    })
    for (let i = 0; i < paths.length; i++) {
        let cityFinal = finish[i]
        if (!star.includes(cityFinal)) return cityFinal
    }
};
