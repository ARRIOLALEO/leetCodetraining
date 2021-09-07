class Solution:
    def tribonacci(self, n: int) -> int:
        fb = [0,1,1]
        if n < 3:
            return fb[n]
        else:
            for i in range(2,n):
                fb.append(fb[i-2]+fb[i-1]+fb[i])
            return fb[n]
