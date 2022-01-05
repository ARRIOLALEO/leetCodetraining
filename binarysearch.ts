function search(nums: number[], target: number): number {
    let left:number = 0;
    let right:number = nums.length - 1
    let middle:number = 0
    if(nums.length < 3){
        if(nums[0] === target){
            return 0
        }else if(nums[1] === target){
            return 1
        }else{
        return -1
        }
    }
    while(left <= right){
        
        middle = Math.floor((right + left)/2) | 0
        if(nums[middle] === target){
            
            return middle
            
        }else if(nums[middle] > target){
            
            right = middle -1
            
        }else{
            
            left = middle +1
        }
    }
    return -1
};
