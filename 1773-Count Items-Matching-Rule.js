/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
 let solution = 0;
 let search = "";
 items.forEach(item =>{
     if(ruleKey === "type")
     {
         search = 0;
     }
     else if(ruleKey === "color")
     {
               search = 1;
      }
     else
     {
          search = 2;
     }
     
     if(item[search]== ruleValue)
     {
         solution++
     }
 })
    return solution
};
