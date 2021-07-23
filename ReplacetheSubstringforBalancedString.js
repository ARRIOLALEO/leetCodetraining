class Solution:
    def balancedString(self, s: str) -> int:
        dictionary = {'Q':0, 'W':0,'E':0, 'R':0}
        n = len(s)// 4
        extras ={}
        
        for c in s:
            dictionary[c] += 1
        counter = 0
        for element in dictionary:
            if dictionary[element] > n:
                extras[element] = dictionary[element] - n
                counter += dictionary[element] - n
        if counter == 0:
            return 0
        res = len(s)
        i = 0
        for j in range(len(s)):
            if s[j] in extras:
                extras[s[j]] -=1
                while max(extras.values()) <= 0:
                    res =min(res ,  j - i + 1)
                    if s[i] in extras:
                        extras[s[i]] +=1
                    i += 1
        return res
        
