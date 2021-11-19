class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        
        if len(dict1) != len(dict2):
            return False
        
        for element in dict1:
            if element not in dict2:
                return False
            elif dict1[element] != dict2[element]:
                return False
            else:
                pass
        return True
