class Solution:
    def validPalindrome(self, s: str) -> bool:
        ar = [x for x in s]
        l = 0
        r = len(s)-1
        
        while l <= r:
            if ar[l] != ar[r]:
                temp1 = "".join(ar[:l] + ar[l+1:])
                temp2 = "".join(ar[:r] + ar[r+1:])
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]
                    
            l +=1
            r -=1
            
        return True
