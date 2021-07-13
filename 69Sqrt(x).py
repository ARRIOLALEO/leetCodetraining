class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        if x == 2:
            return 1
        for i in range(x):
            pre_solution = i * i
            if pre_solution == x:
                return i
            if pre_solution > x:
                return i -1
        
