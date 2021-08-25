class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s2 = ""
        while len(s2) < len(s) and len(words) > 0:
            s2 += words.pop(0)
        if s2 == s:
            return True
        return False
