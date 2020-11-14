/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {

      let size = nums1.length
      let counter = n - 1
      
      if (n > 0) {
          for (let i = size - 1; i > size - n - 1; i--) {
              nums1[i] = nums2[counter]
              counter--
                 }
          nums1 = nums1.sort((a, b) => a - b)
                 } else if (m === 0) {
                   for (let i = 0; i < n; i++) {
                   nums1[i] = nums2[i]
                 }
}
};
