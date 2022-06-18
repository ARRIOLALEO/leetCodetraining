/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
    const myQueue  = []
    const myDictionary = {}
    let maxFruits = 0
    for(let fruit of fruits){
        fruit = (fruit).toString()
        if(myDictionary[fruit]){
            myDictionary[fruit].push(fruit)
            myQueue.push(fruit)
        }else{
            if(Object.keys(myDictionary).length <2){
                myDictionary[fruit] = [fruit]
            }else{
                while(Object.keys(myDictionary).length >1){
                    let element = myQueue.shift();
                    if(myDictionary[element].length > 1){
                        myDictionary[element].pop()
                    }else{
                        delete myDictionary[element]
                    }
                }
                myDictionary[fruit] = [fruit]
               
            }
             myQueue.push(fruit)
        }
        maxFruits = Math.max(maxFruits,myQueue.length)
    }
    return maxFruits
};
