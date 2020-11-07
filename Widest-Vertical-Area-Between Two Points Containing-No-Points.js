var maxWidthOfVerticalArea = function(points) { 
  points = points.sort((a,b) => a[0] - b[0])
  let maximun= 0;
  let prev = points[0][0]
  points.map(element =>{
    maximun= Math.max(maximun ,element[0] - prev  )
    prev = element[0]
  })
  return maximun
};
