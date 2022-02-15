/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let obj = new Map()
    for(let n of nums){
        if(obj.has(n)){
            obj.delete(n)
        }else{
            obj.set(n,true)
        }
    }
    
    let [sn] = obj.keys()
    return sn
};
