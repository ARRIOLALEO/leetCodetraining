var maximumUniqueSubarray = function(nums) {
    const dictionary = []
    let maxEresure = 0
    for(let [index, value] of nums.entries()){
        while(dictionary.indexOf(value) > -1){
            dictionary.shift()
        }
        dictionary.push(value)
        let tempMax = dictionary.reduce((acc,el)=>acc + el,0)
        maxEresure = Math.max(maxEresure,tempMax)
    }
    return maxEresure
};
