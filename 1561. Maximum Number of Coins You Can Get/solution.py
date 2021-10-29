class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_piles =0 
        left , right =  0 , len(piles) -2 
        while left < right:
            max_piles += piles[right]
            right -= 2
            left +=1
        return max_piles
      
      
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_piles =0 
        while piles:
            piles.pop(-1)
            max_piles += piles.pop(-1)
            piles.pop(0)
        return max_piles
        
