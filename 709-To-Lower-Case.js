/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function(str) {
 let myArray = [...str]
 let solution = myArray.reduce((acc,leter)=>{
         let ascii = leter.charCodeAt(0);
     if (ascii >= 65 && ascii <= 90) return acc += String.fromCharCode(ascii + 32);
     else return  acc += leter.charAt(0);
 },[])
 return solution
};
