class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        words = [list(i) for i in words]
        leters = list(brokenLetters)
        mnw  = 0
        for word in words:
            counter = 0
            for leter in leters:
                if leter in word:
                    counter += 1
                    break
            if counter == 0:
                mnw +=1
        return mnw
