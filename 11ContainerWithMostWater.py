class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height) -1
        init , end = 0, size
        area = 0
        
        for width in range(size  , 0 ,-1 ):
            if height[init] < height[end]:
                area = max(area, width * height[init])
                init +=1
            else:
                area = max(area, width * height[end])
                end -=1
        return area
