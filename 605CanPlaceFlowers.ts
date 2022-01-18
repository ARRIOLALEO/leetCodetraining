function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let plantedFlowers:number = 0;
    let startPoint: number = flowerbed.indexOf(0)
    
    for(let point:number=startPoint ;point < flowerbed.length ;point++){
        if((flowerbed[point-1] === 0 || point - 1 < 0 ) && flowerbed[point] === 0 && (flowerbed[point+1] === 0 || point+1 >= flowerbed.length)){
            flowerbed[point] = 1
            plantedFlowers++
        }
        
    
    }
    
    if(plantedFlowers >= n){
        return true
    }
    
    return false

}; 
