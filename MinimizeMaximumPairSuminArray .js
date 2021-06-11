/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    // i need to order the array i will use merge sort
    //     after that we need to find the center 
    //     after finding the center we go to the sides till end paring the array
    //     we need track the max number

    function mergeSort(array) {
        let half = array.length / 2
        if (array.length <= 1) {
            return array
        }
        const left = array.splice(0, half)
        return mergeArray(mergeSort(left), mergeSort(array))
    }
    let ordenedArray = mergeSort(nums)
    let center = ordenedArray.length / 2
    let max = 0;
    for (let i = 0; i < center; i++) {
        let partial = (ordenedArray[center - 1 - i] + ordenedArray[center + i])
        max = Math.max(max, partial)
    }
    return max
};

function mergeArray(left, right) {
    let sortedArr = []; // the sorted elements will go here

    while (left.length && right.length) {

        if (left[0] < right[0]) {
            sortedArr.push(left.shift());
        } else {
            sortedArr.push(right.shift());
        }
    }
    return [...sortedArr, ...left, ...right];
}
