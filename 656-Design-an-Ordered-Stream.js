/**
 * @param {number} n
 */
var OrderedStream = function(n) {
this.array = new Array(n)
    this.index =0
};

OrderedStream.prototype.insert = function(id, value) {
  this.array[id -1] = value
   const solution =[]
   while(this.array[this.index]){
       solution.push(this.array[this.index++])
   }
    return solution
};

/** 
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(id,value)
 */
