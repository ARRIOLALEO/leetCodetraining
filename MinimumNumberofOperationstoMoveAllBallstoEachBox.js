/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
    //  i need to creare an array to save all the results 
    //      than i can create a for to go for every step of the array 
    //      i need to count the position that we have to the sides to move the boxes 

    let solution = []
    for (let i = 0, n = boxes.length; i < n; i++) {
        solution.push(toSides(boxes, i, n))
    }
    return solution
};

function toSides(boxes, pointer, size) {
    let sume = [0, 0]
    for (let i = pointer; i >= 0; i--) {
        if (boxes[i] == 1) {
            sume[0] += (pointer - i)
        }
    }

    for (let j = pointer; j < size; j++) {
        if (boxes[j] == 1) {
            sume[1] += (j - pointer)
        }
    }
    return (sume[0] + sume[1])
}

// Photo by Shannon McInnes on Unsplash
