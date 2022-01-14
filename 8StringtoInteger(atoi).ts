function myAtoi(s: string): number {
    const toAtoi:string[]= s.split("");
    let atoiJs:string[] =[];
    
    let solution:number = 0;
    
    while(toAtoi[0] === " " && toAtoi.length >0){
        toAtoi.splice(0,1)
    }

    while(toAtoi[0] !== " " && toAtoi.length > 0){
        atoiJs = [...atoiJs,...toAtoi.splice(0,1)]
    }
    
    solution = parseInt(atoiJs.join(""))

    if(isNaN(solution)){
        return 0
    }
    
    if(solution <= -Math.pow(2, 31)){
        return -Math.pow(2, 31)
    }
    if(solution >= Math.pow(2, 31) - 1){
        return Math.pow(2, 31) - 1
    }
    
    return solution
};
