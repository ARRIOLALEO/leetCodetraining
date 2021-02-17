/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    let  solution = [];
    let doesntExist = arr1.filter(x=> !arr2.includes(x))
    arr2.forEach(x=>{
       arr1.forEach(y=>{
           if( x === y)  solution.push(x)
       })
      
    })
    return [...solution , ... doesntExist.sort((a,b)=> a -b)]    
};
