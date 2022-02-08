/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    num = [...num.toString()]
    while(num.length > 1){
        num = num.reduce((acc,n)=> acc + parseInt(n) , 0)
        if(num > 9){
            num = [...num.toString()]
        }
        
    }
    return num
};

var addDigits = function(num) {
    return num ? 1 + (num - 1) % 9 : 0
};
