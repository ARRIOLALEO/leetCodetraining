var canFormArray = function(arr, pieces) {
// join our array
    arr = arr.join("")
//     we create a counter to check the length of the
//     result 
    let counter = ""
//     iterate the pieces 
    let response = true
    pieces.forEach(piece => {
        piece = piece.join("")
        counter += piece
        if(arr.indexOf(piece) == -1){ 
          response =  false
        }
    })
    if(counter.length < arr.length  ){response= false}
    return response
};
