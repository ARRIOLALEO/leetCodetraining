class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = [x for x in strs]
        
        for i,element in enumerate(copy):
            x = list(element)
            x.sort()
            copy[i] = "".join(x)
        dc = dict.fromkeys(copy,[]) 
        
        for i in strs:
            ar = [x for x in i]
            ar.sort()
            ar = "".join(ar)
            temp = dc[ar] + [i]
            dc[ar] = temp
        solution = []
        
        for i in dc:
            solution.append(dc[i])
            
        return solution
        
