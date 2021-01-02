/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    let goodTriplets = 0
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            let x = Math.abs(arr[i] - arr[j]) <= a
            if (!x) continue
            for (let k = j + 1; k < arr.length; k++) {
                let y = Math.abs(arr[j] - arr[k]) <= b
                if (!y) continue
                let z = Math.abs(arr[i] - arr[k]) <= c
                if (z) goodTriplets += 1
            }

        }
    }
    return goodTriplets
