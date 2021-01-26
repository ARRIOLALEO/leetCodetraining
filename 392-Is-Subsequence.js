/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let solution = [],
        shadow = t,
        startpoint = 0
    for (let i = 0; i < s.length; i++) {
        let sentinel = true
        for (let j = startpoint; j < shadow.length; j++) {
            if (s[i] === shadow[j]) {
                if (sentinel === true) {
                    solution.push([shadow[j], j])
                    startpoint = j + 1
                    sentinel = false
                }
            }
        }

    }
    let prev = -Infinity
    if (solution.length !== s.length) return false
    for (let w = 0; w < solution.length; w++) {
        if (prev < solution[w][1]) {
            prev = solution[w][1]
        } else {
            return false
            break
        }

    }
    return true
};


// second Solution
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
 let solution = 0  , shadow = t , startpoint = 0
    for(let i =0 ;i < s.length ; i++){
        let sentinel = true
        for(let j = startpoint ; j < shadow.length; j++){
            if(s[i] === shadow[j]){
               if(sentinel === true){
                  solution++
                   startpoint = j + 1
                   sentinel = false
               } 
            }
        }
        
    }
if(s.length !== solution) return false
return true
};
