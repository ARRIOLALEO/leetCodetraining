/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
 const   ipArray =address.split(".")
 let res = []
   for (let i = 0;i<(ipArray.length);i++){
     res.push(ipArray[i] ,"[.]")
   }
  res.pop()
 return res.join("")
};
