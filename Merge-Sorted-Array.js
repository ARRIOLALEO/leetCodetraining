/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
//     get the size of the first array
      let size = nums1.length
//       counter to get positon ot move into the array n
      let counter = n - 1
// if the array n is longer than 1
// and we now tha in array m we have enought space
      if (n > 0) {
//           the size minus the numbers to replace
// and we remove one becuase arrays starts from 0
          for (let i = size - 1; i > size - n - 1; i--) {
              nums1[i] = nums2[counter]
              counter--
                 }
// we sort our array 
          nums1 = nums1.sort((a, b) => a - b)
//  in the case that we have only one position on m we need to just replace the array
                 } else if (m === 0) {
                   for (let i = 0; i < n; i++) {
                   nums1[i] = nums2[i]
                 }
}
};
