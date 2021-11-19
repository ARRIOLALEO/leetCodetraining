class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        
        p = list(p)
        p.sort()
        p = "".join(p)
        len_p = len(p)
        max_len = len(s) - (len_p - 1)
        for index in range(max_len):
            temp = s[index:index+ len_p]
            temp = list(temp)
            temp.sort()
            if "".join(temp) == p:
                anagrams.append(index)
        return anagrams
                
