/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function(num) {
    let maxNumber = -Infinity
    let myArray = num.toString();
    myArray = [...myArray]
    for (let i = 0; i < myArray.length; i++) {
        let helper = myArray[i];
        if (helper === 9) {
            myArray[i] = 6
        } else {
            myArray[i] = 9
        }
        maxNumber = Math.max(maxNumber, parseInt(myArray.join("")))
        myArray[i] = helper
    }
    return maxNumber
};
