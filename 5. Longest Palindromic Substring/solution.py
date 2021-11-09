class Solution:
    def __init__(self):
        self.max_palindrome = ""
    def longestPalindrome(self, s: str) -> str:
        
        def palindromeCheck(center):
            response = []
            left = center
            right = center + 1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp = s[left:right+1]
                if len(temp) > len(self.max_palindrome):
                    self.max_palindrome = temp
                left -= 1    
                right += 1
            
            left = center
            right = center 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp = s[left:right+1]
                if len(temp) > len(self.max_palindrome):
                    self.max_palindrome = temp
                left -= 1    
                right += 1

        for index in range(len(s)):
            palindromeCheck(index)
        
        return self.max_palindrome
        
        
