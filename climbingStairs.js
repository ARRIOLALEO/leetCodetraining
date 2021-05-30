function climbingStairs(n) {
if(n === 1) return 1
if(n === 2) return 2
let buffer = [ 1 , 2 ]
solution = 0
for(let i = 2; i < n ; i++){
    if(i === (n - 1)){
      solution = buffer[i-2] + buffer[i-1]
    }else{
        memory.push(buffer[i-2] + buffer[i-1])
    }
}
return solution
}
