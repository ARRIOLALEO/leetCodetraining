/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    let solution =[]
    rectangles.forEach(x=>{
       solution.push(Math.min(x[0],x[1]))
    })
    let max = solution.sort((a,b)=> a - b).pop()
    if(solution.length === 0) return 1
     let result = 1 
    for(let i = solution.length -1 ; i >= 0 ; i--){
        if(solution[i] !== max){
           return result
        }else{
             result++ 
        }
          
    }
    
};
