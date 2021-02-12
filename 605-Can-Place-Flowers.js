/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let prevPlant = 0;
    if (n === 0) return true
    for (let i = 0; i < flowerbed.length; i++) {
        let therIsPlant = flowerbed[i]
        if ((i + 1) === flowerbed.length && prevPlant === 0 && therIsPlant === 0) {
            flowerbed[i] = 1
            n--
            if (n === 0) return true
            prevPlant = 1
        } else if (prevPlant === 0 && therIsPlant === 0 && flowerbed[i + 1] === 0) {
            flowerbed[i] = 1
            n--
            if (n === 0) return true
            prevPlant = 1
        } else {
            prevPlant = flowerbed[i]
        }
    }
    return false
};
