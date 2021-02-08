/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    let decode = [first]
    for (let i = 0 ; i < encoded.length ; i ++){
      decode.push(decode[decode.length -1] ^ encoded[i])
    }
    return decode
};
