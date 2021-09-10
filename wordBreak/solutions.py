class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # pass my arr to a set  allow to look in O(1) 
        wordDict = set(wordDict)
        # memoization i need to know where the word start
        # 0 is my base case the word start there
        memo =[0]
        #walking the array leter by leter
        for i in range(len(s)):
            #check all the starts of the words
            for j in memo:
                # check is the word exist in the dictionary
                if s[j:i+1] in wordDict:
                    # if the word exist i add the new begining of the word
                    memo.append(i+1)
                    #if find it i need to stop
                    break
        #is is possible to break the last element of my memo is the same
        # as the len of my word
        
        return memo[-1] == len(s)
        
