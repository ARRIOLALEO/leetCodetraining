/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
   const checker = haystack.includes(needle)
    if(checker){
        return haystack.indexOf(needle)
    }
    return -1
};
