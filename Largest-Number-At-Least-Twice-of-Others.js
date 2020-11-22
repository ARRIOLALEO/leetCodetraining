/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    // order the elements andg get the last one 
    if (nums.length > 1) {
        let theBiggest = [...nums].sort((a, b) => a - b)
        let theSecond = theBiggest[theBiggest.length - 2]
        console.log(theSecond)
        theBiggest = theBiggest[theBiggest.length - 1]
        console.log(theBiggest)

        // compared it with the one before it 
        if (theBiggest >= (theSecond * 2)) {
            // if the element is 2 times bigger than the one htat is before 
            for (let i = 0; i < nums.length; i++) {
                if (nums[i] === theBiggest)
                    return i
            }
        }
        //if not return -1
        return -1
    } else {
        return 0
    }
};
