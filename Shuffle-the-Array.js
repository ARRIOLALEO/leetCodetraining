var shuffle = function(nums, n) {
  const firstArray= [...nums].slice(n) 
 const secondArray =[...nums].slice(0,n)
 const solution=[]
 for(i=0;i<n;i++){
   solution.push(secondArray[i])
   solution.push(firstArray[i])
 }
  return solution
};
