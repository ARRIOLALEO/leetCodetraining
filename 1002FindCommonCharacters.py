class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        solution = []
        size = len(words)
        for i in words[0]:
            count = 0
            for j in range(1,len(words)):
                if i in words[j]:
                    count += 1
                    tem = [x for x in words[j]]
                    ind = tem.index(i)
                    tem.pop(ind)
                    tem = "".join(tem)
                    words[j] = tem  
            if count >= size - 1:
                solution.append(i)
        
        return solution
        
