class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        print(tokens)
        while len(tokens) > 0 and power >= tokens[0] :
            if power >= tokens[0]:
                score +=1
                power -= tokens[0]
                del tokens[0]
                if len(tokens) >= 2 and power < tokens[0]:
                    power += tokens[-1]
                    score -=1
                    del tokens[-1]
 
        return score
