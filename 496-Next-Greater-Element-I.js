/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    const solution =[]
    for(let i = 0; i < nums1.length ; i++){
    const findTheindex = (element) => element === nums1[i]
      let elementIndex = nums2.findIndex(findTheindex)
      let nextGreatElement = ""
      for(let j = elementIndex ; j < nums2.length ; j++){
          if(nums2[j] > nums1[i]){
              nextGreatElement = nums2[j]
              break
          }
      }
    nextGreatElement !== "" ? solution.push(nextGreatElement):solution.push(-1)      
    }
    return solution
};
