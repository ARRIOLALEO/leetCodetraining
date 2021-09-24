class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelstack =[]
        s = [i for i in s]
        for v in s:
            if v in "aeiouAEIOU":
                vowelstack.append(v)
        
        for index, v in enumerate(s):
            if v in "aeiouAEIOU":
                s[index] = vowelstack.pop(-1)
                
        return "".join(s)
