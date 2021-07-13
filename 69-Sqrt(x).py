class Solution:
    def mySqrt(self, x: int) -> int:
        init ,end = 0, x
        centinel = True
        while centinel:
            center = init + round((init + end)/2)
            if (center * center) == x or (center * center) < x and ((center + 1) * (center+1) ) > x:
                centinel = False
                return center
            if (center * center) > x:
                end = center -1
            else:
                init = center + 1
