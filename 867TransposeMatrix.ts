function transpose(matrix: number[][]): number[][] {
    const solution:number[][] = [];
    const cols:number = matrix[0].length;
    const rows:number = matrix.length;
    
    for(let col:number =  0 ; col < cols ;col++){
        let temp:number[] =[]
        for(let row:number = 0 ; row < rows;row++){
            temp.push(matrix[row][col])
        }
        solution.push(temp)
    }
    return solution

};
