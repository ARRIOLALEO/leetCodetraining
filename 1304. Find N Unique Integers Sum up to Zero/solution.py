class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        arr = []
        if n % 2 != 0:
            arr.append(0)
        else:
            arr = []
        count = n
        f = n
        while len(arr) != n:
            arr.append(-f)
            arr.append(f)
            f -=1
        return arr
            
            
        
