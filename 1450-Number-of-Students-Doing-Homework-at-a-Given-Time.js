/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number} queryTime
 * @return {number}
 */
var busyStudent = function(startTime, endTime, queryTime) {
 let studentsBusy = 0, counter = 0
 startTime.forEach(start=>{
     if(queryTime >=  start && queryTime <= endTime[counter] ){
         studentsBusy += 1
     }
     counter += 1
 })
    return studentsBusy
};
