/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
      s = s.match(/[a-zA-Z^\d+$]/g)
    if(s === "" || s === null) {
        return true
    }
    let leters = [... s].reverse().join("")
    if(leters.toLowerCase() === s.join("").toLowerCase()){
        return true
    } else{
        return false
    }
};
