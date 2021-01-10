/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    let peak = 0
    if (arr.length < 3) return false
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] >= arr[i + 1]) {
            peak = i
            if (peak === 0) return false
            for (let j = peak; j < arr.length - 1; j++) {
                if (arr[j] <= arr[j + 1]) return false
            }
            return true
        }
    }
    return false
};
