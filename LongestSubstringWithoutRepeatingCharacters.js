/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let max_number = 0 , start = 0 , end = 0 , set = new Set()
    while(end < s.length){
        if(!set.has(s[end])){
            set.add(s[end])
            max_number = Math.max(max_number , end - start + 1)
            end++
        }
        else
            {
                set.delete(s[start])
                start++
            }
    }
    return max_number
    
};
