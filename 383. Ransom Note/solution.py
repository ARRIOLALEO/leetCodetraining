class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dict1 = collections.Counter(ransomNote)
        dict2 = collections.Counter(magazine)
        
        for letter in dict1:
            if letter not in dict2:
                return False
            elif dict1[letter] > dict2[letter]:
                return False
            else:
                pass
        return True
        
