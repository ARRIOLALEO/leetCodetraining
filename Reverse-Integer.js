/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let centinel = x
    if( centinel  < 0){
        centinel  = x * -1
    }
     if (centinel  > Math.pow(2, 31)) {
        return 0
    }
    else {
    const number = x.toString().split("")
    const result = []
    let simblr = ""
    while (number[number.length - 1] === 0) {
        number[number.length - 1].slice()
    }
    if (number[0] === "-") {
        simblr = "-"
    }
    number.map(number => {
        result.unshift(number)
    })
        return parseInt((simblr + result.join("")))
    }
};
